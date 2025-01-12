from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Notification

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_notifications(request):
    # try:
    notifications = Notification.objects.filter(recipient=request.user).order_by('-created_at')
    data = [
        {
            "actor": notification.actor.username,
            "verb": notification.verb,
            "target": str(notification.target),
            "created_at": notification.created_at,
            "is_read": notification.is_read
        }
        for notification in notifications
    ]
    return Response(data)

    # except Exception as e:
    #     return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)