from django.core.management import BaseCommand
from django.core.management.base import CommandError
from accounts.models import CustomUser
import json
import requests


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("count", type=int)

    def handle(self, *args , **options):
        count = options.get("count")
        user_list = []
        for i in range(count, 0, -5000):
            if i > 5000:
                req_count = 5000
            else:
                req_count = count
            api_url = "https://randomuser.me/api/?results=" + str(req_count)
            res = requests.get(api_url)
            user_infos = json.loads(res.text)["results"]
            for user_info in user_infos:
                name = user_info["name"]["first"]
                surname = user_info["name"]["last"]
                gender = user_info["gender"]
                email = user_info["email"]
                age = int(user_info["dob"]["age"])
                phone = user_info["phone"]
                city = user_info["location"]["city"]
                state = user_info["location"]["state"]
                custom_user = CustomUser(
                    name=name,
                    surname=surname,
                    gender=gender,
                    email=email,
                    age=age,
                    phone=phone,
                    city=city,
                    state=state
                )
                user_list.append(custom_user)
        CustomUser.objects.save_data(users=user_list)

