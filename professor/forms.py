from django.forms import ModelForm
from .models import Professor

class ProfessorForm(ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
