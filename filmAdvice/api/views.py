from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from rest_framework import status
from filmAdvice.api.schemas import *
from filmAdvice.system.load_data import *


@api_view(['GET'])
@schema(HelloSchema, )
def hello(a):
    try:
        return Response({"detail": load_movie_data()},
                        status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"detail": str(ex)}, status=status.HTTP_400_BAD_REQUEST)