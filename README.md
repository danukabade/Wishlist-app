# Wishlist-app
A full-stack web application for managing product wishlists. Built with Flask (backend) and React (frontend).
📌 Features
User authentication (if implemented)
CRUD operations for wishlist items
Frontend built with React
Backend powered by Flask & SQLAlchemy
API integration for seamless communication

##Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/danukabade/Wishlist-app.git
cd Wishlist-app

2️⃣ Backend Setup
cd wishlist-app-backend
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt

📌 Database Migration
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

📌 Run Backend Server
python app.py

3️⃣ Frontend Setup
📌 Install dependencies
cd wishlist-frontend
npm install

📌 Start React App
npm start

🔹 Tech Stack
Frontend: React, JavaScript, JSX, CSS
Backend: Flask, Python, SQLAlchemy
Database: SQLite (or your preferred database)
Deployment: GitHub Pages (Frontend)
