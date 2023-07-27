def a(roll_no, name): 
     # Adding values to list,tuple,set,dict 
     _list = [roll_no, name] 
     _tuple = (roll_no, name) 
     _set = {roll_no, name} 
     _dict = {'roll_no': roll_no, 'name': name} 
  
     # Printing  
     print("Initial data structures:") 
     print("List:", _list) 
     print("Tuple:", _tuple) 
     print("Set:", _set) 
     print("Dictionary:", _dict) 
  
     # Changing values during runtime 
     new_roll_no = input("Enter new roll number: ") 
     new_name = input("Enter new name: ") 
  
     _list[0] = new_roll_no 
     _list[1] = new_name 
  
     _tuple = (new_roll_no, new_name) 
  
     _set.remove(roll_no) 
     _set.add(new_roll_no) 
     _set.remove(name) 
     _set.add(new_name) 
  
     _dict['roll_no'] = new_roll_no 
     _dict['name'] = new_name 
  
     # Printing the updated data structures 
     print("Updated data structures:") 
     print("List:", _list) 
     print("Tuple:", _tuple) 
     print("Set:", _set) 
     print("Dictionary:", _dict) 
  
     # Deleting data structures 
     del _list 
     # print(_list) 
     del _tuple 
     # print(_tuple) 
     del _set 
     # print(_set) 
     del _dict 
     # print(_dict) 
  
  
  
a("123", "Aryan")