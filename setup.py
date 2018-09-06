#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-outreach",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Simon Data",
    url="http://simondata.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_outreach"],
    install_requires=[
        "singer-python==5.2.0",
        'requests==2.18.4',
        "pendulum==1.2.0",
    ],
    entry_points="""
    [console_scripts]
    tap-outreach=tap_outreach:main
    tap-outreach-kit=tap_outreach.kit:main
    """,
    packages=["tap_outreach"],
    package_data = {
        "schemas": ["tap_outreach/schemas/*.json"]
    },
    include_package_data=True,
)
