from typing import override
from requests import Request, Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from user_app.models import User
from user_app.serializers import UserSignUpSerializer


class UserViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSignUpSerializer

    @override
    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()
        return Response(
            data={"id": user.id, "phone_number": user.phone_number},
            status=status.HTTP_201_CREATED,
        )
