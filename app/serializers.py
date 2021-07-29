from rest_framework.serializers import ModelSerializer
from app.models import Project, Client


class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        depth = 2
        fields = '__all__'



class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        depth = 2
        fields = '__all__'


