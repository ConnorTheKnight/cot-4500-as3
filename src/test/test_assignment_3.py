#Test Input
def function(t, y):
    return t-(y*y)
a = 0
b = 2
N = 10
h = ((b-a)*(1.0))/N
w0 = 1
#Question 1
w = w0
index = 0
ti = a
while(index<N):
    ti = (a+(index*h))
    w = (w + (function(ti,w)*h))
    index+=1
print(str(w)+"\n")
#Question 2
w = w0
index = 0
ti = a
while(index<N):
    ti = a+(index*h)
    k1 = function(ti,w) * h
    k2 = function(ti+(h/2),w+(k1/2)) * h
    k3 = function(ti+(h/2),w+(k2/2)) * h
    k4 = function(ti+h,w+k3) * h
    w = w + ((k1+(2*k2)+(2*k3)+k4)/6)
    index+=1
print(str(w)+"\n")