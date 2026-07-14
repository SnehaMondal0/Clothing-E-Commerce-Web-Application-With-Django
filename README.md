# StyleHaven - Clothing E-Commerce Web Application

StyleHaven is a fully functional e-commerce web application built with **Django**. It features a complete shopping experience with user authentication, product management for managers, and a seamless checkout process.

## 🚀 Features

### 🛒 Customer Features
* **User Authentication:** Secure Signup & Login system.
* **Product Browsing:** Filter products by Category (Men, Women, Kids) and Price.
* **Shopping Bag:** Add to cart, update quantities, and remove items.
* **Checkout System:** Simple checkout flow to place orders.
* **Search Functionality:** Find products instantly.

### 👨‍💼 Manager/Admin Features
* **Manager Dashboard:** Dedicated panel to manage inventory.
* **Product Management:** Add, Edit, and Delete products with image uploads.
* **Order Tracking:** View and manage customer orders.

## 🛠️ Tech Stack
* **Backend:** Python, Django 5.0
* **Frontend:** HTML5, CSS3, Tailwind CSS, JavaScript
* **Database:** SQLite (Default) / PostgreSQL (Production ready)

## 📂 Project Structure

A quick look at the codebase organization:

bash
shop_project/
├── adminApp/            # Manager dashboard & product logic
├── usersApp/            # Customer facing views (Home, Cart, Checkout)
├── templates/           # HTML files (Tailwind integrated)
│   ├── adminApp/        # Admin specific templates
│   ├── userApp/         # Customer specific templates
│   └── base.html        # Main layout wrapper
├── static/              # CSS, JavaScript, and Images
├── media/               # User uploaded product images
├── db.sqlite3           # Database file
└── manage.py            # Django command-line utility

Component	Technology
Backend	Python 3.10, Django 5.0
Frontend	HTML5, Tailwind CSS, JavaScript
Database	SQLite (Dev), PostgreSQL (Production ready)
Version Control	Git & GitHub

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/RevanthKunala/Clothing-E-Commerce-Web-Application-With-Django.git](https://github.com/RevanthKunala/Clothing-E-Commerce-Web-Application-With-Django.git)
    cd Clothing-E-Commerce-Web-Application-With-Django
    ```

2.  **Create a Virtual Environment (Optional but Recommended):**
    ```bash
    python -m venv venv
    # Activate on Windows:
    venv\Scripts\activate
    # Activate on Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run Migrations:**
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (Admin):**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server:**
    ```bash
    python manage.py runserver
    ```

7.  **Access the App:**
    Open your browser and go to `http://127.0.0.1:8000/`

## 📸 Screenshots
*(You can upload screenshots of your Homepage and Dashboard here later)*

## 👤 Author
**Revanth Kunala**
- GitHub: [RevanthKunala](https://github.com/RevanthKunala)
