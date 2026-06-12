# Healthcare Backend API

A REST API for a healthcare application built with Django, DRF, PostgreSQL, and JWT authentication.

## Setup

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your DB credentials (see `.env` example below)
4. Run migrations: `py manage.py migrate`
5. Start server: `py manage.py runserver`

## .env
SECRET_KEY=your-secret-key
DEBUG=True
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your-password
DB_HOST=localhost
DB_PORT=5432

## API Endpoints
- POST /api/auth/register/
- POST /api/auth/login/
- GET/POST /api/patients/
- GET/PUT/DELETE /api/patients/<id>/
- GET/POST /api/doctors/
- GET/PUT/DELETE /api/doctors/<id>/
- GET/POST /api/mappings/
- GET/DELETE /api/mappings/<id>/