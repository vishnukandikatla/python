i = "vishnu"
for ch in i :
    if ch == 's':
        print(ch, "found in index", i.index(ch))
        break
    else:
        print(ch, "not found in index", i.index(ch))
    print(ch)