import requests

from dagster import ConfigurableResource
from pydantic import Field


class EventResource(ConfigurableResource):
    url: str = Field(
        description=(
            "The URL accessed to get event data."
        ),
        default="https://api.apilayer.com/checkiday/events?adult=false"
    )

    api_key: str = Field(
        description=(
            "API key for accessing the API."
        )
    )

    def get_events(self):
        headers = {'apiKey': self.api_key}
        res = requests.get(self.url, headers=headers)
        events = res.json()
        return events

