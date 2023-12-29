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
    
    
    


class ModifyVideo(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        # try:
            serializer = ModifyVideoSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            youtube_link = serializer.validated_data['youtube_link']
            text_to_add = serializer.validated_data.get('text_to_add', 'Your Name')
            print(youtube_link , text_to_add )
            yt = YouTube(youtube_link)
            video_stream = yt.streams.filter(file_extension='mp4').first()
            video_path = video_stream.download()
            text_clip = TextClip(text_to_add, fontsize=30, color='white', bg_color='black')
            duration = VideoFileClip(video_path).duration
            text_video = text_clip.set_duration(duration)
            original_video = VideoFileClip(video_path)
            final_video = CompositeVideoClip([original_video, text_video])
            os.makedirs("modified_videos", exist_ok=True)
            modified_video_path = f"modified_videos/{yt.video_id}_modified.mp4"
            final_video.write_videofile(modified_video_path, codec='libx264', audio_codec='aac')

            return Response({"message": "Video modified successfully", "modified_video_path": modified_video_path}, status=status.HTTP_200_OK)

        # except Exception as e:
        #     return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)