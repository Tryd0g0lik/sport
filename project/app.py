import datetime
import json

from project.counter import get_time
from project.reader import change_name_files, readCleans_files, get_sport_meanList, renameLinesOf_sport_meanList


def main():
    list_m15 = []
    list_m16 = []
    list_m18 = []

    list_w15 = []
    list_w16 = []
    list_w18 = []
    l = change_name_files()
    categories = readCleans_files(l) # -> list "[{'m15': '1 место Золотая медаль'}]"
    # print('[categories:]', categories[0], '/', len(categories))
    spot_men_list = get_sport_meanList() # -> list
    total_list_ofMen = renameLinesOf_sport_meanList(spot_men_list)

    total_list_ofTime = get_time(total_list_ofMen)
    total_list_ofMen.clear()
    # for categore_list in categories:
    #     for categore in categore_list:
    for one_mane in total_list_ofTime:
        categore = one_mane['Категория'].lower()
        # number_position_ofCategore = int(list(categore.values())[0].split('место')[0].strip())
        # name_categore = categore
        if categore.find('m15') >= 0:
            list_m15.append(one_mane)
        elif categore.find('m16') >= 0:
            list_m16.append(one_mane)
        elif categore.find('m18') >= 0:
            list_m18.append(one_mane)

        elif categore.find('w15') >= 0:
            list_w15.append(one_mane)
        elif categore.find('w16') >= 0:
            list_w16.append(one_mane)
        else:
            list_w18.append(one_mane)
        total_list_ofTime.pop(0)

    ''' The counter of positions below '''
    categories_list = [list_m15, list_m16, list_m18,
                     list_w15, list_w16, list_w18]
    position_sorted_list = []
    try:
        for one_list in categories_list:
            for i in range(0, 10) : # len(one_list) - 1
                if i == 0:
                    position_sorted_list.append(one_list[0])
                else:

                    corrector_index = -1
                    for ind in range(0, len(position_sorted_list)) :
                        if ind >= len(position_sorted_list):
                            continue

                        first = datetime.datetime.strptime(position_sorted_list[ind]["Время"], "%H:%M:%S").time()
                        second = datetime.datetime.strptime(one_list[i]["Время"], "%H:%M:%S").time()
                        if first <= second:
                            if ind == 0 and corrector_index < ind:
                                corrector_index = 0

                            continue
                        elif first > second:
                            corrector_index = ind + 1

                    position_sorted_list.insert(corrector_index, one_list[i])
                    corrector_index = -1


            ''' The counter of place/positions below '''
            file_name = ''
            for ind, obj in enumerate(position_sorted_list):


                position_sorted_list[ind]["Место"] = str(ind + 1)
                key_ = position_sorted_list[ind]["Категория"].lower()

                place = 0
                new_l = l.copy()
                for val in readCleans_files(new_l): # position_sorted_list: # enumerate(categore_list):
                    k = list(val[0].keys())[0]
                    for v in val:
                        if k.find(key_) < 0:
                            val.clear()
                            continue

                        if int(position_sorted_list[ind]['Место']) == int(list(v.values())[0].split('место')[0]):
                            position_sorted_list[ind]['Приз'] = list(v.values())[0].split('место')[-1].lstrip()

                            place +=1
                            val.clear()
                            continue

                        if place == 49:
                            val.clear()
                            continue

            file_name += position_sorted_list[ind]["Категория"].lower()
            with open(f"data-out/{file_name}.json", "w", encoding='utf-8') as f:
                json.dump(position_sorted_list, f, ensure_ascii=False, indent=4)
            position_sorted_list.clear()

        if len(categories_list) > 0:
            categories_list.pop(0)


        pass
    except Exception as e:
        raise ValueError(f'[position_sorted_list]: Something what is wrong! {e}')
    pass


