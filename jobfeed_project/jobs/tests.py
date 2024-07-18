from django.test import TestCase
from .models import Job

class JobModelTest(TestCase):

    def setUp(self):
        Job.objects.create(title="Software Engineer", company="ABC Corp", location="New York", description="Job Description")

    def test_job_creation(self):
        job = Job.objects.get(title="Software Engineer")
        self.assertEqual(job.company, "ABC Corp")