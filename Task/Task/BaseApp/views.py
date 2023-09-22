from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import CRMLedSerializer, MASSlmSerializer
from collections import defaultdict
from datetime import datetime
from .crm import *
from .master import *
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


def calculate_forecast_amount(opportunities):
    # Create a dictionary to store forecast values by month
    forecast_by_month = defaultdict(int)

    # Get the current date
    current_date = datetime.now().date()

    # Iterate through the opportunities and calculate the forecasted amount
    for opp in opportunities:
        if opp.closed_on is None:
            # Calculate the forecasted amount using the formula
            forecast_amount = opp.probability * opp.amount / 100

            # Get the target date of the opportunity
            target_date = opp.target_date

            # Check if the target date is in the future
            if target_date > current_date:
                # Extract the year and month from the target date
                year_month = target_date.strftime('%b %Y')

                # Add the forecast amount to the corresponding month in the dictionary
                forecast_by_month[year_month] += forecast_amount

    # Sort the dictionary by month
    sorted_forecast = dict(sorted(forecast_by_month.items(), key=lambda x: datetime.strptime(x[0], '%b %Y')))

    return sorted_forecast


def forecast_view(request):
    # Retrieve the CRMopp objects you want to calculate the forecast for
    opportunities = CRMOpp.objects.all()

    # Calculate the forecasted amounts
    forecast_values = calculate_forecast_amount(opportunities)

    # Render a template with the forecasted values
    return render(request, 'Base/forecast.html', {'forecast_values': forecast_values})


def home(request):
    context = {}
    return render(request, "Base/index.html",context)


class CRMLedListCreateView(generics.ListCreateAPIView):
    queryset = CRMLed.objects.all()
    serializer_class = CRMLedSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]   
    permission_classes = [IsAuthenticated]    

class CRMLedRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CRMLed.objects.all()
    serializer_class = CRMLedSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]   
    permission_classes = [IsAuthenticated]    

class MASSlmListCreateView(generics.ListCreateAPIView):
    queryset = MASSlm.objects.all()
    serializer_class = MASSlmSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]   
    permission_classes = [IsAuthenticated]  

class MASSlmRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MASSlm.objects.all()
    serializer_class = MASSlmSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]   
    permission_classes = [IsAuthenticated]    
