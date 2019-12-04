from django.db import models

from django.db import models

from django.utils.translation import gettext as _
class sighting(models.Model):
    Latitude = models.FloatField(help_text=_('Latitude'),
                               max_length=10,)
    Longitude = models.FloatField(help_text=_('Longitude'),
                               max_length=10,)
    Unique_Squirrel_ID = models.IntegerField(max_length = 20, primary_key=True,) 
    def __str__(self):
      return self.Unique_Squirrel_ID

