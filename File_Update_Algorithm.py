# Update file through Python

# assign 'import file' to the name of the file
import_file = "allow_list.txt"

# create 'with' statement to open the file
with open(import_file, "r") as file:
  #use .read() to convert the file into a string 
  ip_addresses = file.read()
  
# convert the string into a list
ip_addresses = ip_addresses.split()

# build for loop
#if element is in 'remove_list', remove it
for element in remove_list:
  if element in ip_addresses:
    ip_addresses.remove(element)

#convert 'ip_addresses' back into a string
ip_addresses = "\n".join(ip_addresses)

#create 'with' statement to rewrite the original file
with open(import_file, "w") as file:
  file.write(ip_addresses)
