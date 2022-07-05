import json
import os

diff = 0
for dir in sorted(os.listdir('./')):
    # if os.path.isdir(dir) and dir.startswith('bronze'):
    if os.path.isdir(dir) and os.path.exists(os.path.join(dir, "results.json")):

        print(dir)

        results_json = os.path.join(dir, "results.json")
        # Opening JSON file
        with open(results_json) as data_file:
            data = json.load(data_file)

        checker_path = './checker.txt'
        with open(checker_path) as f0:
            # read file into a list
            checker = f0.readlines()

        tests_checker = './tests+checker/'
        if not os.path.exists(tests_checker):
            os.makedirs(tests_checker)

        directory = os.path.join(dir, "tests")

        for filename in os.listdir(directory):
            f = os.path.join(directory, filename)
            if os.path.isfile(f):
                
                input = '//'

                # cal the num
                num = int(filename[:-2].split('_')[-1])
                new_num = num - diff
                new_filename = filename.replace(str(num), str(new_num))
                item = dir + "/_tests/_group_1/" + new_filename

                for i in data[item]:
                    for j in i.split(','):
                        input += j + ' '
                input += '\n'

                file = []
                file.append("//" + item + "\n")
                file.append(input)
                file.append("//\n")

                with open(f) as f1:
                    for line in f1:
                        if line.startswith("void compute"):
                            file.append("#include <time.h> // for clock_t, clock(), CLOCKS_PER_SEC\n")
                            file.append("typedef enum { false, true } logical;\n\n")
                            index = line.rfind(')')
                            new_line = line[:index] + ", int comp_flag" + line[index:]
                            file.append(new_line)
                            file.append("    double time_spent = 0.0;\n")
                            file.append("    clock_t begin = clock();\n\n")
                        elif "printf" in line:
                            file = file + checker
                        elif "compute" in line:
                            num_args = line.count(',') + 1
                            file.append("  int comp_flag = atoi(argv[{}]);\n".format(num_args+1))
                            index = line.rfind(')')
                            new_line = line[:index] + ", comp_flag" + line[index:]
                            file.append(new_line)
                        else:
                            file.append(line)
                    
                # write to a new file
                with open(os.path.join(tests_checker, filename), "w") as f2:
                    for line in file:
                        f2.write(line)
    
        diff += 1000