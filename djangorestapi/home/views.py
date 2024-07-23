from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import PersonSerializer 
from .models import Person

@api_view(['GET','POST','PUT'])
def index(request):
    if request.method == 'GET':
        people_detail = {
            'name' : 'praveen',
            'age' : 25, 
            'job' : 'it'
         }
 

        return Response(people_detail)
    elif request.method ==  'POST':
        print("THIS IS A POST METHODE")
        return Response("THIS IS A POST METHODE")
    elif request.method == 'PUT':
        print("THIS IS A PUT METHODE")
        return Response("THIS IS A PUT METHODE")


@api_view(['GET','POST','PUT', 'PACH','DELETE'])
def person(request):
    if request.method == 'GET':
        objPerson = Person.objects.all()
        serializer = PersonSerializer(objPerson, many=True)
        return Response(serializer.data)
    elif request.method == 'POST' :
        data = request.data
        serializer = PersonSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.method == 'PUT':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data = data , partial = False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    elif request.methode == 'PACH':
        data = request.data
        obj = Person.objects.get(id = data['id'])
        serializer = PersonSerializer(obj, data = data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
 
        
