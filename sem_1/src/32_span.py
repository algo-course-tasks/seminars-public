def stock_span(prices: list[int]) -> list[int]:
    """
    Замечание: span[i] = i - j, где j — индекс ближайшего
    дня СЛЕВА с ценой строго больше prices[i].
    Если такого нет, span[i] = i + 1.

    Это задача "Previous Greater Element" — решается
    монотонным стеком (убывающим), проход слева направо.

    В стеке храним индексы; выталкиваем всех, чья цена ≤ текущей.
    """
    n = len(prices)
    span = [0] * n
    stack = []  # индексы; prices[stack[...]] — убывающая последовательность

    for i in range(n):
        # Убираем дни с ценой ≤ текущей
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()

        # Если стек пуст — все предыдущие дни имели цену ≤ текущей
        span[i] = (i - stack[-1]) if stack else (i + 1)
        stack.append(i)

    return span


prices = [100, 80, 60, 70, 60, 75, 85]
print(f"Цены: {prices}")
print(f"Span: {stock_span(prices)}")
# Цены: [100, 80, 60, 70, 60, 75, 85]
# Span: [1, 1, 1, 2, 1, 4, 6]
