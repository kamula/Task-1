# How to build and run the API

**Ensure that you have python3 correctly installed and configured in your Operating System**

**Ensure that you have PostgreSQL correctly installed and configured in your Operating System**

**Ensure that you have Postman installed in your Operating System**

## Steps to build the application

### In Development

1.  Clone the Repository into your local computer

2.  Navigate to the root directory of the project using your Terminal

3.  Create a .env file at the root directory of the project

    The .env file should have the following attributes as shown in the image
    ![debug3](https://user-images.githubusercontent.com/35394098/218056462-53673c9d-d978-4b9d-83ce-4d826cd786ce.png)

    `DB_NAME= Name of your PostgreSQL database`

    `DB_USER= database user`

    `DB_PASSWORD= database user password`

    `DB_HOST= database host`

4.  Create a virual environment using the command `python3 -m venv venv`

5.  Activate the Virtual environment using the commands below:

    - On Linux Operating system use the command `source ./venv/bin/activate`

    - On Windows Operating System use the command `venv\Scripts\activate.bat`

    You will notice that **venv** appears before the beginnning of your Terminal. This indicates that the Virual environment is activated.

6.  Install the dependencies for the project using the command `pip install -r requirements.txt`

7.  Run the the command `python3 manage.py makemigrations` in order to generate SQL commands

8.  Run the the command `python3 manage.py migrate` in order to execute those SQL commands in the database

9.  Run the app using the command `python3 manage.py runserver`

### In Production

Change the `DEBUG` attribute to `False` and change the `DB_HOST` to point to the location of your database in the .env file and follow the installation guidelines provided by the production platform

## API Structure

The API has 3 main modules (directories):

1. src - Contains the API configurations

2. authentication - Module (app) responsible for handling authentication functions, User creation & login functionalities

3. transfers - Module (app) responsible for handling all the financial transactions

## API Description

In order to access the API endpoints, users must register and login in order to obtain an auth Token (JWT).

The API schema can be accessed via this url [http://localhost:8000/schema](http://localhost:8000/schema)

1. For user registration, access the andpoint via a POST request and pass the following attributes in the request body (full_name,phone_number,password) as shown below.

![user registration](https://user-images.githubusercontent.com/35394098/218393025-f8239ff0-4141-4f61-bfe7-4afe3d68a046.png)

2. For user Login, access the andpoint via a POST request and pass the following attributes in the request body (phone_number,password) as shown below.

![userloginview](https://user-images.githubusercontent.com/35394098/218395556-d44dc9ac-230d-4db6-b1de-0106f2cf0ccd.png)

2. For Account creation, pass the access token on the Authorization section of the POST request headers as shown below: 

![authorization](https://user-images.githubusercontent.com/35394098/218416270-efac688c-ec75-4e75-a59a-048fe3dd9113.png)

After that pass the staring balance in the request body as shown below:

![starting_balance](https://user-images.githubusercontent.com/35394098/218416667-1761f9f2-102f-437b-8931-3cec742f4f41.png)

If an account has already been created: An error message will occur at the response body as shown below"

![Add Event](https://user-images.githubusercontent.com/35394098/218418275-e687b23b-9e9e-4a7e-b353-75a278bfe9f0.png)






