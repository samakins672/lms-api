# Library Management System

This is a Library Management System with two independent API services:

- **Frontend API:** Allows users to browse, enroll, and borrow books from the library.
- **Backend/Admin API:** Allows the admin to manage the catalog, users, and borrowed books.

## Features

### Frontend API

- **User Enrollment**: Enroll users using email, first name, and last name.
- **List Books**: View all available books in the catalog.
- **View Book by ID**: Fetch the details of a book by its unique ID.
- **Filter Books**: Filter books by publishers (e.g., Wiley, Apress) or by category (e.g., Fiction, Technology).
- **Borrow Book**: Borrow a book for a specified number of days (if available).

### Backend/Admin API

- **Add New Book**: Add new books to the library catalog.
- **Remove Book**: Remove a book from the catalog.
- **List Users**: Fetch a list of all users.
- **List Borrowed Books**: View which users have borrowed which books.
- **Unavailable Books**: List books that are currently unavailable and display their expected return date.

## Installation

### Prerequisites

- Docker and Docker Compose installed
- Python 3.9+

### Step-by-Step Guide

1. Clone this repository:

   ```bash
   git clone https://github.com/samakins672/lms-api.git
   cd lms-api
   ```

2. Build and run the application using Docker:

   ```bash
   docker-compose up --build
   ```

3. The services will be available at:

   - **Frontend API**: `http://localhost:8000`
   - **Backend/Admin API**: `http://localhost:8001`

4. **Access the database**:

   - Frontend DB: `localhost:5432`
   - Backend DB: `localhost:5433`

### Frontend API Endpoints

- **Enroll User**: `POST /users`
- **List All Books**: `GET /books`
- **Get Book by ID**: `GET /books/{id}`
- **Filter Books**: `GET /books/filter`
  - Example: `?publisher=Wiley&category=Technology`
- **Borrow Book**: `POST /books/borrow/{id}`

### Backend/Admin API Endpoints

- **Add New Book**: `POST /books`
- **Remove Book**: `DELETE /books/{id}`
- **List Users**: `GET /users`
- **List Users with Borrowed Books**: `GET /users/borrowed`
- **Unavailable Books**: `GET /books/unavailable`

### Configuration

You can change the database credentials or API configurations by editing the `docker-compose.yml` and configuration files:

```yaml
# Example in docker-compose.yml
POSTGRES_USER: new_user
POSTGRES_PASSWORD: new_password
POSTGRES_DB: new_frontend_db
```

### Testing

To run the tests for both the frontend and backend APIs, use:

```bash
docker-compose exec frontend pytest
docker-compose exec backend pytest
```

Unit and integration tests are included for the core features.

## Deployment

1. Ensure Docker and Docker Compose are installed on the server.
2. Push your code to the repository.
3. Run the Docker containers using `docker-compose up` on the server.

## Communication Between Services

The two services use separate databases. Communication between the `Frontend API` and `Backend API` is achieved through periodic sync mechanisms (e.g., gRPC, message queues) for updating book availability across services.

## Contact

For any issues or questions, feel free to contact me at [akinyemisamuel170@gmail.com](mailto:akinyemisamuel170@gmail.com).
