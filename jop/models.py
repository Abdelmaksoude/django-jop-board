from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
# Create your models here.
JOP_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)
JOP_PLACE = (
    ('Menofia','Menofia'),
    ('Cairo','Cairo'),
    ('Giza','Giza'),
    ('Tanta','Tanta'),
    ('Mansora','Mansora'),
    ('Kafr Elshek','Kafr Elshek'),
    ('6 Octper','6 Octper'),
)
def image_upload(instance , filename):
    imagename , extension = filename.split(".")
    return "jops/%s.%s"%(instance.id,extension)

class Jop(models.Model):
    owner = models.ForeignKey(User , related_name='jop_owner' , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    place = models.CharField(choices=JOP_PLACE , max_length=20)
    Jop_Type = models.CharField(choices=JOP_TYPE , max_length=15)
    Description = models.TextField(max_length=1000)
    Published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1)
    Salary = models.IntegerField(default=0)
    Experiance = models.IntegerField(default=1)
    Category = models.ForeignKey('Category' , on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload)
    slug = models.SlugField(null=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super(Jop,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Apply(models.Model):
    jop = models.ForeignKey(Jop , related_name='apply_jop' , on_delete=models.CASCADE)
    name = models.ForeignKey(User , related_name='user_apply_jop' , on_delete=models.CASCADE)
    cover_letter = models.TextField(max_length=500)
    creted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)
    
class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    comment = models.TextField()

    def __str__(self):
        return str(self.user)