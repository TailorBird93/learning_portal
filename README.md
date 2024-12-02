# Learning Portal

A Django-based e-learning platform where users can browse, purchase, and access tutorials. The project includes user authentication, Stripe payment integration, and an admin panel for tutorial management.

---

## Table of Contents
- [User Stories](#user-stories)
- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Future Enhancements](#future-enhancements)
- [Credits](#credits)
- [License](#license)

---
## User Stories

### As a User:
1. I want to create an account so that I can log in and access my purchased tutorials.
2. I want to browse tutorials by category so that I can easily find content relevant to my interests.
3. I want to view a tutorial's details before purchasing so that I can decide if it meets my needs.
4. I want to purchase a tutorial securely using a payment system so that I can unlock its content.
5. I want to see the chapters of a purchased tutorial so that I can learn in a structured way.
6. I want to access my purchased tutorials from a dashboard so that I can continue learning at my own pace.

### As an Admin:
1. I want to log in to an admin panel so that I can manage the website content.
2. I want to add, edit, or delete tutorials so that the platform stays up-to-date.
3. I want to categorize tutorials so that users can easily browse content.
4. I want to manage user accounts so that I can provide support and ensure security.
5. I want to view and manage Stripe transactions so that I can monitor payments.

### As a Business Owner:
1. I want to showcase my tutorials professionally so that I can attract more users.
2. I want to receive payments securely through Stripe so that I can generate revenue.
3. I want to analyze user activity so that I can improve my tutorials and services.



## Features
- **User Authentication**: Register, login, and logout functionalities.
- **Stripe Payment Integration**: Secure payments for purchasing tutorials.
- **Tutorial Organization**:
  - Tutorials are categorized.
  - Each tutorial contains multiple chapters.
- **Admin Panel**: Manage users, tutorials, and categories.
- **Responsive Design**: Mobile-friendly layout using Bootstrap.

---

## Technologies
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Bootstrap), JavaScript
- **Database**: SQLite (default, can be upgraded to PostgreSQL for production)
- **Payment Gateway**: Stripe

---

## Setup Instructions

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- Git

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/learning_portal.git
   cd learning_portal
2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
4. Create and configure a .env file in the project root:
    ```bash
    SECRET_KEY=your-django-secret-key
    STRIPE_PUBLIC_KEY=your-stripe-public-key
    STRIPE_SECRET_KEY=your-stripe-secret-key
    DEBUG=True
5. Apply the database migrations:
    ```bash
    python manage.py migrate
6.  Create a superuser for accessing the admin panel:
    ```bash
    python manage.py createsuperuser
7.  Start the development server:
    ```bash
    python manage.py runserver
8. Access the app at http://127.0.0.1:8000/.

## Usage

### For Users
1. **Register/Login**: Create an account or log in to your existing account.
2. **Browse Tutorials**: View available tutorials categorized for easier navigation.
3. **Purchase**: Use Stripe to securely purchase a tutorial and unlock its content.
4. **Access Content**: View purchased tutorials and their chapters from your dashboard.

### For Admins
1. Log in to the admin panel at `http://127.0.0.1:8000/admin/`.
2. Manage:
   - **Tutorials**: Add, edit, or delete tutorials.
   - **Categories**: Organize tutorials into meaningful categories.
   - **Users**: View and manage user accounts.


## Future Enhancements
- Add tutorial ratings and reviews to gather feedback.
- Implement a search history feature for improved user experience.
- Introduce a subscription-based model for unlimited access to all tutorials.
- Enable email notifications to notify users about new tutorials or special offers.

---

## Credits
- **Django Documentation**: [https://docs.djangoproject.com/](https://docs.djangoproject.com/)
- **Bootstrap**: [https://getbootstrap.com/](https://getbootstrap.com/)
- **Stripe API**: [https://stripe.com/docs/api](https://stripe.com/docs/api)

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Author
Developed by Bartosz Krawczyk.
