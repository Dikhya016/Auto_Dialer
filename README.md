# Auto Dialer Application

This Django-based Auto Dialer application allows users to send auto-generated audio messages to a list of contacts stored in a phonebook. The app integrates with Twilio's API for automated calling. The application also supports user authentication, contact management, and call record tracking.

## Features

### 1. **User Authentication**
- **Sign-up/Registration**: New users can sign up and create accounts.
- **Login**: Registered users can log in to access the application.

### 2. **Contact/Phonebook Management**
- **Phonebook Creation**: Users can create and name phonebooks to group their contacts.
- **Manage Contacts**:
  - Add, edit, delete, and view contacts within the phonebook.
  - Contacts have fields for:
    - First Name
    - Last Name
    - City
    - Phone Number
  - Contacts can be associated with multiple phonebooks.

### 3. **Auto Dialer**
- **Select Phonebook & Message**:
  - Users can select a phonebook and input a text message.
  - A personalized audio message (using Twilio Text-to-Speech) is generated for each contact, mentioning the contact's First Name, Last Name, or City.
  
- **Twilio Integration**:
  - The system uses Twilio to dial each number in the selected phonebook and deliver the personalized audio message.

### 4. **Call Records**
- Lists all calls made, along with:
  - Contact Name
  - Phone Number
  - Date/Time of the call
  - Call Duration
  - Cost of the call

## Prerequisites

To run the project, you will need to install the following:

1. **Python 3.x**: Make sure Python 3 is installed on your system.
2. **Django**: Django framework for running the project.
   ```bash
   pip install django
3. **Twilio**: For integrating the auto-dialing functionality.
    ```bash
   pip install twilio
4. **Bootstrap**: For styling the frontend

## Twilio Credentials
You need to sign up for a Twilio account and provide the following credentials:

- **Account SID**: Your Twilio account SID.
- **Auth Token**: Your Twilio authentication token.
- **Twilio Phone Number**: A valid Twilio phone number from which calls will be made.

  ```bash
  TWILIO_ACCOUNT_SID=your_account_sid_here
  TWILIO_AUTH_TOKEN=your_auth_token_here
  TWILIO_PHONE_NUMBER=your_twilio_number_here

## Project Setup

Follow these steps to set up the project:

### 1. Clone the repository

    ```bash
      git clone https://github.com/your-repo/auto-dialer.git
      cd auto-dialer
### 2. Install the dependencies

    ```bash
    pip install -r requirements.txt

### 3. Set up Django environment
    
  Create a .env file and add your environment variables (as shown above) for Twilio credentials.

### 4. Apply database migrations
    ```bash
    python manage.py migrate

### 5. Start the server
    ```bash
    python manage.py runserver
The application will be available at http://127.0.0.1:8000/.





