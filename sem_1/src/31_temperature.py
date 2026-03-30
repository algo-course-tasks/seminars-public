def daily_temperatures(temperatures: list[int]) -> list[int]:
    """
    По сути — та же задача Next Greater Element,
    но нужен не сам элемент, а РАССТОЯНИЕ до него.

    Поэтому в стеке храним индексы.
    Идём слева направо: если текущая температура выше,
    чем у элемента на вершине стека — нашли ответ,
    расстояние = i - stack.pop().
    """
    n = len(temperatures)
    result = [0] * n
    stack = []  # индексы дней, для которых ищем ответ

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_day = stack.pop()
            result[prev_day] = i - prev_day
        stack.append(i)

    return result


temps = [73, 74, 75, 71, 69, 72, 76, 73]
print(f"Температуры: {temps}")
print(f"Ожидание:    {daily_temperatures(temps)}")
# Температуры: [73, 74, 75, 71, 69, 72, 76, 73]
# Ожидание:    [1, 1, 4, 2, 1, 1, 0, 0]
