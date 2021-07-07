#programme to accept a file name from the user and print the extension of that
f=input("Enter the filename: ")
d=f.split(".")
print("The extension of the file is : "+repr(d[-1]))
