# Условный оператор, циклы

## Логические выражения

Для проверки условий используется тип, у которого всего два
возможных значения: правда и ложь. С этими значениями можно
выполнять логические операции.

```
False and False
True or False
not True
```

Существуют стандартные команды, которые возвращают значения
булева типа. Например, операции сравнения.

```
7 > 5
7 >= 5
7 < 5
7 <= 5
7 == 5
7 != 5
2 < 5 <= 7 < 6

a = 3 > 2 and 10 < 5
a or (5 >= 7)
```

Преобразовать в булев тип можно с помощью команды `bool`.

```
bool(False)
bool(True)

bool(0)
bool(-1)

bool(0.0)
bool(0.5)

bool('')
bool("A")
```

Значения булева типа также можно рассматривать
как целые числа и использовать там, где используются
целые числа (например, в арифметических выражениях).

```
int(True)
int(False)
3 * False + True
True / (False - 2 * True)
```

## Условный оператор if

С помощью условного оператора можно проверить значение выражения
на правдивость. 

```
if True:
    print("YES")  
```

Все действия которые необходимо выполнить, должны следовать после
двоеточия в блоке команд, выделенных отступом.

```
if False:
    print("NO")
    print("NO")
  
if False:
    print("NO")
print("NO")
```

Если необходимо при выполнении условия делать одни действия, а иначе
другие, то используется else.

```
if 7 > 5:
    print("A")
else:
    print("B")
```

Полная запись условного оператора позволяет выбрать из нескольких
условий.

```
x = input()
if x == "a":
    print("Action A")
elif x == "b":
    print("Action B")
elif x == "c":
    print("Action C")
else:
    print("Default action")
```

В проверяемом выражении могут использоваться значения
любого типа. В этом случае условие выполняется, если результат
приведения к булеву типу - это «правда».

```
x = ""
y = 10

if x:
    print("A")
if y:
    print("B")
if x or y:
    print("C")
```

## Цикл while

Цикл while позволяет выполнять действия пока условие правдиво.

```
i = 0
while i < 10:
    print(i)
    i = i + 1
```

Внутри цикла могут быть команды break и continue. Первая 
завершает цикл, вторая переходит к следующему шага цикла,
игнорируя оставшиеся действия на этом шагу.

```
i = 0
while i < 100:
    i = i + 1
    if i > 10:
      break
    if i % 2 == 0:
      continue
    print(i)
```

## Цикл for и команда range

Цикл for предназначен для того, чтобы перебирать элементы
последовательностей. Пока мы знаем один тип последовательностей —
это строки.

```
for x in "abcde":
  print(x)
```

Чтобы перебрать диапазон целых чисел, необходимо
воспользоваться командой range, которая создает
последовательность чисел, представляющих диапазон.

```
r = range(10)
for x in r:
  print(x)

for x in range(3, 10):
  print(x)
  
for x in range(3, 10, 2):
  print(x)
  
for x in range(10, 3, -1):
  print(x)
```

Отмечу, что это «ленивая» последовательность и элементы
создаются не все сразу, а по мере необходимости.

```
for x in range(10**100):
  if x >= 10:
    break
  print(x)
```