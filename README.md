# Zillancer Task

develop APIs for the CRMLED and MASSLM models in Django. Additionally, create a function to calculate forecasted amounts based on specific conditions using data from the CRMopp model. Organize and list these forecasted values by month according to the CRMopp.target_date.


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)


## Features

## Features

This task involves the development of APIs for two Django models: `CRMLED` and `MASSLM`. Additionally, it requires implementing a function to calculate forecasted amounts based on specific conditions using data from the `CRMopp` model. These forecasted values are organized and listed by month according to the `CRMopp.target_date`.


## Installation

1. **Clone the Repository:**

git clone https://github.com/ProgrammerAhmedO/zillancer_task.git
cd task


2. **Install Dependencies:**

Ensure you have Python 3.9 installed or higher. Create and activate a virtual environment (optional but recommended), then install the required packages:
```python
pip install -r requirements.txt
```
3. **Active the env:**
   ```python
   source Task/bin/activate
   ```
4. **Database Configuration:**

4.1. Apply Migrations:
Apply the initial database migrations:
```python
python3 manage.py makemigrations
python3 manage.py migrate
```
4.2. Create Superuser:
Create a superuser using the following command:
```python
python manage.py createsuperuser
```

## Usage:
   
5.1 Run the Development Server:
Start the development server:
```python
python manage.py runserver
```
The application will be accessible at http://localhost:8000/.
![Screenshot 2023-09-22 at 6 40 40 PM](https://github.com/ProgrammerAhmedO/zillancer_task/assets/84571800/4584cd5d-5e2c-4d59-b32d-1498d5f3b4a8)
![Screenshot 2023-09-22 at 6 42 02 PM](https://github.com/ProgrammerAhmedO/zillancer_task/assets/84571800/33e3aa5c-9970-4bc3-a690-90cd6298c22a)


5.2. Access the Admin Panel:
Open the admin panel by visiting http://localhost:8000/admin/ and logging in with your superuser credentials.
5.3. Run the Test File:
To run the Test File manually, use the following command:
```python
python3 manage.py test BaseApp.tests
```
This will show you the result of the required calculate_forecast_amount function.

![Screenshot 2023-09-22 at 5 25 12 PM](https://github.com/ProgrammerAhmedO/zillancer_task/assets/84571800/545c45d3-89f4-4964-b92f-e2329a8b8510)


## API Documentation

**CRMLedListCreateView and CRMLedRetrieveUpdateDestroyView**
CRMLedListCreateView is a view class that allows the listing and creation of instances of the CRMLed model.
CRMLedRetrieveUpdateDestroyView is a view class that allows the retrieval, updating, and deletion of individual instances of the CRMLed model.
These views are secured using session-based and basic authentication, ensuring that only authenticated users can access them.
The CRMLedSerializer is used to serialize CRMLed model instances and convert them into JSON format for API responses.
Additionally, the detail_url field is added to the serializer, which generates the URL for accessing the detail view of a specific CRMLed instance.

**MASSlmListCreateView and MASSlmRetrieveUpdateDestroyView**
MASSlmListCreateView is a view class that allows the listing and creation of instances of the MASSlm model.
MASSlmRetrieveUpdateDestroyView is a view class that allows the retrieval, updating, and deletion of individual instances of the MASSlm model.
Like the CRMLed views, these views are also secured using session-based and basic authentication.
The MASSlmSerializer is used to serialize MASSlm model instances and convert them into JSON format for API responses.
Similar to the CRMLed serializer, the detail_url field is added to the MASSlmSerializer for generating URLs to access the detail view of specific MASSlm instances.

![Screenshot 2023-09-22 at 6 42 31 PM](https://github.com/ProgrammerAhmedO/zillancer_task/assets/84571800/6fb4bf95-b52d-4d54-bee3-f286ea069dec)
![Screenshot 2023-09-22 at 6 42 36 PM](https://github.com/ProgrammerAhmedO/zillancer_task/assets/84571800/82ca5d60-d24c-4624-8d72-417ca159a3c3)
![Screenshot 2023-09-22 at 6 42 52 PM](https://github.com/ProgrammerAhmedO/zillancer_task/assets/84571800/9d18a9c6-a89e-411d-b36a-7701ea6a94c9)
![Screenshot 2023-09-22 at 6 43 03 PM](https://github.com/ProgrammerAhmedO/zillancer_task/assets/84571800/df960ea4-01fc-46d7-9c7a-a326ee5b2d40)

