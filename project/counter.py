import datetime


def get_time(json_mean: object):
	'''
	TODO: On the entrypoint get single position. It's has
	 template "{'Имя и Фамилия': 'Фаина Martin', 'Нагрудный номер': 1, 'Категория': 'W15', 'Время старта': '18:01:50', 'Время финиша': '23:14:12'}"

	:param json_mean:
	:return: average time between 'Время старта' and "Время финиша"
	'''
	try:
		time_start = "01:29:23"
		time_end = "09:23:52"
		if json_mean.get("Время старта") != None and \
			json_mean.get("Время финиша") != None:

			time_start = json_mean["Время старта"]
			time_end = json_mean["Время финиша"]
		# Convertation the data's string type to a time type
		start = datetime.datetime.strptime(time_start, "%H:%M:%S")
		end = datetime.datetime.strptime(time_end, "%H:%M:%S")
		time_result = (end - start)
		print(time_result)
	except Exception as e:
		pass