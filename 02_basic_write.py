authors = [
    [1, "almasud", "Abdullah Al Masud"],
    [2, "rimon", "Rimol Ali"],
    [3, "niloy", "Niloy Roy"],
    [4, "sourov", "Sourov Deb Sharma"],
    [5, "sathi", "Sathi Rani Roy"]
]

with open("list_output.txt", "w+") as file_handler:
    for author in authors:
        file_handler.write(",".join(str(x) for x in author)+"\n")
