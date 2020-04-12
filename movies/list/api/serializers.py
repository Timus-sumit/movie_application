from rest_framework import serializers
from list.models import List
from django.contrib.auth.models import User
from rest_framework.serializers import  HyperlinkedIdentityField



class ListSerializer(serializers.ModelSerializer):

    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = List
        fields = [ 'user','title', 'pub_date']


class UserSerializer(serializers.ModelSerializer):
    list = serializers.PrimaryKeyRelatedField(many=True, queryset=List.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username','list']





class UserSerializer(serializers.HyperlinkedModelSerializer):
    list = serializers.HyperlinkedRelatedField(many=True, view_name='list-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'list']
