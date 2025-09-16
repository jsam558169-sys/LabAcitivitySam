# method

def hanoi(arr):
    n = len(arr)
    iteration = 1
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            print(f"Items compared: [{arr[j]}, {arr[j + 1]}]", end=" ")
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                print(f"➔ swapped {arr}")
            else:
                print("➔ not swapped")
        if swapped:
            print(f"Iteration #{iteration} {arr}")
            iteration += 1
    print(f"Output values = {arr}")


input_values = list(
    map(int, input("Enter values separated by space: ").split()))
hanoi(input_values)
