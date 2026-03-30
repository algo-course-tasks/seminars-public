class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        """Добавить элемент в конец стека"""
        self.items.append(x)

    def pop(self):
        """Удалить и вернуть последний элемент (выбросит ошибку на пустом стеке)"""
        return self.items.pop()

    def peek(self):
        """Вернуть последний элемент без удаления (выбросит ошибку на пустом стеке)"""
        return self.items[-1]

    def view(self):
        """Вернуть весь стек"""
        return self.items


def main() -> None:
    stack = Stack()
    print(stack.view())
    stack.push(1)
    print(stack.view())
    stack.push(2)
    print(stack.view())
    stack.push(3)
    print(stack.view())
    stack.pop()
    print(stack.view())
    stack.pop()
    print(stack.view())
    stack.pop()
    print(stack.view())


if __name__ == '__main__':
    main()
