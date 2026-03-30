def is_valid(s: str) -> bool:
    """
    Идея: открывающую скобку кладём в стек,
    при встрече закрывающей — проверяем, что на вершине
    стека лежит парная ей открывающая.

    Время:  O(n)
    Память: O(n)
    """
    matching = {")": "(", "]": "[", "}": "{"}
    stack = []

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            # Стек пуст или скобки не совпадают
            if not stack or stack[-1] != matching[ch]:
                return False
            stack.pop()

    return len(stack) == 0


# Демонстрация
tests = ["([]){}", "([)]", "((()))", ")(", ""]
for t in tests:
    print(f"{t!r:>12} -> {is_valid(t)}")
