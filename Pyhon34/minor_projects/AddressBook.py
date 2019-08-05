import pickle

class AddressBook():

  def __init__(self):
    self.data = {}
    with open('Contacts.pkl', 'rb') as f:
      self.data = pickle.load(f)

  def print(self):
    print()
    for key, value in self.data.items():
      print(key + ' : ' + value)
    print()

  def rem(self, key_to_remove):
    try:
      self.data.pop(key_to_remove)
    except:
      print("Such contact doesn't exist....!")

  def get(self, key_to_find):
    print(self.data.get(key_to_find, "Such contact doesn't exist....!"))

  def set(self, key_to_set, value):
      self.data[key_to_set] = value

  def replace(self, key_to_replace, value):
    for key in self.data.keys():
      if key == key_to_replace:
        self.data[key_to_replace] = value

  def save(self):
    with open('Contacts.pkl', 'wb') as f:
        pickle.dump(self.data, f, pickle.HIGHEST_PROTOCOL)

contact = AddressBook()
print('Example: add, remove, change, show, find, exit')
while(True):
  user = input('What would you like to do > ').lower()
  if user == 'add':
    name = input('Enter the name of contact> ')
    number = input('Enter the number of contact> ')
    contact.set(name, number)
  elif user == 'remove':
    name = input('Enter the name of contact> ')
    contact.rem(name)
  elif user == 'show':
    contact.print()
  elif user == 'change':
    name = input('Enter the name of contact> ')
    if name in contact.data.keys():
      number = input('Enter the new number of contact> ')
      contact.replace(name, number)
    else:
      print("Such contact doesn't exist....!")
  elif user == 'find':
    name = input('Enter the name of contact> ')
    contact.get(name)
  elif user == 'exit':
    ask = input('Do you want save?(Y | n): ').lower()
    if ask == 'y':
      contact.save()
      break
    else: 
      break
  else:
    print('No such command, please try again!')