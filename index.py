numbers = [1,2,3,4,5,6,7,8,9,10]
value = 7

left = 0
right = len(numbers) - 1

while left <= right:
    middle = (left + right) // 2
    prediction = numbers[middle]
    
    print(f"\n\nSearching in range {numbers[left:right+1]}")
    print(f"Prediction: {prediction}")
    
    if prediction == value:
        print(f"Found {prediction} at index {middle}")
        break
    elif prediction > value:
        print("Prediction is more than target, searching left half")
        right = middle - 1
    else:
        print("Prediction is less than target, searching right half")
        left = middle + 1
else:
    print("Value not found in the list")