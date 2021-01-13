#Approach:
####To overload +, –, * operators, we will create a class named matrix and then make a public function to overload the operators.

To overload operator ‘+’ use prototype:
Return_Type classname :: operator +(Argument list)
{
    // Function Body
}
####For Example:

Let there are two matrix M1[][] and M2[][] of same dimensions. Using Operator Overloading M1[][] and M2[][] can be added as M1 + M2.

In the above statement M1 is treated hai global and M2[][] is passed as an argument to the function “void Matrix::operator+(Matrix x)“.

In the above overloaded function, the appproach for addition of two matrix is implemented by treating M1[][] as first and M2[][] as second Matrix i.e., Matrix x(as the arguments).

To overload operator ‘-‘ use prototype:
Return_Type classname :: operator -(Argument list)
{
    // Function Body
}
####For Example:

Let there are two matrix M1[][] and M2[][] of same dimensions. Using Operator Overloading M1[][] and M2[][] can be added as M1 – M2.

In the above statement M1 is treated hai global and M2[][] is passed as an argument to the function “void Matrix::operator-(Matrix x)“.



In the above overloaded function, the appproach for substraction of two matrix is implemented by treating M1[][] as first and M2[][] as second Matrix i.e., Matrix x(as the arguments).

To overload operator ‘*’ use prototype:
Return_Type classname :: operator *(Argument list)
{
    // Function Body
}
Let there are two matrix M1[][] and M2[][] of same dimensions. Using Operator Overloading M1[][] and M2[][] can be added as M1 * M2.

In the above statement M1 is treated hai global and M2[][] is passed as an argument to the function “void Matrix::operator*(Matrix x)“.

In the above overloaded function, the appproach for multiplication of two matrix is implemented by treating M1[][] as first and M2[][] as second Matrix i.e., Matrix x(as the arguments).

#Program OUTPUT: 

![image](https://user-images.githubusercontent.com/72355871/104428845-f3eb0880-55aa-11eb-9d4d-7bf9b662c3cb.png)
