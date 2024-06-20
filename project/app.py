import datetime

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


    categories_list = [list_m15, list_m16, list_m18,
                     list_w15, list_w16, list_w18]
    position_sorted_list = []
    try:
        for one_list in categories_list:
            for i in range(0, len(one_list) - 1) :
                if i == 0:
                    position_sorted_list.append(one_list[0])
                else:

                    for ind in range(0, len(position_sorted_list)) :
                        if ind >= len(position_sorted_list):
                            return
                        first = datetime.datetime.strptime(position_sorted_list[ind]["Время"], "%H:%M:%S").time()
                        second = datetime.datetime.strptime(one_list[i]["Время"], "%H:%M:%S").time()
                        if first <= second:
                            position_sorted_list.append(one_list[i])
                        elif first > second:


                            position_sorted_list.insert(i - 1, one_list[i])


        pass
    except Exception as e:
        raise ValueError(f'[position_sorted_list]: Something what is wrong! {e}')
    pass


