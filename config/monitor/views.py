from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone

from .models import Keyword, ContentItem, Flag
from .serializers import KeywordSerializer, ContentItemSerializer, FlagSerializer


# 🔹 Create Keyword
@api_view(['POST'])
def create_keyword(request):
    serializer = KeywordSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# 🔹 Create Content
@api_view(['POST'])
def create_content(request):
    serializer = ContentItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


# 🔥 Scan Content (WITH FIXED SUPPRESSION)
from .services import run_scan

@api_view(['POST'])
def scan_content(request):
    flags = run_scan()
    serializer = FlagSerializer(flags, many=True)
    return Response(serializer.data)


# 🔹 Update Flag (Review API)
@api_view(['PATCH'])
def update_flag(request, id):
    try:
        flag = Flag.objects.get(id=id)
    except Flag.DoesNotExist:
        return Response({"error": "Flag not found"}, status=404)

    status_value = request.data.get('status')

    if status_value not in ['pending', 'relevant', 'irrelevant']:
        return Response({"error": "Invalid status"}, status=400)

    flag.status = status_value
    flag.reviewed_at = timezone.now()
    flag.save()

    return Response({"message": "Flag updated successfully"})


@api_view(['GET'])
def get_flags(request):
    flags = Flag.objects.all()
    serializer = FlagSerializer(flags, many=True)
    return Response(serializer.data)