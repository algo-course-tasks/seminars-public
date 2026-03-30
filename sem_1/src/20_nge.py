def next_greater_naive(nums: list[int]) -> list[int]:
    """Для каждого элемента ищем вправо первый больший — O(n²)."""
    n = len(nums)
    result = [-1] * n
    for i in range(n):
        for j in range(i + 1, n):
            if nums[j] > nums[i]:
                result[i] = nums[j]
                break
    return result


def next_greater(nums: list[int]) -> list[int]:
    """
    Идея: идём справа налево и поддерживаем стек,
    в котором лежат "кандидаты" на ответ — элементы
    в порядке убывания снизу вверх.

    Для текущего nums[i]:
    1) Выкидываем из стека всё, что ≤ nums[i]
       (эти элементы уже никогда не станут ответом
        для элементов левее — nums[i] ближе и больше).
    2) Если стек не пуст — вершина и есть ответ.
    3) Кладём nums[i] в стек.

    Время:  O(n) — каждый элемент push/pop не более 1 раза
    Память: O(n)
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # хранит значения (можно индексы — зависит от задачи)

    for i in range(n - 1, -1, -1):
        # Убираем всех, кто не может быть "next greater"
        while stack and stack[-1] <= nums[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(nums[i])

    return result


def next_greater_left_to_right(nums: list[int]) -> list[int]:
    """
    Другой стиль: идём слева направо,
    в стеке храним ИНДЕКСЫ элементов, для которых
    ещё не нашли ответ.

    Когда nums[i] > nums[stack[-1]] — мы нашли ответ
    для элемента на вершине стека.
    """
    n = len(nums)
    result = [-1] * n
    stack = []  # индексы

    for i in range(n):
        while stack and nums[i] > nums[stack[-1]]:
            idx = stack.pop()
            result[idx] = nums[i]
        stack.append(i)

    return result


# Демонстрация

# Массив:       [2, 1, 2, 4, 3]
# Next greater: [4, 2, 4, -1, -1]
a = [2, 1, 2, 4, 3]

print("1. next_greater_naive")
print(f"Массив:       {a}")
print(f"Next greater: {next_greater_naive(a)}")

print("2. next_greater")
print(f"Массив:       {a}")
print(f"Next greater: {next_greater(a)}")

print("3. next_greater_left_to_right")
print(f"Массив:       {a}")
print(f"Next greater: {next_greater_left_to_right(a)}")

# Проверка: оба варианта дают одинаковый результат
assert next_greater(a) == next_greater_left_to_right(a)
print("4. next_greater & next_greater_left_to_right")
print("Оба варианта совпадают")
