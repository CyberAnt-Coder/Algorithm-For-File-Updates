# Algorithm-For-File-Updates

## Description
For this project, we were required to update a file that identifies which employees can access restricted content based on their IP addresses. There is also a remove list which includes IP addresses of employees that must be removed from the first file. To make this easier, I was tasked with creating an algorithm that automates removing the unwanted IP addresses from the allow list. 
<br />

# Walkthrough:<br>

## Open the file that contains the allow list
To open the file that contains the allow list, we must first import the file and assign it to a variable. For my variable I chose the name `import_file`. <br><br>
<br>`import_file = “allow_list.txt”`<br><br>
Next I used a `with` statement to open the file.<br>
<br>`with open(import_file, “r”)as file:`<br><br>
Using the `with` statement and `.open()` command opens the `“allow_list.txt”` file and lets us read the contents inside. The `with` statement lets the computer know to close the file after to save resources. The open command has 2 arguments. The first argument is the file to be opened, and the second argument indicates what to do with the file. In this case, the file we are opening is in the variable `“import_file”` and as of right now we only intend to read it so we just pass through `“r”`. We also use the keyword `“as”` to assign the file to a variable called `“file”`. This stores the output of open and allows us to use it in the code within the with statement .

## Read the file contents
Next, we use the `.read()` function to convert the contents of `“allow_list.txt”` into a string so that we can read them. <br>
<br>`ip_addresses = file.read()`<br><br>
While within the with statement, we use the `file.read()` to assign the `“allow_list.txt”` string into a variable known as `“ip_addresses”`. This will allow us to organize and remove the unwanted IP addresses at a later time.<br>

## Convert the string into a list
Here we use the `split()` function to convert the string into a list. <br>
<br>`ip_addresses = ip_addresses.split()`<br><br>
Since we pass no argument through the `.split()` function, it will split the string at each white space into a separate element in the list. Converting it into a list will make it easier for us to loop through the IP addresses and remove the unwanted ones. <br>

## Iterate through the remove lsit
Now it is time to iterate through the list. I do this using a `for` loop.<br>
<br>`For element in ip_addresses:`<br><br>
This for loop will iterate through the remove list and allow me to access each element by using the loop variable `“element”`. The keyword in shows us to iterate through the list and assign each value to the loop variable `“element”`. <br>

## Remove IP addresses that are on the remove list
Here the algorithm will remove any IP addresses on the allow list if it is in the remove list. <br>
<br>`For element in ip_addresses:
	If element in remove_list:
	ip_addresses.remove(element)`<br><br>
Within the `for` loop, I created a conditional statement that checked if the loop variable element is in the remove list. If the statement is true, the algorithm then removes the element by using the `.remove()` function.

## Update the file with the revised list of IP addresses
For the final step, the algorithm must update the allow list file. To do so the list must be converted back into a string.<br>
<br>`ip_addresses = “\n”.join(ip_addresses)`<br><br>
We use the `.join()` function to do so. It collects all items in a list and converts them into a string. This will allow us to pass the updated string into the `.write()` function.<br>
<br>`with open(import_file, “w”) as file:
	file.write(ip_addresses)`<br><br>
We use another `with` statement. But this time in the `open()` command we will pass the second argument as `“w”` as we are looking to rewrite the file. In the with statement we use the `.write()` function to rewrite the list into the new updated list. Once complete the restricted content will not be able to be accessed by any IP addresses from the remove list. <br>

## Summary
The algorithm removes any IP addresses identified in the `“remove_list”` variable from the  `“allow_list.txt”` file. This algorithm included opening a file, converting it into a string, converting the string into a list, iterating through the Ip address in the list, checking if any elements of the list matched any elements in the `“remove_list”`. If it was, the algorithm applied the `.remove()` function to erase the element. After this I used the `.join()` method to convert the list back into a string in order to write over the original `“allow_list.txt”` with a new updated list of IP addresses. 


