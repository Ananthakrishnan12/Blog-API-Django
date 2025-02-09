from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from Blogpost.models import blogpost,Comment
from Blogpost.api.serializer import BlogpostSerializer,CommentSerializer
from rest_framework.permissions import IsAuthenticated
from Blogpost.api.permissions import IsAdminUser
from rest_framework import filters
from Blogpost.api.throttling import BlogListThrottle
from rest_framework.throttling import  AnonRateThrottle
from rest_framework.exceptions import ValidationError


class BlogList(generics.ListAPIView):
    queryset = blogpost.objects.all()
    serializer_class = BlogpostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title','content']
    throttle_classes = [BlogListThrottle,AnonRateThrottle]
    #pagination_class = BloglistViewPagination
    
class BloglistAV(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request):
        post = blogpost.objects.all()
        serializer = BlogpostSerializer(post,many=True)
        return Response(serializer.data)    

    def post(self, request):
        serializer =BlogpostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogdetailAV(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request,pk):
        try:
            post = blogpost.objects.get(pk=pk)
            serializer = BlogpostSerializer(post)
            return Response(serializer.data)
        except blogpost.DoesNotExist:
            return Response({"message":"Blogpost not found"},status=status.HTTP_404_NOT_FOUND)
        
    def put(self, request,pk):
        post = blogpost.objects.get(pk=pk)
        serializer =BlogpostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)  
        
    def delete(self,request,pk):
        post=blogpost.objects.get(pk=pk)
        post.delete()
        return Response({"message":"Post deleted successfully"},status=status.HTTP_200_OK)
    
class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Comment.objects.all()
    
    def perform_create(self,serializer):
        pk=self.kwargs.get('pk')
        post=blogpost.objects.get(pk=pk)
        
        comment_user=self.request.user
        
        comment_queryset=Comment.objects.filter(blogpost=post,comment_user=comment_user)
        
        if comment_queryset.exists():
            raise ValidationError("You have already liked and comment this post!!!")
        
        post.total_likes = sum(comment.likes for comment in post.comments.all())
        post.save()
        
        serializer.save(blogpost=post,comment_user=comment_user)
        
class CommentList(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer   
    
    def get_queryset(self):
        pk=self.kwargs.get('pk')
        return Comment.objects.filter(blogpost=pk)
    
class CommentDetail(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer 
    permission_classes = [IsAdminUser]    
    
   
                  