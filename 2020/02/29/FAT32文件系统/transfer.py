# -*- coding: utf-8 -*- 
#~ #------------------------------------------------------------------
#~ module:base64 os re
#~ Filename:transfer.py 
#~ Description:transfer pacific file into base64 string and write into
#~ a text file with form of Markdown quote
#~ Function : 
#~ def get_filename(filepath):return files' name under filepath
#~ def name_fliter(file_name_list):remove files that are not image form
#~ def trans(file_name_list): base64encode image and write into txt
#~ Date: 2020-1-15 
#~ Author:Alexi Bi 
#~ Email:alexi_bi@qq.com 
#~ #------------------------------------------------------------------
#~ #------------------------------------------------------------------



import base64
import os
import re

# return files' name under filepath
def get_filename(filepath):
	file_name_list=[]
	for root,dirs,files in os.walk(filepath):
		file_name_list+=files
	return file_name_list
	
# remove files that are not image form
def name_fliter(file_name_list):
	for words in file_name_list[::-1]:
		if not (re.match(r'.*((.jpg)|(.png)|(.jpeg)|(.psd)|(.bmp))$',words)):
			file_name_list.remove(words)
	
# write into a txt file 
def trans(file_name_list):
	if len(file_name_list)!=0:
		fs=open(target,'a+')
		for files in file_name_list:
			type=os.path.splitext(files)[1][1:]
			f=open(path+'\\'+files,'rb')
			ls_f=base64.b64encode(f.read())
			fs.write('['+files+']:data:image/'+type+';base64,')
			fs.write(ls_f.decode())
			fs.write('\n')	
			f.close()
		fs.close()



print("这个小脚本可以将你选择的路径下的图片base64编码\n")
print("并且将编码以Markdown引用的格式写在当前目录下的result.txt里\n")
print("引用标签就是对应的文件名\n")
print("这样你就不用再配图床的负载啦\n")
#path=input("请输入图片的目录(也可以直接开脚本改，说不定还方便一点)：")
target='D:\\test\\source\\_posts\\2020~02~29~FAT32文件系统.md'
path=('D:\\test\\source\\image\\FAT32文件系统')	
file_name_list=get_filename(path)
name_fliter(file_name_li