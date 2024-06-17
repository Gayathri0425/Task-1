#creating a tuple
original_tuple=(1,2,4)
#adding a new element to the tuple
new_element=8
Updated_tuple=original_tuple +(new_element,)
#removing an element in the tuple
Updated_tuple=original_tuple[:1]+original_tuple[3:]
#modifing an element in the tuple
modifying_element=5
updated_tuple=original_tuple[:1]+(modifying_element,)+original_tuple[3:]
print(updated_tuple)
