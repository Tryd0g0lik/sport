import json
import re
from random import random

from project.env import DIRECTORY_PRIZES

def number_counter(start = 15) -> int:
	for i in range(start, 19):
		yield i
		start += 1

def change_name_files() -> list:
	removed_list = []
	out_filnames = []

	for i in number_counter():
		for name_file in [f'prizes_list_m{i}.txt',f'prizes_list_w{i}.txt']:
			try:
				if removed_list.count(name_file) > 0:
					continue
				else:
					'''Check the name file '''
					with open(f'data/{name_file}', 'r', encoding='utf-8') as f:
						# print(f"File 'f'data/{name_file}' exists")
						f.close()

					out_filnames.append(name_file)
					# print(f'[removed_list]: {removed_list.count(name_file)}')
			except Exception as e:
				removed_list.append(name_file)
	# print(f'[RESPONCE]: {out_filnames}')
	return out_filnames

def readCleans_files(name_list:list):
	result = []
	try:
		for i in range(0, len(name_list)):
			with open(f'data/{name_list[0]}', 'r', encoding='utf-8') as f:

				lines = f.readlines()
				f.close()
				for line in lines:
					line = re.sub(r'\n', '', line)
					name_file = name_list[0].split('.txt')[0]
					result.append({name_file[-3:]: line})
			name_list.pop(0)
		# print(f'[result]: {result}')

	except Exception as e:
		raise ValueError(f'[ERROR message]: Something what is wrong with function "read_files". Message: {e}')

def get_sport_meanList()-> dict:
	try:
		with open(f'data/race_data.json', 'r', encoding='utf-8') as f:
			return json.load(f)
	except Exception as e:
		raise ValueError(f'[ERROR message]: Something what is wrong with function "get_sport_meanList". Message: {e}')

		# print(f'[f_json]: {f_json}')