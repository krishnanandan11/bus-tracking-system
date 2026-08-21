# Real-Time Bus Tracking System

A **Real-Time Bus Tracking System** designed to track and display the live location of multiple buses on an interactive map. The project aims to provide a simple and efficient way for users, drivers, and administrators to monitor bus locations in real time.

> **Project Status: In Progress**

## Features

* Real-time bus location tracking
* Interactive map using **Leaflet.js** and **OpenStreetMap**
* Support for tracking multiple buses
* Real-time location updates using **Flask-SocketIO**
* Search functionality using bus code or bus number
* Admin panel for managing bus information
* Driver interface for updating bus locations
* User interface for viewing and tracking buses

## Technologies Used

### Backend

* Python
* Flask
* Flask-SocketIO
* SQLite

### Frontend

* HTML
* CSS
* JavaScript
* Leaflet.js

### Maps

* OpenStreetMap

## How It Works

1. The Driver updates the current location of the bus.
2. The location data is sent to the Flask backend.
3. Flask-SocketIO broadcasts the updated location in real time.
4. The User Dashboard displays the bus location on an interactive map.
5. The Admin Panel can manage and monitor available buses.

## Project Structure

```text
Bus-Tracking-System/
│
├── app.py
├── bus.db
├── requirements.txt
│
├── templates/
│   ├── index.html
│   ├── admin.html
│   ├── driver.html
│   └── user.html
│
├── static/
│   ├── css/
│   └── js/
│
└── README.md
```

## Future Improvements

* Add GPS integration for automatic location tracking
* Add user authentication and authorization
* Improve the admin dashboard
* Add bus route information
* Add estimated arrival time (ETA)
* Add notifications for bus arrivals
* Deploy the application online

## Project Goal

The goal of this project is to build a practical **real-time tracking application** using Python and web technologies. It demonstrates the use of **Flask, WebSockets, databases, and interactive maps** to solve a real-world transportation tracking problem.

## Author

**Krishna Nandan**

BCA (AI & Data Science) | Aspiring Data Analyst
