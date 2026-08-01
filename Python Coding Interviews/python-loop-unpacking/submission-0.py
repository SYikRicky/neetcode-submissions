from typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:
    best_student = (str, 0)
    for name, score in scores:
        if score > best_student[1]:
            best_student = (name, score)
    return best_student[0]

    

# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
