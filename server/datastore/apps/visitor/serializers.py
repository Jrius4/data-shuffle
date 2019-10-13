from rest_framework import serializers
from .models import Visitor

class VisitorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = ('url','email','first_name','last_name','phone_number','occupation','address','country','work_place','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validated_data):
        password = validated_data.pop('password')
        visitor = Visitor(**validated_data)
        visitor.username = validated_data.get('email')
        visitor.set_password(password)
        visitor.save()
        return visitor
        