# Notes_App

A simple Notes application built with **FastAPI**, **MongoDB**, and **Bootstrap**. This project demonstrates FastAPI fundamentals, template rendering with Jinja2, and basic CRUD operations with MongoDB.

---

## Features

- **Add Notes:** Create new notes with a title and description.
- **View Notes:** Display all saved notes on the homepage.
- **Responsive UI:** Styled with Bootstrap for modern look and mobile compatibility.

---

## Technologies Used

- **Backend:** FastAPI
- **Frontend:** HTML, Bootstrap, Jinja2
- **Database:** MongoDB (via PyMongo)
- **Environment Management:** python-dotenv

---

## Getting Started

### Prerequisites

- Python 3.7+
- MongoDB instance (local or cloud, e.g., MongoDB Atlas)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/JAIKUMAR07/Notes_App.git
   cd Notes_App
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment:**
   - Create a `.env` file in the root directory.
   - Add your MongoDB URI:
     ```
     MONGO_URI=your_mongodb_uri_here
     ```

4. **Run the app:**
   ```bash
   uvicorn main:app --reload
   ```

5. **Open in browser:**  
   Visit [http://localhost:8000](http://localhost:8000)

---

## Project Structure

```
Notes_App/
│
├── main.py                # FastAPI application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html         # Main HTML template (Bootstrap/Jinja2)
├── static/                # Static files (CSS, JS, images, etc.)
└── .env                   # Environment variables (MongoDB URI)
```

---

## Example Usage

- **Home Page:**  
  Displays a form to add a new note and shows a list of saved notes.

- **Adding Notes:**  
  Fill in the note title and description, submit the form, and the note appears in the list.

---

## Code Highlights

- **FastAPI routes:**  
  - `/` : Home page - displays and adds notes.
  - `/items/{id}` : Placeholder for viewing a single note (expandable).

- **MongoDB Integration:**  
  Uses PyMongo to store and retrieve notes.

---

## Future Improvements

- Edit and delete notes.
- User authentication.
- API endpoints for JSON CRUD.
- Improved U
