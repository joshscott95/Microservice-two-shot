from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json
import requests

from common.json import ModelEncoder
from .models import Shoe, BinVO


class ShoeEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "id",
        "size",
        "color",
        "manufacturer",
        "model_name",
        "picture",
        # "bin",
    ]


@require_http_methods(["GET", "POST"])
def api_list_shoes(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        shoe_dicts = [shoe.to_dict() for shoe in shoes]
        return JsonResponse(
            {"shoes": shoe_dicts},
            safe=False,
        )
    else:  # POST
        content = json.loads(request.body)

        try:
            shoe = Shoe.objects.create(**content)
            
            return JsonResponse(
                shoe.to_dict(),
                safe=False,
            )
        except KeyError:
            response = JsonResponse({"message": "Required fields not provided in the request"})
            response.status_code = 400
            return response

@require_http_methods(["DELETE", "GET", "PUT"])
def api_list_shoe(request, pk):
    if request.method == "GET":
        try:
            shoe = Shoe.objects.get(id=pk)
            return JsonResponse(
                shoe.to_dict(),
                safe=False
            )
        except Shoe.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            shoe = Shoe.objects.get(id=pk)
            shoe_dict = shoe.to_dict()  # Save dictionary representation before deletion
            shoe.delete()
            return JsonResponse(
                shoe_dict,
                safe=False,
            )
        except Shoe.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
            
    else:  # PUT
        try:
            content = json.loads(request.body)
            shoe = Shoe.objects.get(id=pk)

            props = ["manufacturer", "model_name", "color", "picture"]
            for prop in props:
                if prop in content:
                    setattr(shoe, prop, content[prop])
            shoe.save()
            return JsonResponse(
                shoe.to_dict(),
                safe=False,
            )
        except Shoe.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
