#导入随机工具包
#注意：在导入工具包时，应该将导入的语言放在文件的顶部
#这样可以方便下方的代码，在任何时候使用工具包中的工具
import random
#从控制台输入要出的拳——石头[1]/剪刀[2]/布[3]
player = int(input("请输入您要出的拳 石头[1]/剪刀[2]/布[3]:"))
#电脑 随机 出拳 —— 先
computer = random.randint(1,3)
print("玩家选择的拳头是%d - 电脑出的拳头是%d" % (player,computer))
#比较胜负
#1 石头 胜 剪刀
#2 剪刀 胜 布
#3 布 胜 石头
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):

    print("欧耶，电脑弱爆了！")
#平局
#1 石头 平 石头
#2 剪刀 平 剪刀
#3 布 平 布
elif(player == computer):
    print("真是心有灵犀啊，再来一局")
else:
    print("不服气，决战到天明！")
