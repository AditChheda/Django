from django.db import models


class AccountDatabase(models.Model):
  FirstName = models.TextField()
  LastName  = models.TextField()
  Username  = models.TextField()
  Email     = models.EmailField()
  Password  = models.TextField()

  def __str__(self):
      return self.FirstName
  

class UserInformation(models.Model):
  Name           = models.TextField(default="")
  College        = models.TextField()
  CollegeAddress = models.TextField()
  AcademicYear   = models.TextField()
  Department     = models.TextField()
  Division       = models.DecimalField(max_digits = 10, decimal_places = 0)
  RollNo         = models.DecimalField(max_digits = 10, decimal_places = 0)
  LinkedIn       = models.URLField()
  GithubUrl      = models.URLField()
  InstagramUrl   = models.URLField()
  Skills         = models.TextField()
  Description    = models.TextField()
  Image          = models.ImageField(upload_to = 'accounts/images', default="")

  def __str__(self):
      return self.College
  

class CollegeName(models.Model):
  CollegeName = models.TextField()

  def __str__(self):
    return self.CollegeName
