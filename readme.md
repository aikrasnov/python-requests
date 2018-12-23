[![Build Status](https://travis-ci.org/aikrasnov/python-requests.svg?branch=master)](https://travis-ci.org/aikrasnov/python-requests)

## Как запустить тесты
### Локально
0) Получить доступ к апи на https://fixer.io/dashboard
1) Установить переменую окружения ACCESS_KEY
2) Склонировать репу
3) Установить pipenv ([инструкция](https://github.com/pypa/pipenv#installation))
4) Запустить `pipenv install --dev && pipenv run pytest`

### Посмотреть отчеты
1) Установить allure ([инструкция](https://docs.qameta.io/allure/#_installing_a_commandline))
2) Запустить тесты
3) Выполнить `allure generate report --clean && allure open allure-report`

### Ретраи и параллельность
[Ретраи](https://pypi.org/project/pytest-rerunfailures/), [параллельность](https://pypi.org/project/pytest-xdist/)

### Напечатать курл
`pipenv run pytest --showcurl` выведет курл для каждого запроса
