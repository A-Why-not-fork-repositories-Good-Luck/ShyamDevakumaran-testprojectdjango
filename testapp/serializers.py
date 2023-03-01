from rest_framework import serializers
from  .models import  Customer, Student
from .models import Marks
from .models import Contact
class Studentserializers(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields ='__all__'
        # fields = ("name","department","batch","id_rollno")

class Marksserializers(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'

class Contactserializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Customer
        fields=(
            'cus_id',
            'cus_name',
            'cus_email',
            'cus_phone'
        )