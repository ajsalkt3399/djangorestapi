from rest_framework import serializers
from home.models import Person , Team
import re

class TeamSerializer(serializers.ModelSerializer): 

    class Meta:
        model = Team
        fields = ['team_name']

class PersonSerializer(serializers.ModelSerializer):
    team = TeamSerializer()
    team_info = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = '__all__'
        depth = 1

    def get_team_info(self, obj):
        return "extra serializer field"
    
    def validate_name(self, value):
        # Regular expression to check for special characters
        if not re.match("^[A-Za-z0-9 ]*$", value):
            raise serializers.ValidationError("Name should not contain special characters.")
        return value

    def validate_age(self, value):
        # Age validation logic
        if value < 0 or value > 120:
            raise serializers.ValidationError("Age must be between 0 and 120.")
        return value