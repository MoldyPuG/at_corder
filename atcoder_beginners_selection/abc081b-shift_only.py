N = int(input())

while True:
    inputs = list(map(int, input().split()))
    if len(inputs) == N:
        A = [int(x) for x in inputs]
        break
    else:
        print(f"Please enter exactly {N} integers.")

operation_count = 0

while True:
    if all(x % 2 == 0 for x in A) is True:
        A = list(map(lambda x: int(x/2), A))
        operation_count += 1
    else:
        break

print(operation_count)