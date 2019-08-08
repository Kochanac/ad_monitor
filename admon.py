#!/usr/bin/python3

import json
from back import get, render
from os import path

base_dir = path.dirname(__file__)
config = json.load(open( path.abspath(path.join(base_dir, "config.json")) , 'r'))

if config["enabled"]:
	data = get(url=config["url"], parser=config["parser"], teamname=config["teamname"])

	rendered = render(data=data, bar=config["bar"], config=config)

	print(rendered)

