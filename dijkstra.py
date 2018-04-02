distance = list()
found = list()
weight = list()
altline = list()

INT_MAX = 2147483647
T = 1
F = 0
INF = 1000

file = open("path.txt", "r")

for i in range(8):
    if i == 0:
        MAX_VERTICES = int(file.readline())
    else:
        line = str(file.readline())
        line = line.strip('\n')
        line = line.split(', ')
        for num in line:
            if num != 'INF':
                num = int(num)
            else:
                num = INF
            altline.append(num)
        weight.append(altline)
        altline = []

print(weight)
file.close()

def choose(distance, n, found):
    minimum = INT_MAX
    minpos = -1
    for i in range(n):
        if(distance[i]<minimum and (found[i] == False)) :
            minimum = distance[i]
            minpos = i
    return minpos

def shortest_path(start, n):
    for i in range(n):
        distance.append(weight[start][i])
        found.append(F)
    found[start] = T
    distance[start] = 0
    for i in range(n-2):
        u = choose(distance, n, found)
        found[u] = T
        for w in range(n):
            if(found[w] == False):
                if(distance[u]+weight[u][w]<distance[w]):
                    distance[w] = distance[u] + weight[u][w]

shortest_path(0, MAX_VERTICES)
