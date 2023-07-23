from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import requests
import json

from common.json import ModelEncoder
from .models import Hat, LocationVO


class HatEncoder(ModelEncoder):
    model = Hat
    properties = [
        "id",
        "fabric",
        "style_name",
        "color",
        "picture_url",
        "wardrobe_location",
    ]


@require_http_methods(["GET", "POST"])
def api_list_hats(request):
    if request.method == "GET":
        hats = Hat.objects.all()
        hat_dicts = [hat.to_dict() for hat in hats]
        return JsonResponse(
            {"hats": hat_dicts},
            safe=False,
        )
    else:  # POST
        content = json.loads(request.body)

        location_id = content.get('wardrobe_location')

        try:
            response = requests.get(f'http://wardrobe-api:8000/api/locations/{location_id}/')
            response.raise_for_status()

            # Create a LocationVO instance
            location_data = response.json()
            location_instance, created = LocationVO.objects.get_or_create(
                id=location_data["id"],
                defaults={
                    "closet_name": location_data["closet_name"],
                    "section_number": location_data["section_number"],
                    "shelf_number": location_data["shelf_number"]
                },
            )

            # Assign the location instance to the 'wardrobe_location' key
            content['wardrobe_location'] = location_instance

            # Create the Hat instance
            hat = Hat.objects.create(**content)

            return JsonResponse(
                hat.to_dict(),
                encoder=HatEncoder,
                safe=False,
            )
        except requests.exceptions.HTTPError:
            response = JsonResponse({"message": "Location does not exist"})
            response.status_code = 404
            return response
        except KeyError:
            response = JsonResponse({"message": "Wardrobe location not provided in the request"})
            response.status_code = 400
            return response


@require_http_methods(["DELETE", "GET", "PUT"])
def api_list_hat(request, pk):
    if request.method == "GET":
        try:
            hat = Hat.objects.get(id=pk)
            return JsonResponse(
                hat.to_dict(),
                safe=False
            )
        except Hat.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            hat = Hat.objects.get(id=pk)
            hat.delete()
            return JsonResponse(
                hat.to_dict(),
                safe=False,
            )
        except Hat.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
    else: # PUT
        try:
            content = json.loads(request.body)
            hat = Hat.objects.get(id=pk)

            if 'wardrobe_location' in content:
                location = LocationVO.objects.get(id=content['wardrobe_location'])
                content['wardrobe_location'] = location

            props = ["fabric", "style_name", "color", "picture_url", "wardrobe_location"]
            for prop in props:
                if prop in content:
                    setattr(hat, prop, content[prop])
            hat.save()
            return JsonResponse(
                hat.to_dict(),
                safe=False,
            )
        except Hat.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
        except LocationVO.DoesNotExist:
            response = JsonResponse({"message": "Location does not exist"})
            response.status_code = 400
            return response
