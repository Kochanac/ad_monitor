#!/usr/bin/python3

import json
import os, subprocess
from os import path

base_dir = path.dirname(__file__)


test_json = """{"name": "Teamname", "place": 1, "score": 1337, "services": {"first": {"status": "up", "sla": 14.68, "flag_points": 1200, "flags": {"got": 42, "lost": 2}}, "second": {"status": "down", "sla": 12.01, "flag_points": 228, "flags": {"got": 5, "lost": 30}}}, "round": 124}"""
def get(url, teamname, parser):
	if url == "test":
		return json.loads(test_json)
		
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
