gmail = input("Create Your Own Gmail: ")

valid = True
if gmail.endswith("@gmail.com"):
    if gmail.startswith('.') or gmail.startswith("_") or gmail.startswith("-"):
        valid = False
    else:
        if gmail.count("@") > 1:
            valid = False
        else:
            first_part = gmail.split("@")[0]
            if first_part.endswith(".") or first_part.endswith("_") or first_part.endswith("-"):
                valid = False
            else:
                if len(first_part) in range(6, 31):
                    final_test = ""
                    for i in range(len(first_part)):
                        if first_part[i] == first_part[i-1]:
                            if first_part[i] == "." or first_part[i] == "-" or first_part[i] == "_":
                                valid = False
                        if not first_part[i] == '.' and not first_part[i] == '_' and not first_part[i] == '-':
                            final_test += first_part[i]
                    if not final_test.isalnum() or not final_test.isascii():
                        valid = False
                else:
                    valid = False
else:
    valid = False

if valid:
    print("Your Gmail has been created successfully!")
else:
    print("Invalid format!")

