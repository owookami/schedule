from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from rest_framework import viewsets

from rest_framework.response import Response
from rest_framework.decorators import api_view

from django_filters.rest_framework import DjangoFilterBackend

from .models import Schedule
from .serializers import ScheduleSerializer,ScheduleCreateSerializer

# Create your views here.
@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

# @api_view(['GET'])
# def selectedDateSchedule(request,selectedDate):
#     Schedule = Schedule.objects.

# class ScheduleViewSet(viewsets.ModelViewSet):
#     queryset = Schedule.objects.all()
#     # permission_classes = [CustomReadOnly]
#     filter_backends = [DjangoFilterBackend]
#     filterset_fields = ['date']
    
#     def get(self):
#         return ScheduleSerializer
    

class ScheduleAPIView(APIView):
    def get(self, request):   
        if request.GET.get('date') is not None:
            date = request.GET.get('date')
            schedules = Schedule.objects.filter(date=date)
        else:
            schedules = Schedule.objects.all()
        serializer = ScheduleSerializer(schedules, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class ScheduleCreateAPIView(APIView):
    def post(self, request):
        serializer = ScheduleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
class ScheduleDeleteAPIView(APIView):
    def delete(self, request, **kwargs):
        if kwargs.get('selectedDate') is None:
            return Response('Invalid request', status=status.HTTP_400_BAD_REQUEST)
        else:
            selectedDate = kwargs.get('selectedDate')
            schedule_object = Schedule.objects.get(date=selectedDate)
            schedule_object.delete()
            return Response('delete ok', status=status.HTTP_200_OK)