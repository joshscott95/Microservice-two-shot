from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import Shoe

class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "manufacturer",
        "model_name",
        "id",
    ]

class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "size",
        "color",
        "manufacturer",
        "model_name",
        "picture",
        "bin",
    ]

@require_http_methods(["GET", "POST"])
def api_list_shoes(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        print(shoes[0].bin)
        
        return JsonResponse(
            {"shoes": shoes},
            encoder=ShoeListEncoder,
            safe=False
        )
    else:
        content = json.loads(request.body)
        shoe = Shoe.objects.create(**content)
        return JsonResponse(
            shoe,
            encoder=ShoeListEncoder,
            safe=False
        )

@require_http_methods(["DELETE", "GET", "PUT"])
def api_show_shoe(request, pk):

    if request.method == "GET":
        try:
            shoe = Shoe.objects.get(id=pk)
            return JsonResponse(
                {"shoe": shoe},
                encoder=ShoeDetailEncoder,
            )
        except Shoe.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response
    elif request.method == "DELETE":
        try:
            shoe = Shoe.objects.get(id=pk)
            shoe.delete()
            return JsonResponse(
                shoe,
                encoder=ShoeDetailEncoder,
                safe=False,
            )
        except Shoe.DoesNotExist:
            return JsonResponse({"message": "Does not exist"})
    else:
        try:
            content = json.loads(request.body)
            shoe = Shoe.objects.get(id=pk)

            props = [
                "size",
                "color",
                "manufacturer",
                "model_name",
                "picture",
                "bin",
            ]
            for prop in props:
                if prop in content:
                    setattr(shoe, prop, content[prop])
            shoe.save()

            return JsonResponse(
                shoe,
                encoder=ShoeDetailEncoder,
                safe=False,
            )
        except Shoe.DoesNotExist:
            response = JsonResponse({"message": "Does not exist"})
            response.status_code = 404
            return response