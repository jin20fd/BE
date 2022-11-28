from django.db import models
from account.models import User

class Board(models.Model):
    created_user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="created_user", to_field="username")
    title = models.TextField()
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    visible = models.BooleanField(default=True)
    important = models.BooleanField(default=False)

    class Meta:
        db_table = "board"