from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def index(request):
    people_detail = {
        'name' : 'praveen',
        'age' : 25, 
        'job' : 'it'

    }

    return Response(people_detail)