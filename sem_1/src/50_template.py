def monotonic_stack_template(nums: list[int]) -> list[int]:
    """
    Шаблон: Next Greater Element (справа налево).

    Для Next Smaller — поменять > на <.
    Для Previous Greater — идти слева направо.
    Для строгого/нестрогого — менять <= на <.
    """
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(n - 1, -1, -1):  # направление
        while stack and stack[-1] <= nums[i]:  # условие монотонности
            stack.pop()
        if stack:
            result[i] = stack[-1]  # или i - stack[-1] для расстояния
        stack.append(nums[i])  # или i для индексов

    return result
