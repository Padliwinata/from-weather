from dagster import Definitions, load_assets_from_modules, EnvVar, AssetSelection, ScheduleDefinition, define_asset_job

from from_weather import assets  # type: ignore
from from_weather.resources import EventResource

all_assets = load_assets_from_modules([assets])

event_job = define_asset_job("event_job", selection=AssetSelection.all())

event_schedule = ScheduleDefinition(
    job=event_job,
    cron_schedule="0 12 * * *"
)

defs = Definitions(
    assets=all_assets,
    schedules=[event_schedule],
    resources={
        'event_resource': EventResource(api_key=EnvVar("API_KEY"))
    },
)
