#!/usr/bin/env python3
from hassapi import Hass

import configparser
import os


config = configparser.ConfigParser()
config.read(os.path.expanduser("~/.hass"))


# If you want to bypass certificate verification. Default set to True
hass = Hass(
    hassurl=config["config"]["endpoint"], token=config["config"]["token"], verify=False
)

hass.turn_off("switch.sonoff_a4800a5f5f")
