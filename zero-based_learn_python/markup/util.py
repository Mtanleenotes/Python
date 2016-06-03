# coding=utf-8
# lines生成器只是在文件的最后加一个空行
def lines(file):
    for line in file:
    	yield line
    yield '\n'

def blocks(file):
	block = []
	for line in lines(file):
		if line.strip():
			block.append(line)
		elif block:
			yield ''.join(block).strip()
			block = []