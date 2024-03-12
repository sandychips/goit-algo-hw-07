# Визначення класу для вузла дерева
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Завдання 1: Знаходження найбільшого значення у двійковому дереві
def find_max_value(root):
    # Перевірка, чи дерево пусте
    if root is None:
        return float('-inf')  # Повертаємо негативну нескінченність, якщо дерево порожнє
    
    # Проходження по правим гілкам дерева
    while root.right is not None:
        root = root.right
    
    # Повертаємо значення найбільшого вузла
    return root.value

# Завдання 2: Знаходження найменшого значення у двійковому дереві
def find_min_value(root):
    # Перевірка, чи дерево порожнє
    if root is None:
        return float('inf')  # Повертаємо позитивну нескінченність, якщо дерево порожнє
    
    # Проходження по лівим гілкам дерева
    while root.left is not None:
        root = root.left
    
    # Повертаємо значення найменшого вузла
    return root.value

# Завдання 3: Знаходження суми всіх значень у двійковому дереві
def find_sum(root):
    # Перевірка, чи дерево порожнє
    if root is None:
        return 0  # Повертаємо 0, якщо дерево порожнє
    
    # Рекурсивно обходимо всі вузли дерева і додаємо їх значення
    return root.value + find_sum(root.left) + find_sum(root.right)

# Приклад використання:
# Створення дерева
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.right = TreeNode(20)

# Виклик функцій і виведення результатів
print("Максимальне значення у дереві:", find_max_value(root))
print("Мінімальне значення у дереві:", find_min_value(root))
print("Сума всіх значень у дереві:", find_sum(root))
