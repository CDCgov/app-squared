#!bin/env/python
import argparse
import os
import pandas as pd
import re

parser = argparse.ArgumentParser()

parser.add_argument("-i", dest="input", help="input file generated by running contact_diffs.py", required=True)
parser.add_argument("-o", dest="output", help="output file name", required=True)
args = parser.parse_args()

def compare_files(test_file):
    with open(test_file) as parsed_file:
        E_sites = []
        for line in parsed_file:
            #match = re.search(r'501',line)
            match = re.search(r'57|59|61|62|63|64|75|78|79|80|81|82|83|87|91|92|94|260|261|262|265',line)
            if match:
                print(line)
                E_sites.append(line)
    return E_sites

E_adj = compare_files(args.input)
#print(D_adj)
diff_df = pd.DataFrame(E_adj)
diff_df.to_csv(args.output)

