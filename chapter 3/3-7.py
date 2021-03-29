# Copyright 2021/3/29 LI ZHUORAN. All rights reserved.
# 你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
# 所以打印一条你只能邀请两位嘉宾共进晚餐的消息
# 使用pop()不断的删除名单中的嘉宾，直到只有俩位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾直到你很抱歉。
# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列
# 使用del将最后两位嘉宾删除，让名单变成空

invite = ['friends', 'friend', 'enemy']
message = "hello" + invite[0] + invite[1] + invite[2]
print(message)
print(invite[1] + "来不了")
invite[1] = 'hi'
for welcome in invite:
    print("欢迎" + welcome)
print("我找到了更大的桌子")
invite.insert(0, "mama")
invite.insert(2, "baba")
invite.append("nb")
for again in invite:
    print("欢迎" + again)
print("对不起，桌子坏了，只能邀请两位嘉宾")

while len(invite) > 2:
    kick = invite.pop()
    print("对不起" + kick)
for welcome2wei in invite:
    print("欢迎二位" + welcome2wei)
