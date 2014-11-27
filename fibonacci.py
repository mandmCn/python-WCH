def f(n):
    fi_list = []
    for i in range(n):
	if i == 0:
	    fi_list.append(1)
	elif i == 1:
	    fi_list.append(2)
	else:
	    fi_list.append(fi_list[i-2] + fi_list[i-1])
    return fi_list[-1]

print f(100)
