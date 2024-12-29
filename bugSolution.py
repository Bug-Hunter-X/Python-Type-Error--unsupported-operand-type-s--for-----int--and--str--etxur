def function(a, b):
    try:
        return int(a) + int(b)
    except ValueError:
        return "Error: Cannot add non-numeric values."

result = function(10, "hello")
print(result)

result = function(10, 20)
print(result) 