from urllib import request

file = open("address.txt")
string = file.read()
# 定义两个变量：分别表示开始的字符串，结束的字符串
start1 = 'img src="'
end1 = '&amp'
# 使用find找到开始截取的位置
s = string.find(start1)
#只要s不等于-1，说明找到了http
while s!= -1:
    #找结束位置
    e = string.find(end1, s)
    #截取字符串
    sub_str = string[s+9:e]

    temp1 = sub_str[0:len(sub_str)-27]
    temp2 = sub_str[len(sub_str) - 21:len(sub_str)]

    url = temp1 + 'orignal/' + temp2

    print(url)

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Host': 's12.sinaimg.cn'
    }

    req = request.Request(url=url, headers=headers, method='GET')
    response = request.urlopen(req)

    filename = url[len(url) - 21:len(url)] + ".jpg"
    file = open(filename, "wb")
    file.write(response.read())
    file.close()

    #找到下一个开始位置
    #如果没有找到下一个开始的位置，相当于写了一句s=-1,while循环的条件不成立，结束循环
    s = string.find(start1, e)
