def disStuInfo(schoolID, *firstName, **lastEmail):
    for name in firstName:
        if name in lastEmail:
            print(schoolID)
            print(name)
            print(lastEmail[name])
        else:
            print(schoolID)
            print("unmatched")
            print(name)
            if name in lastEmail:
                print(lastEmail[name])

disStuInfo(10001, 'John', 'Petter', Smith='jSmith@gmail.com', Potter="Petter@yahoo.com", Doe="j@gmail.com")