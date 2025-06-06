def display(q):
    if len(q)==0:
        print("empty")
    else:
        print(q)
q=[]
q.append(10)
display(q)
q.append(20)
display(q)
q.append(30)
display(q)
print("removing elements")
q.pop(0)
display(q)
q.pop(0)
display(q)
q.pop(0)
display(q)

