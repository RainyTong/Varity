# $1 is the directory of output files to parse
python3 filter.py $1 

python3 naming.py

python3 rewriter.py

python3 combine.py