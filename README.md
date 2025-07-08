# GainsGalore 🏋🏾

**GainsGalore** is a Django full-stack web application designed for fitness enthusiasts and personal trainers. It allows users to register, view workout plans, and access premium content through Stripe-powered payments.

---

## 🚀 Features

* **User Authentication**: Secure registration and login system.
* **Custom User Model**: Extended to support profile pictures and roles (coach/client).
* **Workout Plans**:

  * View free & premium plans
  * See descriptions, difficulty levels, and video links
* **Stripe Integration**: Users can upgrade to premium using test Stripe payment flows.
* **Admin Panel**: Admins can manage workouts and users.
* **JavaScript**: Toggle workout plan details dynamically on the homepage.
* **Environment Security**: API keys stored securely using `python-decouple` and `.env` file.

---

## 🛠 Technologies

* Python 3.12
* Django 5.2
* PostgreSQL / SQLite (dev)
* Stripe (Test Mode)
* HTML/CSS + JavaScript
* Git + GitHub for version control

---

## 📂 Project Structure

```
gainsgalore/
├── users/           # Custom user model + auth
├── workouts/        # WorkoutPlan model and views
├── payments/        # Stripe payment handling
├── templates/       # HTML templates (login, register, home)
├── static/          # Static files (optional)
├── .env             # Environment secrets (not pushed)
└── README.md
```

---

## 🔐 Security & Environment

* Stripe and Django secrets are managed with `python-decouple`
* `.env` file is excluded using `.gitignore`
* `DEBUG` should be set to `False` before deploying

---

## 💳 Stripe Test Keys

All payments run in Stripe **test mode**. You can use the test card number `4242 4242 4242 4242` to simulate payments.

---

## 📄 Attribution

* Stripe integration based on [Stripe Docs](https://stripe.com/docs)
* `python-decouple` used for securing environment variables
* Django starter project inspired by course boilerplate

---

## 🧪 Run Locally

```bash
git clone https://github.com/ZacPearce/gainsgalore.git
cd gainsgalore
python -m venv gainsgalore-env
source gainsgalore-env/bin/activate
pip install -r requirements.txt

# Create .env file with your own test keys
python manage.py migrate
python manage.py runserver
```

---


## 🧠 Author

Zachary Pearce

## ⭐ Special Thanks: 

Ebad Majeed, my tutor for the past year for his time help and effort.