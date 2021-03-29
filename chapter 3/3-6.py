# Copyright 2021/3/29 LI ZHUORAN. All rights reserved.
# 你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想还想邀请哪三位嘉宾

invite = ['friends', 'friend', 'enemy']
message = "hello" + invite[0] + invite[1] + invite[2]
print(message)
print(invite[1] + "来不了")
invite[1] = 'hi'
for welcome in invite:
    print("欢迎" + welcome)
print("我找到了更大的桌子")
invite.insert(0,"mama")
invite.insert(2, "baba")
invite.append("nb")
for again in invite:
    print("欢迎" + again)