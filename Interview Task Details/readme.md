Requirements:

1. Create apis for the following models 
          CRMLED in crm.py file
          MASSLM in master.py

2. Write a function to calculate forcast amount from CRMopp (oppurtunity model)
     
     CRMopp.probability = CRMpil.probability_percent * CRMopp.amount 
     
     Forecast value = for each oppurtunity sum CRMopp.probability, filter closed_on date is null or blank only.

     List forecast value by month based on CRMopp.target_date
          e.g: Jan   235000
               feb   350000
               Mar   500000

