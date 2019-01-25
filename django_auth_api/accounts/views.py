from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.models import CustomUser
from accounts.serializers import CustomUserSerializer
from accounts.forms import CustomUserForm



class CustomUserAPIView(APIView):
    form_class = CustomUserForm

    def get(self, request, format=None):
        filter_params = self.request.query_params
        users = CustomUser.objects.filter(**filter_params.dict())
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        form = self.form_class(data=request.data)
        if not form.is_valid():
            raise ValueError("Invalid")
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = CustomUser(**serializer.data)
            CustomUser.objects.save_data(users=[user])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, 
                            status=status.HTTP_400_BAD_REQUEST)
        

