# Define the filename
filename = 'output.txt'

# Open the file in write mode
with open(filename, 'w') as file:
    # Write the number 321 to the file
    file.write('321')

print(f'{filename} has been created with the number 321 inside.')