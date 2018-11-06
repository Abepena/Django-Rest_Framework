from rest_framework import serializers
from . import models


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'url')
        model = models.Course

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        #explicitly specify fields according to DRF documentation
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'rating',
            'created_at',
        )
        model = models.Review
