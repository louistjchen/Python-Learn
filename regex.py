import re

fh = open('/Users/louischen/Desktop/regex_sum_16155.txt')

lst = list()
lst_int = list()

for line in fh:
	lst = re.findall('[0-9]+', line)
	for word in lst:
		lst_int.append(int(word))

print(sum(lst_int))
