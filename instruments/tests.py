import pytest
from rest_framework.test import APIClient
from .urls import reverse
from django.contrib.auth import get_user_model
from .models import Instrument


@pytest.fixture
def user():
    return get_user_model().objects.create_user(username='testuser', password='testpassword')


@pytest.fixture
def instrument(user):
    return Instrument.objects.create(store_name=user, instrument='Guitar', model='Acoustic', price='1000', desc='A beautiful guitar.')


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_instrument_list_view(api_client, instrument, user):
    url = reverse('instruments')
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['instrument'] == instrument.instrument


@pytest.mark.django_db
def test_instrument_detail_view(api_client, instrument, user):
    url = reverse('instrument_detail', args=[instrument.id])
    api_client.force_authenticate(user=user)
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data['instrument'] == instrument.instrument


@pytest.mark.django_db
def test_create_instrument_view(api_client, user):
    url = reverse('instruments')
    api_client.force_authenticate(user=user)
    data = {
        'store_name': user.id,
        'instrument': 'Piano',
        'model': 'Grand',
        'price': '5000',
        'desc': 'A beautiful piano.'
    }
    response = api_client.post(url, data)
    assert response.status_code == 201
    assert Instrument.objects.filter(instrument='Piano').exists()


@pytest.mark.django_db
def test_update_instrument_view(api_client, instrument, user):
    url = reverse('instrument_detail', args=[instrument.id])
    api_client.force_authenticate(user=user)
    data = {
        'instrument': 'Updated Instrument',
        'model': 'Updated Model',
        'price': '999',
        'desc': 'Updated description.'
    }
    response = api_client.put(url, data)
    assert response.status_code == 200
    instrument.refresh_from_db()
    assert instrument.instrument == 'Updated Instrument'
    assert instrument.model == 'Updated Model'


@pytest.mark.django_db
def test_delete_instrument_view(api_client, instrument, user):
    url = reverse('instrument_detail', args=[instrument.id])
    api_client.force_authenticate(user=user)
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Instrument.objects.filter(id=instrument.id).exists()

