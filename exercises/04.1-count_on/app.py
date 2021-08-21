hello = []
my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]


for item in my_list:
        t=type(item)
        hello.append(t)
        
print(hello)
