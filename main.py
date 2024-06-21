import time

from project.app import main
result = []
if __name__ == '__main__':
    for i in range(0, 3):

        start_time = time.time()
        main()
        end_time = time.time()
        result.append(end_time - start_time)

    answ = 0.0
    for k, v in enumerate(result):
        if k == len(result) - 1:
            print(f"Время выполнения: {round(answ / len(result) - 1, 2)} секунд")

        else:
            answ += v



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
