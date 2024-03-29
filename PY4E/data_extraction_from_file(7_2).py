# -*- coding: utf-8 -*-
"""Data_extraction_from_file(7.2).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_8kQ8W1OKOr2N1G7PZPo58vB89PEutWD

Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
"X-DSPAM-Confidence:    0.8475"
Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
"""

no_of_line = 0
total_value = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    no_of_line +=1
    colonpos = line.find(":")
    extracted_data = line[colonpos+1:]
    float_value = float(extracted_data.strip())
    total_value += float_value
print("Average spam confidence:",total_value/no_of_line)