from django.db import models

# Create your models here.

class Ebw_data(models.Model):

    machine_name = models.CharField(max_length=100)
    component_name = models.CharField(max_length=100)
    material_name = models.CharField(max_length=100)
    joint_dia = models.FloatField()
    joint_depth = models.FloatField()
    backup = models.FloatField()
    gtwd = models.FloatField()
    max_dop = models.FloatField()
    min_dop = models.FloatField()

    predicted_focus_current = models.FloatField()
    predicted_beam_current = models.FloatField()

