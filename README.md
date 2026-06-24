# Daily Diet API

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.0-black.svg)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-8.4-orange.svg)](https://mysql.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue.svg)](https://docker.com/)

---

## Table of Contents

1. [About the Project](#about-the-project)
2. [Features](#features)
3. [Technologies](#technologies)
4. [Installation](#installation)
5. [Database Setup](#database-setup)
6. [Usage](#usage)
7. [API Endpoints](#api-endpoints)
8. [Project Structure](#project-structure)
9. [Author](#author)

---

## About the Project

**Daily Diet API** is a RESTful API built with Flask for managing daily meals and tracking diet adherence.

The project was developed as part of a Rocketseat challenge to practice REST API development, SQLAlchemy persistence, MySQL integration, and CRUD operations.

The API allows users to:

* Register meals
* Update meals
* Delete meals
* List all meals
* Retrieve a specific meal
* Track diet-related metrics

---

## Features

* Create meals
* List all meals
* Retrieve a meal by ID
* Update meals
* Delete meals
* MySQL database integration
* SQLAlchemy ORM
* Dockerized database environment
* JSON standardized responses

---

## Technologies

* Python 3
* Flask
* Flask-SQLAlchemy
* MySQL
* Docker
* PyMySQL

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/FelipeLuizonDev/daily-diet-api.git
```

### 2. Navigate to the project folder

```bash
cd daily-diet-api
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Database Setup

Start the MySQL container:

```bash
docker compose up -d
```

Verify that the container is running:

```bash
docker ps
```

---

## Usage

Run the application:

```bash
python app.py
```

The API will be available at:

```text
http://127.0.0.1:5000
```

---

## API Endpoints

| Method | Endpoint    | Description     |
| ------ | ----------- | --------------- |
| POST   | /meals      | Create a meal   |
| GET    | /meals      | List all meals  |
| GET    | /meals/{id} | Retrieve a meal |
| PUT    | /meals/{id} | Update a meal   |
| DELETE | /meals/{id} | Delete a meal   |

---

## Project Structure

```plaintext
daily-diet-api/
│
├── models/
│   ├── __init__.py
│   └── meal.py
│
├── database.py
├── utils.py
├── app.py
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## Author

**Felipe Luizon**

GitHub: https://github.com/FelipeLuizonDev

LinkedIn: https://linkedin.com/in/felipeluizon
