n = int(input("n = "))

print(f"Enter {n} array elements:")
arr = [int(input()) for _ in range(n)]

print("Original array:", arr)

positive_elements = [x for x in arr if x > 0]

if positive_elements:
    max_positive = max(positive_elements)
    print("Maximum positive element:", max_positive)
else:
    print("No positive elements in the array.")

