# 🧠 Backend Intern Project - Slab 2

This repository contains the **backend solutions** developed as part of the **Slab 2 tasks** for the CodeX Backend Internship. It includes two complete backend systems built using Flask and SQLAlchemy:

- 📅 **Event Management System**
- 💼 **Job Portal System**

---

## 📁 Folder Structure

backend_intern_project_slab_2/
│
├── event_management/ # Event management backend app
│ ├── app/
│ ├── run.py
│ └── requirements.txt
│
├── job_portal/ # Job portal backend app
│ ├── app/
│ ├── run.py
│ └── requirements.txt
│
└── README.md


---

## 🔧 Technologies Used

- **Python 3.11+**
- **Flask**
- **Flask-JWT-Extended**
- **Flask-CORS**
- **SQLAlchemy**
- **SQLite** (for local DB)
- **Postman** (for API testing)

---

## 📅 Event Management System

### ✨ Features
- User Registration & Login (with JWT)
- Admin-only Event Creation
- Event Registration by Users
- Attendee List View
- Cancel Registration

### 🔐 Role-based Access
- `admin` – Can create/manage events
- `user` – Can register for and cancel events

---

## 💼 Job Portal System

### ✨ Features
- User & Recruiter Registration/Login (JWT)
- Job Postings by Recruiters
- Job Applications by Users
- View Applied Jobs
- Admin access for moderation (if needed)

---

## 🚀 How to Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/Nayonika28/backend_intern_project_slab_2.git
cd backend_intern_project_slab_2

# 2. Set up a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Navigate to each project and install dependencies
cd event_management
pip install -r requirements.txt

# 4. Run the app
python run.py

# Similarly for job_portal:
cd ../job_portal
pip install -r requirements.txt
python run.py

📬 API Testing
All APIs were tested using Postman with Bearer Token Authentication.

Example headers:
Authorization: Bearer <JWT_TOKEN>
Content-Type: application/json

👩‍💻 Developer
Nayonika P
Backend Developer Intern
GitHub Profile
