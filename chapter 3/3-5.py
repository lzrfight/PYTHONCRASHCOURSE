# Copyright 2021/3/29 LI ZHUORAN. All rights reserved.
invite = ['friends', 'friend', 'enemy']
message = "hello" + invite[0] + invite[1] + invite[2]
print(message)
print(invite[1] + "来不了")
invite[1] = 'hi'
for welcome in invite:
    print("欢迎" + welcome)