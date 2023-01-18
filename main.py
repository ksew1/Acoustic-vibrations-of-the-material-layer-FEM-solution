from problem import Problem

n = int(input("Type number of elements"))
while n < 1:
    print("Number of elements must be greater than 1")
    n = int(input("Type number of elements"))

problem = Problem(n)
problem.solve()
