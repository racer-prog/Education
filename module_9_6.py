def all_variants(text):

    for x in range(len(text)):
        for y in range(len(text)-x):
            yield text[y:y+x+1]

def all_variants2(text):
    i = 0
    for x in range(len(text)):
        # print(len(text), "len(text)")
        for y in range(len(text)-x):
            print("Result:", "'",text[y:y+x+1],"'", "при X,Y:", x,y)
            i += 1
            # if i >= (len(text)) * 2 - 1:
            #     break





if __name__ == "__main__":
    a = all_variants("abc")
    for i in a:
        print(i)

    #all_variants2("abc")
    # all_variants2("abcd")



