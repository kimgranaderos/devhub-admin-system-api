from django.db import models

# Create your models here.
class CoWorkingSpace(models.Model):
    space_name = models.CharField(max_length=20, unique=True)
    hour = models.SmallIntegerField()
    whole_day = models.SmallIntegerField(null=True, blank=True)

    def __str__(self):
        return self.space_name

class Conference(models.Model):
    pax = models.CharField(max_length=20, unique=True)
    hour = models.SmallIntegerField()

    def __str__(self):
        return f"{self.pax} pax"

class Membership(models.Model):
    membership_type = models.CharField(max_length=20, unique=True)
    monthly = models.SmallIntegerField()

    def __str__(self):
        return self.membership_type

class Customer(models.Model):
    cust_name = models.CharField(max_length=30, unique=True)
    co_working = models.ForeignKey(CoWorkingSpace, null=True, blank=True, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, null=True, blank=True, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, null=True, blank=True, on_delete=models.CASCADE)
    payment = models.SmallIntegerField()

    def __str__(self):
        return self.cust_name