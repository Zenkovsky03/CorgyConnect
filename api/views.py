from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import DogSerializer
from doggs.models import Dog, Review
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
# @permission_classes([IsAuthenticated])
def getDogs(request):
    dogs = Dog.objects.all()
    serializer = DogSerializer(dogs, many=True) #many=True to znaczy ze wiele obiektow a nie tylko jeden
    return Response(serializer.data)


@api_view(['GET'])
def getDog(request, pk):
    dog = Dog.objects.get(id=pk)
    serializer = DogSerializer(dog, many=False) #many=True to znaczy ze wiele obiektow a nie tylko jeden
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def dogVote(request, pk):
    dog = Dog.objects.get(id=pk)
    user = request.user.profile
    data = request.data
    review, created = Review.objects.get_or_create(
        owner=user,
        dog=dog,
    )
    # czy istnieje recenzja w bazie danych, której właścicielem jest określony użytkownik dla określonego psa.
    # Jeśli taka recenzja już istnieje, jest ona pobierana. Jeśli nie istnieje, jest tworzona nowa recenzja.
    # Zmienna created informuje nas, czy recenzja została utworzona podczas tej operacji czy nie
    review.value = data['value']
    review.save()
    dog.getVoteCount
    serializer = DogSerializer(dog, many=False)
    return Response(serializer.data)
