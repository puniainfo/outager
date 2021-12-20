from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

class OutageModel(models.Model):
    received_from =  models.CharField(max_length=100)
    application_name =  models.CharField(max_length=100)
    outage_start_time = models.DateTimeField()
    outage_end_time = models.DateTimeField(blank=True,null=True)
    outage_time = models.IntegerField(default=0)
    outage_status = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table  = "outage_model"
