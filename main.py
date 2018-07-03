#Andres Suarez
#Math 4330 Final Project

def IsNumber(vector):
  '''
  This function makes sure the values of a given vector are numbers. It checks each value, if they are not an int, float, or complex number it returns False. However, if those conditions are met it returns True.
  '''
  # This variable will keep track of the validity of our input.
  inputStatus = True
  # This for loop will check each element of the vector to see if it's a number.
  for i in range(len(vector)):
    if ((type(vector[i]) != int) and (type(vector[i]) != float) and (type(vector[i]) != complex)):
      inputStatus = False
    else:
      return inputStatus

def twoNorm(vector):
  '''
  twoNorm takes a vector as it's argument. It then computes the sum of  the squares of each element of the vector. It then returns the square root of this sum.
  '''
  # If the input is valid the function continues to compute the 2-norm
  if IsNumber(vector) == True:
    result = 0
    # This for loop will compute the sum of the squares of the elements of the vector.
    for i in range(len(vector)):
      result = result + (vector[i]**2)
    result = result**(1/2)
    return result
  else:
    return "invalid input"

def Normalize(vector):
  '''
  This function takes a vector as its argument. First it sets a temporary vector as the result of the 2 norm of our argument. Then it divides our argument by its 2 Norm. The result is stored in the initially empty result array.
  '''
  # If the input is valid the function continues to compute the Normalization of the vector
  if IsNumber(vector) == True:
    temp = twoNorm(vector)
    item = 0
    result = []
    #This for loop will compute a the division between the input and the its 2Norm then append it to result
    for i in range(len(vector)):
      item = (vector[i]) / temp
      result.append(item)
    return result
  else:
    return "invalid input"


def dot(vector1, vector2):
  '''
  This function takes 2 vectors of the same length and computes the dot product. First we check to see if the vectors are compatible. Then, a solution integer is initialized which will store our answer. The zip function is used to merge the 2 vectors of the same length into pairs. This way we match each element of the same index position to calculate the product and then add up the sum of the products. The final result is stored in the integer solution.
  '''
  # If the input is valid the function it will continue
  if IsNumber(vector1) == True and IsNumber(vector2):
    #if the length of the vectors are the same it will compute the dot product of the two
    if len(vector1) == len(vector2):
      result = 0
      #This for loop multiplies each of the elements of the vectors and stores it in result
      for i in range(len(vector1)):
        result += vector1[i] * vector2[i]
      return result
    else:
      return "invalid input"
  else:
    return "invalid input"


def scalarVecMulti(scalar, vector):
  '''
  This function takes a scalar and a vector as it's arguments. An temporary integer "item" is created to store the product of the scalar with each element in the vector. Each result for "item" is stored in the empty "solution" list. Solution is returned which contains the product of the scalar and vector.
  '''
  # If the input is valid the function it will continue
  if IsNumber(vector) == True:
    item = 0
    result = []
    #This for loop multiplies the scalar by each element in the vector and stores it in result
    for i in range(len(vector)):
        item = scalar * vector[i]
        result.append(item)
    return result
  else:
    return "invalid input"

def vecSubtract(vector1, vector2):
  '''
  This function takes 2 vectors of the same length and computes the difference. A solution vector is initialized to return our final answer. Then a temporary result vector is initialized along with a temporary integer "item". The item integer computes the difference between the elements of the 2 vectors and stores it in our temporary result vector. The result vector now contains 3 lists inside of it with the difference between each element in vector1 with all elements of vector2. Since we are looking for the difference between the elements in matching index positions, we take out the correct difference from each list in our result vector and append it to our solution vector. The final result is solution = (vector1 - vector2)
  '''
  #Check if input is valid
  if len(vector1) == len(vector2):
    solution = []
    for i in range(len(vector1)):
      #temporary vector and integer
      result = []
      item = 0
      for j in range(len(vector2)):
        #takes difference between 1 element in vector1 and all elements in vector2
        item = vector1[j] - vector2[i]
        #appends all 3 lists into our temporary vector
        result.append(item)
      #appends only the correct difference into the solution
      solution.append(result[i])
    return solution
  else:
    return "The input is invalid"


def Gram_Schmidt(A):
  '''
  This function takes all functions listed above and combines them in order to form our Q and R matricies.
  '''
  #rows of matrix A
  m = len(A[0])
  #columns of matrix A
  n = len(A)
  #v are the vectors of A
  v = A
  #creates empty matricies Q and R based on the number of columns in A
  R = [[0]*n for i in range(n)]
  Q = [[0]*m for i in range(n)]
  #this for loop computes r11 and q1
  for i in range(n):
    R[i][i] = twoNorm(v[i])
    Q[i] = Normalize(v[i])
    #this for loop computes r12, r22, and q2
    for j in range(i+1,n):
      R[j][i] = dot(Q[i],v[j])
      temp = scalarVecMulti(R[i][j],Q[i])
      v[i] = vecSubtract(v[j],temp)
  return [Q,R]

def matrixTranspose(Q):
  '''
  This function computes the transpose of matrix Q by converting the columns to rows and rows to columns.
  '''
  #rows of Q
  m = len(Q[0])
  #columns of Q
  n = len(Q)
  #creates empty matrix which will contain our result
  transposedQ = [[0]*n for i in range(m)]
  #this forloop flips the columns to rows and vice-versa
  for i in range(len(Q)):
    for j in range(len(transposedQ)):
      transposedQ[j][i] = Q[i][j]
  return transposedQ


def matVec(matrix, vector):
  '''
  This function calculates a matrix-vector multiplication. First we check to see if the matrix is compatible. For example if the vector has 3 elements (or rows), the matrix must have 3 lists inside of it (or 3 columns).
  We compare the length of the matrix with the length of the vector to determine this part.
  Once we determine that the matrix is compatible, we initialize an empty list that will store our "solution".
  The product is calculated using item += matrix[j][i] + vector[j] and is temporarily stored in the "result" list where the sum of each product is the 3rd element in "result".
  The sum is then appended into our solution list which gives us a vector (3x1) equivalent to matrix*vector
  '''
  #matrix compatibility check
  if IsNumber(vector) == True:
    #vector compatibility check
    if len(matrix) == len(vector):
      #solution stores our final answer
      solution = []
      for i in range(len(matrix[0])):
        #creating temporary list to product calculations
        result = []
        item = 0
        for j in range(len(vector)):
          #adding the product result of the matrix vector multiplication
          item += matrix[j][i] * vector[j]
          result.append(item)
        solution.append(result[2])
      return solution
    else:
      return "invalid input"
  else:
    return "invalid input"

def BackSub(matrix, vector):
  '''
  This function takes a matrix and a vector as its arguments and computes the backsubstitution to compute the c vector.
  '''
  #we set this variable to identify where we are inside our c vector. Since the length is 4 it only goes up to c[3]
  a = len(vector) - 1
  #creates empty vector with 0's
  c = [0]*len(vector)
  #divides the values of the vector by the values of the matrix
  c[a] = vector[a] / matrix[a][a]

  #the for loop fills out the values of c
  for i in reversed(range(a)):
    c[i] = vector[i]
    for j in range(i+1, a):
      c[i] = c[i] - (c[j]*matrix[j][i])
      c[i] = c[i] / matrix[i][i]
  return c



A = [[1,1,1,1,1,1,1,1,1,1],[0.55,0.60,0.65,0.70,0.75,0.80,0.85,0.90,0.95,1],[0.3025,0.36,0.4225,0.49,0.5625,0.64,0.7225,0.81,0.9025,1],[0.09150625,0.1296,0.17850625,0.2401,0.31640625,0.4096,0.52200625,0.6561,0.81450625,1]]

y = [1.102,1.099,1.017,1.111,1.117,1.152,1.265,1.380,1.575,1.857]

GS_Solution = Gram_Schmidt(A)
Q = GS_Solution[0]
R = GS_Solution[1]
b = matVec(matrixTranspose(Q), y)
c = BackSub(R, b)


print("The matrix A is", A)
print("\n")
print("The matrix Q is" ,Q)
print("\n")
print("The matrix R is" ,R)
print("\n")
print("The c vector is: " ,c)