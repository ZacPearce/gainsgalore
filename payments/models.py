from django.db import models

from django.db import models
from users.models import CustomUser
from workouts.models import WorkoutPlan

class Payment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    workout = models.ForeignKey(WorkoutPlan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    stripe_payment_intent = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.amount} - {self.timestamp}"