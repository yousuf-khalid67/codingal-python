tuple1=(1, 5, 68, 65, 111, 160)
print(f"length of the tuple1: {len(tuple1)}")
print(tuple1[1:5])

tuple2=("hi", "hello", 0.1, 0.7, "wait")
print(f"length of tuple2: {len(tuple2)}")
print(tuple2[1:4])

tuple3=tuple1[1:5]+tuple2[1:4]
print(tuple3)

list1=[]
for i in tuple3: 
    if isinstance(i, str):
        list1.append(i)
print(f"string found: {list1}")
