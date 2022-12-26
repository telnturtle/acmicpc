def f(stairs):
    N = len(stairs)
    table = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for i in range(len(table[0])):
        table[0][i] = 0
    for row in table:
        row[0] = 0
    
