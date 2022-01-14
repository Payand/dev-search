from django.db import models
import uuid




class Project(models.Model):
    id_name = models.CharField(max_length=150, blank=True, null=True, unique=True)
    first_name = models.CharField(max_length=200,blank=False,null=False)
    last_name = models.CharField(max_length=200, blank=False, null=False)
    your_email = models.EmailField(max_length=100,blank=False, null=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.id_name
    
    
