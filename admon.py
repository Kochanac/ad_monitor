#!/usr/bin/python3

import json
from back import get, render
from os import path

base_dir = path.dirname(__file__)
config = json.load(open( path.abspath(path.join(base_dir, "config.json")) , 'r'))

default_bars = {"polybar", "tint2"}

if config["enabled"]:
	data = get(url=config["url"], parser=config["parser"], teamname=config["teamname"])

	if config["bar"].lower() in default_bars:
		bar = "default"
	else:
		bar = config["bar"]

	rendered = render(data=data, bar=bar, config=config)

	print(rendered)

