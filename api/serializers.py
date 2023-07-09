from rest_framework import serializers
from core.models import UploadPDF
from api.models import TrainModel, TrainModelDB

class CustomTrainModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadPDF
        fields = "__all__"

class CustomTrainSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainModel
        fields = "__all__"

class CustomTrainDBSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainModelDB
        fields = "__all__"
