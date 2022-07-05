import os

OUTDIR = './tests'

if not os.path.exists(OUTDIR):
    os.makedirs(OUTDIR)

for dir in sorted(os.listdir('./')):
    if os.path.isdir(dir) and dir.startswith('bronze'):
        os.system("cp {}/tests/* {}".format(dir, OUTDIR))