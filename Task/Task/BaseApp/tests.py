from django.test import TestCase
from .models import CRMOpp
from .views import calculate_forecast_amount
from datetime import datetime

class ForecastTest(TestCase):
    def setUp(self):
        # Create test CRMopp objects with different closed_on and target_date values
        self.opp1 = CRMOpp.objects.create(opportunity_name='Opportunity 1', probability=50, amount=1000, closed_on=None, target_date='2023-10-01')
        self.opp2 = CRMOpp.objects.create(opportunity_name='Opportunity 2', probability=75, amount=2000, closed_on=None, target_date='2023-11-01')
        self.opp3 = CRMOpp.objects.create(opportunity_name='Opportunity 3', probability=60, amount=1500, closed_on='2023-09-15', target_date='2023-12-01')

        
    def test_forecast_calculation(self):
        opportunities = CRMOpp.objects.all()
        
        # Override current_date within the test with a time component to match target_date
        current_date = datetime(2023, 9, 1, 0, 0, 0).date()

        forecast_values = calculate_forecast_amount(opportunities)

        # Ensure that the function produces the expected results
        self.assertEqual(forecast_values['Oct 2023'], 500.0)
        self.assertEqual(forecast_values['Nov 2023'], 1500.0)
        self.assertNotIn('Dec 2023', forecast_values)  # Expecting 'Dec 2023' to be absent
