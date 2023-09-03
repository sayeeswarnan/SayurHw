#5.Answer
print("My Tables")

for outer in range(1, 4):
    print(f"Table  {outer}")
    
    print("Easy numbers")
    for inner in range(1, 11):
        result = outer * inner
        print(f"{outer} * {inner} = {result}")

    print("Advanced numbers")
    for inner in range(11, 21):
        result = outer * inner
        print(f"{outer} * {inner} = {result}")

    print("**********")

print("End of tables")