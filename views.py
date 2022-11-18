from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class EmployeeAPI(APIView):
    def get(self, request):
        try:
            emp = EmpPersonalDetails.objects.all()
        except EmpPersonalDetails.DoesNotExist:
            return Response(data={'msg': 'employee details not found', 'success': 'false', 'employee': []},
                            status=status.HTTP_404_NOT_FOUND)
        if not emp:
            return Response(data=None, status=status.HTTP_204_NO_CONTENT)
        serializer = EmpPersonalDetailsModelSerializer(emp, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        try:
            serializer = EmpPersonalDetailsModelSerializer(data=request.data)
        except:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(
                data={'msg': 'employee created successfully', 'success': 'true', 'empid': request.data.get('regid')},
                status=status.HTTP_201_CREATED)
        else:
            if EmpPersonalDetails.objects.filter(email=request.data.get('email')):
                return Response(data={'msg': 'employee already exist', 'success': 'false'}, status=status.HTTP_200_OK)
            else:
                return Response(data={'msg': 'invalid body request', 'success': 'false'},
                                status=status.HTTP_404_NOT_FOUND)


class EmpAPI(APIView):
    def get(self, request, pk=None):
        try:
            emp = EmpPersonalDetails.objects.get(pk=pk)
        except EmpPersonalDetails.DoesNotExist:
            return Response(data={'msg': 'employee details not found', 'success': 'false', 'employee': []},
                            status=status.HTTP_404_NOT_FOUND)
        serializer = EmpPersonalDetailsModelSerializer(emp)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


    def delete(self, request, pk=None):
        if pk != '':
            try:
                emp = EmpPersonalDetails.objects.get(
                    pk=pk)
            except:
                return Response(data={'msg': 'no employee found with this regid', 'success': 'false'},
                                status=status.HTTP_404_NOT_FOUND)
            emp.delete()
            return Response(data={'msg': 'employee deleted successfully', 'success': 'true'}, status=status.HTTP_200_OK)
        else:
            return Response(data={'msg': 'employee deletion failed', 'success': 'false'}, status=status.HTTP_200_OK)

    def put(self, request, pk=None):
        try:
            emp = EmpPersonalDetails.objects.get(
                pk=pk)
        except EmpPersonalDetails.DoesNotExist:
            return Response(data={'msg': 'no employee found with this regid'}, status=status.HTTP_404_NOT_FOUND)
        serializer = EmpPersonalDetailsModelSerializer(
            data=request.data, instance=emp)
        if serializer.is_valid():
            serializer.save()
            return Response(data={'msg': 'employee details updated successfully', 'success': 'true'},
                            status=status.HTTP_200_OK)
        else:
            if EmpPersonalDetails.objects.filter(email=request.data.get('email')):
                return Response(data={'msg': 'employe details updation failed', 'success': 'false'},
                                status=status.HTTP_200_OK)
            else:
                return Response(data={'msg': 'invalid body request', 'success': 'false'},
                                status=status.HTTP_404_NOT_FOUND)

