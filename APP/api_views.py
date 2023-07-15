from rest_framework.views import APIView
from rest_framework.response import Response

# Using Class-Based View because all request will show result at a SINGLE ENDPOINT


class UserViewSet(APIView):
    def get(self, request):  # If user want to just see what are the datas
        return Response({"message": "GET request"})

    def post(self, request):  # If user wants to post some new data
        return Response({"message": "POST request"})

    def put(self, request):  # If user wants to update a complete pack of data
        return Response({"message": "PUT request"})

    def patch(self, request):  # If user wants to update just a specific field of a packet of data
        return Response({"message": "PATCH request"})

    def delete(self, request):  # If user wants to delete a single field/packet/all packets
        return Response({"message": "DELETE request"})
