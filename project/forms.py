from django.forms import ModelForm, fields
from .models import Project






class ProjectForm(ModelForm):
    class Meta:
        model= Project
        fields= ['id_name','first_name', 'last_name', 'your_email']