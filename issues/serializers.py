from rest_framework.serializers import ModelSerializer,SerializerMethodField
from .models import Issue


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = '__all__'

    spent_time = SerializerMethodField()

    def get_spent_time(self, obj):
        return obj.get_spent_time()

    author_username = SerializerMethodField()
    def get_author_username(self, obj):
        return obj.author.username
