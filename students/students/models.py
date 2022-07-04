# modules
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
import uuid

# models
from schools.models import Schools

class Students(models.Model):

    def randomUnique():
        return str(uuid.uuid4().hex[:20].upper())

    # detected max number for schools
    def validate_max_number(value):
        # finding how max number in school
        get_data_school = Schools.objects.filter(name=value).values('max_number', 'id').first()
        
        # detected school is exists
        if get_data_school == None:
            raise ValidationError(
                _('This School is not found!!')
            )
        
        max_number = int(get_data_school["max_number"])
        school_id = int(get_data_school["id"])

        # finding how number students in school
        total_number = int(Students.objects.filter(school_id=school_id).count())

        if max_number <= total_number:
            raise ValidationError(
                _('This %(value)s is full!!!'),
                params={'value': value},
            )

    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    student_identification  = models.CharField(max_length=20,default=randomUnique)
    school = models.ForeignKey(Schools,on_delete=models.CASCADE, validators=[validate_max_number])