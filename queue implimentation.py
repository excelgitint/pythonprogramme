Q=[]
def enq(Q,ele):
    Q.append(ele)
def isempty(Q):
    return len(Q)==0
def deq(Q):
    if isempty(Q):
        print("QUEUE IS EMPTY!!!!!!!!!!!!!!")
    else:
        return Q.pop(0)
def size(Q):
    return len(Q)
def display(Q):
    print(Q)
print("adding the elements to q")
enq(Q,10)
display(Q)
enq(Q,20)
display(Q)
enq(Q,30)
display(Q)
print("removing the elements")
deq(Q)
display(Q)
deq(Q)
display
deq(Q)
display(Q)
display(Q)
