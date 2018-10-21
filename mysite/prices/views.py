import re

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from flats.models import Flat
from houses.models import House
from prices.serializers import PricesSerializer

flat_model = Flat
house_model = House


@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def upload_prices(request):
    serializer = PricesSerializer(data=request.data)

    if serializer.is_valid():
        check_is_owner_house(user=request.user, house_id=serializer.validated_data['house_id'])

        number_of_success_updated = update_flat_prices(data=serializer.validated_data)

        content = {
            'message': 'Кол-во квартир у которых обновилась цена равно {number_of}.'
                .format(number_of=number_of_success_updated)
        }
        status = 200
    else:
        content = serializer.errors
        status = 400

    return Response(content, status=status)


def check_is_owner_house(user, house_id):
    house = house_model.objects.filter(user=user).filter(pk=house_id)

    if not house:
        raise Http404()


def update_flat_prices(data):
    number_of_success_updated = 0

    for line in data['price']:
        clean_line = line.decode('utf-8').rstrip()

        is_correct_format = re.search('^[0-9]+~[0-9]+$', clean_line)
        if not is_correct_format:
            continue

        numbers_prices = clean_line.split('~')

        flat = flat_model.objects.filter(
            house_id=data['house_id']
        ).filter(
            number=numbers_prices[0]
        ).first()

        if flat:
            flat.price = numbers_prices[1]
            flat.save()
            number_of_success_updated += 1

    return number_of_success_updated
