from rest_framework import serializers
from main.models import * 


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Works
        fields = "__all__"

        