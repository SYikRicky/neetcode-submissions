import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opt = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv
        }
        store = []
        for token in tokens:
            if token not in opt:
                store.append(int(token))
            else:
                second = store.pop()
                first = store.pop()
                res = opt[token](first, second)
                store.append(res)

        return store.pop()