import sys

if len(sys.argv) != 2:
    print("Usage: python table.py <number>")
    sys.exit(1)

num = int(sys.argv[1])

print(f"Multiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
