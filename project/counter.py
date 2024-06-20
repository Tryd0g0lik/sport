import datetime
from project.env import APP_START, APP_END
from project.servis import cleaning_service


def get_time(json_list: list):
	'''
	TODO: On the entrypoint get single position. It's has
	 template "{'Имя и Фамилия': 'Фаина Martin', 'Нагрудный номер': 1, 'Категория': 'W15', 'Время старта': '18:01:50', 'Время финиша': '23:14:12'}"

	:param json_mean:
	:return: average time between 'Время старта' and "Время финиша"
	'''
	try:
		new_list_position = []
		for json_var in json_list:
			if json_var.get("Время старта") != None and \
				json_var.get("Время финиша") != None:


				# Convertation the data's string type to a time type

				responce = cleaning_service(json_var, APP_START, APP_END, True)
				new_list_position.append(responce)
		return  new_list_position

	except Exception as e:
		pass
