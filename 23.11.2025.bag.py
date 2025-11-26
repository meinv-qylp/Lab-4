import time
import sys

RED='\u001b[91m'
YELLOW='\u001b[93m'
BLUE='\u001b[94m'
a='\u001b[0m'

items = [
    ("吸入器","i", 1 , 5 ),("步枪","r", 3 , 25 ),("手枪","p", 2 , 15 ),
    ("弹药","a", 2 , 15 ),("急救箱","m", 2 , 20 ),("刀","k", 1 , 15 ),
    ("斧头","x", 3 , 20 ),("护身符","t", 1 , 25 ),("烧瓶","f", 1 , 15 ),
    ("解药","d", 1 , 10 ),("食物","s", 2 , 20 ),("弓弩","c", 2 , 20 )
]


def method():
    m = input("how big is a hero's bag?\n  size of a bag: ")
    package = int(m)
    used_space = 0
    total_points = 15
    final_item = []
    final_item_name = []
    table = []

    new_items = sorted(items, key=lambda x: x[3]/x[2], reverse=True)
    #按照key要求的顺序进行排列   
    # sorted(可迭代对象，key = 排序依据，reverse = 是否反转)
    

    print(f'\n{BLUE}{"nothing"}{a}')
    loading_multiple(2)
    print()
    for item in new_items:
        name,number,size,points = item
        if used_space + size <= package:
            final_item.append(item)
            used_space += size
            total_points += points
            final_item_name.append(item[0])
    print(f'{BLUE}{final_item_name}{a}\n')

    for item_x in final_item:
        new_items.remove(item_x)
            
    for no_items in new_items:
        name_2,number_2,size_2,points_2 = no_items
        total_points -= points_2     

    for item in final_item:
        for _ in range(int(item[2])):
            table.append(f"[{item[1]}]")
    print(f'{YELLOW}{table[:4]}{a}')
    print(f'{YELLOW}{table[4:]}{a}\n')    

    print(f"{BLUE}final score: {total_points}{a}\n")


    if total_points < 0 :
        print(f"{RED}you have no chance of survival.....{a}")
    elif total_points == 0:
        print(f"{RED}you survived, but it was so difficult...{a}") 
    elif total_points > 0 :
        print(f"{BLUE}you survived successfully!!)){a}")      
    print(f"{BLUE}THE END{a}")


def loading_multiple(m):
    bar = 30
    for p in range(m):
        for i in range(1, bar + 1):
            time.sleep(0.05)  
            percent = i * 100 // bar
            b=" "
            L = b * i + "0" * (bar - i)
            sys.stdout.write(f'\rTask {p+1}/{m} [{L}] {percent:3d}%')
            sys.stdout.flush()
    
        sys.stdout.write('\r' + ' ' * (50 + bar) + '\r')
        sys.stdout.flush()

print(f"{RED}The post-apocalyptic environment is being generated.{a}")
loading_multiple(3)
method()