import sys

def insert_str(string, str_to_insert, index):
    return string[:index] + str_to_insert + string[index:]

# for i in lines:
#     i = insert_str(i, "|", 4)
#     i = insert_str(i, "|", 21)
#     i = insert_str(i, "|", 26)
#     i = insert_str(i, "|", 30)
#     i = insert_str(i, "|", 33)
#     i = insert_str(i, "|", 49)
#     i = insert_str(i, "|", 66)
#     i = insert_str(i, "|", 69)
#     i = insert_str(i, "|", 86)
#     i = insert_str(i, "|", 95)
#     w.writelines(i)

if __name__ == '__main__':

    f = open(str(sys.argv[1]),"r", encoding = "Big5")
    w = open(str(sys.argv[2]), "w")
    lines = f.readlines()

    for i in lines:
        i = insert_str(i, str(sys.argv[3]), int(sys.argv[4]))
        w.writelines(i)
        print(i)




