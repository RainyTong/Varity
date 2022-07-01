import json
import os

tests = '/home/yutong98/Repository/github/Varity/varity/COE-CS-blue_293540/_tests/_group_1'
reserved_tests = '/home/yutong98/Repository/github/Varity/varity/COE-CS-blue_293540/tests'
results_json = '/home/yutong98/Repository/github/Varity/varity/COE-CS-blue_293540/results.json'

if not os.path.exists(reserved_tests):
    os.makedirs(reserved_tests)


# Opening JSON file
with open(results_json) as data_file:
    data = json.load(data_file)

filetodelete = 0
for item in data:
    for input in data[item]:
        for filename in data[item][input]["CS"]:
            res = (data[item][input]["CS"][filename])
            
            if 'inf' in res or 'nan' in res or res == '-0' or res == '0':
                print("Do not keep: ", filename, res)
                filetodelete += 1
            else:
                test_to_copy = os.path.join(tests, filename.split('/')[-1]+'.c')
                os.system("cp " + test_to_copy + " " + reserved_tests)
               

print("Total files to delete: ", filetodelete)
 