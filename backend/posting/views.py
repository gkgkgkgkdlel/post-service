import json
import bcrypt
import re
from django.shortcuts import redirect, HttpResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post


from .serializers import PostSerializer, PostUpdateSerializer


class PostView(APIView):
    def get(self, request):
        post_set = Post.objects.all().order_by("-created_at")

        serializer = PostSerializer(post_set, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = json.loads(request.body)
        password = data["password"]

        if len(password) < 6:
            return Response(
                {"message": "PASSWORD_LENGTH_ERROR"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        elif re.search("[0-9]+", password) is None:
            return Response(
                {"message": "PASSWORD_No_NUMBER_ERROR"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        )

        decoded_password = hashed_password.decode("utf-8")
        data["password"] = decoded_password

        serializer = PostSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
            )


class PostUpdateView(APIView):
    def put(self, request):
        data = json.loads(request.body)
        post_id = data["id"]
        password = data["password"]

        encoded_password = password.encode("utf-8")

        post = Post.objects.get(id=post_id)
        post_password = post.password
        encoded_post_password = post_password.encode("utf-8")

        result = bcrypt.checkpw(encoded_password, encoded_post_password)

        if result:

            hashed_password = bcrypt.hashpw(
                password.encode("utf-8"), bcrypt.gensalt()
            )

            decoded_password = hashed_password.decode("utf-8")
            data["password"] = decoded_password
            serializer = PostUpdateSerializer(instance=post, data=data)

            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "SUCCESS"}, status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                {"message": "WRONG_PASSWORD"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class PostDeleteView(APIView):
    def delete(self, request):
        data = json.loads(request.body)
        post_id = data["id"]
        password = data["password"]

        encoded_password = password.encode("utf-8")

        post = Post.objects.get(id=post_id)
        post_password = post.password
        encoded_post_password = post_password.encode("utf-8")

        result = bcrypt.checkpw(encoded_password, encoded_post_password)

        if result:

            post.delete()

            return Response(
                {"message": "SUCCESS"},
                status=status.HTTP_200_OK,
            )

        else:
            return Response(
                {"message": "WRONG_PASSWORD"},
                status=status.HTTP_400_BAD_REQUEST,
            )
