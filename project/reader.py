import json
import re
from random import random

from project.env import APP_DIRECTORY_PRIZES, APP_FIRSTNAME, APP_SECONDNAME
from project.servis import cleaning_service


def number_counter(start = 15) -> int:
	for i in range(start, 19):
		yield i
		start += 1

def change_name_files() -> list:
	'''
	TODO: There is we only getting True file names
	:return:  list names
	'''
	removed_list = []
	out_filnames = []

	for i in number_counter():
		for name_file in [f'prizes_list_m{i}.txt',f'prizes_list_w{i}.txt']:
			try:
				if removed_list.count(name_file) > 0:
					continue
				else:
					'''Check the name file '''
					with open(f'{APP_DIRECTORY_PRIZES}/{name_file}', 'r', encoding='utf-8') as f:
						# print(f"File 'f'data/{name_file}' exists")
						f.close()

					out_filnames.append(name_file)
					# print(f'[removed_list]: {removed_list.count(name_file)}')
			except Exception as e:
				removed_list.append(name_file)
	# print(f'[RESPONCE]: {out_filnames}')
	return out_filnames

def readCleans_files(name_list:list) -> list:
	'''
	TODO: There we clean the content from charasterc
	:param name_list:
	:return: list
	'''
	result = []
	try:
		# for i in range(0, len(name_list) - 1):

		while len(name_list) > 0:
			# hook = None
			with open(f'{APP_DIRECTORY_PRIZES}/{name_list[0]}', 'r', encoding='utf-8') as f:

				lines = f.readlines()
				f.close()
				for line in lines:
					line = re.sub(r'\n', '', line)
					name_file = name_list[0].split('.txt')[0]
					result.append({name_file[-3:]: line})
			print('[name_list:]', name_list[0], '/', len(name_list))
			yield  result
			name_list.pop(0)
			i = 0
		# return result
		# print(f'[result]: {result}')

	except Exception as e:
		raise ValueError(f'[ERROR message]: Something what is wrong with function "read_files". Message: {e}')

def get_sport_meanList()-> list:
	try:
		with open(f'{APP_DIRECTORY_PRIZES}/race_data.json', 'r', encoding='utf-8') as f:
			return json.load(f)
	except Exception as e:
		raise ValueError(f'[ERROR message]: Something what is wrong with function "get_sport_meanList". Message: {e}')

def renameLinesOf_sport_meanList(json_list: list)-> list:
	'''
	TODO: There we ganging dictionary/object.
	Before was: `{
        "Нагрудный номер": 1,
        "Категория": "W15",
        "Имя": "Фаина",
        "Фамилия": "Martin",
        "Время старта": "18:01:50",
        "Время финиша": "23:14:12"
    },`
  After will be: '
  {'Имя и Фамилия': 'Дмитрий Clark',
   'Нагрудный номер': 16800,
   'Категория': 'M16',
   'Время старта': '21:19:23',
   'Время финиша': '03:16:06'}'

	:param json_list: is a entrypoin for a list of sport men
	:return: list
	'''


	new_list_position = []
	for json_ in json_list:
		new_list_position.append(cleaning_service(json_, APP_FIRSTNAME, APP_SECONDNAME, False))

	return new_list_position
