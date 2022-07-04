import json
import os
import sys

repo = sys.argv[1]


tests = './{}/_tests/_group_1'.format(repo)
reserved_tests = './{}/tests'.format(repo)
results_json = './{}/results.json'.format(repo)

if not os.path.exists(reserved_tests):
    os.makedirs(reserved_tests)

# Opening JSON file
with open(results_json) as data_file:
    data = json.load(data_file)

filetodelete = 0
for item in data:
    filename = item.split('/')[-1]
    for input in data[item]:
        for o_level in data[item][input]["gcc"]:
            res = (data[item][input]["gcc"][o_level])
            
            if 'inf' in res or 'nan' in res or res == '-0' or res == '0':
                print("Do not keep: ", filename, res)
                filetodelete += 1
            else:
                test_to_copy = os.path.join(tests, filename)
                os.system("cp " + test_to_copy + " " + reserved_tests)
               

print("Total files to delete: ", filetodelete)
 









