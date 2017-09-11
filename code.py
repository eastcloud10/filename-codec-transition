import os
import glob
fn = glob.glob("*.wav")
line = ""
for i in range(len(fn)):
	line = fn[i]
	print("原文件名： "+line)
	print("解码文件名： "+line.encode(encoding="gbk").decode(encoding="shift_jis"))
	print("")
	os.rename(line,line.encode(encoding="gbk").decode(encoding="shift_jis"))
	
