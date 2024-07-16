# Print 2s table taking user input
# int is important to convert the input from string to integer
# as in python {input} consider the input as string

n = int(input("Enter the number up to which you want to print the 2s table"))
[print(f"2 * {i} = {2 * i}")
for i in range(1, n + 1)]
