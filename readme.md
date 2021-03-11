# Version crawler

Crawl.py - скрипт для поиска неправильно именованных релизов (см. Правила именования в релизах зрелых продуктов: https://ximc.ru/projects/office/wiki/Правила_именования_выходных_файлов )

# Запуск

```
python Crawl.py
```
В окне Default path прописывается путь к папке, в которой ищутся неправильно именованные файлы
В окнах Correct regexp и Bad regexp соотвественно прописываются корректные и некорректные правила именования релиза.
Например, по умолчанию хорошее правило записано как: 
```
^([a-z_\d])+-(\d{1,2}\.\d{1,2}\.\d{1,2})(\.[a-z\d]{1,4})?(-[a-z_\d]+(\.([\d]+|x))?(\.([\d]+|x))?)?(-\([a-z_\d]+\))?(\.(zip|7z|tar\.gz|cod|json|txt|exe|sh|rpm|jar|swu|img|bin|deb|pdf))$
```
что означает, что к правильным символам относятся символы латинского алфавита. Тогда, чтобы добавить к списку правильных имен имена с символами русского алфавита, нужно переделать правило таким образом:
```
^([a-zа-я_\d])+-(\d{1,2}\.\d{1,2}\.\d{1,2})(\.[a-zа-я\d]{1,4})?(-[a-zа-я_\d]+(\.([\d]+|x))?(\.([\d]+|x))?)?(-\([a-zа-я_\d]+\))?(\.(zip|7z|tar\.gz|cod|json|txt|exe|sh|rpm|jar|swu|img|bin|deb|pdf))$
```
После этого необходимо нажать кнопку "Save config" и нажать "Start crawl".
В итоге в файлах Crawl_results_bad.txt и Crawl_results_good.txt появятся названия плохо и хорошо именованных релизов соответственно.

# Выпуск бинарных релизов

## Для Windows

Чтобы создать исполняемый exe-файл `version crawler` нужно запустить скрипт `release.bat`. Исполнимый файл `Crawl.exe` будет находится в папке release. Туда же будут помещены файлы `default.ini` и `readme.md`.