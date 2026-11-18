

with open('C:/Users/USER/2nd Contact Session Assign/Question1/text_file.txt', "r") as file:
    for li in file:
        if "FIRST" in li or "MIDDLE" in li or "LAST" in li:
            print(li)
    