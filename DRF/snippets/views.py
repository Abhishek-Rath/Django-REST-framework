from rest_framework import status, generics
from django.contrib.auth.models import User
# from rest_framework.decorators import APIView
# from rest_framework.response import Response

from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

                                    
                                    # Method 1

# Create your views here.
# @api_view(['GET', 'POST'])
# def snippet_list(request, format = None):
#     """
#     List all code snippets, or create a new snippet
#     """
#     if request.method == "GET":
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many = True)
#         return Response(serializer.data)

#     elif request.method == "POST":
#         serializer = SnippetSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'DELETE'])
# def snippet_detail(request, pk, format = None):
#     """ Retrieve, update or delete a code snippet
#     """
#     try:
#         snippet = Snippet.objects.get(pk = pk)
#     except Snippet.DoesNotExist:
#         return Response(status = status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer = SnippetSerializer(snippet, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         snippet.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)

                            
                            #  Method 2

# class SnippetList(APIView):
#     """ List all the snippets, or create a new snippet"""

#     def get(self, request, format = None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many = True)
#         return Response(serializer.data)
    
#     def post(self, request, fornat = None):
#         serializer = SnippetSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status = status.HTTP_201_CREATED
#             )
#         return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk = pk)
#         except:
#             return Http404
    
#     def put(self, request, pk, format = None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format = None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer