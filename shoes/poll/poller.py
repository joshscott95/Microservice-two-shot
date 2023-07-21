import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shoes_project.settings")
django.setup()

from shoes_rest.model import BinVO, Shoe


def get_bins():
    response = requests.get('http://wardrobe-api:8000/api/bins/')
    bins = response.json()
    for bin in bins:
        bin, created = BinVO.objects.get_or_create(
            closet_name=bin['closet_name'],
            bin_number=bin['bin_number'],
            bin_size=bin['bin_size'],
        )
        if created:
            print(f'New BinVO created: {bin}')

def poll():
    while True:
        print('Shoes poller polling for data')
        try:
            get_bins()
            print("success")

            shoes = Shoe.objects.all()
            for shoe in shoes:
                shoe.bin = bin
                shoe.save()

        except Exception as e:
            print(f'Polling error: {e}', file=sys.stderr)
        time.sleep(60)


if __name__ == "__main__":
    poll()
