from pprint import pprint

def hello():
    return 'Hello World!'

def puzzle(rows=5, columns=5):
    puzzle = [[0 for i in range(columns)] for j in range(rows)]
    return puzzle


if __name__ == '__main__':
    print(hello())
    pprint(puzzle(6,6))
    p = puzzle(2,2)
    p[0][0] = 1
    pprint(p)
