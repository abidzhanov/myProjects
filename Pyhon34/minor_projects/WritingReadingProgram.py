#asks action that must be done over
ask = input('You want read, write or add file?(r, w, a): ')
# asks the user to give name of file
filename = input('Name of file: ')
#Opens file to write
file = open(filename, ask)

# asks user write the content of file
if ask == 'w':
  content = input('> ')
  #prints content of text.txt
  print('\n')
  print(file.write(content))
elif ask == 'a':
  content = input('> ')
  #prints content of text.txt
  print('\n')
  print(file.write(content))
else:
  print('\n')
  print(file.read())

#closes file in order to releive the memory
file.close()
