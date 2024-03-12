from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DogSerializer
from doggs.models import Dog
@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET':'/api/dogs'},
        {'GET': '/api/dogs/id'},
        {'POST': '/api/dogs/vote'},

        {'POST': '/api/users/token'},
        {'POST': '/api/users/token/refresh'},

    ]

    return Response(routes)

@api_view(['GET'])
def getDogs(request):
    dogs = Dog.objects.all()
    serializer = DogSerializer(dogs, many=True) #many=True to znaczy ze wiele obiektow a nie tylko jeden
    return Response(serializer.data)


@api_view(['GET'])
def getDog(request, pk):
    dog = Dog.objects.get(id=pk)
    serializer = DogSerializer(dog, many=False) #many=True to znaczy ze wiele obiektow a nie tylko jeden
    return Response(serializer.data)