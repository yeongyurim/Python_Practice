st1 = input().lower()
t = 0
for c in st1 :
    if c == 'a' or c == 'b' or c == 'c' :
        t += 3
    if c == 'd' or c == 'e' or c == 'f' :
        t += 4
    if c == 'g' or c == 'h' or c == 'i' :
        t += 5
    if c == 'j' or c == 'k' or c == 'l' :
        t += 6
    if c == 'm' or c == 'n' or c == 'o' :
        t += 7
    if c == 'p' or c == 'q' or c == 'r' or c == 's' :
        t += 8
    if c == 't' or c == 'u' or c == 'v' :
        t += 9
    if c == 'w' or c == 'x' or c == 'y' or c=='z' :
        t += 10
print(t)