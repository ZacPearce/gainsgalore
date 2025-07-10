# GainsGalore 🏋🏾

**GainsGalore** is a Django full-stack web application designed for fitness enthusiasts and personal trainers. It allows users to register, view workout plans, and access premium content through Stripe-powered payments.

---

## 🚀 Features

- **User Authentication**: Secure registration and login system.
- **Custom User Model**: Extended to support profile pictures and roles (coach/client).
- **Workout Plans**:
  - View free & premium plans
  - See descriptions, difficulty levels, and video links
- **Stripe Integration**: Users can upgrade to premium using test Stripe payment flows.
- **Admin Panel**: Admins can manage workouts and users.
- **JavaScript**: Toggle workout plan details dynamically on the homepage.
- **Bootstrap 5**: For quick, responsive styling.
- **Environment Security**: API keys stored securely using `python-decouple` and `.env` file.

---

## 🛠 Technologies

- Python 3.12
- Django 5.2
- PostgreSQL / SQLite (dev)
- Stripe (Test Mode)
- HTML, CSS + JavaScript
- Bootstrap 5
- Git + GitHub for version control

---

## 📂 Project Structure

```
gainsgalore/
├── users/             # Custom user model + authentication
├── workouts/          # WorkoutPlan model and views
├── payments/          # Stripe payment handling
├── templates/         # HTML templates (login, register, home)
├── static/            # Static files including CSS
│   └── css/
│       └── style.css
├── .env               # Environment secrets (not pushed to GitHub)
├── requirements.txt   # Python dependencies
├── build.sh           # Render build script
├── render.yaml        # Render deployment config
└── README.md
```

---

## 🔐 Security & Environment

- Stripe and Django secrets are managed with `python-decouple`
- `.env` file is excluded using `.gitignore`
- `DEBUG` is turned off in production for safety

---

## 💳 Stripe Test Keys

All payments run in Stripe **test mode**. You can use the test card number below to simulate payments: 

- Card Number: 4242 4242 4242 4242
- Expiry: Any future date
- CVC: Any 3 digits
- ZIP: Any 5 digits

---

## 🧪 Manual Testing

The following features were manually tested:

- ✅ **User registration & login**: Forms validate correctly. Invalid submissions are blocked.
- ✅ **Workout access**: Free workouts are visible to all. Premium workouts hidden unless payment is made.
- ✅ **Stripe checkout**: Test cards simulate both successful and failed payments.
- ✅ **JavaScript toggling**: Clicking a workout title expands/collapses details smoothly.
- ✅ **Responsive layout**: Layout adapts across mobile, tablet, and desktop via Bootstrap 5.

---

## 🧠 Author

**Zachary Pearce**

---

## ⭐ Special Thanks

**Ebad Majeed**, my tutor for the past year — thank you for your time, help, and effort.

---

## 📄 Attribution

- Stripe integration based on [Stripe Docs](https://stripe.com/docs)
- `python-decouple` used for managing environment variables
- Django starter project inspired by course boilerplate

---

## 🧰 Run Locally

```bash
git clone https://github.com/ZacPearce/gainsgalore.git
cd gainsgalore
python -m venv gainsgalore-env
source gainsgalore-env/bin/activate
pip install -r requirements.txt

# Add your .env file with Stripe test keys
python manage.py migrate
python manage.py runserver
