def calcDamage(s):
    strength = 1
    total_damage = 0
    for i in s:
        if i == 'C':
            strength = strength * 2
        elif i == 'S':
            total_damage = total_damage + strength
    return strength, total_damage

def run_algo(string, acceptable):
    steps = 0
    for j in range(len(string)):
        for i in range(len(string) - 1):
            t1, t2 = calcDamage(''.join(string))
            if  t2 <= acceptable:
                return 0
            else:
                if string[i] == 'C':
                    if string[i + 1] == 'S':
                        t = string[i]
                        string[i] = string[i + 1]
                        string[i + 1] = t
                        s, d = calcDamage(''.join(string))
                        steps = steps + 1
                        if d <= acceptable:
                            return steps
    return "IMPOSSIBLE"

t = int(input())
res = []

for i in range(t):
    D, S = input().split()
    # res.append("Case #%d: %s" %((i + 1), run_algo(list(S), int(D))))
    print("Case #%d: %s" %((i + 1), run_algo(list(S), int(D))))

# for i in res:
#     print(i)
