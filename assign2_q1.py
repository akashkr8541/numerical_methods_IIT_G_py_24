# Write a code to evaluate sine(x) using Taylor’s series. Consider different number of
# terms at a time and find out the relative error. You can plot the variation in relative error
# with number of terms used (at least 6 terms).
import numpy
import matplotlib.pyplot as plt


def factorial(n):
    if n == 0:
        result = 1
    else:
        i=1
        result = 1
        for i in range(n):
            result = result*(i+1)
            i = i+1
    return result


def sine_taylor(t, x):
    j = 0
    value = 0
    for j in range(t):
        value = value + ((-1)**j) * (x**(2*j+1))/factorial(2*j+1)
        j = j+1
    return value


def relative_error(Approximate_value, True_value):
    Relative_error = abs(Approximate_value - True_value)/True_value
    return Relative_error


k = int(input('enter number of terms of taylor series : '))
y = float(input('enter the value at which error to be found out : '))
Approximate_value = sine_taylor(k,y)
True_value = numpy.sin(y)
print('relative error at ' + str(y) + ' is ', relative_error(Approximate_value,True_value))


# plotting using matplot
data_list = list(range(1,11))
relative_error_list = []
for l in range(1, 11):
    k = l
    Approximate_value = sine_taylor(k, y)
    True_value = numpy.sin(y)
    relative_error_list.append(relative_error(Approximate_value,True_value))
    l = l+1

plt.plot(data_list,relative_error_list, marker='*')
plt.xlabel('number of terms taken in taylor series expansion of sin(x) -->')
plt.ylabel('relative error -->')
plt.title('Number of terms  vs  Relative error ')
plt.grid(True)
plt.show()

print('plot data are: ', data_list)
print(relative_error_list)
