from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.template import RequestContext
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.models import Project, Client
from app.serializers import ProjectSerializer, ClientSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import logout


@csrf_exempt
def logout_view(request):
    logout(request)
    return redirect('/index/?page=registerclient')

@csrf_exempt
def index(request):
    page_name =  request.GET["page"]


    if not request.user.is_authenticated:
        return redirect("/admin/login/?next=/index/?page="+page_name)


    ctx={"status":True}

    if page_name == "myprojects":
        ctx["project_list"] =  Project.objects.filter(users=request.user)
        print(ctx["project_list"])
    if page_name =="editclient":
        id = request.GET["id"]
        c = Client.objects.get(id=id)
        ctx["name"]=c.name
        ctx["email_id"]=c.email_id
        ctx["mobile_number"]=c.mobile_number
        ctx["description"]=c.description
        ctx["id"]=c.id


    if page_name =="addproject":
        ctx["users"]=User.objects.all()


    return render(request, page_name+".html", ctx)

@csrf_exempt
def adduser_view(request):
    data=json.loads(request.body.decode('utf-8'))

    project_id = data["project_id"]
    project=Project.objects.get(id=project_id)
    u_list = project.users.all()
    for u in u_list:
        project.users.remove(u)

    for key,u in data["users"].items():
        user=User.objects.get(id=key)
        project.users.add(user)


    return JsonResponse({'status':True})

@csrf_exempt
def client_name_view(request):
    name = request.GET["name"]
    c_list = Client.objects.filter(name=name)
    if not c_list:
        return JsonResponse({'status': False})
    return JsonResponse({'status':True,'id':c_list[0].id})


@csrf_exempt
@api_view(['GET', 'POST'])
def project_list(request):
    if request.method == 'GET':
        items = Project.objects.order_by('pk')
        serializer = ProjectSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
    try:
        item = Project.objects.get(pk=pk)
    except Project.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ProjectSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProjectSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)


@csrf_exempt
@api_view(['GET', 'POST'])
def client_list(request):
    if request.method == 'GET':
        items = Client.objects.order_by('pk')
        serializer = ClientSerializer(items, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def client_detail(request, pk):
    try:
        item = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=404)

    if request.method == 'GET':
        serializer = ClientSerializer(item)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ClientSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        item.delete()
        return Response(status=204)
