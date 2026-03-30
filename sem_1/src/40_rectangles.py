def largest_rectangle_two_pass(heights: list[int]) -> int:
    """
    Шаг 1: для каждого i находим left[i] — индекс ближайшего
            столбца слева, который СТРОГО ниже heights[i].
    Шаг 2: аналогично right[i] — справа.
    Шаг 3: площадь для столбца i = heights[i] * (right[i] - left[i] - 1).

    Время:  O(n)
    Память: O(n)
    """
    n = len(heights)
    left = [-1] * n  # previous smaller
    right = [n] * n  # next smaller
    stack = []

    # Проход слева направо — ищем Previous Smaller
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    stack.clear()

    # Проход справа налево — ищем Next Smaller
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    # Считаем максимальную площадь
    max_area = 0
    for i in range(n):
        width = right[i] - left[i] - 1
        area = heights[i] * width
        max_area = max(max_area, area)

    return max_area

def largest_rectangle_debug(heights):
    """Версия с выводом промежуточных данных."""
    n = len(heights)
    left = [-1] * n
    right = [n] * n
    stack = []

    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    stack.clear()

    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    print(
        f"{'i':>3} | {'h[i]':>4} | {'left':>4} | {'right':>5} | {'ширина':>6} | {'площадь':>7}"
    )
    print("-" * 45)
    max_area = 0
    for i in range(n):
        w = right[i] - left[i] - 1
        area = heights[i] * w
        max_area = max(max_area, area)
        marker = " <<<" if area == max_area and area > 0 else ""
        print(
            f"{i:>3} | {heights[i]:>4} | {left[i]:>4} | {right[i]:>5} | {w:>6} | {area:>7}{marker}"
        )

    return max_area

def largest_rectangle_one_pass(heights: list[int]) -> int:
    """
    Один проход с "сентинелом" (sentinel).
    Сторожевое значение, обозначающее конец данных.
    https://en.wikipedia.org/wiki/Sentinel_value

    Добавляем 0 в конец массива — это гарантирует,
    что все столбцы будут вытолкнуты из стека.

    Когда столбец выталкивается — мы знаем его правую
    границу (текущий i) и левую границу (новая вершина стека).
    """
    heights = heights + [0]  # сентинел
    stack = [-1]  # сентинел-индекс для левой границы
    max_area = 0

    for i in range(len(heights)):
        while stack[-1] != -1 and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area



h = [2, 1, 5, 6, 2, 3]

print(f"Высоты: {h}")
print(f"Макс. площадь: {largest_rectangle_two_pass(h)}")
# Макс. площадь: 10

largest_rectangle_debug(h)

# Проверка
assert largest_rectangle_one_pass([2, 1, 5, 6, 2, 3]) == 10
assert largest_rectangle_one_pass([2, 4]) == 4
assert largest_rectangle_one_pass([1]) == 1
print("Все тесты пройдены")
