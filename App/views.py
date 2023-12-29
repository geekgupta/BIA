from django.shortcuts import render 
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BooksSerializer , ModifyVideoSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated , AllowAny
from rest_framework import status
from .models import Books
from pytube import YouTube
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os
# Create your views here.

def DashboardPage(request):
    return render(request , "Home.html")

## create an account and use this api to create new books  and get all books 
class BookList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

## Update / delete / view  particular book details  
class BookDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Books.objects.get(pk=pk)
        except Books.DoesNotExist:
            return Response({"detail": "Book not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk):
        book = self.get_object(pk)
        serializer = BooksSerializer(book)
        return Response(serializer.data)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response({"detail": "Book deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    
    
    


from django.http import HttpResponse
from moviepy.editor import VideoClip, TextClip, CompositeVideoClip
from moviepy.config import change_settings

change_settings({"IMAGEMAGICK_BINARY": "/usr/bin/convert", "IMAGEMAGICK_POLICY_PATH": "App/policy.xml"})
class ModifyVideo(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        try:
            user_name = request.data['user_name']
            text_clip = TextClip(user_name, fontsize=30, color='white', bg_color='black')
            video_clip = CompositeVideoClip([text_clip], size=(640, 480), bg_color='black')
            duration = 10
            video_clip = video_clip.set_duration(duration)
            response = HttpResponse(content_type='video/mp4')
            response['Content-Disposition'] = 'attachment; filename="output_video.mp4"'
            video_clip.write_videofile(response, codec='libx264', audio_codec='aac', fps=24)
            return response
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
