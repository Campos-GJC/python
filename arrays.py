import array as arr

# Create a array in python
new_array = arr.array('i',[5,55,55,55,555555555,55]) # Array with elements
array_without = arr.array('i',) # Array without elements
"""
new_array - Name of array
(TypeCode, Elements)

TYPECODE	C TYPE	PYTHON TYPE	SIZE
'b'	signed char	int	1
'B'	unsigned char	int	1
'u'	wchar_t	Unicode character	2
'h'	signed short	int	2
'H'	unsigned short	int	2
'i'	signed int	int	2
'I'	unsigned int	int	2
'l'	signed long	int	4
'L'	unsigned long	int	4
'q'	signed long long	int	8
'Q'	unsigned long long	int	8
'f'	float	float	4
'd'	double	float	8
"""

# Getting the matrix size
print(f"Matrix size {len(new_array)}")

# Discorver if a value exist in array
try:
    new_array.index(51)
    print("Exist")
except:
    print("No exist, add please")
print(new_array)

# Add values in the array
new_array.append(5) # One value
new_array.extend([25,52,874,756455]) # A lot of values
new_array.insert(0,50) ## Add the int number "50" in position 0
print(new_array)
# Removing values in arrays
new_array.pop() # Delete the last value

values_delete = {25,52,874}

for value in values_delete:
    print(value)
    new_array.remove(value) # Removes the first occurrence of number

print(new_array)

