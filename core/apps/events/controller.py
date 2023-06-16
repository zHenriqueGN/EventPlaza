from .models import Event
from django.contrib.messages import add_message, constants


def event_register(request, data) -> bool:
    owner = data.get("owner")
    title = data.get("title")
    logo = data.get("logo")
    description = data.get("description")
    start_date = data.get("start_date")
    end_date = data.get("end_date")
    duration = data.get("duration")
    Event(
        owner=owner,
        title=title,
        logo=logo,
        description=description,
        start_date=start_date,
        end_date=end_date,
        duration=duration,
    ).save()
    add_message(request, constants.SUCCESS, "Event successfully registered!")
    return True
