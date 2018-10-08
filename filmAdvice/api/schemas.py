import coreapi
import coreschema
from rest_framework.schemas import ManualSchema

HelloSchema = ManualSchema(fields=[
    coreapi.Field(
        'name',
        required=True,
        location="body",
        schema=coreschema.String()
    ),
])