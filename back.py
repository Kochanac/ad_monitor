#!/usr/bin/python3

import json
import os, subprocess
from os import path

base_dir = path.dirname(__file__)

def get(url, teamname, parser):
	parserpath = path.join(base_dir, "parsers", parser.lower())
	parsesh = [parserpath, url, teamname]
	info = subprocess.run( parsesh, stdout=subprocess.PIPE ).stdout.decode('utf-8')

	data = json.loads(info)

	assert "name" in data \
		   and "score" in data \
		   and "place" in data \
		   and "services" in data

	for service in data["services"].values():
		assert "status" in service \
			   and "sla" in service \
			   and "flag_points" in service


	return data


def render(data, bar, config):
	barpath = path.join(base_dir, "bars", bar.lower())
	rendersh = [barpath, json.dumps(data), json.dumps(config)]
	rendered = info = subprocess.run( rendersh, stdout=subprocess.PIPE ).stdout.decode("utf-8")

	return rendered
