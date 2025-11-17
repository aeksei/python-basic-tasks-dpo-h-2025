## Как развернуть проект

1  Развернуть виртуальное окружение
```commandline
python3 -m venv venv 
```
    Примечание
    https://docs.python.org/3/library/venv.html#how-venvs-work

2. Установить зависимости
```commandline
 pip install -r requirements.txt
```

## Настройка pre-commit
Активировать pre-commit
```commandline
pre-commit install
```

Деактивировать pre-commit
```commandline
pre-commit uninstall
```