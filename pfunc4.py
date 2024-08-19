# 1
def max_num(a,b,c):
    return max([a,b,c])

# 2
def mult_list(num):
    if len(num) == 0:
        return 0
    prod = num[0]
    if len(num) > 1:
        for i in num[1:]:
            prod = prod * i
    return prod

# 3
def rev_string(string):
    return string[::-1]

# 4
def num_within(x,a,b):
    return x in range(a,b+1)
    
# 5
triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev)+1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1
    for row in triangle:
      print(row)

print(max_num(10,5,8))
print(mult_list([1,2,3]))
print(rev_string("potato"))
print(num_within(1,5,7))
pascal(10)