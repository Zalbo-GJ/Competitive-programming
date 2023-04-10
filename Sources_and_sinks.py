n = int(input())

matrix = []
for r in range(n):
    row = list(map(int,input().split()))

    matrix.append(row)

non_source = []
non_sink = []

for st in range(n):
    for dest in range(n):
        if matrix[st][dest] == 1:
            non_source.append(dest+1)
            non_sink.append(st+1)

source = []   
sink = []
for ind in range(1,n+1):
    if ind not in non_source:
        source.append(ind)
    if ind not in non_sink:
        sink.append(ind)

print(len(source), *source)
print(len(sink), *sink)
