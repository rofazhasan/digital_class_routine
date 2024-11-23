
# **Class Schedule Web Application**

This project is a dynamic class routine web application built using Flask, Tailwind CSS, and PostgreSQL. It displays the current class with a real-time countdown timer, along with the schedule for the day. The application also includes real-time updates using WebSockets and an animated UI with hover interactions.

---

## **Features**

### 🕒 **Real-Time Class Updates**
- Shows the current class with details such as:
  - **Subject Name**
  - **Teacher Name**
  - **Room Number**
- Includes a countdown timer indicating how much time is left for the current class to end.

### 💡 **Dynamic UI**
- **Smooth Horizontal Scrolling:** The current class section scrolls from left to right, pausing when the cursor hovers over it.
- **Color Changes on Hover:** The current class section changes color and highlights details when hovered.

### 🎨 **Complementary Color Scheme**
- Background and component colors are designed using complementary color theory for a professional look.
- Tailwind CSS ensures a responsive and modern design.

### 📡 **Real-Time Data with WebSockets**
- WebSocket integration allows for real-time updates of class schedules and current class information.

---

## **Technologies Used**

### Backend:
- **Flask**: Python web framework to handle routes and server logic.
- **Socket.IO**: Real-time communication between server and client.
- **PostgreSQL**: Database for storing class schedules.

### Frontend:
- **HTML/CSS**: Structuring and styling the web pages.
- **Tailwind CSS**: Modern CSS framework for designing responsive UIs.
- **JavaScript**: Handles countdown timer logic, animations, and WebSocket integration.

---

## **Installation Instructions**

### **1. Clone the Repository**
```bash
git clone https://github.com/rofazhasan/digital_class_routine.git
cd class-schedule-app
```

### **2. Set Up the Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Set Up PostgreSQL**
1. **Create a Database:**
   ```sql
   CREATE DATABASE class_schedule;
   ```
2. **Update Configuration:** Modify `config.py` with your PostgreSQL credentials.

3. **Run Migrations:**
   ```bash
   flask db upgrade
   ```

### **5. Run the Application**
```bash
flask run
```

### **6. Access the App**
- Open your browser and go to `http://localhost:5000`

---

## **Folder Structure**

```
class-schedule-app/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   └── index.html
│   └── config.py
├── migrations/
├── requirements.txt
└── README.md
```

---

## **Usage**

1. **Add Classes:** Update the `classes` table in PostgreSQL with details like subject, teacher, and room number.
2. **WebSocket Interaction:** The app will automatically fetch and display the current class with real-time countdowns.

---

## **Future Enhancements**
- **Admin Panel:** For adding and managing class schedules.
- **User Authentication:** Secure access for teachers and students.
- **Mobile App:** Develop a responsive version for mobile devices.

---

## **Developer**
- **Md. Rofaz Hasan Rafiu**  
- **Contact:** [mdrofazhasanrafiu@gmail.com](mailto:mdrofazhasanrafiu@gmail.com)  
- **LinkedIn:** [Md. Rofaz Hasan Rafiu](https://www.linkedin.com/in/md-rofaz-hasan-rafiu)  

---

Enjoy using the Class Schedule App! 🚀
