# 🌐 Django Blog

A modern blog application built with Django that allows users to create, browse, and interact with blog posts. The project includes user authentication, profile management, comments, tags, search functionality, and password recovery.

> 🚧 This project is currently under active development. More features and UI improvements are being added regularly.

---

## ✨ Features

- 📝 Create and manage blog posts
- 🔍 Search posts
- 🏷️ Tag-based filtering
- 💬 Comment system
- 👤 User registration and authentication
- 🖼️ User profiles with profile pictures
- 🔗 Social media links (GitHub, LinkedIn, Instagram, Website)
- 🔐 Password change and password reset via email
- 📱 Responsive design (Work in Progress)

---

## 🛠️ Tech Stack

- Python
- Django
- HTML5
- CSS3
- SQLite
- Django Taggit
- Django Sitemap
- Gmail SMTP (for email authentication)

---

## 📂 Project Structure

```text
mySite/
│
├── accounts/
├── blog/
├── mySite/
├── manage.py
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

```bash
python -m venv env
```

Activate it:

**Windows**

```bash
env\Scripts\activate
```

**macOS/Linux**

```bash
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
SECRET_KEY=your_secret_key

EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password

DEBUG=True
```

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 📸 Screenshots

Screenshots will be added as the UI evolves.

---

## 📚 Learning Goals

This project is being developed to strengthen my understanding of:

- Django Framework
- Authentication & Authorization
- Database Design
- Template Inheritance
- Responsive Web Design
- Full-Stack Web Development
- Deployment Best Practices

---

## 👩‍💻 Author

**Ishani Basu**

- GitHub: https://github.com/ishanibasu
- LinkedIn: https://www.linkedin.com/in/ishani-basu-113945328
