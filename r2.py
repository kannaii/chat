
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding='utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines


def convert(lines):
	new =[]
	person = None # 若一開始沒有人名
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('allen説了', allen_word_count, '個字')
	print('allen傳了', allen_sticker_count, '張貼圖')
	print('allen傳了', allen_image_count, '張圖片')
	print('viki說了', viki_word_count, '個字')
	print('viki傳了', viki_sticker_count, '張貼圖')
	print('viki傳了', viki_image_count, '張圖片')
		# print(s)
	
# 清單的分割介紹
# n = [2, 6, 6, 8, 4]
# 前3個: n[:3] = [2, 6, 6]
# 中間 n[2:4] = [6, 8]
# 結尾 n[-2:] = [8, 4] # -2表示從尾部往前數第2個開始, 把剩下都拿完

def write_file(filename, lines):
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	# write_file('output.txt', lines)

main()