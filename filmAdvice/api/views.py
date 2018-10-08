from rest_framework.response import Response
from rest_framework import status
from filmAdvice.api.schemas import *
from rest_framework.decorators import api_view, schema


@api_view(['GET'])
@schema(HelloSchema, )
def hello():
    try:
        return Response({"detail": "Hello"},
                        status=status.HTTP_200_OK)
    except Exception as ex:
        return Response({"detail": str(ex)}, status=status.HTTP_400_BAD_REQUEST)