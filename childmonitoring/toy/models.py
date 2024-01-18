
from django.db import models
from django.db.models.fields import TimeField

from childmonitoring.settings import TIME_ZONE

# Create your models here.
class StudyLevel(models.TextChoices):
    FirstYear=('1st','FirstYear')
    SecondYear=('2nd','SecondYear')
class person(models.Model):
#id=models.BigAutoField(primary_key=True)
    firstName=models.CharField(name='first_name', max_length=50 )
    lastName=models.CharField(name='_name', max_length=50 )
    birthDate=models.DateField(null=True , blank=True )
    photo=models.ImageField( null=True , blank=True, upload_to='media')
    class Meta :
        abstract = True 
        ordering=['first_name','last_name']
class Parent(person):
    #pass
    class Meta :
      db_table="parent"



class Child(person):
    #id=models.BigAutoField(primary_key=True)
    
    study_level=models.CharField(max_length=3,choices=StudyLevel.choices,default=StudyLevel.FirstYear)
    photo=models.ImageField( null=True , blank=True, upload_to='media')
    id_parent=models.ForeignKey(Parent,on_delete=models.CASCADE)
    class Meta:
        db_table="child"


class Place(models.Model):
    longitude=models.FloatField()
    lattitude=models.FloatField()
    childPlaces=models.ManyToManyField(Child,through='ChildPlace',through_fields=('place','child'))

 


class ChildPlace(models.Model):
    child=models.ForeignKey(Child,on_delete=models.CASCADE)
    place=models.ForeignKey(Place,on_delete=models.CASCADE)
    date=models.DateField
    time=models.TimeField(null=True,blank=True)
    class Meta:
     db_table='Child_Place'
