def makeFunction(input):
    def function(t, y):
        return eval(input)
    return function
#User input
functionIn = input()
f = makeFunction(functionIn)
RangeIn = input().split()
a = int(RangeIn[0])
b = int(RangeIn[1])
Iterations = input()
N = int(Iterations)
h = ((b-a)*(1.0))/N
InitialPoint = input()
w0 = int(InitialPoint)
#Question 1
w = w0
index = 0
ti = a
while(index<N):
    ti = (a+(index*h))
    w = (w + (f(ti,w)*h))
    index+=1
print(str(w)+"\n")
#Question 2
w = w0
index = 0
ti = a
while(index<N):
    ti = a+(index*h)
    k1 = f(ti,w) * h
    k2 = f(ti+(h/2),w+(k1/2)) * h
    k3 = f(ti+(h/2),w+(k2/2)) * h
    k4 = f(ti+h,w+k3) * h
    w = w + ((k1+(2*k2)+(2*k3)+k4)/6)
    index+=1
print(str(w)+"\n")