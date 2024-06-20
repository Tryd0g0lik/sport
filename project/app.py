from project.counter import get_time
from project.reader import change_name_files, readCleans_files, get_sport_meanList, renameLinesOf_sport_meanList


def main():
    l = change_name_files()
    # name_clean_list = readCleans_files(l)
    spot_men_list = get_sport_meanList()
    total_list_ofMen = renameLinesOf_sport_meanList(spot_men_list)
    print(total_list_ofMen[0])
    # for v in total_list_ofMen:
    #     get_time(total_list_ofMen[0].copy())
    #     total_list_ofMen.pop(0)
    #     v.clear()
    get_time(total_list_ofMen[0].copy())



