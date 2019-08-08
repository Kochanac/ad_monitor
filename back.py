#!/usr/bin/python3

import json
import os, subprocess
from os import path

base_dir = path.dirname(__file__)

def get(url, teamname, parser):
	# exec('from parsers import {}'.format(path_to_parser))
	# parsesh = "./parsers/{parser} '{url}' '{teamname}'".format(parser=parser.lower(), url=url, teamname=teamname)
	parsepath = path.join(base_dir, "parsers", parser.lower())
	parsesh = [parsepath, url, teamname]
	
	info = subprocess.run( parsesh, stdout=subprocess.PIPE).stdout.decode('utf-8')

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
	# rendersh = "./bars/{bar} '{data}'".format(bar=bar.lower(), data=json.dumps(data))
	barpath = path.join(base_dir, "bars", bar.lower())
	rendersh = [barpath, json.dumps(data), json.dumps(config)]

	rendered = info = subprocess.run( rendersh, stdout=subprocess.PIPE ).stdout.decode("utf-8")

	return rendered
	