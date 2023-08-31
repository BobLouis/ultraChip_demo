import os
import subprocess

# Get all files that start with "BLOCK"
files = [f for f in os.listdir() if f.startswith('BLOCK')]
subprocess.run(["gcc", "lzss.c", "-o", "lzss"])
subprocess.run(["gcc", "lzss_split.c", "-o", "lzss_split"])

sum = 0
cnt = 0
block_size_sum = 0
for file in files:
    # Echo the filename
    print("=======================================================")
    print(file)

    # Execute the trans.py with --split argument
    subprocess.run(["python3", "trans.py", file, "--split"])
    # Execute the trans.py without any argument after file
    subprocess.run(["python3", "trans.py", file])

    # compress all
    print("compress all")
    subprocess.run(["./lzss", "e", "output.txt", "compress.txt"])
    all_total_output = subprocess.run(["./lzss", "e", "output.txt", "compress.txt"], capture_output=True, text=True).stdout
    all_total = int(all_total_output.split('total:')[1].split()[0])
    block_size_sum += int(all_total_output.split('text:')[1].split()[0])

    # split
    print("split")
    split_total_output = subprocess.run(["./lzss_split", "e", "data.txt", "compress.txt"], capture_output=True, text=True).stdout
    subprocess.run(["./lzss_split", "e", "data.txt", "compress.txt"])
    split_total = int(split_total_output.split('total:')[1].split()[0])

    sum += min(all_total, split_total)
    cnt += 1

print("=======================================================")
print("all sum ", sum, "bytes")
print("average ", sum/cnt, "bytes")
print("compress ratio(high): ",sum*100/(cnt*643),"%" )
print("compress ratio(low): ",sum*100/(block_size_sum),"%" )
