<h1 align="center">DentistFinder</h1>

<p align="center">	
  <a href="https://github.com/Mohammad533643/Dentist_site/blob/main/LICENSE.md" target="_blank">
    <img alt="License: MIT" src="https://img.shields.io/github/license/Mohammad533643/Dentist_site?color=informational" />
  </a>

  <img alt="Repo size" src="https://img.shields.io/github/repo-size/Mohammad533643/Dentist_site?color=informational" />
</p>

<p align="center">
  <img alt="Short GIF of the website" src="https://github.com/Mohammad533643/Dentist_site/blob/main/Dentist/assets/DentistFinder.gif" target="_blank">
</p>
<br>

### Project structure

```Bash
Dentist_site
    │   LICENSE.md
    │   README.md
    │   
    └───Dentist
        │   .gitignor
        │   db.sqlite3
        │   manage.py
        │   requirments.txt
        │   
        ├───account_app
        │   │   admin.py
        │   │   apps.py
        │   │   models.py
        │   │   tests.py
        │   │   urls.py
        │   │   views.py
        │   │   __init__.py
        │   │   
        │   ├───migrations
        │   │   │   __init__.py
        │   │   │   
        │   │   └───__pycache__
        │   │           __init__.cpython-313.pyc
        │   │
        │   ├───static
        │   │       change_password.css
        │   │       register.css
        │   │       
        │   └───__pycache__
        │           admin.cpython-313.pyc
        │           apps.cpython-313.pyc
        │           models.cpython-313.pyc
        │           urls.cpython-313.pyc
        │           views.cpython-313.pyc
        │           __init__.cpython-313.pyc
        │
        ├───assets
        │       DentistFinder.gif
        │       
        ├───Dentist
        │   │   asgi.py
        │   │   settings.py
        │   │   urls.py
        │   │   wsgi.py
        │   │   __init__.py
        │   │
        │   └───__pycache__
        │           settings.cpython-313.pyc
        │           urls.cpython-313.pyc
        │           wsgi.cpython-313.pyc
        │           __init__.cpython-313.pyc
        │
        ├───dentist_info_app
        │   │   admin.py
        │   │   apps.py
        │   │   forms.py
        │   │   models.py
        │   │   seializers.py
        │   │   signals.py
        │   │   tests.py
        │   │   urls.py
        │   │   views.py
        │   │   __init__.py
        │   │
        │   ├───migrations
        │   │   │   0001_initial.py
        │   │   │   0002_dentist_profile_img_alter_dentist_user_id.py
        │   │   │   0003_booking_alter_dentist_profile_img.py
        │   │   │   0004_booking_appointment_id.py
        │   │   │   0005_booking_date_now.py
        │   │   │   0006_rename_date_booking_date_booking_and_more.py
        │   │   │   0007_booking_patient_alter_booking_appointment_id.py
        │   │   │   0008_alter_booking_dentist_id.py
        │   │   │   0009_remove_booking_dentist_id_booking_dentist.py
        │   │   │   0010_alter_booking_date_booking_contact.py
        │   │   │   0011_dentist_city.py
        │   │   │   0012_alter_dentist_profile_img.py
        │   │   │   __init__.py
        │   │   │
        │   │   └───__pycache__
        │   │           0001_initial.cpython-313.pyc
        │   │           0002_dentist_profile_img_alter_dentist_user_id.cpython-313.pyc
        │   │           0003_booking_alter_dentist_profile_img.cpython-313.pyc
        │   │           0004_booking_appointment_id.cpython-313.pyc
        │   │           0005_booking_date_now.cpython-313.pyc
        │   │           0006_rename_date_booking_date_booking_and_more.cpython-313.pyc
        │   │           0007_booking_patient_alter_booking_appointment_id.cpython-313.pyc
        │   │           0008_alter_booking_dentist_id.cpython-313.pyc
        │   │           0009_remove_booking_dentist_id_booking_dentist.cpython-313.pyc
        │   │           0010_alter_booking_date_booking_contact.cpython-313.pyc
        │   │           0010_contact.cpython-313.pyc
        │   │           0011_contact_date_now_alter_booking_date_booking.cpython-313.pyc
        │   │           0012_alter_contact_date_now_alter_contact_gmail.cpython-313.pyc
        │   │           0013_alter_contact_date_now.cpython-313.pyc
        │   │           0014_alter_contact_date_now.cpython-313.pyc
        │   │           __init__.cpython-313.pyc
        │   │
        │   ├───static
        │   │   ├───css
        │   │   │       appointment.css
        │   │   │       base.css
        │   │   │       booking.css
        │   │   │       contact.css
        │   │   │       dentists.css
        │   │   │
        │   │   └───images
        │   │           default.png
        │   │
        │   └───__pycache__
        │           admin.cpython-313.pyc
        │           apps.cpython-313.pyc
        │           forms.cpython-313.pyc
        │           models.cpython-313.pyc
        │           seializers.cpython-313.pyc
        │           urls.cpython-313.pyc
        │           views.cpython-313.pyc
        │           __init__.cpython-313.pyc
        │
        ├───media
        │   └───images
        │           abstract-futuristic-technology-background-vector.jpg
        │           dentist_1.jpg
        │           Dentist_2.jpg
        │           dentist_3.jpg
        │
        └───template
            ├───account
            │       change_password.html
            │       login.html
            │       sign_up.html
            │
            └───dentist_info
                    base.html
                    booking.html
                    contact.html
                    dentists.html
                    home.html
                    message.html
                    search.html
                    user_appointments.html
```

# 📝 Features

✅ This website allows you to find a dentist and book an appointment (of course, this is just a practice project).<br/>
✅ This website is compatible with all browsers.<br>

<br>

# 💻 Technologies used

<p align="center">
  <img alt="HTML5" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" />
  <img alt="CSS3" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" />
  <img alt="Django" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img alt="Django REST Framework" src="https://img.shields.io/badge/Django_REST_Framework-092E20?style=for-the-badge&logo=django&logoColor=white" />
  <img alt="SQLite" src="https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white" />
</p>

<br>

# 🎨 Frontend Technologies

This project utilizes the following frontend technologies:

- **HTML5** (🌐): The core markup language for the website.
- **CSS3** (🖌️): Styles for designing the website and creating a beautiful UI.
<br>

# 💻 Backend Technologies

This project utilizes the following backend technologies:

- **Django** (⚙️):<br>
        django-import-export: For download data from the database in certain file formats such as CSV, XML, etc., in the admin dashboard.<br>
        django-spectacular: For automatically generating documentation and an OpenAPI UI for APIs in Swagger and Redoc.
- **Django REST Framework** (🌐): For building robust APIs(JWT for Athentication).
- **SQLite** (🗃️): The default Django database for managing data.. 

# 🚀 Installation and Setup

Follow the steps below to get your project up and running.
<br>

### Prerequisites

Before starting, make sure Git is installed on your device; otherwise, install it and then open the project according to the steps below.

### 1. Clone the repository

First, clone the repository to your local devie:

```bash
git clone https://github.com/Mohammad533643/Dentist_site.git
```

Then change your directory to:
```Bash
cd Dentist_site/Dentist
```

### 2. Set up a virtual environment (optional but recommended)

It’s recommended to use a virtual environment for your Python projects. You can create one using the following commands:

```Bash
pip install pipenv
```

### 3. Install dependencies
Install the required Python packages using pipenv:
```Bash
pipenv install -r requirements.txt
```
### 4. Configure the database

This project uses SQLite3 by default, Just run the following command to set up the database tables:

```Bash
py manage.py migrate
```

### 5. Access the admin panel (recommended)

To access the admin panel and use the important features of the website create a superuser by this command: 

```Bash
py manage.py createsuperuser
```

### 6. Run the project

After everything is set up, you can run the development server with the following command:

```Bash
py manage.py runserver
```

If you have any suggestions or criticisms, I would be happy to share them with me in
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mohammadmahdi-rajaei-628009350?utm_source=share&utm_campaing=share_via&utm_content=profile&utm_medium=android_app).

