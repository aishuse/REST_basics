from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins

from api_basic.models import Article
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

# MODEL VIEWSET

class ArticleViewset(viewsets.ModelViewSet):
    
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()



# GENERIC VIEWSET

# class ArticleViewset(viewsets.GenericViewSet,
#                      mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin,
#                      mixins.RetrieveModelMixin
#                      ):
#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()


# VIEWSET

# class ArticleViewset(viewsets.ViewSet):
#
#     def list(self, request):
#         queryset = Article.objects.all()
#         serializer = ArticleSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def create(self,request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def retrieve(self, request, pk=None):
#         queryset = Article.objects.all()
#         article = get_object_or_404(queryset, pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def update(self, request, pk=None):
#         queryset = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(queryset, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GENERIC API VIEW

# class GenericAPIView(generics.GenericAPIView,
#                      mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.DestroyModelMixin):
#
#         queryset = Article.objects.all()
#         serializer_class = ArticleSerializer
#         # authentication_classes = [SessionAuthentication, BasicAuthentication]
#         authentication_classes = [TokenAuthentication]
#
#         permission_classes = [IsAuthenticated]
#
#         lookup_field = 'id'
#
#         def get(self, request, id=None):
#             if id:
#                 return self.retrieve(request)
#             else:
#                 return self.list(request)
#
#         def post(self, request):
#             return self.create(request)
#
#         def put(self, request, id=None):
#             return self.update(request, id)
#
#         def delete(self, request, id=None):
#             return self.destroy(request, id)



# class ArticleList(generics.ListCreateAPIView):
#
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
# class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
#
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView
#                   ):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# class ArticleDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



# class ArticleList(APIView):
#     def get(self, request, format=None):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'POST'])
# # @csrf_exempt
# def article_list(request):
#     if request.method == 'GET':
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         # data = JSONParser().parse(request)
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# class ArticleDetail(APIView):
#     def get_object(self, pk):
#         try:
#             article = Article.objects.get(pk=pk)
#         except Article.DoeSNoTExisT:
#             return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     def get(self, request, pk, format=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         article = Article.objects.get(pk=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD)
#
#     def delete(self, request, pk, format=None):
#         article = Article.objects.get(pk=pk)
#         article.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)

#
#
# @api_view(['GET', 'PUT', 'DELETE'])
# # @csrf_exempt
# def article_detail(request, pk):
#     try:
#         article = Article.objects.get(pk=pk)
#     except Article.DoeSNoTExisT:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#             # data = JSONParser().parse(request)
#             serializer = ArticleSerializer(article, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         article.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)