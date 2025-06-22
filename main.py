from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Get Mongo URI from .env
MONGO_URI = os.getenv("MONGO_URI")

# Connect to MongoDB
conn = MongoClient(MONGO_URI)

# Set up FastAPI app
app = FastAPI()

# Static and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Home route
@app.get("/", response_class=HTMLResponse)
async def show_home(request: Request, id: str = ""):
    docs = conn.notes.notes.find({})  # fetch all notes
    newDocs = []
    for doc in docs:
        newDocs.append({
            "id": str(doc["_id"]),  # cast ObjectId to string for HTML
            "note": doc.get("note", "No note found")

        })
    
    return templates.TemplateResponse("index.html", {
        "request": request,
        "newDocs": newDocs
    })

# Item route
@app.get("/items/{id}", response_class=HTMLResponse)
async def show_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {
        "request": request,
        "id": id
    })
