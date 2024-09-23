from setuptools import find_packages, setup

setup(
    name="from_weather",
    packages=find_packages(exclude=["from_weather_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "requests",
        "openmeteo-requests",
        "requests-cache",
        "retry-requests",
        "numpy",
        "pandas",
        "beautifulsoup4"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
