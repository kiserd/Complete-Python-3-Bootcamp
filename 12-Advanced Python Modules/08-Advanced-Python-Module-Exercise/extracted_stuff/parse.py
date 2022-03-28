import os
import re

def main():
	dir_names = os.listdir('extracted_content')
	regex = r'\d{3}-\d{3}-\d{4}'
	for dir_name in dir_names:
		file_names = os.listdir(f'./extracted_content/{dir_name}')
		for file_name in file_names:
			# print(f'{dir_name}/{file_name}')
			with open(f'./extracted_content/{dir_name}/{file_name}', 'r') as fptr:
				# print(f'dir_name: {dir_name}')
				# print(f'file_name: {file_name}')
				file_contents = fptr.read()
				# print(f'file_contents: {file_contents}')
				match = re.search(regex, file_contents)
				# print(f'match.group: {match.group}')
				if match:
					print(f'{match.group()}')
					return dir_name + '/' + file_name + ':' + match.group()

		


if __name__ == '__main__':
	main()
