from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import UserSerializers #,Custom_Doctor_Serializer
from rest_framework.response import Response
from rest_framework import status


class PRegisterView(GenericAPIView):
    serializer_class = UserSerializers
    def post(self, request):
        serializer = UserSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# class DRegisterView(GenericAPIView):
#     serializer_class = Custom_Doctor_Serializer
#     def post(self, request):
#         serializer = Custom_Doctor_Serializer(data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

