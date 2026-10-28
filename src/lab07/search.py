"""задание A: линейный и бинарный поиск, две версии Two Sum"""


def linear_search(nums: list[int], x: int) -> int:
    """Индекс первого вхождения x или -1

    linear_search([4, 2, 7, 2], 2) -> 1
    linear_search([4, 2, 7, 2], 9) -> -1
    """
    for i in range(len(nums)):
        if nums[i] == x:
            return i
    return -1


def binary_search(sorted_nums: list[int], x: int) -> int:
    """Индекс x в отсортированном по возрастанию списке или -1

    На неотсортированном списке результат не определён

    binary_search([1, 3, 5, 7], 5) -> 2
    binary_search([1, 3, 5, 7], 4) -> -1
    """
    low = 0
    high = len(sorted_nums) - 1 #-1 тк это индекс ласт элем
    while low <= high:
        mid = (low + high) // 2
        if sorted_nums[mid] == x:
            return mid
        if sorted_nums[mid] < x:
            low = mid + 1      # искомо правее середины
        else:
            high = mid - 1      # искомое левее середины
    return -1


def two_sum_brute(nums: list[int], target: int) -> tuple[int, int] | None:
    """Пара индексов (i, j), где i<j, с суммой target или None

    Перебирает все пары

    two_sum_brute([2, 7, 11, 15], 9) -> (0, 1)
    two_sum_brute([1, 2], 10) -> None
    """
    for i in range(len(nums)):
        # j начинается после i: число не складываем само с собой
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


def two_sum_fast(nums: list[int], target: int) -> tuple[int, int] | None:
    """То же, что two_sum_brute, но за один проход со словарём 0(n)

    При нескольких подходящих парах может вернуть другую, чем перебор

    two_sum_fast([2, 7, 11, 15], 9) -> (0, 1)
    """
    seen = {}       # значение -> его индекс
    for i, x in enumerate(nums):
        need = target - x 
        if need in seen:
            return (seen[need], i)
        seen[x] = i
    return None
