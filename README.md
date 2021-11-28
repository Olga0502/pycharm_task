# Профилизатор в PyCharm
Результат для filter.py:

![1](https://user-images.githubusercontent.com/93836720/143690360-55b364fd-cecc-433c-b1c4-35286e09d7cf.jpg)

Результат для old_filter.py:

![2](https://user-images.githubusercontent.com/93836720/143690369-0abb0a71-5303-4cc2-8c51-fc0de17235be.jpg)Cancel changes


Из данных скриншотов мы видим, что время выполнения нового файла больше. Это связано с тем, что у нас есть ввод данных с консоли.

Результат для filter_with_filename.py:

![3](https://user-images.githubusercontent.com/93836720/143690370-fb40b284-a834-44b6-ae4b-a4e0a6e3b764.jpg)

Без ввода данных мы можем заметить, как сильно уменьшилось время, благодаря исправлению ошибок в программе, использованию библиотек и выделению функций.


# Изображения
Изображение до обработки: 

![img2](https://user-images.githubusercontent.com/93836720/143719660-8c0b8ed1-ba7c-4ae5-ac5d-62793faea510.jpg)

После обработки old_filter.py:

![res](https://user-images.githubusercontent.com/93836720/143719788-dce68f67-e0c8-4906-8c42-8c7b522db94e.jpg)

После обработки filter.py:

![f1](https://user-images.githubusercontent.com/93836720/143719797-d3b93cf9-d2dd-4c57-aa6c-1d214a810f63.jpg)


После обработки filter_with_filename.py:

![f2](https://user-images.githubusercontent.com/93836720/143719814-37ae3915-fcc9-4f96-9572-41f9bdcec0ae.jpg)


# DOC-тесты

Doc-тест для функции get_brightness:

![test](https://user-images.githubusercontent.com/93836720/143733664-7ee466a4-d591-4b38-99b8-fa5cb07048c4.jpg)

Тест выполняется:

![done](https://user-images.githubusercontent.com/93836720/143733678-5d55de4b-1fea-4338-9ab8-db0e37f3a7b1.jpg)

Если же тест не выполняется:

![no](https://user-images.githubusercontent.com/93836720/143733684-f53870bd-8cda-4a47-a44a-eeed745cf7ae.jpg)

Для функции set_color нет тестов, т.к. функция ничего не возвращает.

Для функции grey_img нет тестов, т.к. функция возвращает итоговое изображение(объект numpy).
