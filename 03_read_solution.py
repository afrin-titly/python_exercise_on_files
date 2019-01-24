with open("list_output.txt", "r") as file_handler:
    with open("read_solution_output.txt", "w+") as file_handler_output:
        for line in file_handler:
            a,b,c = line.split(",")
            file_handler_output.write(a+"-"+c)
