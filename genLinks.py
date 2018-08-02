# 根据基本的类型和链接生成所有要爬取的链接
links = []
with open('type_links.txt', 'rt') as f:
    for line in f:
        links.append(line.strip())
print('类型数为' + str(len(links)))

token = 'c232b098ee7611faeffc46409e836360'
limit_page = 10
all_links = []

for page in range(1, limit_page + 1):
    num = 0  # 第一个类型
    for link in links:
        next_page = links[num].split('，')[2].format(token, str(page))
        next_str = links[num].split('，')[0] + "，" + links[num].split('，')[1] + "，" + next_page
        all_links.append(next_str)
        num += 1  # 下一个类型
print('页面数量为' + str(len(all_links)))
with open('links.txt', 'wt') as f:
    for i in all_links:
        f.write(i + "\n")