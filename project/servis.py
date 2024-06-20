from datetime import datetime


def __common_service(k_item1: str, k_item2: str,
                v_item1: str, v_item2: str,
                tryFalse:bool = False) -> object:

	if tryFalse == False:
		return {f'{k_item1} и {k_item2}': f'{v_item1} {v_item2}'}
	else:
		return {f'{k_item1}': f'{v_item1}'}

def cleaning_service(json_:object, item1: str, item2: str, tryFalse:bool) -> object:
	new_json_position = {}
	new_list_position = []
	if (json_.get(item1) != None) and (json_.get(item2) != None):
		name = json_.get(item1)
		secondname = json_.get(item2)
		if tryFalse == False:
			resp: object = __common_service(item1, item2, name, secondname)
			new_json_position.update(resp)
		if tryFalse != False:
			start = json_[item1]
			end = json_[item2]
			start = datetime.strptime(start, "%H:%M:%S")
			end = datetime.strptime(end, "%H:%M:%S")
			time_result = (end - start)

			# new_time_result = (str(time_result)[1:] if '-' in str(time_result)[:2] else str(time_result)) if 'day' in str(time_result) else str(time_result)
			new_time_result = str(time_result).split(' ')[-1]
			resp: object = __common_service("Время", '', str(new_time_result), '', tryFalse)
			new_json_position.update(resp)



	for k, v in json_.items():
		if k.find(item1) < 0 and (k.find(item2) < 0):
			new_json_position.update({k: v})
	new_list_position.append(new_json_position.copy())
	new_json_position.clear()
	return  new_list_position[0]

