from rest_framework import serializers
from .models import Board, User

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id','created_user', 'title', 'content', 'created_time','visible','important']