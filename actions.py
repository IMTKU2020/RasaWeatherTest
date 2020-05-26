import logging

from typing import List
from rasa_core_sdk.forms import FormAction, EntityFormField
from rasa_core_sdk.events import SlotSet
from requests import (
    ConnectionError,
    HTTPError,
    TooManyRedirects,
    Timeout
)
from api import get_weather_by_day


logger = logging.getLogger(__name__)


class ActionReportWeather(FormAction):
    RANDOMIZE = True

    @staticmethod
    def required_fields():
        return [
            EntityFormField("address", "address"),
            EntityFormField("date", "date"),
        ]

    def name(self):
        return "action_report_weather"

    def submit(self, dispatcher, tracker, domain):
        address = tracker.get_slot('address')
        date_time = tracker.get_slot('date')

        logger.debug("get address and date: {}|{}".format(address, date_time))

        date_time_number = text_date_to_number_date(date_time)

        if isinstance(date_time_number, str):  # parse date_time failed
            return [SlotSet("matches", "暂不支持查询[{}{}]的天气".format(
                address, date_time))]
        else:
            try:
                weather_data = get_text_weather_date(address,
                                                     date_time,
                                                     date_time_number)
            except:
                return [SlotSet("matches", "暂不支持查询[{}{}]的天气".format(
                    address, date_time))]

            return [SlotSet("matches", "{}".format(weather_data))]

