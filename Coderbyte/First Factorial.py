def FirstFactorial(num):

  # code goes here
  ans = 1
  for i in range(num):
    ans *= (i + 1)
  return ans

# keep this function call here 
print(FirstFactorial(input()))