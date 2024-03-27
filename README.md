# Vector3
a library to work with 3d vectors. Including simple features like adding, multiplication or invert.

# Base
a vector3 is just a array of 3 numbers like:
a = [1, 2, 3]

# Modules
## vector_math
`unit(vector)`
**none distructive**
returns the unit-vector


`invert(vector)`
**none distructive**
retruns the inverted vector


`midVector3(vectorA, vectorB)`
returns the mid point between those vectors


`sumVector3(vectorA, vectorB)`
returns the sum of two vectors


`multiplyVector3(vector, multiplier)`
returns the vector multipied


`calcVector3(vectorA, vectorB)`
returns vectorB - vectorA


`addVector3(vectorA, vectorB)`
returns vectorA + vectorB


`dotProduct(vectorA, vectorB)`
returns dotproduct of the two vectors


`crossProduct(vectorA, vectorB)`
returns crossproduct


`point3plan(vectorA, vectorB, vectorC)`
creates and returns a plane3 obj from three points


## intersection

`vector_is_equal(vectorA, vectorB)`
compares vectors and returns (true or false)


`compare_dir_v(vectorA, vectorB)`
compares two vectors also if they are inverted


`intersection(lineA, lineB)`
if intersection point returns intersection point
if parallel/don't cross/are equal returns None

## Line

class *Line(supportVector, directionVector)*

`lenV`
returns length of a vector

`unitV`
returns the unit vector

`point(s)`
returns a point on the line from an s(int) values

`info()`
returns info about the line

`__str__`
returns a nice formate of the line

## ComplexLine

class *ComplexLine(vectorA, vectorB)*

Represents a complex line in 3D space defined by two vectors.

### Attributes

- `a`: The starting point of the line represented as a 3D vector.
- `b`: The ending point of the line represented as a 3D vector.
- `sV`: The support vector of the line.
- `dV`: The direction vector of the line.
- `lower_x_bound`: The lower bound of the line in the x-dimension.
- `higher_x_bound`: The higher bound of the line in the x-dimension.
- `lower_y_bound`: The lower bound of the line in the y-dimension.
- `higher_y_bound`: The higher bound of the line in the y-dimension.
- `lower_z_bound`: The lower bound of the line in the z-dimension.
- `higher_z_bound`: The higher bound of the line in the z-dimension.

### Methods

`__init__(v1, v2)`
Initializes the ComplexLine with two 3D vectors.

`calcVar(v1, v2)`
Calculates missing values such as bounds based on the given vectors.

`calcVfromX(x_value)`
Calculates a point on the line for a given x-coordinate.

`calcVfromY(y_value)`
Calculates a point on the line for a given y-coordinate.

`calcVfromZ(z_value)`
Calculates a point on the line for a given z-coordinate.

`lenV(v)`
Calculates the length of a 3D vector.

`unitV(v)`
Calculates the unit vector of a given vector.

`point(s)`
Calculates a point on the line given a scalar parameter.

`pointInsideLine(point)`
Checks if a given point is inside the bounds of the line.

`print()`
Prints the attributes of the ComplexLine object.

`info()`
Prints the type of the ComplexLine object and its support and direction vectors.

## plane3

Represents a 3D plane. Accepts one of three possible input formats and calculates the missing forms.

### Attributes

- `param`: parameter form of the plane
- `normal`: normal form of the plane
- `coord`: coordinate form

### Methods

`getParam()`
Gets the parameter form of the plane.

`getNormal()`
Gets the normal form of the plane.

`getCoord()`
Gets the coordinate form of the plane.

`getForms()`
Gets the missing forms.

`print()`
Prints the planes to visualize.

## plane3coord

Coordinate Representation of a plane 
x1 + x2 + x3 = n

### Attributes

- `x1`: (number) value one
- `x2`: (number) value two
- `x3`: (number) value three
- `n`: (number) n value

### Methods

`normalForm()`
returns the normal form of the plane

`paramForm()`
returns the parameter form of the plane 

`print()`
prints the plane specs 

## plane3normal

Normal Plane representation

### Attributes

- `nV`: (vector) normal vector
- `supportV`: (vector) support vector

### Methods

`paramForm()`
returns the parameter form of the plane 

`coordFord()`
returns the coordinate form of the plane

`print()`
prints the plane specs 

## plane3param

Plane representation with support and two clamping vectors

### Attributes

- `supportV`: (vector) support vector
- `clampingA`: (vector) clamping vector A
- `clampingB`: (vector) clamping vector B

### Methods

`point(r, s)`
retuns a point on the plane with the values r,s (number)

`normalVector()`
calculates the normal vector of the plane

`coordForm()`
returns the coordinate form of the plane

`normalForm()`
returns the normal form of the plane

`print()`
prints the plane specs 