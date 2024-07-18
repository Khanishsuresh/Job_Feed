# Job Feed Project

## Setup Instructions

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Configure the database settings in `settings.py`.
4. Run migrations: `python manage.py migrate`
5. Start the server: `python manage.py runserver`
6. Access the job feed at `http://127.0.0.1:8000/jobs/feed/`.

## Adding Job Postings

- Using Django Admin Interface:
    1. Navigate to the admin interface at http://127.0.0.1:8000/admin/.
    2. Log in with your superuser credentials.
    3. Click on "Jobs" and then "Add" to create a new job posting.
- Verifying XML Feed Updates:
    1. Visit http://127.0.0.1:8000/jobs/feed/ to verify that the XML feed updates with the new job.

