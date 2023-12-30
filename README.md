
```markdown
# BIA Assignment

This project uses Django and is dockerized for deployment using Kubernetes on Google Cloud Platform (GCP).

## Setup

### Using GitHub
Clone this repository:
```bash
git clone https://github.com/geekgupta/BIA.git
```

### Using Docker
Pull the Docker image:
```bash
docker pull puru21/bia:0.0.3
```

## Installation

### Manual Installation
1. Create a virtual environment.
2. Run:
   ```bash
   pip install -r requirements.txt
   ```

### Using Docker
Run:
```bash
docker-compose up
```

## Start the Project
Run:
```bash
python manage.py runserver
```

## Deployment
The project is deployed on [http://34.42.249.190/](http://34.42.249.190/) using Kubernetes on GCP.

---

## Task 1: Framework Setup

1. **Django:**
   - Create a new Django project.

2. **Flask:**
   - Set up a new Flask project.

3. Implement a simple route or view that returns a "Hello, Django!" or "Hello, Flask!" message.

- Online: [http://34.42.249.190/](http://34.42.249.190/)
- Offline: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Task 2: RESTful API Development

1. **Django:**
   - Implement a minimal Django REST framework API for managing a collection of items (e.g., books, movies).

2. **Flask:**
   - Implement a minimal Flask RESTful API for managing a collection of items.

3. Include endpoints for retrieving all items and adding a new item.

   - Login: [http://34.42.249.190/account/login/](http://34.42.249.190/account/login/)
     - Request body:
       ```json
       {
         "username": "guptron1@gmail.com",
         "password": "Password"
       }
       ```

   - Registration: [http://34.42.249.190/account/registration/](http://34.42.249.190/account/registration/)

   - API Endpoints ( first generate a token from login API and than use in request header before calling below APIs )  :
     - List all books: [http://34.42.249.190/api/books/](http://34.42.249.190/api/books/)
     - Add new book: [http://34.42.249.190/api/books/](http://34.42.249.190/api/books/)
     - Update book details: [http://34.42.249.190/api/books/<book_id>/](http://34.42.249.190/api/books/<book_id>/)
     - Delete book: [http://34.42.249.190/api/books/<book_id>/](http://34.42.249.190/api/books/<book_id>/)
     - Get book details: [http://34.42.249.190/api/books/<book_id>/](http://34.42.249.190/api/books/<book_id>/)

---

## Task 3: Database Interaction

1. **Django:**
   - Use Django models for database interaction with the API.

2. **Flask:**
   - Use an ORM (e.g., SQLAlchemy) for database interaction.

Check the App folder for details in `models.py` and `view.py`.

---

## Task 4: Authentication (Optional)

1. **Django:**
   - Implement token-based authentication using Django REST framework.

2. **Flask:**
   - Implement token-based authentication using Flask-JWT-Extended.

   - Basic Authentication is also used.
   - JWT authentication is implemented but commented.

   - Login: [http://34.42.249.190/account/login/](http://34.42.249.190/account/login/)
     - Request body:
       ```json
       {
         "username": "guptron1@gmail.com",
         "password": "Password"
       }
       ```

   - Registration: [http://34.42.249.190/account/registration/](http://34.42.249.190/account/registration/)

---

## Task 5: Video Generation (Optional)

1. If time allows, choose a Python library (e.g., MoviePy) for video generation.

2. Implement a basic command or API endpoint to process a sample video file.

   - Video Modification: [http://34.42.249.190/modify_video/](http://34.42.249.190/modify_video/)
     - Request body:
       ```json
       {
         "user_name": "enter text"
       }
       ```

