from collections import defaultdict
from typing import List, Dict


def count_chars(s: str) -> Dict[str, int]:
    count_dict = defaultdict(int)
    for char in s:
        count_dict[char] += 1
    return count_dict

def nested_list_to_dict(nums: List[List[int]]) -> Dict[int, List[int]]:
    my_dict = defaultdict(list)
    for num_list in nums:
        for i in range(1, len(num_list)):
            my_dict[num_list[0]].append(num_list[i])
    return my_dict

# do not modify below this line
print(count_chars("hello"))
print(count_chars("helloworld"))
print(count_chars("areallylongstringwhyareyoureadingthishahalol"))

print(nested_list_to_dict([[1, 2, 3], [4, 5, 6], [1, 4]]))
print(nested_list_to_dict([[1, 2, 3, 4], [4, 5, 6, 7], [1, 4, 5, 6]]))
print(nested_list_to_dict([[5, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8, 9]]))
print(nested_list_to_dict([[3, 2, 3, 4, 5], [4, 5, 6, 7, 8], [5, 6, 7, 8]]))
