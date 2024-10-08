import json
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse


# Create your views here.
def users_list(request):
    pass

def user_detail(request, username):
    pass

def create_user(request):
    if request.method == "POST":
        # Getting data
        decoded_body = request.body.decode('utf-8')
        body = json.loads(decoded_body)

        # Data validation
        errors = []
        if body['username'] == "":
            errors.append({'username': 'username cannot be empty'})

        if body['birth_date'] == "":  # TODO: Validate date format
            errors.append({'birth_date': 'Incorrect date format'})

        if body['email'] == "":  # TODO: Validate email format
            errors.append({'birth_date': 'Incorrect email format'})

        if len(errors) > 0:
            return JsonResponse({'errors': errors}, status=400)

        # Saving data in DB:
        user = User.objects.create(
            username=body['username'],
            password=body['password'],
            email=body['email'],
            birth_date=body['birth_date'],
            biography=body['biography']
        )

        return JsonResponse(data={'message': 'Created user', 'id': user.id, 'username': user.username})

    return HttpResponse("Method not allowed", status=405)

def update_user(request, username):
    pass

def delete_user(request, username):
    pass

