# Job Feed Project

This Django project generates an XML job feed compatible with Indeed's requirements. It allows you to add job postings via the Django admin interface and automatically updates the XML feed.

## Setup Instructions

### Prerequisites

- Python (version 3.x recommended)
- Django (version 3.x)

```bash
pip install django
```

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Khanishsuresh/Job_Feed.git
   cd .\jobfeed_project
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt

### Configuration

1. **Database Setup:**
   - Configure your database settings in `settings.py`.
2. **Migrations:**
    ```bash
    python manage.py migrate

### Running the Server
```bash
python manage.py runserver
```
Access the job feed at http://127.0.0.1:8000/jobs/feed/.


### Usage
## Adding Job Postings

1. Using Django Admin Interface:

    - Navigate to http://127.0.0.1:8000/admin/.
    - Log in with your superuser credentials.
    - Click on "Jobs" and then "Add" to create a new job posting.
2. Verifying XML Feed Updates:

    - Visit http://127.0.0.1:8000/jobs/feed/ to verify that the XML feed updates with the new job.
  

### Project Demo

## Home page
![image](https://github.com/user-attachments/assets/4d7d7906-035c-4144-961b-e153c22f2353)

## Feed page
![image](https://github.com/user-attachments/assets/24773f7b-ef2c-48e5-bca9-abe63b83c7d0)

## Admin page
![image](https://github.com/user-attachments/assets/461bde26-957a-4997-af35-47870d6c0216)
