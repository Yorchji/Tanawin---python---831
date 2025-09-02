even_numbers =[]
for i in range (2,21,2):
    even_numbers.append(i)
    total=0
    index=0
    while index < len(even_nubers):
        total += even_numbers[index]
        index += 1 
        print("Even numbers:",even_numbers)
        print("Sum:",total)