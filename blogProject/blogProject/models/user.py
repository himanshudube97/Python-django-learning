from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255,default="") # user's name
    last_name = models.CharField(max_length=255, default="") # user's last name
    email = models.EmailField(max_length=255, ) # user's email
    password = models.CharField(max_length=255) # user's password
    isLoggedIn = models.BooleanField(default=False) # user's login status
    isActive = models.BooleanField(default=True) # user's account status
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation, cannot be overwritten
    updated_at = models.DateTimeField(auto_now=True)      # Automatically set on save,cannot be overwritten

    def __str__(self):  # this method represents the object as a string
        return f'{self.first_name} {self.last_name} {self.email} User'
    


## What exactly is __str__?
#   post = Post.objects.get(id=1)
# print(post)  # Output: My First Blog Post
# Why it’s useful: Without a __str__ method, printing a model instance would look something like this:

# <Post: Post object (1)>


# By defining __str__, you can provide a more readable representation for your model instances, making debugging or working in the admin panel much more user-friendly.






# It is important to note that CharFields and TextFields are never saved as NULL in the Django database. Instead, blank values are stored as an empty string ('')