import zipfile

zipped_obj = zipfile.ZipFile('unzip_me_for_instructions.zip', 'r')
zipped_obj.extractall('extracted_stuff')
zipped_obj.close()
