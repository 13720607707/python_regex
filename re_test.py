import re
#match 匹配以xxx开头的字符串，第一个参数是正则，第二个是所需要匹配的字符串

strdata='python is best'
res=re.match('y',strdata,re.I)#re.I忽略大小写
print(res)#对象
res.group()#匹配的值
res.groups()#元组形式直接输出（不支持索引）
res.group(1)#如果有多个匹配结果以元组的形式存放在哪group对象中

res=re.match('python',strdata)#可以是单词

'''
. 匹配除了换行符之外的字符
[abc] 匹配中括号中任意字符

'''
data='aaaa'

res2=re.match('.',data)
print(res2.group())

names='李明','李华','小明'

for name in names:
    res3=re.match('李.',name)
    print(res3.group())


str1='hello'

res4=re.match('[he]',str1)#只匹配开头，[abc]代表匹配a或者b或者c

print(res4.group())
#[a-z]a到z




#\d匹配一个数字 0-9(一位)


data='w1234abcdef'
print(re.match('\d',data).group())

#\D匹配非数字
#\s匹配空格
#\S匹配非空格
data='  hello'
print(re.match('\s\s',data).group())#两位空格
#\w匹配单词字符 a-z A-Z 0-9
#\W  非单词字符
data='2Yssdf'
print(re.match('\w\w',data).group())#结果2Y



'''
匹配字符数量符号
'''
# * 匹配前一个字符出现0次或者无限次，即可有可无

re.match('[A-Z][A-Z]*','My')
print(res.group())#结果M  若没*报错
print(re.match('[A-Z][a-z]*','Annnny').group())#结果 Annnny
print(re.match('[A-Z][a-z]*','AnnnNny').group())#结果 Annn


# +匹配前一个字符出现1次或者无限次，即最少有一次

print(re.match('[A-Z]+','mmTDAJD').group())#报错
print(re.match('[a-zA-Z]+','mmTDAJD').group())#全部
print(re.match('[A-Z]+','MJJJJnnTDAJD').group())# MJJJJ

print(re.match('[a-zA-Z_]+[\w]*','111mmTDAJD').group())# 报错 匹配规范不能以数字开头

# \?匹配前一个字符出现1次或者0次，即要么有一次，要么没有

print(re.match('[a-zA-Z][0-9]','mm3TDAJD').group())#报错 []代表一位
print(re.match('[a-zA-Z][0-9]？','mm3TDAJD').group())#不报错 结果m
print(re.match('[a-zA-Z][0-9]？','m3mTDAJD').group())#m3
print(re.match('[a-zA-Z]+[0-9]？','mm333TDAJD').group())#mm3



# {m}匹配前一个字符出现m次

print(re.match('\d{4}','123').group())#匹配不成功
print(re.match('\d{4}','1234').group())#1234
print(re.match('\d{3}','1234567').group())#123

# {m,}匹配前一个字符至少出现m次
print(re.match('\d{3，}','1234').group())#1234

# {n,m}匹配前一个字符出现从n到m次
print(re.match('\d{3，8}','12345').group())#12345
print(re.match('\d{3，8}','12345678888').group())#12345678

'''
原生字符串  \n换行 \t tab键 \\ 表示本身\
'''

mypath='G:\py\上课\课件.html'
print(mypath)#路径输出异常  \乱码
print('G:\\py\\上课\\课件.html')#正常
print(re.match('c:\\a.txt','c:\\a.txt').group())#报错
print(re.match('c:\\\\a.txt','c:\\a.txt').group())#成功
print(re.match(r'c:\\a.txt','c:\\a.txt').group())#r表示原生字符串


#  ^以什么开头   $以什么结尾

print(re.match('^p.*','python is best').group())#全部

print(re.match('^P.*','python is best').group())#报错

print(re.match('[\w]{5,15}@[\w]{2,3}.com$','abcdjeiarhohf@qq.com').group())#匹配成功
print(re.match('[\w]{5,15}@[\w]{2,3}.com$','abcdjeiarhohf@qq.coma').group())#失败

'''
分组匹配
'''
# |匹配左右任意一个表达式

string='wergagdud888'
print(re.match('(wergagdud|wergagdud888)',string).group())#  结果wergagdud 从前往后匹配


#（ab）将括号中的字符作为一个分组


print(re.match('([0-9]*)-(\d*)','3123-123435').group(0))#3123-123435
print(re.match('([0-9]*)-(\d*)','3123-123435').group(1))#3123
print(re.match('([0-9]*)-(\d*)','3123-123435').group(2))#123435

print(re.match('([^-]*)-(\d*)','3123-123435').group(0))# ^- 取反 匹配不是-的字符
#\num 引用分组num匹配到的字符串
htmltag='<html><h1>测试数据</h1></html>'
re.match(r'<(.+)><(.+)>(.+)</\2></\1>',htmltag)#引用前面引用过的内容


#(?P) 分组起别名
#(?P=name)引用别名为name分组匹配到的字符串
data='<div><h1>baidu</h1></div>'
print(re.match(r'<(?P<div>\w*)><(?P<h1>\w*)>.*</(?P=h1)></(?P=div)>',data).group())#取别名



'''

re.compile  提高效率  在使用正则表达式时，python会将字符串转化为正则表达式对象  
'''

reobj=re.compile('\d{4}')
rs=reobj.match('1235678')
print(rs.group())#1235

'''  
re.search  全文中匹配一次，匹配就返回
'''
data='我爱中国，I love China，China is a great country'

print(re.search('China',data).group())#结果 China   第一个China

'''
findall  匹配所有返回一个列表 
'''

data='dadhaiodhoaidh'

print(re.findall('d.',data))   #结果 da   dh dh dh
print(re.search('d.',data).group())  #结果  da  只要有一个满足立马返回

reo_obj=re.compile('d.')
print(reo_obj.search(data))
print(reo_obj.findall(data))


'''
re.sub  将匹配到的数据进行替换
'''
datas='python 是语言'
pattern='[a-zA-Z]+'#字符集的范围  + 号  代表 前导字符模式出现一次以上
ret=re.sub(pattern,'C#',datas)#  python 替换为C#

re.subn(pattern,'C#',datas)#以元组形式返回被替换的数量  （C# 是语言，1）


'''
re.split  根据匹配进行切割字符串，并返回一个列表

'''


datass='百度，腾讯，阿里'
print(re.split(',',datass))#   [‘百度’，‘腾讯’，‘阿里’]


''''
贪婪模式  非贪婪模式


'''


re.match('.*\d','a2222').group()  #a2222

re.match('.*?\d','a11112').group()  #a1  加？非贪婪模式  尽可能少的去匹配


