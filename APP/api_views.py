from rest_framework.views import APIView
from rest_framework.response import Response
from APP.serializers import *

# Using Class-Based View because all request will show result at a SINGLE ENDPOINT


class UserViewSet(APIView):
    def get(self, request):  # If user want to just see what are the datas
        user_datas=userSerializer(User.objects.all(),many=True)
        return Response(user_datas.data)
        

    def post(self, request):  # If user wants to post some new data
        user_datas=userSerializer(data=request.data)
        if user_datas.is_valid():
            user_datas.save()
            return Response({"Message":"New USER added!!"})
        else:
            return Response(user_datas.errors)
        

    def put(self, request):  # If user wants to update a complete pack of data
        data=request.data
        update_user=data['username']
        user_datas=userSerializer(data=data)
        if user_datas.is_valid():
            user_datas.save()
            return Response({"Message":f"USER OF USERNAME: {update_user} IN WHOLE UPDATED!!!!"})
        else:
            return Response(user_datas.errors)
        

    def patch(self, request):  # If user wants to update just a specific field of a packet of data
        data=request.data
        update_user=data['username']
        user_datas=userSerializer(data=data,partial=True)
        if user_datas.is_valid():
            user_datas.save()
            return Response({"Message":f"ATTRIBUTE/S OF USER OF USERNAME: {update_user} UPDATED!!!!"})
        else:
            return Response(user_datas.errors)
        

    def delete(self, request):  # If user wants to delete a single field/packet/all packets
        data=request.data
        delete_user=data['username']
        if delete_user!="*":
            obj=User.objects.get(Farmer=delete_user).delete()
            return Response({"Message":f"USER OF USERNAME : {delete_user} DELETED!!!!"})
        else:
            obj=User.objects.all().delete()
            return Response({"Message":f"ALL USERS ARE DELETED!!!!"})
