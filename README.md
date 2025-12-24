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
    └───Dentist
        ├───account_app
        │   ├───migrations
        │   │   └───__pycache__
        │   ├───static
        │   └───__pycache__
        ├───assets
        ├───Dentist
        │   └───__pycache__
        ├───dentist_info_app
        │   ├───migrations
        │   │   └───__pycache__
        │   ├───static
        │   │   ├───css
        │   │   └───images
        │   └───__pycache__
        ├───media
        │   └───images
        └───template
            ├───account
            └───dentist_info
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

