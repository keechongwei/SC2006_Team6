# SC2006 Team 6 Web Application

This project is a web application built using **Vue.js (Frontend)** and **Flask (Backend)**. It includes features such as **user authentication, educational institution search, career advice,**.


---

# 🚀 Getting Started

This guide will help you set up the **frontend (Vue.js)** and **backend (Flask)** on your local machine.

## 🛠 Prerequisites
Ensure you have the following installed:

### **Windows & macOS**
1. **Node.js (for Vue.js)**
   - Download & install: [https://nodejs.org/](https://nodejs.org/)
   - Check installation:
     ```
     node -v
     npm -v
     ```

2. **Python 3 (for Flask)**
   - Download & install: [https://www.python.org/](https://www.python.org/)
   - Check installation:
     ```
     python --version
     ```

3. **MongoDB (for Database)**
   - Download & install: [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community)
   - Ensure MongoDB is running:
     ```
     mongod --version
     ```

---

# 📌 Setting Up the Backend (Flask)
### **1️⃣ Navigate to the Backend Directory**
```
cd backend
```
2️⃣ Create the virtual environment
`python -m venv venv`
3️⃣ Activate the Virtual Environment

Windows:
`venv\Scripts\activate`

macOS/Linux:
`source venv/bin/activate`

4️⃣ Install Dependencies
`pip install -r requirements.txt`

5️⃣ Start MongoDB (If Not Running)
`mongod`

6️⃣ Run the Flask Server
`python app.py`

# 📌 Setting Up the Backend (Flask)
1️⃣ Navigate to the Frontend Directory
`cd frontend`

2️⃣ Install Dependencies
`npm install`
3️⃣ Start the Vue.js Development Server
`npm run serve`

