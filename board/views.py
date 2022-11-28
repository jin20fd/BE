from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import BoardSerializer
from board.models import Board
from utils.get_obj import *

class BoardView(APIView):
    def post(self, request):
        data = request.data
        obj = {
            "created_user" : request.user,
            "title" : data['title'],
            "content" : data['content'],
            "visible" : data['visible'],
            "important" : data['important']
        }
        
        serializer = BoardSerializer(data=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoardDetailView(APIView):
    def get():
        return
    def put(self, request, board_id):
        board = get_board(board_id)
        if(board.created_user != request.user): #게시글 생성자만 수정 가능
            return Response("권한없음", status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        obj = {
            "created_user" : board.created_user,
            "title" : data['title'],
            "content" : data['content'],
            "visible" : data['visible'],
            "important" : data['important']
        }
        serializer = BoardSerializer(data=obj)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, board_id):
        board = get_board(board_id)
        if(board.created_user != request.user): #게시글 생성자만 삭제 가능
            return Response("권한없음", status=status.HTTP_400_BAD_REQUEST)
        board.delete()
        return Response("삭제",status=status.HTTP_200_OK)