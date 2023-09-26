import json
from django.core.exceptions import ValidationError
from django.http import JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Robot, RobotModel


@csrf_exempt
def create_robot(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            model = data['model']
            version = data['version']
            created = data['created']

            # Проверка на соответствие существующим моделям
            if not RobotModel.objects.filter(name=model).exists():
                return JsonResponse(
                    {'error': f'Model {model} does not exist.'},
                    status=400
                )
            robot_model = RobotModel.objects.get(name=model)

            # Проверка на валидность даты
            try:
                created_date = (
                    timezone.datetime.strptime(created, '%Y-%m-%d %H:%M:%S')
                )
            except ValueError:
                return JsonResponse(
                    {'error': 'Invalid date. Use "YYYY-MM-DD HH:MM:SS".'},
                    status=400
                )

            robot = Robot(
                model=robot_model,
                version=version,
                created=created_date
            )
            robot.save()
            return JsonResponse(
                {'message': 'Robot created successfully.'},
                status=201
            )

        except (json.JSONDecodeError, KeyError, ValidationError) as error:
            return JsonResponse({'error': str(error)}, status=400)
    else:
        return JsonResponse(
            {'error': 'Only POST requests allowed.'},
            status=405
        )
