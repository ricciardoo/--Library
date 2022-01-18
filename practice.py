#python三剑客练习
#前两章节的练习
name1 = 'daniel ricciARrdo'
name2 = 'lAnce stroll'
name3 = 'jay cHou'
sentence = f'Hello,{name1.title()},{name2.upper()},{name3.lower()}\
,would you like to learn some Python today?'
print(sentence)
print('退钱哥曾说，"RNM退钱"。')

#新建多个变量并赋值
x, y, z = 1, 2, 3
#常量
MAX = 4
#加减乘除
print(5 + 3)
print(16 / 2)
print(4 * 2)
print(9 - 1)

#第三章 列表简介
#3.1 列表是什么
brands = ['apPle','sonY','xIaomI','oPPo']
print(brands)
print(brands[2])
print(brands[2].title())
print(brands[2].upper())
print(brands[-1])
message = f"My first smartphone brand is {brands[1].upper()}."
print(message)

#practice3.1
names = ['daniel','jerry','tom','jacky']
print(names[0],names[1],names[2],names[3])

#practice3.2
sentance1 = f'hello,my friend {names[0].title()}!'
sentance2 = f'hello,my friend {names[1].title()}!'
sentance3 = f'hello,my friend {names[2].title()}!'
sentance4 = f'hello,my friend {names[3].title()}!'
print(sentance1)
print(sentance2)
print(sentance3)
print(sentance4)
print("------------------------")

#practice3.3
transportations = ['F1 car','Suzuki motorcycle','Mclaren 720s','cheap car']
sentance1 = f"I would like to own a {transportations[0]}."
sentance2 = f"I would like to own a {transportations[1]}."
sentance3 = f"I would like to own a {transportations[2]}."
sentance4 = f"I would like to own a {transportations[3]}."
print(sentance1)
print(sentance2)
print(sentance3)
print(sentance4)
print('------------------------')

#3.2 修改、添加和删除元素
#append增加 insert插入 del删除
cars = ['Honda','Toyota','Renault']
print(cars)
cars[2] = 'Mclaren'
print(cars)

cars.append('Tesla')
cars.append('Ford')
print(cars)

from os import remove


motorcycles = []
motorcycles.append('Honda')
motorcycles.append('Yamaha')
motorcycles.append('Suzuki')
print(motorcycles)

motorcycles.insert(0,'Ducati')
motorcycles.insert(0,'KTM')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

#pop删除
poped_motorcycle = motorcycles.pop()
print(f"The last sold moto is {poped_motorcycle.title()}.")
print(motorcycles)
print('------------------------')

lotion = ['Cetaphil','Cerave','Avene']
my_love_lotion = lotion.pop(2)
print(f"My favorite lotion is {my_love_lotion.title()}")
print(lotion)
print('------------------------')

#remove删除 可以在后面继续使用它的值
lotion = ['Cetaphil','Cerave','Avene']
print(lotion)
lotion.remove('Cerave')
print(lotion)

lotion = ['Cetaphil','Cerave','Avene']
expensive = 'Cetaphil'
lotion.remove(expensive)
print(lotion)
print(f"\nA {expensive.title()} is too expensive!")
print('------------------------')
#practice3.4
list = ['daniel','tom','jerry']
print(f"Hello,{list[0].title()},welcome to my dine in my house!")
print(f"Hello,{list[1].title()},welcome to my dine in my house!")
print(f"Hello,{list[2].title()},welcome to my dine in my house!")
print('------------------------')
#practice3.5 假设tom无法参加
print(f"{list[1].title()} can not come to my house!")
list[1] = 'dan'
print(f"Hello,{list[0].title()},welcome to my dine in my house!")
print(f"Hello,{list[1].title()},welcome to my dine in my house!")
print(f"Hello,{list[2].title()},welcome to my dine in my house!")
print('------------------------')
#practice3.6
print('I found a big table!')
list.insert(0,'jojo')
list.insert(2,'jacky')
list.append('may')
print(list)
print(f"Hello,{list[0].title()},welcome to my dine in my house!")
print(f"Hello,{list[1].title()},welcome to my dine in my house!")
print(f"Hello,{list[2].title()},welcome to my dine in my house!")
print(f"Hello,{list[3].title()},welcome to my dine in my house!")
print(f"Hello,{list[4].title()},welcome to my dine in my house!")
print(f"Hello,{list[5].title()},welcome to my dine in my house!")
print('------------------------')
#practice3.7
print('没桌子，只能来两个人！')
list2 = list.pop()
list3 = list.pop()
list4 = list.pop()
list5 = list.pop()
print(f"Sorry {list2.title()},you can not come to my house.")
print(f"Sorry {list3.title()},you can not come to my house.")
print(f"Sorry {list4.title()},you can not come to my house.")
print(f"Sorry {list5.title()},you can not come to my house.")

print(f"Hello {list[0].title()},you can come to my house.")
print(f"Hello {list[1].title()},you can come to my house.")

del list[0]
del list[0]

print(list)
print('------------------------')

#3.3组织列表
