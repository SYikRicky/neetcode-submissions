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
            print(f"token: {token} store: {store}")
            if token not in opt:
                store.append(int(token))
            else:
                res = opt[token](store.pop(), store.pop())
                store.append(res)

        return store.pop()