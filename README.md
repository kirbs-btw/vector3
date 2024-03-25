# Vector3
a library to work with 3d vectors. Including simple features like adding, multiplication or invert.

# Base
a vector3 is just a array of 3 numbers like:
a = [1, 2, 3]

# Modules
## vector_math
*unit(vector)*  
**none distructive**
returns the unit-vector


*invert(vector)*
**none distructive**
retruns the inverted vector


*midVector3(vectorA, vectorB)*
returns the mid point between those vectors


*sumVector3(vectorA, vectorB)*
returns the sum of two vectors


*multiplyVector3(vector, multiplier)*
returns the vector multipied


*calcVector3(vectorA, vectorB)*
returns vectorB - vectorA


*addVector3(vectorA, vectorB)*
returns vectorA + vectorB


*dotProduct(vectorA, vectorB)*
returns dotproduct of the two vectors


*crossProduct(vectorA, vectorB)*
returns crossproduct


*point3plan(vectorA, vectorB, vectorC)*
creates and returns a plane3 obj from three points


## intersection

*vector_is_equal(vectorA, vectorB)*
compares vectors and returns (true or false)


*compare_dir_v(vectorA, vectorB)*
compares two vectors also if they are inverted


*intersection(lineA, lineB)*
if intersection point returns intersection point
if parallel/don't cross/are equal returns None