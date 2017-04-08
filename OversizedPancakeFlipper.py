def solve(S,k):
    changes = 0
    for i in range(1, len(S)):
        temp=S

        if temp[i]==temp[i-1]:
            if temp[i-1]==temp[i-2]:
                pass
            changes+=1
        changes+=1



        if S[i] != S[i-1]:
            changes += 1

    if S[-1] == "+":
        return changes
    else:
        return changes + 1

if __name__ == "__main__":
    import fileinput
    f = fileinput.input()
    """The first line of the input gives the number of test cases, T. T test cases follow. Each consists of one line with a string S, each character of which is either + (which represents a pancake that is initially happy side up) or - (which represents a pancake that is initially blank side up). The string, when read left to right, represents the stack when viewed from top to bottom."""
    # strr, k = f.split()
    T = int(f.readline())
    for case in range(1, T+1):
        S = f.readline().strip()
        strr, k = S.split()
        # print(strr)
        # print(k)
        solution = solve(S,k)
        print("Case #{0}: {1}".format(case, solution))
