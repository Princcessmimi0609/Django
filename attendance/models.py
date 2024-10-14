from django.db import models, transaction
from multiselectfield import MultiSelectField


# Define choices for the name field
NAME_CHOICES = (
    ('Bob', 'Bob'),
    ('Alice', 'Alice'),
    ('John', 'John'),
)

# Define choices for the category field
CATEGORY_CHOICES = (
    ('Baptized', 'Baptized'),
    ('Confirmed', 'Confirmed'),
    ('Visitor', 'Visitor'),
)

# Define choices for the meeting field
MEETING_CHOICES = (
    ('team', 'Team Meeting'),
    ('client', 'Client Meeting'),
    ('project', 'Project Meeting'),
)

# Define choices for attended as radio button options
ATTENDED_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('zoom', 'Zoom'),
)

class Attendance(models.Model):
    attendance_number = models.PositiveIntegerField(unique=True, editable=False)
    name = MultiSelectField(choices=NAME_CHOICES, default=['Bob'])
    category = MultiSelectField(choices=CATEGORY_CHOICES, default=['Baptized'])
    email_address = models.EmailField(max_length=100, blank=True, null=True)
    meeting = MultiSelectField(choices=MEETING_CHOICES, default=['team'])
    remarks = models.CharField(max_length=50, blank=True, null=True)
    date_of_meeting = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    attended = models.CharField(max_length=5, choices=[('yes', 'Yes'), ('no', 'No')], default='no')

    def save(self, *args, **kwargs):
        if not self.attendance_number:
            with transaction.atomic():
                # Retrieve the last attendance number in a transaction-safe way
                last_attendance = Attendance.objects.select_for_update().order_by('-attendance_number').first()
                self.attendance_number = last_attendance.attendance_number + 1 if last_attendance else 1
        super().save(*args, **kwargs)



    def __str__(self):
        return f'Attendance: {self.name}'
