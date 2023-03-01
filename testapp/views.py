from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from rest_framework import viewsets, views, response, generics , mixins
from .serializers import Studentserializers
from .models import Marks , Contact , Customer
from .serializers import Marksserializers , Contactserializers , CustomerSerializer 

# Create your views here.

# def index(request):
#     return HttpResponse("HELLO SHYAM DEVAKUMARAN")


    # def index(request):
    #     obj = Marks.objects.all()
    #     return render(request, 'index.html', {'obj': obj})


def index(request):
    obj = Customer.objects.all()
    return render(request,'index.html',{'obj':obj})





def get(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        output = serializer.data
        for data in output:
            data["passed"] = True
        return response.Response(output)


    

class Studentviewset(viewsets.ModelViewSet):
    serializer_class = Studentserializers
    queryset = Student.objects.all()


class Marksviewset(viewsets.ModelViewSet):
    serializer_class = Marksserializers
    queryset = Marks.objects.all()


class Studentview(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserializers

class Contactviewset(viewsets.ModelViewSet):
    serializer_class = Contactserializers
    queryset = Contact.objects.all()

class CustomerAPIView(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    lookup_field='cus_id'

    def get(self, request, cus_id=None):
        if cus_id:
            return self.retrieve(request, cus_id)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request) 

    def perform_create(self, serializer):
        serializer.save()

    def put(self, request, cus_id=None):
        return self.update(request, cus_id)

    def perform_update(self, serializer):
        return serializer.save()

    def delete(self, request, cus_id=None):
        return self.destroy(request, cus_id)