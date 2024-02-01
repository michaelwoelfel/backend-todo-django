from rest_framework import serializers
from .models import Todo  # Import your Todo model

# Create a serializer for the Todo model
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields =  ['author','date', 'title', 'description','my_field' ]  # Or list the fields you want to include, e.g. ['id', 'title', 'description', 'completed']
