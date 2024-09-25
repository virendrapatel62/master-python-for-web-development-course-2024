from typing import List, Dict, Tuple, Union, Optional


def number_or_name(a) -> Union[int, str]:
    if a < 10:
        return 10
    return "Number is greater then 10"


def number_or_name2(a) -> Optional[str]:
    if a < 10:
        return None
    return "Number is greater then 10"


number_or_name2(90)


def abc(numbers: List[int], phone_numbers: Dict[str, int]) -> Tuple[int, str, float]:
    pass


result = abc([1, 2, 43], {"a": 43545})

i = result[2]
