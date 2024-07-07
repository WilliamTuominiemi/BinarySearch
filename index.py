numbers = [1,2,3,4,5,6,7,8,9,10]
prediction = numbers[int(len(numbers) / 2)]
value = 7

while prediction != value:
    print("\n\nSearching from numbers ", numbers)

    prediction = numbers[int(len(numbers) / 2)]
    print(prediction)
    if prediction > value:
        print("prediction is more than target, search start")
        numbers = numbers[:int(len(numbers) / 2)]
    elif prediction < value:
        print("prediction is less than target, search end")
        numbers = numbers[int(len(numbers) / 2):]
else:
    print("Found", prediction)