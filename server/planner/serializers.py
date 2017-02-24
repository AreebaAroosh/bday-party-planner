from rest_framework import serializers

from . import models


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = models.User
        fields = ('id', 'url', 'email', 'birthday')


class PartySerializer(serializers.HyperlinkedModelSerializer):

    class Meta(object):
        model = models.Party
        fields = ('id', 'url', 'date', 'date_from', 'date_to', 'users')
