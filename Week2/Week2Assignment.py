"""
#Assignment1

"""
def find_and_print(messages, current_station):
    map_difference = {}

    for name, msg in messages.items(): #先檢驗名字跟訊息裡的站名
        distance = []
        for sublist in [list2, list3] if current_station == "Xiaobitan" else [list1, list2, list3]:
          #按目前所在點是不是 xiaobitan檢視不同list, (不同路線) A:2,3, B:1,2,3
            if current_station in sublist: #如果找到同樣在同樣的list （同樣路線），按照list[index]來計算距離
                distances = [abs(sublist.index(item) - sublist.index(current_station)) for item in sublist if item in msg]
                distance.extend(distances)
        if distance:
            map_difference[name] = distance #本來map_difference{},開始記錄後，對應本來key(name): value(distance)
            #print(map_difference)

    # 紀錄 the minimum distance for each friend
    #print(min_distance_map) 驗證用
    shortest_distance = min(map_difference.values())
    closest_friend = [key for key, value in map_difference.items() if value == shortest_distance]
    #上面是列表生成式，說明一下我只要在 closest_friend 中有一個字串str, 預設是最近的朋友，這個朋友是從我放入map_difference的 name:distance去選擇 name
    #而我只要 name的部分，所以 closest_friend =[key 後面說明從哪裡取key]: for key, value in map_difference.items()，從value是最小距離的那個 key（name）取出
    print(closest_friend)
    return
messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
}

    # 先分出三個線路
list1 = ["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing",
             "Songjiang Nanjing","Zhongshan","Beimen","Ximen","Xiaonanmen",
             "Chiang Kai-Shek Memorial Hall","Guting","Taipower Building",
             "Guongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian"
             ] #main line

list2 = ["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing",
             "Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting",
             "Taipower Building","Guongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xiaobitan"
             ] #branch line-1

list3 = ["Xiaobitan","Qizhang","Xindian City Hall","Xindian"] #branch line-2


# Test cases
print("<Assignment1>")
find_and_print(messages, "Wanlong") # print Mary
find_and_print(messages, "Songshan") # print Copper
find_and_print(messages, "Qizhang") # print Leslie
find_and_print(messages, "Ximen") # print Bob
find_and_print(messages, "Xindian City Hall") # print Vivian

"""
#Assignment2

"""
def book(consultants, hour, duration, criteria):
    # Step 1: 確認所有顧問的BookedTime
    for consultant in consultants:
        if not consultant.get("BookedTime"): #字典用.get(), 如果不是字典的話像list, 直接執行就好：if not my_list:
            consultant["BookedTime"] = []

    # Step 2: 判斷預定時間是否與現有預定重疊，並取出時間上可以的顧問
    available_consultants = [] #預設目前沒有可以供預訂的顧問
    for consultant in consultants:
        is_overlap = False #預設一開始顧問的時間都沒有重疊
        for existing_time in consultant["BookedTime"]:
            if check_overlap(existing_time, (hour, hour + duration)):
                is_overlap = True
                break #如果已經有查到重複的時間段，就跳出，不需要查完全部的時間段
        if not is_overlap: #True
            available_consultants.append(consultant)

    # Step 3: 如果所有顧問時間都有重疊，print "No Service" 後return
    if not available_consultants:
        print("No Service")
        return #（就跳出 book()函式，不需要繼續往下判斷criteria了。

    # Step 4 & 5: 根據criteria選擇最小或最大值
    # print(available_consultants) 測試用
    if criteria == "price":
        selected_consultant = min(available_consultants, key=lambda x: x["price"]) 
        #參考使用了匿名函式，記得 available_consultants 是字典的list，全寫有點多，這段表示比較 price後，取出list的item=x(dict)
    elif criteria == "rate":
        selected_consultant = max(available_consultants, key=lambda x: x["rate"])

    # print
    print(selected_consultant["name"])

    # Step 6: 將預定時間添加到所選顧問的BookedTime中
    selected_consultant["BookedTime"].append((hour, hour + duration))
    selected_consultant["BookedTime"].sort()
    # 合併相鄰的時間範圍
    i = 0
    while i < len(selected_consultant["BookedTime"]) - 1:
        if selected_consultant["BookedTime"][i][1] == selected_consultant["BookedTime"][i + 1][0]:
            selected_consultant["BookedTime"][i] = (selected_consultant["BookedTime"][i][0], selected_consultant["BookedTime"][i + 1][1])
            del selected_consultant["BookedTime"][i + 1]
        else:
            i += 1
    #print(selected_consultant["BookedTime"]) 確認上面編寫的時間範圍

# 檢查時間重疊的函式
def check_overlap(existing_time, new_time):
    return existing_time[0] < new_time[1] and existing_time[1] > new_time[0]


# 執行
consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800}
]
print("")
print("<Assignment2>")
book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")   # John
book(consultants, 11, 1, "rate")   # Bob
book(consultants, 11, 2, "rate")   # No Service
book(consultants, 14, 3, "price")  # John

"""
Assignment3

"""
def func(*data):
    for name in data:
        # 提取中間名
        middle_name = ""
        if len(name) in [2, 3]:
            middle_name = name[1]
        elif len(name) in [4, 5]:
            middle_name = name[2]

        # 檢查中間名是否唯一，skill: 設定一個unique變數，預設True，去iterate其他名字
        unique = True
        for other_name in data: #這邊以O(n)跟外面整體會變成 O(n^2)
            if name != other_name:
                if len(other_name) in [2, 3]:
                    if middle_name == other_name[1]:
                        unique = False
                        break
                elif len(other_name) in [4, 5]:
                    if middle_name == other_name[2]:
                        unique = False
                        break

        # 如果中間名唯一就印出
        if unique:
            print(name)
            return

    # 如果沒有唯一的中間名就印出"沒有"
    print("沒有")

# 測試
print("")
print("<Assignment3>")
func("彭大牆", "陳王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆")  # print 夏曼藍波安

"""
Assignment4

"""

def get_number(n):
    group_index = n // 3  # 求商表示所在的組的索引
    remainder = n % 3     # 求餘表示在組內的位置
    return 7 * group_index + 4 * remainder

# Test cases
print("")
print("<Assignment4>")
print(get_number(1))   # print 4
print(get_number(5))   # print 15
print(get_number(10))  # print 25
print(get_number(30))  # print 70

"""
我找到的規律是這樣 
以三個數字為一組 第一組是(0,4,8) 第二組是(7,11,15) 第三組是(14,18,22) 第四組是(21,25,29) 
每組的第一個數是7*[i] 後面第二、第三個數分別+4 然後再用 extend 合成一個新的數列。

所以如果寫作程式碼的話 get_number(Number)

可以制定一個函式 list = [(0,4,8),(7,11,15),(14,18,22),(21,25,29)...] 
延續下去 Number/3，商數就是表示在第n組(n=index)、餘數就表示在第r個(r有0,1,2）。 . 
得出來的數字應該就是 7n+4r，並輸出 . 寫寫看
"""