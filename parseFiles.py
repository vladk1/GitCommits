import fileinput
import sys
import operator

bumpCounts= {}
hotfixCounts = {}
finalPercentage = {}
BUMP_SEPARATOR="countsBump[] = "
HOTFIX_SEPARATOR="foundFixCommits[] = "
COMA_SEPARATOR=", "

for line in open(sys.argv[1]):
    if BUMP_SEPARATOR in line: 
    	bump_args = line.replace(BUMP_SEPARATOR, "").split(COMA_SEPARATOR)
    	bumpCounts[bump_args[0]] = bump_args[1]

    elif HOTFIX_SEPARATOR in line:
    	hotfix_args = line.replace(HOTFIX_SEPARATOR, "").split(COMA_SEPARATOR)
    	hotfixCounts[hotfix_args[0]] = hotfix_args[1]

for key in bumpCounts:
	if key in hotfixCounts:
		finalPercentage[key] = float(hotfixCounts[key])/float(bumpCounts[key])
		
sorted_x = sorted(finalPercentage.items(), key=operator.itemgetter(1))
new_file = open(sys.argv[2], 'w+')
for key,value in sorted_x:
	print(key+" "+str(value))
	new_file.write(key+" "+str(value)+"  hf="+hotfixCounts[key].replace("\n", "")+" bc="+bumpCounts[key].replace("\n", ""))
	new_file.write("\n")