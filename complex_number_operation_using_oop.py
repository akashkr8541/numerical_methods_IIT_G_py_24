# Assignment 1  question 3
#  Develop a Class of complex number, having funtionality of adding, subtracting, multiplying
# two complex numbers and also to find the complex conjugate of a complex number. Show
# its capabilities using examples.
class ComplexNumber:    # defining class
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def add(self, other):
        real_result = self.real_part + other.real_part
        imag_result = self.imaginary_part + other.imaginary_part
        return ComplexNumber(real_result, imag_result)

    def subtract(self, other):
        real_result = self.real_part - other.real_part
        imag_result = self.imaginary_part - other.imaginary_part
        return ComplexNumber(real_result, imag_result)

    def multiply(self, other):
        real_result = (self.real_part * other.real_part) - (self.imaginary_part * other.imaginary_part)
        imag_result = (self.real_part * other.imaginary_part) + (self.imaginary_part * other.real_part)
        return ComplexNumber(real_result, imag_result)

    def conjugate(self):
        return ComplexNumber(self.real_part, -self.imaginary_part)

    def display(self):
        print(f"{self.real_part} + {self.imaginary_part}j")


# Example usage
z1 = ComplexNumber(3, 2)
z2 = ComplexNumber(1, -1)  # here 1 is real part and -1 is imaginary part

# Perform operations
z_sum = z1.add(z2)
z_diff = z1.subtract(z2)
z_product = z1.multiply(z2)
z_conjugate = z1.conjugate()

# Displaying  results
print("z1 =", end=" ")  # end for printing real and imaginary part in same line
z1.display()

print("z2 =", end=" ")
z2.display()

print("z1 + z2 =", end=" ")
z_sum.display()

print("z1 - z2 =", end=" ")
z_diff.display()

print("z1 * z2 =", end=" ")
z_product.display()

print("Conjugate of z1 =", end=" ")
z_conjugate.display()
