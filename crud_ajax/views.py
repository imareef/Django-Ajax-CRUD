from django.views.generic import ListView
from django.views import View
from django.http import JsonResponse

from crud_ajax.models import CrudUser


class CrudView(ListView):
    model = CrudUser
    template_name = 'crud_ajax/crud.html'
    context_object_name = 'users'


class CreateCrudUser(View):
    def get(self, request):
        name1 = request.GET['name']
        address1 = request.GET['address']
        age1 = request.GET['age']

        obj = CrudUser.objects.create(
            name=name1,
            address=address1,
            age=age1,
        )

        user = {
            'id': obj.id,
            'name': obj.name,
            'address': obj.address,
            'age': obj.age,
        }

        data = {
            'user': user,
        }

        return JsonResponse(data)


class UpdateCrudUser(View):
    def get(self, request):
        id1 = request.GET['id']
        name1 = request.GET['name']
        address1 = request.GET['address']
        age1 = request.GET['age']

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {
            'id': obj.id,
            'name': obj.name,
            'address': obj.address,
            'age': obj.age,
        }

        data = {
            'user': user
        }

        return JsonResponse(data)


class DeleteCrudView(View):
    def get(self, request):

        id1 = request.GET['id']
        CrudUser.objects.get(id=id1).delete()

        data = {
            'deleted': True
        }

        return JsonResponse(data)


