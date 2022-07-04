import os
diff = 0
for dir in sorted(os.listdir('./')):
    if os.path.isdir(dir) and dir.startswith('bronze'):
        print(dir)
        for file in sorted(os.listdir(os.path.join(dir, 'tests'))):
            num = int(file[:-2].split('_')[-1])
            new_file = file.replace(str(num), str(num + diff))

            file_p = os.path.join(dir, 'tests', file)
            new_file_p = os.path.join(dir, 'tests', new_file)

            os.system('mv {} {}'.format(file_p, new_file_p))
        diff += 1000
        