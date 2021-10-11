from rest_framework.response import Response
# rest_framework.views provides an APIView class that is the base of all views in REST framework.
from rest_framework.views import APIView
from users.api.serializers import UserDisplaySerializer


class CurrentUserAPIView(APIView):
    """
    Provide username of user which is currently connected
    """

    def get(self, request):
        serializer = UserDisplaySerializer(request.user)
        return Response(serializer.data)
