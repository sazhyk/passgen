# passgen

Скрипт для генерации паролей.

Маленький подручный генератор паролей. Запускается из командной строки. Требует наличия python3.

Перед запуском необходимо сделать файл исполняемым. Например:
```bash
user@host:~$ chmod +x passgen.py
```
И зарустить
```bash
user@host:~$ ./passgen.py
```

## Пример
```bash
use@host:~$ ./passgen.py
Введите длину желаемого пароля.
Это должно быть число в диапазоне от 6 до 64: 10
Укажите количество требуемых паролей.
Это должно быть число в диапазоне от 1 до 20: 5
DqCi1DHBOO
8mvotivls5
SrQibTLSJT
nzTk6K8uSN
y3Rxc8RcbK
```
