# TaskFlow - Task Management System
TaskFlow is a web-based Task Management System developed using Django that helps users efficiently create, organize, update, and track their daily tasks. The application provides a clean and user-friendly interface for managing personal productivity and task workflows.

## 🚀 Features

* Create new tasks
* View all tasks
* Update existing tasks
* Delete completed or unwanted tasks
* User profile management
* Responsive and intuitive interface
* Django-powered backend architecture
* Template inheritance for efficient UI development

## 🛠️ Technologies Used

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* JavaScript

### Database

* SQLite

### Version Control

* Git
* GitHub

## 📂 Project Structure

```text
taskflow/
├── base/
│   ├── migrations/
│   ├── templates/
│   │   ├── home.html
│   │   ├── read_task.html
│   │   ├── update_task.html
│   │   ├── delete_task.html
│   │   └── profile.html
│   ├── admin.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── myproject/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── static/
│   ├── css/
│   └── js/
│
├── templates/
│   ├── main.html
│   └── nav.html
│
├── manage.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/taskflow.git
```

### Navigate to the Project Directory

```bash
cd taskflow
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Run the Development Server

```bash
python manage.py runserver
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

## 📸 Screenshots
<img width="1919" height="917" alt="image" src="https://github.com/user-attachments/assets/d8b45b99-3570-4af4-add2-e55958df18fd" />
<img width="1913" height="910" alt="image" src="https://github.com/user-attachments/assets/c22266aa-07d1-4d1f-8c88-516ce243b7d0" />
<img width="1908" height="842" alt="image" src="https://github.com/user-attachments/assets/04541e50-79e0-488a-a4cb-9d4277a1c638" />


## 🎯 Learning Objectives

* Django Web Development
* CRUD Operations
* Database Integration
* Template Inheritance
* User Interface Design
* Project Structure Organization
* Git and GitHub Workflow

## 🔮 Future Enhancements

* User Authentication System
* Task Prioritization
* Task Categories
* Due Date Reminders
* Search and Filter Tasks
* Dashboard Analytics
* Dark Mode Support

## 👩‍💻 Author

Keerthana K R
Engineering Student | Aspiring Web Developer | Data Science Enthusiast

## 📄 License

This project is created for educational and portfolio purposes.
