from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
import json

from common.json import ModelEncoder
from .models import BinVO, Shoe

class BinVODetailEncoder(ModelEncoder):
    model = BinVO
    properties = [
        "closet_name",
        "import_href",
    ]

class ShoeListEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "manufacturer",
        "model_name",
    ]

    def get_extra_data(self, o):
        return {"bin": o.bin.import_href}

class ShoeDetailEncoder(ModelEncoder):
    model = Shoe
    properties = [
        "color",
        "manufacturer",
        "model_name",
        "picture",
        "bin",
    ]
    encoders = {
        "bin": BinVODetailEncoder(),
    }

@require_http_methods(["GET", "POST"])
def api_list_shoes(request):
    if request.method == "GET":
        shoes = Shoe.objects.all()
        return JsonResponse(
            {"shoes":shoes},
            encoder=ShoeListEncoder,
            safe=False
        )
    else:
        content = json.loads(request.body)
        print(content)

        try:
            bin_href = content["bin"]
            print(f'this is the href {bin_href}')
            bin = BinVO.objects.get(import_href=bin_href)
            print(f'this is the bin: {bin}')
            content["bin"] = bin

        except BinVO.DoesNotExist as e:
            print(e)
            return JsonResponse(
                {"message": "Invalid bin id"},
                status=400
            )

        try:
            shoe = Shoe.objects.create(**content) #put at the end of the function after trying to create a bin variable that is getting the BinVO using id or href then setting the content at bin to the BinVO that we just got then if it works then create the shoe
            return JsonResponse(
                shoe,
                encoder=ShoeDetailEncoder,
                safe=False
            )

        except Exception as e:
            print(e)  # Print the exception
            return JsonResponse(
                {"message": "An error occurred. Check server logs for more information."},
                status=400,
            )



# @require_http_methods(["DELETE", "GET", "PUT"])
# def api_show_shoe(request, pk):

#     if request.method == "GET":
#         shoe = Shoe.objects.get(id=pk)
#         return JsonResponse(
#             {"shoe": shoe},
#             encoder=ShoeDetailEncoder,
#         )
#     elif request.method == "DELETE":
#         try:
#             shoe = Shoe.objects.get(id=pk)
#             shoe.delete()
#             return JsonResponse(
#                 shoe,
#                 encoder=ShoeDetailEncoder,
#                 safe=False,
#             )
#         except Shoe.DoesNotExist:
#             return JsonResponse({"message": "Does not exist"})