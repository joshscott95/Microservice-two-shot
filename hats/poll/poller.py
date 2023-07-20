import django
import os
import sys
import time
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hats_project.settings")
django.setup()

from hats_rest.models import Hat, LocationVO


def poll():
    while True:
        print('Hats poller polling for data')
        try:
            response = requests.get('http://wardrobe-api:8000/api/locations/')
            locations = response.json()
            for loc in locations:
                # Check if location already exists in our model, if not create new one
                location, created = LocationVO.objects.get_or_create(
                    closet_name=loc['closet_name'], 
                    section_number=loc['section_number'], 
                    shelf_number=loc['shelf_number']
                )
                if created:
                    print(f'Created new LocationVO: {location}')

                # At this point, you should decide which hat should be in this location.
                # In this example, all hats are assigned to every location, which is unlikely your real case.
                # You probably want to match hats with locations based on some rule.
                hats = Hat.objects.all()
                for hat in hats:
                    hat.wardrobe_location = location
                    hat.save()

        except Exception as e:
            print(f'Error while polling: {e}', file=sys.stderr)
        time.sleep(60)

if __name__ == "__main__":
    poll()
