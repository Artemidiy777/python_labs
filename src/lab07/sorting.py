"""три сортировки"""


def bubble_sort(nums: list[int]) -> list[int]:
    """Новый список по возрастанию, меняя местами соседние пары

    Флаг change даёт ранний выход на отсортированных данных

    bubble_sort([3, 1, 2]) -> [1, 2, 3]
    bubble_sort([]) -> []
    """
    nums = nums.copy()
    for i in range(len(nums)):
        change = False
        for j in range(len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                change = True
        if not change: 
            break
    return nums


def selection_sort(nums: list[int]) -> list[int]:
    """Новый список по возрастанию, выбирая минимум оставшейся части

    Делает не больше n обменов

    selection_sort([3, 1, 2]) -> [1, 2, 3]
    """
    nums = nums.copy()
    for i in range(len(nums)):
        min_i = i
        # минимум ищем вручную: min() в этой лабе запрещён
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_i]:
                min_i = j
        nums[i], nums[min_i] = nums[min_i], nums[i]
    return nums


def insertion_sort(nums: list[int]) -> list[int]:
    """Новый список по возрастанию, вставляя элемент в готовую левую часть

    insertion_sort([3, 1, 2]) -> [1, 2, 3]
    """
    nums = nums.copy()
    for i in range(1, len(nums)): 
        elem = nums[i]    
        j = i - 1
        # при j = -1 второе не вычисляется
        while j >= 0 and nums[j] > elem:
            nums[j + 1] = nums[j]       # двигаем большее вправо
            j -= 1
        nums[j + 1] = elem              # цикл ушёл левее необходим места
    return nums
