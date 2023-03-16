from django.db import models

# Create your models here.
SITUATION=(
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Disapproved','Disapproved')
)

class Candidate(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    job=models.CharField(max_length=5)
    email=models.EmailField(max_length=50)
    Age=models.CharField(max_length=2)
    phone=models.CharField(max_length=15)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    Situation = models.CharField(max_length=50,null=True,choices=SITUATION)

    #Captilize (FirstName and LastName)
    def clean(self):
        self.firstname=self.firstname.capitalize()
        self.lastname=self.lastname.capitalize()
    def __str__(self):
        return self.firstname
    

