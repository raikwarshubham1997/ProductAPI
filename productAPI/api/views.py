from functools import partial
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from rest_framework import status
from rest_framework.views import APIView

# Category Api

class CategoryAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            cate = Category.objects.get(id=id)
            serializer = CategorySerializer(cate)
            return Response(serializer.data)

        cate = Category.objects.all()
        serializer = CategorySerializer(cate, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, format=None):
        id = pk
        cate = Category.objects.get(pk=id)
        serializer = CategorySerializer(cate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):
        id = pk
        cate = Category.objects.get(pk=id)
        serializer = CategorySerializer(cate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        cate = Category.objects.get(pk=id)
        cate.delete()
        return Response({'msg': 'Data Deleted'})

# Product api

class ProductAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            prod = Product.objects.get(id=id)
            serializer = ProductSerializer(prod)
            return Response(serializer.data)

        prod = Product.objects.all()
        serializer = ProductSerializer(prod, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request, pk, format=None):
        id = pk
        prod = Product.objects.get(pk=id)
        serializer = ProductSerializer(prod, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Complete Data Updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, pk, format=None):
        id = pk
        prod = Product.objects.get(pk=id)
        serializer = ProductSerializer(prod, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        prod = Product.objects.get(pk=id)
        prod.delete()
        return Response({'msg': 'Data Deleted'})


#Function based api

# @api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
# def product_api(request, pk=None):
#     if request.method == 'GET':
#         id = pk
#         if id is not None:                      
#             prod = Product.objects.get(id=id)
#             serializer = ProductSerializer(prod)
#             return Response(serializer.data)

#         prod = Product.objects.all()
#         serializer = ProductSerializer(prod, many=True)
#         return Response(serializer.data)

        



