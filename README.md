# Algorithm-For-File-Updates

## Description
For this project, we were required to update a file that identifies which employees can access restricted content based on their IP addresses. There is also a remove list which includes IP addresses of employees that must be removed from the first file. To make this easier, I was tasked with creating an algorithm that automates removing the unwanted IP addresses from the allow list. 
<br />

# Walkthrough:<br>

## Open the file that contains the allow list
To open the file that contains the allow list, we must first import the file and assign it to a variable. For my variable I chose the name `import_file`. <br>
#insert image<br>
Next I used a `with` statement to open the file.<br>
#insert image<br>
Using the `with` statement and `.open()` command opens the `“allow_list.txt”` file and lets us read the contents inside. The `with` statement lets the computer know to close the file after to save resources. The open command has 2 arguments. The first argument is the file to be opened, and the second argument indicates what to do with the file. In this case, the file we are opening is in the variable `“import_file”` and as of right now we only intend to read it so we just pass through `“r”`. We also use the keyword `“as”` to assign the file to a variable called `“file”`. This stores the output of open and allows us to use it in the code within the with statement .

## Read the file contents
