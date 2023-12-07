from typing import List

def number_is_accepted(num: int, final_value: int = 1, power: int = 2) -> bool:
    '''
    Check if number complies with the rules
    '''
    history = set()
    while num != final_value:
        if num in history: return False
        history.add(num)
        num = sum([int(digit) ** power for digit in str(num)])
    else:
        return True

def get_numbers(limit: int = 10) -> List[int]:
    '''
    Get list of the first x numbers that comply with the rules
    '''
    numbers = []
    candidate = 1

    while len(numbers) < limit:
        if number_is_accepted(candidate):
            numbers.append(candidate)
        candidate += 1

    return numbers

if __name__ == '__main__':
    result = get_numbers(10)
    print(f'Result: {result}')