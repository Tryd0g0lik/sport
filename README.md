[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/YeZ4Jj1g)
### Задание Python

В файле race_data.json находятся данные о соревновании, в котором участвуют 100000 спортсменов.

В файлах m15/16/18 и w15/16/18.txt находятся данные о призовом фонде для каждой категории спортсменов.

У каждого спортсмена есть категория, порядковый номер, имя и фамилия. А также время старта и время финиша.

В файлах о призовом фонде находятся данные в виде "№ место Приз"

 Необходимо рассчитать время забега каждого спортсмена по категориям и составить JSON файлы вида:
``` json
[
  {
    "Нагрудный номер": 10,
    "Имя и Фамилия": "Иван Иванов",
    "Время": "05:04:33",
    "Место": 1,
    "Приз": "Золотая медаль"
  },
  {
    "Нагрудный номер": 23,
    "Имя и Фамилия": "Петр Сидоров",
    "Время": "05:04:33",
    "Место": 2,
    "Приз": "Серебряная медаль"
  }
]
```
 Названием JSON файла должна быть категория спортсменов, которые в нем содержатся (m15, m16, m18 ...) .

Чем меньше времени спортсмен потратил на забег, тем выше должно быть его место. Если у спортсменов совпадает время, выше в итоговом результате становится тот, у кого нагрудный номер ближе к 1.

Призы раздаются только за первые 49 мест в каждой категории. У остальных спортсменов поле "приз" должно отсутствовать.

### Обратите внимание:
Задание выполнять только стандартными средствами языка программирования. Без установки сторонних библиотек. Не допускается использование модулей `sys` и `os`.

Оценивается как полнота выполнения задания, так и скорость выполнения программы.

Код запускается несколько раз, и считается среднее время за все запуски.

Точка входа должна находиться в файле `main.py`

В конце файла должен находиться код вида:
``` python
if __name__ == "__main__":
	main()
```
Выполнения команды `python main.py` должно быть достаточно для того, чтобы программа выполнилась полностью и создала все необходимые файлы.
