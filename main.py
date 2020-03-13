import sys

def check_mapping(s1:str, s2:str):
    if len(s1) != len(s2):
        print("two strings are not equal in length")
        return False
    dict = {}
    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]
        if not c1 in dict:
            dict[c1] = c2
        else:
            if dict[c1] != c2:
                return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("exactly 2 parameters needed")
    print(check_mapping(sys.argv[1], sys.argv[2]))