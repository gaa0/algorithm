def FirstReverse(strParam):

  # code goes here
  answer = ''.join([s for s in strParam][::-1])

  return answer

# keep this function call here 
print(FirstReverse(input()))