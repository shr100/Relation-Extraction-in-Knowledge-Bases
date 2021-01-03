import json



def store(f, op):
	award_dict = json.load(f)
	i = 0
	for award in award_dict:
		if 'dependencies' not in award :
		    continue
		else:
		    for value in award['dependencies']:
		    	if 'tree' not in value:
		    		continue
		    	else:
		    		print(value["tree"], file=op)
		    		i = i+1
	op.close()

def main():
	f = open("Test/test.json", "r")
	op = open("Test/test_tree.txt","w")
	store(f,op)

main()