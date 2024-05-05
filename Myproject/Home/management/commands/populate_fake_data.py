from django.core.management.base import BaseCommand
from faker import Faker
from Home.models import Employee

class Command(BaseCommand):
    help = 'Populate Employee model with fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        try:
            for _ in range(1000000):  # Generate 10lac fake employees
                # Generate a 10-digit phone number
                phone_number = '9' + str(fake.random_number(digits=9))
                employee = Employee(
                    eid=fake.unique.random_number(digits=5),
                    ename=fake.name(),
                    eemail=fake.email(),
                    econtact=phone_number,
                    edept=fake.job(),
                    ecity=fake.city(),
                )
                employee.save()
                print(f'Creating employee: {employee.ename}, {employee.eemail}, {employee.econtact}')  # Print employee details
            self.stdout.write(self.style.SUCCESS('Successfully populated Employee model with fake data'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error: {e}'))
