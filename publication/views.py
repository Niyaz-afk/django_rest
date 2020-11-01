from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer


class PostView(APIView):
    def get(self,request):
        """Вывод всех статей"""
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({ 'posts': serializer.data })

    def post(self,request):
        """Добавление статьи"""
        post = request.data.get('post')

        serializer = PostSerializer(data=post)
        if serializer.is_valid(raise_exception= True):
            post_saved =serializer.save()
        return Response({'success': "Post '{}' created successfully".format(post_saved.title)})

    def put(self, request, pk):
        """Редактирование статьи"""
        saved_post = get_object_or_404(Post.objects.all(), pk = pk)
        data = request.data.get('post')
        serializer = PostSerializer(instance=saved_post, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            post_saved = serializer.save()
        return Response({
            "success": "Post '{}' updated successfully".format(post_saved.title)
        })

