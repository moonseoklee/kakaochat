from django.http import JsonResponse
import json

def keyboard(request):
    return JsonResponse({
        'type' : 'buttons',
        'buttons' : ['Tron', 'Bitcoin', 'ADA']
    })

def message(request):
    #message = ((request.body).decode('utf-8'))
    #return_json_str = json.loads(message)
    #return_str = return_json_str['content']

    return JsonResponse({
        'message' : {
            'text' : 'result is abc!'
        },
        'keyboard' : {
            'type' : 'buttons',
            'buttons' : ['Tron', 'Bitcoin', 'ADA']
        }
    })