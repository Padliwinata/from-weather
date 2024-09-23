from datetime import datetime
import json
import os
import random

import requests
from bs4 import BeautifulSoup
from dagster import asset, MaterializeResult, AssetExecutionContext
from .resources import EventResource


@asset
def events(context: AssetExecutionContext, event_resource: EventResource) -> MaterializeResult:
    data = event_resource.get_events()

    context.log.info(f"Keys: {data.keys()}")
    os.makedirs('data', exist_ok=True)

    with open("data/events.json", "w") as f:
        json.dump(data, f)

    return MaterializeResult(
        metadata={
            "Adult": False,
            "Date": datetime.today().strftime("%d/%m/%Y"),
            "Number of Events": len(data['events']),
            "Timezone": "America/Chicago"
        }
    )


@asset(deps=[events])
def single_event(context: AssetExecutionContext) -> MaterializeResult:
    with open('data/events.json', 'r') as f:
        event_list = json.load(f)

    # context.log.info(event_list)
    random_event = random.choice(event_list['events'])

    raw_page = requests.get(random_event['url'])
    page = BeautifulSoup(raw_page.content, 'html.parser')
    description = page.find("div", class_='mdl-cell mdl-cell--8-col').find('p').text
    return MaterializeResult(
        metadata={
            'Event': random_event['name'],
            'URL': random_event['url'],
            'Description': description
        }
    )


