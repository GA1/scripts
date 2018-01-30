with open('chinese_characters.txt', 'r') as myfile:
  s = myfile.read().replace('\n', '')
  chars = set()		
  for i in range(len(s)):
    if s[i] > u'\u4e000' and s[i] < u'\u9fff':
      chars.add(s[i])
  chars = list(chars)
  chars.sort()
  print(chars)
  print('number of unique chinese characters is: ' + str(len(chars)))
