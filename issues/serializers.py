from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Issue


class IssueSerializer(ModelSerializer):
    class Meta:
        model = Issue
        fields = ['id', 'title', 'description', 'category', 'status', 'author_username',
                  'assignee_username', 'spent_time']

    spent_time = SerializerMethodField()

    def get_spent_time(self, obj):
        return obj.get_spent_time()

    author_username = SerializerMethodField()

    def get_author_username(self, obj):
        return obj.author.username

    assignee_username = SerializerMethodField()

    def get_assignee_username(self, obj):
        return obj.assignee.username
