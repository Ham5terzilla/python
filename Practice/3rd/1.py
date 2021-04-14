s = input()
new_s = ''
count = 1
for i in range(len(s)):
    if i != len(s)-1:
        if s[i] == s[i+1]:
            count += 1
        else:
            new_s += s[i]
            new_s = "{0}{1}".format(new_s, str(count))
            count = 1
    else:
        new_s += s[i]
        new_s = "{0}{1}".format(new_s, str(count))
        count = 1
print(new_s)