from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from django.conf import settings
from django.views.decorators.http import require_POST
import requests

def zetflix(request):
    return render(request, 'index.html')

def addToList(request):
    username = request.POST.get('username')
    itemid = request.POST.get('itemid')
    print(f"Username: {username}")
    print(f"Item ID: {itemid}")
    if username and itemid:
        backend_url = f"{settings.BACKEND_PATH}/mylist/add"
        payload = {'username': username, 'itemid': itemid }
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(backend_url, json=payload, headers=headers)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Username and item Id required'}, status=400)

def removeFromList(request):
    username = request.POST.get('username')
    itemid = request.POST.get('itemid')
    if username and itemid:
        backend_url = f"{settings.BACKEND_PATH}/mylist/delete"
        payload = {'username': username, 'itemid': itemid}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.delete(backend_url, json=payload, headers=headers)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Username and item ID are required'}, status=400)

def myList(request):
    username = request.POST.get('username')
    if username:
        backend_url = f"{settings.BACKEND_PATH}/mylist/get"
        payload = {'username': username}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.get(backend_url, json=payload, headers=headers)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Username is required'}, status=400)

def getMovie(request):
    return redirect(settings.BACKEND_PATH + '/movie/get')
def getTvshow(request):
    return redirect(settings.BACKEND_PATH + '/tvshow/get')
def getUser(request):
    return redirect(settings.BACKEND_PATH + '/user/get')

def addMovie(request):
    title = request.POST.get('titleMovie')
    if title:
        backend_url = f"{settings.BACKEND_PATH}/movie/create"
        payload = {'title': title}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(backend_url, json=payload, headers=headers)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Title is required'}, status=400)
    
def addTvshow(request):
    title = request.POST.get('titleTvshow')
    if title:
        backend_url = f"{settings.BACKEND_PATH}/tvshow/create"
        payload = {'title': title}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(backend_url, json=payload, headers=headers)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Title is required'}, status=400)


def addUser(request):
    username = request.POST.get('username')
    if username:
        backend_url = f"{settings.BACKEND_PATH}/user/create"
        payload = {'username': username}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.post(backend_url, json=payload, headers=headers)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Username is required'}, status=400)

def removeMovie(request):
    movieId = request.POST.get('movieId')
    if movieId:
        backend_url = f"{settings.BACKEND_PATH}/movie/delete"
        payload = {'movieId': movieId}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.delete(backend_url, json=payload, headers=headers)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'MovieId is required'}, status=400)
    
def removeTvshow(request):
    tvshowId = request.POST.get('tvshowId')
    if tvshowId:
        backend_url = f"{settings.BACKEND_PATH}/tvshow/delete"
        payload = {'tvshowId': tvshowId}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.delete(backend_url, json=payload, headers=headers)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'tvshowId is required'}, status=400)
    
def removeUser(request):
    username = request.POST.get('username')
    if username:
        backend_url = f"{settings.BACKEND_PATH}/user/delete"
        payload = {'username': username}
        headers = {'Content-Type': 'application/json'}
        
        try:
            response = requests.delete(backend_url, json=payload, headers=headers)
            response.raise_for_status()
            return JsonResponse(response.json(), status=response.status_code)
        except requests.RequestException as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Username is required'}, status=400)

def updateMovie():
    return redirect(settings.BACKEND_PATH + '/movie/get')
def updateTvshow():
    return redirect(settings.BACKEND_PATH + '/tvshow/get')
def updateUser():
    return redirect(settings.BACKEND_PATH + '/user/get')


