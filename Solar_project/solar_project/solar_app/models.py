from django.db import models

# Create your models here.
class mysolarrr(models.Model):
    Solar_generation=models.IntegerField(max_length=400,default=0)
    Today_production=models.IntegerField(max_length=400,default=0)
    Monthly_sales=models.IntegerField(max_length=400,default=0)
    Weekly_revenue=models.IntegerField(max_length=400,default=0)
    Investor_power_distribution=models.IntegerField(max_length=400,default=0)
    Total_panels=models.IntegerField(max_length=400,default=0)
    Performance=models.IntegerField(max_length=400,default=0)
    Weather_prediction=models.IntegerField(max_length=400,default=0)
    Hourly_temperature_and_humidity=models.IntegerField(max_length=400,default=0)