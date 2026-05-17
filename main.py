from avl import AVLNode, insert
import heapq

## Завдання 1
## Напишіть алгоритм (функцію), який знаходить найменше значення у двійковому дереві пошуку або в AVL-дереві.
def min(root: AVLNode):
    if not root:
        return None

    left = root.left
    min = root.key

    while left:
        min = left.key
        left = left.left

    return min


## Завдання 2
## Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві.
def sum(root: AVLNode):
    if not root:
        return None

    result = root.key

    if root.left:
        result += sum(root.left)

    if root.right:
        result += sum(root.right)

    return result

## Завдання 3
## Є декілька мережевих кабелів різної довжини,
## їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі, у порядку, який призведе до найменших витрат.
## Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
def cable_management(root):
    if not root:
        return 0, 0

    heapq.heapify(root)

    total_cost = 0
    connect_order = []

    while len(root) > 1:
        l = heapq.heappop(root)
        r = heapq.heappop(root)

        sum = l + r

        connect_order.append([l, r])

        total_cost += sum

        heapq.heappush(root, sum)

    return total_cost, connect_order


def main():
    root = None
    keys = [10, 20, 30, 25, 28, 27, -1]

    for key in keys:
        root: AVLNode = insert(root, key)

    print("min: ", min(root))
    print("sum: ", sum(root))

    nums = [1,2,3,4,5]
    print('cables: ', nums)

    res = cable_management(nums)
    print("cost: ", res[0])
    print("connect order: ", res[1])


if __name__ == "__main__":
    main()
