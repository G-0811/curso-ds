#tabuada de 1 a 10
for num in range(1, 11):
    print(f"TABUADA DO {num}\n")
    for n in range(1, 11):
        res = num * n
        print(f"{num} * {n} = {res}")