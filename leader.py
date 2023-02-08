import json

with open("leaders.json") as fi:

	lb = json.load(fi)


def add_entry(ini,score):
	global lb
	lb.append([ini,score])
	lb = sorted(lb, key=lambda x: x[1],reverse=True)
	with open("leaders.json","w") as fo:
		json.dump(lb,fo)

def top10():
	res = []
	for i in range(len(lb)):
		if i > 9:
			return res
		else:
			res.append(str(lb[i][0])+": "+str(lb[i][1]))


	return res
