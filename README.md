# 🚀 CareerLens AI Dashboard

CareerLens is an intelligent full-stack web application that helps users discover job opportunities based on their skills while providing insights into market demand and skill gaps.

---

## ✨ Features

* 💼 **Job Recommendations**
  Get personalized job suggestions based on your skills

* 🔥 **Top In-Demand Skills**
  Analyze which skills are trending in the job market

* 🎯 **Skill Gap Analysis**
  Identify missing skills you need to learn

* 📊 **Interactive Analytics Dashboard**
  Visualize skill demand using dynamic charts

* ⚡ **Fast & Clean UI**
  Premium dashboard-style interface built for real-world usage

---

## 🛠 Tech Stack

### Backend

* Python (Flask)
* PostgreSQL
* psycopg2

### Frontend

* HTML5
* CSS3 (Custom Premium UI)
* Chart.js

### Tools

* Git & GitHub
* Web scraping (Indeed, Naukri - optional modules)

---

## 🧠 How It Works

1. User enters skills (e.g., `python, sql`)
2. Backend processes and normalizes skills
3. Database is queried to:

   * Match jobs with required skills
   * Calculate match score
   * Identify top demanded skills
4. Results are displayed in a dashboard with:

   * Job cards
   * Skill demand list
   * Skill gap insights
   * Chart visualization

---

## 📂 Project Structure

```
career-lens/
│
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── static/
│   │   └── style.css
│   ├── routes.py
│   └── app.py
│
├── analysis/
│   └── recommendation_engine.py
│
├── database/
│   ├── db_connection.py
│   └── schema.sql
│
├── scraper/
│   └── (job scraping modules)
│
├── venv/
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/career-lens.git
cd career-lens
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install flask psycopg2
```

### 4. Setup PostgreSQL

* Create a database (e.g., `careerlens`)
* Run `schema.sql`
* Update credentials in `recommendation_engine.py`

### 5. Run the app

```bash
python -m app.app
```

👉 Open: http://127.0.0.1:5000

---

## 📸 Screenshots
<img width="1470" height="870" alt="Screenshot 2026-03-24 at 11 10 17 AM" src="https://github.com/user-attachments/assets/70b9206d-3fca-4bec-8146-f2a0d07e952e" />

<img width="402" height="482" alt="Screenshot 2026-03-24 at 11 10 37 AM" src="https://github.com/user-attachments/assets/36d4e051-1e2b-4f52-8159-fb40ec35d0ec" />
<img width="401" height="333" alt="Screenshot 2026-03-24 at 11 10 52 AM" src="https://github.com/user-attachments/assets/5ba73fa2-be0b-4d14-9aa0-4dac8aa72ec4" />

<img width="400" height="365" alt="Screenshot 2026-03-24 at 11 11 06 AM" src="https://github.com/user-attachments/assets/d37aecbd-22d3-40ab-89da-4f47b3d9c365" />

---

## 🚀 Future Improvements

* 🔐 User authentication (login/signup)
* 📍 Location-based filtering
* 🤖 ML-based job recommendation system
* 🌐 Deploy on cloud (Render / Railway)
* 📈 Advanced analytics & insights

---

## 🧑‍💻 Author

**Kurian Thomas**

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
