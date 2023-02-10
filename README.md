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
    ![env](https://user-images.githubusercontent.com/35394098/218055366-034aab19-990c-451b-8e6f-9c988c255718.png)
    

4.  Create a virual environment using the command `python3 -m venv venv`

5.  Activate the Virtual environment using the commands below:

    - On Linux Operating system use the command `source ./venv/bin/activate`

    - On Windows Operating System use the command `venv\Scripts\activate.bat`

    You will notice that **venv** appears before the beginnning of your Terminal. This indicates that the Virual environment is activated.

6.  Install the dependencies for the project using the command `pip install -r requirements.txt`

7.  Run the app using the command `python3 manage.py runserver`

### In Production

Change the DEBUG attribute to False in the .env file and follow the installation guidelines provided by the production platform

## API Structure

The API has 3 main modules (directories):

1. src - Contains the API configurations

2. authentication - Module (app) responsible for handling authentication functions, User creation & login functionalities

3. transfers - Module (app) responsible for handling all the financial transactions
