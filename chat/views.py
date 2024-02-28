from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ChatApi(APIView):
    def get(self, req):
        return Response(
            {"message": "You see this message from ChatAPI"}, status=status.HTTP_200_OK
        )
