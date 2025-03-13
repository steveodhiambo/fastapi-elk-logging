# **FastAPI Logging with Future ELK Integration**  

This repository contains a **FastAPI application** with **structured logging**. The project currently focuses on **logging with Uvicorn** and will later integrate **the ELK Stack (Elasticsearch, Logstash, Kibana) for centralized log management**.  

## **Current Features**  
✅ FastAPI application with basic routes  
✅ Structured logging using Python’s `logging` module  
✅ Logs stored in `app.log` and displayed in the console  
✅ Middleware support for request logging  
✅ Runs with **Uvicorn**  

---

## **Setup and Installation**  

### **1. Clone the Repository**  
```sh
git clone <repository-url>
cd <repository-folder>
```

### **2. Install Dependencies**  
Ensure you have **Python 3.8+** installed, then run:  
```sh
pip install -r requirements.txt
```

### **3. Run the FastAPI Application with Uvicorn**  
Start the server with:  
```sh
uvicorn main:app --reload
```
The application will be available at:  
📌 **http://localhost:8000**

---

## **API Endpoints**  

| Endpoint        | Method | Description                 |
|---------------|--------|-----------------------------|
| `/`           | GET    | Returns "Hello World"       |
| `/file-upload`| GET    | Placeholder for file uploads |

---

## **Logging Implementation**  

### **Current Logging Setup (`logger.py`)**  
- Logs include timestamps, log levels, filenames, and messages.  
- Logs are saved to `app.log` and printed to the console.  
<!-- - Supports **JSON formatting** (preparation for ELK integration).   -->

<!-- ### **Example Log Output:**  
```json
{
  "timestamp": "2025-03-13 12:00:00",
  "level": "INFO",
  "filename": "main.py",
  "line": 20,
  "message": "FastAPI application started..."
} -->
```

---

## **Future Plans: ELK Stack Integration**  
🚀 **Coming Soon:** This project will integrate **Elasticsearch, Logstash, and Kibana** to:  
- Centralize logs from multiple instances  
- Enable real-time log search and visualization  
- Monitor API performance and errors  

---
<!-- 
## **Next Steps**  
🔹 Improve log formatting and add request metadata  
🔹 Implement ELK stack for centralized logging  
🔹 Create Kibana dashboards for log analysis  

--- -->

## **License**  
This project is licensed under the **MIT License**.  

## **Author**  
[Stephen Odhiambo]  