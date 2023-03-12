"""
Pyhon Loops
Python has tow primitive loops and these are:
a. 'for' loop
b. 'while' loop

(i) With the while loop we can execute a set of statements as long as a condition is true.
(ii) With the break statement we can stop the loop even if the while condition is true.
(iii) With the continue statement we can stop the current iteration, and continue with the next.
(iv) With the else statement we can run a block of code once when the condition no longer is true.
"""

#while loop
i = 1
while i < 6:
  print(i)
  i += 1
#break statement within a while loop
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#continue statement within the loop
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#continue statement within the loop
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#else statement within the loop
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")