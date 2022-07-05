# $1 is the directory of output files to parse
python filter.py $1 

python naming.py

python rewriter.py

python combine.py