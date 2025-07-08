nums = [1,2,3]
results = [[f(x) for f in [lambda x : x+1, lambda x: x*2]] for x in nums]
print(results)