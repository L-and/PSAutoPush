arr = list()
for _ in range(3):
    arr.append(input())

for index, value in enumerate(arr):
    if arr[index].isdigit():
        result_i = int(arr[index]) + 3-index

if result_i % 3==0 and result_i % 5==0:
    print("FizzBuzz")
elif result_i % 3==0 and result_i % 5!=0:
    print("Fizz")
elif result_i % 3!=0 and result_i % 5==0:
    print("Buzz")
else:
    print(result_i)