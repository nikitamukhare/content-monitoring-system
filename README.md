# 📌 Content Monitoring System

## 🚀 Project Overview

This is a backend system built using **Django** and **Django REST Framework** that monitors content based on predefined keywords.

It scans content, assigns relevance scores, generates flags, and avoids duplicate alerts using suppression logic.

---

## ⚙️ Tech Stack

* Python
* Django
* Django REST Framework
* SQLite

---

## 📊 Features

### ✅ Keyword Management

* Add keywords via API
* Stored in database

### ✅ Content Management

* Add content (title & body)
* Used for scanning

### ✅ Content Scanning

* Matches keywords with content
* Generates flags with scores

### ✅ Scoring Logic

* Exact match in title → **100**
* Partial match in title → **70**
* Match in body → **40**

### ✅ Flag Review System

* Status options:

  * `pending`
  * `relevant`
  * `irrelevant`
* Stores review timestamp

### ✅ Suppression Logic

* If a flag is marked **irrelevant**, it is not shown again
* Unless the content is updated (`last_updated` field)

---

## 🔌 API Endpoints

### ➤ Create Keyword

```
POST /keywords/
```

### ➤ Create Content

```
POST /content/
```

### ➤ Scan Content

```
POST /scan/
```

### ➤ Get All Flags

```
GET /flags/
```

### ➤ Update Flag Status

```
PATCH /flags/{id}/
```

---

## ▶️ How to Run the Project

1. Clone the repository:

```
git clone https://github.com/nikitamukhare/content-monitoring-system.git
```

2. Navigate to project folder:

```
cd content-monitoring-system
```

3. Create virtual environment:

```
python -m venv venv
```

4. Activate virtual environment:

```
venv\Scripts\activate
```

5. Install dependencies:

```
pip install -r requirements.txt
```

6. Apply migrations:

```
python manage.py migrate
```

7. Run server:

```
python manage.py runserver
```

---

## 🧠 Assumptions

* Used manual/mock content instead of external APIs
* Simple keyword matching logic implemented
* SQLite used for simplicity

---

## 🏗️ Project Structure

* `views.py` → API handling
* `services.py` → business logic
* `models.py` → database models
* `serializers.py` → data conversion

---

## 🎯 Key Highlight

Implemented **suppression logic** to prevent duplicate irrelevant alerts by comparing `reviewed_at` with `last_updated`.

---

## 👩‍💻 Author

**Nikita Mukhare**
