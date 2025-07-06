from django.db import models

from django.db import models
from users.models import CustomUser

class WorkoutPlan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    coach = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='workouts')
    is_premium = models.BooleanField(default=False)
    video_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title