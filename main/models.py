from django.db import models
from django.contrib.auth.models import User

class DishType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.name


class ScheduleItem(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return "%s %s" % (self.date, self.dish)


class Order(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    schedule_item = models.ForeignKey(ScheduleItem, on_delete=models.CASCADE)

    def __str__(self):
        return "%s %s" % (self.schedule_item, self.staff)