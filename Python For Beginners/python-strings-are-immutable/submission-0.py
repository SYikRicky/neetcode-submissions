def remove_fourth_character(word: str) -> str:
    one = word[:3]
    two = word[4:]
    return one + two


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
