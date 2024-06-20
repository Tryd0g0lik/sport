from project.reader import change_name_files, readCleans_files, get_sport_meanList, renameLinesOf_sport_meanList


def main():
    l = change_name_files()
    name_clean_list = readCleans_files(l)
    spot_men_list = get_sport_meanList()
    total_list_ofMen = renameLinesOf_sport_meanList(spot_men_list)
    print(total_list_ofMen[0])

