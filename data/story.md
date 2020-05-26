## greet
* greet OR weather
  - utter_greet

## goodbye
* goodbye
  - utter_goodbye

## weather 1 - address_date
* address_date{"address": "上海", "date": "明天"}
  - utter_waiting
  - action_report_weather
  - utter_report_weather
* address{"address": "上海"} OR date{"date": "明天"}
  - utter_waiting
  - action_report_weather
  - utter_report_weather

## weather 2 - address + date
* address{"address": "上海"}
  - utter_date
* date{"date": "明天"}
  - utter_waiting
  - action_report_weather
  - utter_report_weather
* address{"address": "上海"} OR date{"date": "明天"}
  - utter_waiting
  - action_report_weather
  - utter_report_weather
  
## weather 3 - data + address
* date{"date": "明天"}
  - utter_address
* address{"address": "上海"}
  - utter_waiting
  - action_report_weather
  - utter_report_weather
* address{"address": "上海"} OR date{"date": "明天"}
  - utter_waiting
  - action_report_weather
  - utter_report_weather
  
## weather 4 - greet_1
* greet_address_date{"address": "上海", "date-time": "明天"}
  - utter_waiting
  - action_report_weather
  - utter_report_weather
* address{"address": "上海"} OR date{"date": "明天"}
  - utter_waiting
  - action_report_weather
  - utter_report_weather