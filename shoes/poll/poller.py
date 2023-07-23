import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoes_project.settings")
django.setup()

from shoes_rest.models import BinVO


def get_bins():
    response = requests.get('http://wardrobe-api:8000/api/bins/')
    content = json.loads(response.content)
    bin_obj = None
    for bin in content['bins']:
        bin_obj, created = BinVO.objects.get_or_create( #check this first argument given might have to be unique which is import_href then the rest in the defaults - do not have to include those
            import_href=bin['href'], #create in models left whatever i want to call it, right what is coming from wardrobe
            defaults = {
                "closet_name": bin["closet_name"],
                "bin_number": bin["bin_number"],
                "bin_size": bin["bin_size"],
            }
        )
        if created:
            print(f'New BinVO created: {bin}')
    return bin_obj

def poll():
    while True:
        print('Shoes poller polling for data')
        try:
            get_bins()
            print("success")

            # shoes = Shoe.objects.all()
            # for shoe in shoes:
            #     shoe.bin = bin
            #     shoe.save()

        except Exception as e:
            print(f'Polling error: {e}', file=sys.stderr)
        time.sleep(40)


if __name__ == "__main__":
    poll()
