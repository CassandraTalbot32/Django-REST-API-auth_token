from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from rest_framework.renderers import TemplateHTMLRenderer
from .serializers import UserSerializer, RegisterSerializer, LoginSerializer
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import PolicyForm


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


def LoginAPI(self, request, *args, **kwargs):
	if request.method == GET:
		return Response({
		"user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
#(request, "registration/login.html")
		

def Policy_page(request, *args, **kwargs):
		return render(request, "policy_detail.html/")


def policy_create_view(request):
    form = PolicyForm(request.POST)
    if form.is_valid():
    	form.save()
    	form = PolicyForm()
    context = {
        'form': form
    }
    return render(request, "accounts/policy_create.html", context)



#def policy_detail_view(request, id):
    obj = get_object_or_404(accounts, id=id)
    context = {
        'object': obj
	}
    return render(request, "accounts/policy_detail.html", context)


