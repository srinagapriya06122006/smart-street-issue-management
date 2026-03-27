# 🚦 Smart Street Issue Management System

## 📌 Project Overview

The **Smart Street Issue Management System** is a web-based application that enables citizens to report public issues such as potholes, garbage accumulation, streetlight failures, and drainage problems.

The system allows authorities to efficiently track, manage, and resolve complaints using an SLA-based escalation mechanism.

---

## 🎯 Objectives

* Provide an easy and user-friendly platform for citizens to report issues
* Enable authorities to manage complaints efficiently
* Implement SLA (Service Level Agreement) for timely resolution
* Improve transparency and accountability in public services

---

## ⚙️ Features

* 📝 Complaint Registration System
* 👤 User Authentication (Citizen & Authority)
* 📊 Multiple Dashboards (Ward, Municipality, District, State)
* ⏱ SLA-based Auto Escalation System
* 🔄 Complaint Status Tracking
* 📷 Image Upload for Proof
* 📍 Location-based Complaint Categorization

---

## 🛠️ Technology Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Django (Python)
* **Database:**

  * SQLite (`db.sqlite3`) – Used for running the application
  * MySQL Dump (`Dump20260327.sql`) – Used for database sharing and recreation

---

## 🗂️ Project Structure

```
smart-street-issue-management/
│
├── backend/
│   ├── db.sqlite3
│   ├── manage.py
│   ├── settings.py
│   └── apps (auth_app, complaint_app, etc.)
│
├── frontend/
│   ├── HTML files
│   ├── css/
│   ├── js/
│
├── Dump20260327.sql
└── README.md
```

---

## 🚀 How to Run the Project

### 🔹 Backend Setup

```
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

### 🔹 Frontend Setup

* Open the frontend HTML files in a browser
  **OR**
* Integrate frontend with Django backend APIs

---

## 🗄️ Database Information

* `db.sqlite3` → Used for running the project locally
* `Dump20260327.sql` → Contains database schema and sample data for external use

---

## 🔄 SLA Auto Escalation (Key Feature)

* Each complaint is assigned a time limit (SLA)
* If not resolved within the given time → automatically escalated
* Timer resets when escalated to the next authority level

---

## 📸 Modules

* Citizen Dashboard
* Authority Dashboard
* Complaint Management
* Escalation Monitoring System

---

## 👨‍💻 Authors

**Srinagapriya**
**Sowndharya**
**Vanitha**

Department of Computer Science and Engineering

---

## 📌 Conclusion

This system enhances urban issue management by ensuring faster response times, efficient monitoring, and structured resolution workflows through automation and smart escalation.
