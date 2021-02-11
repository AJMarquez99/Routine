from django.db import models

# Create your models here.
class Refrigerator(models.Model):
    #exp_date = models.DateField(auto_now=False, auto_now_add=True)
    #purchase_date = models.DateField(auto_now=True, auto_now_add=True)
    #longetivity = models.DurationField()
    item_id         = models.PositiveIntegerField()
    user_id         = models.PositiveIntegerField()
    purchase_date   = models.DateField(auto_now_add=True)
    quantity        = models.PositiveSmallIntegerField()

class Item(models.Model):
    name        = models.TextField()
    longetivity = models.DurationField()
    cost        = models.FloatField()
    calories    = models.SmallIntegerField()
    TYPE_ITEM   = [
        ('FD', 'Food'),
        ('DV', 'Device'),
        ('HH', 'Household Object'),
        ('CL', 'Clothing'),
        ('MC', 'Misc'),
    ]
    type        = models.CharField(max_length=30, choices=TYPE_ITEM)

    def __str__(self):
        return self.name[:15]
