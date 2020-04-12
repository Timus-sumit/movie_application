from django.shortcuts import render
from django.contrib.auth.models import User
from.forms import ListForm
from.models import List
from list.models import List
from list.api.serializers import ListSerializer, UserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics,permissions,renderers
from list.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.filters import SearchFilter, OrderingFilter



def create(request):
    form = ListForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ListForm()
    context={
    'form':form
    }
    return render (request, 'list/create.html',context)

# Create your views here.
def home(request):
    list= List.objects
    return render(request, 'list/home.html',{'list':list})



class ListList(APIView):
    """
    Read  list, or create a new list.
    Login to Retrieve, update or delete a list instance.

    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


    def get(self, request, format=None):
        list = List.objects.all()
        serializer = ListSerializer(list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListList(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['user__username','title','pub_date']



class ListDetail(APIView):
    """
    Retrieve, update or delete a list instance.

    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                      IsOwnerOrReadOnly]

    def get_object(self, pk):
        try:
            return List.objects.get(pk=pk)
        except List.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        list = self.get_object(pk)
        serializer = ListSerializer(list)


        return Response(serializer.data)

    def put(self, request, pk, format=None):
        list = self.get_object(pk)
        serializer = ListSerializer(list, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        list = self.get_object(pk)
        list.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['username']


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer




@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'list': reverse('list-list', request=request, format=format)
    })




class ListHighlight(generics.GenericAPIView):
    queryset = List.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        list = self.get_object()
        return Response(list.highlighted)
