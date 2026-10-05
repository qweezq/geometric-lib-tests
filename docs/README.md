# Geometric Lib

## Общее описание решения
Библиотека Geometric Lib содержит функции на языке Python для вычисления площади и периметра базовых геометрических фигур:
- Круг (circle.py)
- Квадрат (square.py)
- Прямоугольник (rectangle.py)
- Треугольник (triangle.py)

---

## Описание функций с примерами вызова

### 1. Круг (circle.py)
- **area(r)**  
  Вычисляет площадь круга по формуле $S = pi * r^2$. 
  Параметры: r (float/int) — радиус круга.  
  Возвращает: float — площадь круга.  
  Пример вызова:
  ```python
  from circle import area
  print(area(5))  # Вывод: 78.53981633974483
  ```

- **perimeter(r)**  
  Вычисляет длину окружности по формуле $P = 2 * pi * r$.
  Параметры: r (float/int) — радиус круга.  
  Возвращает: float — длина окружности.  
  Пример вызова:
  ```python
  from circle import perimeter
  print(perimeter(5))  # Вывод: 31.41592653589793
  ```

### 2. Квадрат (square.py)
- **area(a)**  
  Вычисляет площадь квадрата по формуле $S = a * a$.  
  Параметры: a (float/int) — длина стороны.  
  Возвращает: float/int — площадь квадрата.  
  Пример вызова:
  ```python
  from square import area
  print(area(5))  # Вывод: 25
  ```

- **perimeter(a)**  
  Вычисляет периметр квадрата по формуле $P = 4 * a$.  
  Параметры: a (float/int) — длина стороны.  
  Возвращает: float/int — периметр квадрата.  
  Пример вызова:
  ```python
  from square import perimeter
  print(perimeter(5))  # Вывод: 20
  ```

### 3. Прямоугольник (rectangle.py)
- **area(a, b)**  
  Вычисляет площадь прямоугольника по формуле $S = a * b$.  
  Параметры: a, b (float/int) — стороны прямоугольника.  
  Возвращает: float/int — площадь прямоугольника.  
  Пример вызова:
  ```python
  from rectangle import area
  print(area(5, 5))  # Вывод: 25
  ```

- **perimeter(a, b)**  
  Вычисляет периметр прямоугольника по формуле $P = 2 * (a + b)$.  
  Параметры: a, b (float/int) — стороны прямоугольника.  
  Возвращает: float/int — периметр прямоугольника.  
  Пример вызова:
  ```python
  from rectangle import perimeter
  print(perimeter(5, 5))  # Вывод: 20
  ```

### 4. Треугольник (triangle.py)
- **area(a, h)**  
  Вычисляет площадь треугольника по формуле $S = (a * h) / 2$.  
  Параметры: a (float/int) — основание, h (float/int) — высота.  
  Возвращает: float — площадь треугольника.  
  Пример вызова:
  ```python
  from triangle import area
  print(area(2, 2))  # Вывод: 2.0
  ```

- **perimeter(a, b, c)**  
  Вычисляет периметр треугольника по формуле $P = a + b + c$.  
  Параметры: a, b, c (float/int) — стороны треугольника.  
  Возвращает: float/int — периметр треугольника.  
  Пример вызова:
  ```python
  from triangle import perimeter
  print(perimeter(3, 4, 5))  # Вывод: 12
  ```

---

## История изменения проекта
- 9226055 fix rectangle.py and new file triangle.py
- 6842f51 new file rectangle.py
- d078c8d L-03: Docs added
- 8ba9aeb L-03: Circle and square added