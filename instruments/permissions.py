from rest_framework import permissions

class IsOwnerReadAndPost(permissions.BasePermission):
    message = "You can't edit this Instrument object. You are not the owner!"
    
    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD, and OPTIONS methods for all users
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        
        # Check if the user is the owner of the instrument
        return obj.store_name == request.user