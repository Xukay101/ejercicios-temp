from time import time
from typing import List

def number_is_happy(num: int) -> bool:
    '''
    Check if number is happy
    '''
    history = set()
    while num != 1:
        if num in history: return False
        history.add(num)
        num = sum([int(digit) ** 2 for digit in str(num)])
    else:
        return True

def get_happy_numbers(limit: int = 10) -> List[int]:
    '''
    Get list of the first x happy numbers
    '''
    numbers = []
    candidate = 1

    while len(numbers) < limit:
        if number_is_happy(candidate):
            numbers.append(candidate)
        candidate += 1

    return numbers

if __name__ == '__main__':
    start_time = time()

    result = get_happy_numbers(100)

    end_time = time()
    elapsed_time = end_time - start_time

    print(f'Result: {result}')
    print(f'Time elapsed: {elapsed_time} seconds')