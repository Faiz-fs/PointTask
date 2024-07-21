# Problem Set 2 - A functioning web app with API

I. Please create a website - which should have two components:

Expose all the endpoints using Rest API, with proper permissions, authentication and documentation. Please refer to the image link - https://i.imgur.com/T0ZCO9A.png
1) Admin Facing - Where admin user can add an android app as well as the number of points - earned by user for downloading the app. (Please do not use the default Django Admin)
2) User Facing - where the user can see the apps added by the admin and the points. The user should be able to see the following fields. 
- Signup and Login (Feel free to use any package for the same). 
- Their Name and Profile
- Points Earned.
- Tasks completed. 
- Option to upload a screenshot (which must include drag and drop) for that particular task. (Like if a user downloads a particular app), he can send a screenshot of the open app to confirm that he has indeed downloaded the app. 

## Introduction

PointTask is a comprehensive Django-based web application designed to manage tasks and applications efficiently. It comprises two primary components: the `api` app, responsible for handling models, serialization, and REST APIs, and the `taskapp` app, which manages frontend rendering and data operations.

## Features

- **User Management**: Allows user registration, authentication, and profile management.
- **App Management**: Facilitates adding app details.
- **Task Management**: Users can manage tasks associated with different apps.
- **Admin Interface**: Provides an interface for administrators to manage users, apps, and tasks.
- **RESTful API**: Exposes endpoints for CRUD operations on users, apps, and tasks.
- **File Upload**: Supports uploading app icons and screenshots.
- **Points System**: Tracks and displays user points based on tasks and app interactions.

## Prerequisites

- Python 3.10.12
- SQLite (built-in with Django)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://gitlab.com/yourusername/PointTask.git
    cd PointTask
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Usage

- **Admin Interface**: Access the admin interface at `http://127.0.0.1:8000/admin` to manage users, apps, and tasks.
- **API Endpoints**: The API endpoints are available at `http://127.0.0.1:8000/api/`.

## Folder Structure

- **api/**: Handles models, serialization, and REST APIs.
- **taskapp/**: Manages frontend rendering and data fetching.
- **media/**: Stores uploaded screenshots and icons.
  - **images/**: Stores screenshots.
  - **icon/**: Stores app icons.

## API Endpoints

- **User Endpoints:**
  - `GET /api/user/`: List all users
  - `POST /api/user/`: Create a new user
  - `GET /api/user/<id>/`: Retrieve, update, or delete a user

- **App Endpoints:**
  - `GET /api/app/`: List all apps
  - `POST /api/app/`: Create a new app
  - `GET /api/app/<id>/`: Retrieve, update, or delete an app

- **Task Endpoints:**
  - `GET /api/quest/`: List all tasks
  - `POST /api/quest/`: Create a new task
  - `GET /api/quest/<id>/`: Retrieve, update, or delete a task

## Templates

The `taskapp` app includes various HTML templates to render different pages of the application:

- **addapp.html**: Page for adding a new app
- **details.html**: Page to view app details
- **login.html**: User login page
- **profile.html**: User profile page
- **task.html**: Page to manage user tasks
- **admin.html**: Admin interface page
- **home.html**: Home page displaying apps and tasks
- **point.html**: Page to view user points
- **sign.html**: User sign-up page

## Points System

The application uses a points system to incentivize user interactions. Users earn points for various actions such as adding apps and completing tasks. Points are displayed on the user's profile and points page.

## Media Management

The application supports media uploads, including:

- **App Icons**: Stored in the `media/icon/` directory.
- **Task Screenshots**: Stored in the `media/images/` directory.

## Development

To contribute to the project, follow these steps:

1. **Fork the repository**.
2. **Create a new branch**:
    ```bash
    git checkout -b feature-name
    ```

3. **Make your changes**.
4. **Commit your changes**:
    ```bash
    git commit -m 'Add some feature'
    ```

5. **Push to the branch**:
    ```bash
    git push origin feature-name
    ```

6. **Open a merge request**.

