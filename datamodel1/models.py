from django.db import models 

from datetime import datetime

# ACTORS IN A PLAY #
class Actor(models.Model): 
    name = models.CharField(max_length = 255)

class Director(models.Model):
    name = models.CharField(max_length = 255)

class Roles(models.Model):
    name = models.CharField(max_length = 255)
    lines = models.IntegerField()
    actor = models.ForeignKey(Actor, on_delete= models.CASCADE, related_name= "roles" )

class Play(models.Model):
    title= models.CharField(max_length = 255)
    duration_mins= models.IntegerField()
    director= models.ForeignKey(Director, on_delete= models.CASCADE, related_name= "plays")

 


#PETS AT THE VET # 
class Breed(models.Model): 
    name = models.CharField(max_length = 255)

class Owner(models.Model): 
    name = models.CharField(max_length = 255) 

class Pet(models.Model): 
    name = models.CharField(max_length = 255)
    breed= models.ForeignKey(Breed, on_delete = models.CASCADE, related_name= "pets")
    owner= models.ForeignKey(Owner, on_delete=models.CASCADE, related_name= "pets")

class Clinic(models.Model): 
    name = models.CharField(max_length = 255) 

class Vet(models.Model): 
    name = models.CharField(max_length = 255) 
    clinic = models.ForeignKey(Clinic, on_delete = models.CASCADE, related_name= "vets")

class Appointment(models.Model):
    datetime = models.DateTimeField(default= datetime.now())
    pet = models.ForeignKey(Pet, on_delete= models.CASCADE, related_name= "appointments")
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE, related_name= "appointments")

# APP FOR DENTIST OFFICE# 
class Patient(models.Model): 
    name = models.CharField(max_length = 255)
    phone = models.CharField(max_length = 255)
    issue = models.TextField(null=True)

class Doctor(models.Model): 
    name = models.CharField(max_length = 255)

class Visit(models.Model):
    datetime = models.DateTimeField(default= datetime.now())
    patient = models.ForeignKey(Patient, on_delete= models.CASCADE, related_name= "visits")
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name= "visits")