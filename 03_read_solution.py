with open("list_output.txt", "r") as file_handler:
    for line in file_handler:
        a,b,c = line.split(",")
        # another_string = "-".join(str(x) for x in string)
        print(a+"-"+c)
