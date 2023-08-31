import os
import subprocess
import sys

if len(sys.argv) > 1:  # 檢查是否提供了參數
    file = sys.argv[1]  # 第一個參數是文件名
    print(f"The provided file is {file}")
else:
    print("No file provided.")

subprocess.run(["gcc", "lzss.c", "-o", "lzss"])
subprocess.run(["gcc", "lzss_split.c", "-o", "lzss_split"])



print(file)

# Execute the trans.py with --split argument
subprocess.run(["python3", "trans.py", file, "--split"])
# Execute the trans.py without any argument after file
subprocess.run(["python3", "trans.py", file])

# compress all
print("compress all")
subprocess.run(["./lzss", "e", "output.txt", "compress_all_"+file])
all_total_output = subprocess.run(["./lzss", "e", "output.txt", "compress_all.txt"], capture_output=True, text=True).stdout
all_total = int(all_total_output.split('total:')[1].split()[0])

# split
print("split")
split_total_output = subprocess.run(["./lzss_split", "e", "data.txt", "compress.txt"], capture_output=True, text=True).stdout
subprocess.run(["./lzss_split", "e", "data.txt", "compress_split_"+file])
split_total = int(split_total_output.split('total:')[1].split()[0])

print("compress all", all_total, "bytes")
print("split", split_total, "bytes")

## check lossless
print("decode and diff")
subprocess.run(["./lzss", "d","compress_all_"+file, "decompress_all_"+file])
subprocess.run(["diff", "-s", 'output.txt', "decompress_all_"+file])
