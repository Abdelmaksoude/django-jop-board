from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from multiselectfield import MultiSelectField

# Create your models here.

TRAINING = (
    ('SAS Programming Course','SAS Programming Course'),
    ('Java Programming Course','Java Programming Course'),
    ('ITI-Frontend Development','ITI-Frontend Development'),
    ('ITI-Backend Development','ITI-Backend Development'),
    ('ITI-Machine Learning Development','ITI-Machine Learning Development'),
    ('ITI-Graphic Development','ITI-Graphic Development'),
    ('JavaScript Course','JavaScript Course'),
    ('Linux Programming Course','Linux Programming Course'),
    ('C++ Programming Course','C++ Programming Course'),
    ('Python Programming Course','Python Programming Course'),
    ('Introduction to TCP/IP','Introduction to TCP/IP'),
    ('Cisco CCNP Enterprise-ENARSI','Cisco CCNP Enterprise-ENARSI'),
)

NATIONALITY = (
    ('Egyption','Egyption'),
    ('Saudi Arabian','Saudi Arabian'),
    ('Emirati','Emirati'),
    ('American','American'),
    ('French','French'),
    ('German','German'),
    ('Spanish','Spanish'),
    ('Italian','Italian'),
    ('Russian','Russian'),
)

GENDER = (
    ('Male','Male'),
    ('Female','Female'),
)

COUNTRY = (
    ('Egypt','Egypt'),
    ('Saudi Arabia','Saudi Arabia'),
    ('Emarat','Emarat'),
    ('America','America'),
    ('France','France'),
    ('Germany','Germany'),
    ('Spain','Spain'),
    ('Italy','Italy'),
    ('Russia','Russia'),
)

CATOGRIES = (
    ('Front-end development','Front-end development'),
    ('Back-end development','Back-end development'),
    ('Full-stack development','Full-stack development'),
    ('Mobile development','Mobile development'),
    ('Data science','Data science'),
)

YEARSEXPERIANCE = (
    ('No Experience','No Experience'),
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
    ('More than 5 years of experience','More than 5 years of experience'),
)

LEVELEDUCATION = (
    ('Bachelor Student','Bachelor Student'),
    ('Bachelor Degree','Bachelor Degree'),
    ('Master Degree','Master Degree'),
    ('PHD Degree','PHD Degree'),
    ('No Degree','No Degree'),
)

FACULTY = (
    ('Faculty of computer and information','Faculty of computer and information'),
    ('Faculty of Computers and Artificial Intelligence','Faculty of Computers and Artificial Intelligence'),
    ('Faculty of Engineering and Technology','Faculty of Engineering and Technology'),
    ('Faculty of Computer Science and Information Technology','Faculty of Computer Science and Information Technology'),
    ('Faculty of Computers and Artificial Intelligence','Faculty of Computers and Artificial Intelligence'),
    ('Other','Other')
)

DEPARTMENT = (
    ('Computer Science','Computer Science'),
    ('Information Technology','Information Technology'),
    ('Information Science','Information Science'),
    ('General','General'),
    ('Soft','Soft'),
    ('Bio','Bio'),
    ('No department in my faculty','No department in my faculty'),
)

GRADUATIONYEAR = (
    ('2023','2023'),
    ('2024','2024'),
    ('2025','2025'),
    ('2026','2026'),
    ('2027','2027'),
    ('2028','2028'),
    ('2029','2029'),
    ('I am graduated','I am graduated'),
)

LANGUAGES = (
    ('Arabic','Arabic'),
    ('English','English'),
    ('Spanish','Spanish'),
    ('German','German'),
    ('Italian','Italian'),
    ('Frensh','Frensh'),
)

WORKTIME = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
    ('Freelanc / Project','Freelanc / Project'),
    ('Intership','Intership'),
    ('Student Activaty','Student Activaty'),
    ('Volunteering','Volunteering'),
)

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    bio = models.CharField(max_length=1000)
    country = models.CharField(choices=COUNTRY , max_length=100)
    city = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to='profile/' , default='blank-profile-picture.png' , null=True , blank=True)
    experiance1 = models.CharField(choices=TRAINING , max_length=100)
    experiance2 = models.CharField(choices=TRAINING , max_length=100)
    cv = models.FileField(upload_to='cvProfile/',default='Course_Certificate_En_Database_Fundamentals.pdf' )
    githublink = models.URLField(max_length=150 , unique=True , null=True , db_index=True)
    linkedinlink = models.URLField(max_length=150 , unique=True , null=True , db_index=True)
    nationality = models.CharField(choices=NATIONALITY , max_length=100)
    birthday = models.DateField(auto_now=False , blank=True , null=True)
    gender = models.CharField(choices=GENDER , max_length=50)
    typejop = MultiSelectField(choices=WORKTIME , max_length=100)
    categories = models.CharField(choices=CATOGRIES , max_length=100)
    salary = models.IntegerField(default=4000)
    experianceyears = models.CharField(choices=YEARSEXPERIANCE , max_length=50)
    leveleducation = models.CharField(choices=LEVELEDUCATION , max_length=100)
    faculty = models.CharField(choices=FACULTY , max_length=100)
    department = models.CharField(choices=DEPARTMENT , max_length=100)
    graduationyear = models.CharField(choices=GRADUATIONYEAR , max_length=100)
    languages = MultiSelectField(choices=LANGUAGES , max_length=100)

    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

class WorkTime(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Languages(models.Model):
    languagename = models.CharField(max_length=50)

    def __str__(self):
        return self.languagename