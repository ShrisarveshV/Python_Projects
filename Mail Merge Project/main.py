
with open(r".\Input\Letters\starting_letter.txt","r") as format_obj:
    letter_format=format_obj.readlines()



with open(r".\Input\Names\invited_names.txt","r+") as names_obj:
    names=names_obj.readlines()
    for name in names:
        name=name.strip()
        with open(fr".\Output\letters\{name}.txt", "w") as name_obj:
            for word in letter_format:
                    word=word.replace("[name]",name)
                    name_obj.write(word)







