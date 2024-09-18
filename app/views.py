
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import CreatePostForm , UserForm
from .models import UserProfile,Product
from django.views.generic.edit import CreateView, DeleteView
from .serializers import ProductSerializers
from django.http import JsonResponse
from rest_framework import status, generics
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.views import LoginView



class Login(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'
    success_url = reverse_lazy('home')
    form_class = UserForm


@permission_classes((IsAuthenticated,))
class APIProductViewSet(ModelViewSet):
    queryset =Product.objects.all()
    serializer_class = ProductSerializers


class APIREADProductViewSet(ReadOnlyModelViewSet):
    queryset =Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = (IsAuthenticated,)

# class APIProduct(generics.ListAPIView):
#     queryset =  Product.objects.all()
#     serializer_class = ProductSerializers

# class APIProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset =  Product.objects.all()
#     serializer_class = ProductSerializers



# @api_view(['GET', 'POST'])
# def api_product (request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         serializer = ProductSerializers(products, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = ProductSerializers(data=request.data) 
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET', 'PUT', 'PATCH', 'DELETE']) 
# def api_product_id(request, pk): 
#     rubric = Product.objects.get(pk=pk) 
#     if request.method == 'GET': 
#         serializer = ProductSerializers(rubric) 
#         return Response(serializer.data) 
#     elif request.method == 'PUT' or request.method == "PATCH": 
#         serializer = ProductSerializers(rubric, data=request.data, partial = True) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
#     elif request.method == 'DELETE': 
#         rubric.delete() 
#         return Response ('Success delete',status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def api_rubrics(request) : 
#     if request.method == 'GET':
#         rubrics = Product.objects.all() 
#         serializer = RubricSerializer (rubrics, any-Irel retumn Response (serializer.data) elif request.method = 'POST': serializer = RubricSerializer (data=request .data) if serializer.is valid(): serializer.save () return Response (serializer.data, status=status.HTTP 201 CBATED return Response (serializer.errors, status-status.HITP 400 BAD REQUEST]

def home(request):
    posts=UserProfile.objects.all()
    if request.method == 'POST':
        api_id = request.POST['id_product']
        return redirect(f'api_id/{api_id}')

    return render(request, 'home.html', context= {'posts':posts } )

# @api_view(['GET'])
# def api_product(request):
#     if request.method == 'GET':
#         product = Product.objects.all()
#         serializer = ProductSerializers(product, many = True)
#         return Response(serializer.data)
# @api_view(['GET'])
# def api_product_id(request, pk):
#     if  request.method == 'GET':
#         product = Product.objects.get(pk=pk)
#         serializer = ProductSerializers(product)
#         return Response(serializer.data)
        
def email_massage(request):
    user = UserProfile.objects.get(id=1)
    send_mail(
        "Subject here",
        "Here is the message.",
        "from@example.com",
        [f"{user.email}"],
        fail_silently=False,
    )
    return HttpResponseRedirect("/")

class CreatePost(CreateView):
    model = UserProfile
    success_url = reverse_lazy('home')
    template_name = 'create.html'
    form_class = CreatePostForm

class DeletePost(DeleteView):
    model = UserProfile
    success_url = reverse_lazy('home')
    template_name = 'delete.html'
