from django.shortcuts import render
from rest_framework import status,generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Ddetails_serializers,pdetails_serializers
from .models import Doctor_profile
from rest_framework.generics import GenericAPIView
from patient_details.models import Patient_details

# Create your views here.



# class d_create(GenericAPIView):
#     serializer_class = Ddetails_serializers

#     def post (self, request):
#         data = request.data

#         details = Doctor_profile.objects.create(

#             doctor_name = data['doctor_name'],
#             license_no = data['license_no'],
#             specialty = data['specialty'],
#             email = data['email'],
#             phone_number = data['phone_number'],
#             bio = data['bio']
#             )
#         serializer = Ddetails_serializers(details)
#         return Response(serializer.data)



# creating a doctor account
class d_create(GenericAPIView):
    serializer_class = Ddetails_serializers

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            try:
                details = Doctor_profile.objects.create(
                    doctor_name=validated_data['doctor_name'],
                    license_no=validated_data['license_no'],
                    specialty=validated_data['specialty'],
                    email=validated_data['email'],
                    phone_number=validated_data['phone_number'],
                    bio=validated_data.get('bio', '')  # Get bio if provided, otherwise default to empty string
                )
                serializer = Ddetails_serializers(details)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except KeyError as e:
                return Response({"error": f"Missing key in data: {e}"}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


# fetching all the enterd details
class d_details(GenericAPIView):
    serializer_class = Ddetails_serializers
    queryset = Doctor_profile.objects.all()  # Define the queryset attribute

    def get(self, request):
        details = self.get_queryset()  # Retrieve queryset using get_queryset() method
        serializer = Ddetails_serializers(details, many=True)
        return Response(serializer.data)
    


# class DoctorUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Doctor_profile.objects.all() 
#     serializer_class = Ddetails_serializers
    





# fetching the patient datas from the data base
class p_details(GenericAPIView):
    serializer_class = pdetails_serializers
    queryset = Patient_details.objects.all()

    def get(self,request):    
        details = self.get_queryset()    
        serialzers = pdetails_serializers(details,many = True)
        return Response(serialzers.data)


# creating patient account
class p_create(GenericAPIView):
    serializer_class = pdetails_serializers

    def post(self, request):
        data = request.data

        details = Patient_details.objects.create(
            name = data['name'],
            dob = data['dob'],
            phone_number = ['phone_number'],
            age = ['age'],
            weight = ['weight'],
            height = ['height'],
            sex = ['sex'],
            hyper_tension_bp = ['hyper_tension_bp'],
            chest_pain =['chest_pain'], 
            palpitation = ['palpitation'],
            surgery = ['surgery'],
            any_other =['any_other'],
        )
        serializer = pdetails_serializers(details)
        return Response(serializer.data)