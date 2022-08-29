from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


data=[
    {'data':{'name': 'Computer Hardware'}, 
    'id': 1, 
    'children': [
        {'data': {'name': 'Hard Drives'}, 'id': 3}, 
        {'data': {'name': 'Memory'}, 
        'id': 2, 
        'children': [
            {'data': {'name': 'Desktop Memory'}, 'id': 5}, 
            {'data': {'name': 'Laptop Memory'}, 'id': 6}, 
            {'data': {'name': 'Server Memory'}, 'id': 7}]}
    ,   {'data': {'name': 'SSD'}, 'id': 4}]}, 
    {'data': {'name': 'Desktop'}, 
    'id': 8, 
    'children': [
        {'data': {'name': 'code.desktop'}, 'id': 10}, 
        {'data': {'name': 'commands.txt'}, 'id': 12}, 
        {
            'data': {'name': 'egt'}, 
            'id': 9, 
            'children': [
                {
                    'data': {'name': 'vlcm_docker'}, 
                    'id': 14
                }
                ]
        }, 
        {'data': {'name': 'output.json'}, 'id': 11},
        {
            'data': {'name': 'sample'}, 
            'id': 13, 
            'children': [
                {
                    'data': {'name': 'treebeard'}, 
                    'id': 15
                    }
                    ]
        }]}]