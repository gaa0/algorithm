def LongestWord(sen):

  # code goes here
  max_len = 0
  max_word = ''
  tmp_word = ''
  for s in sen:
    if 48 <= ord(s) <= 57 or 65 <= ord(s) <= 90 or 97 <= ord(s) <= 122:
      tmp_word += s
      if len(tmp_word) > max_len:
        max_len = len(tmp_word)
        max_word = tmp_word
    elif s == ' ':
      tmp_word = ''

  return max_word

# keep this function call here 
print(LongestWord(input()))