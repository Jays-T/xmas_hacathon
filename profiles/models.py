from django.db import models
from django.contrib.auth.models import User


# user creates profile
# when profile is created use signals/reciever to create Advent calendar unique to User 
# when Advent Calendar is created
# send query to database, pull all recipe objects
# from all recipe objects, pick 25 random 
# assign picked recipes to Advent Calendar (either via FK association (AdvCal as FK), or ManyToMany (recipes to AdvCal))
# Advent Calendar is unique to user (User associated as FK)
# in Advent Calendar model can set specific sort
class UserProfile(models.Model):
    """
    Maintain Advent Calendar history for each user
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
