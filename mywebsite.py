maximumNumber=[25,70,85,25]
girls=["Joy","liz","Anita"]
maximum=0
for num in maximumNumber:
    if(maximum<num):
        maximum=num
print(maximum)

prev2=0
prev1=1
print(prev2,prev1)
for fibo in range(20):
    newFibo=prev2+prev1
    print(newFibo)
    prev2=prev1
    prev1=newFibo

def fibonacci(prev1,prev2):
    global count
    if count<=20:
        newFibo=prev1+prev2
        print(newFibo)
        prev2=prev1
        prev1=newFibo
        count+=1
        fibonacci(prev1,prev2)
    else:
        return
fibonacci(1,0)

print("HELLO AGAIN WORLD")
