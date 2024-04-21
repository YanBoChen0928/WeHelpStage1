import json
import csv

# 解析第一個 JSON 檔案

import urllib.request
import re #正則表達式
import json
import csv

#1-2 讀取文件
url1 = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1'
url2 = 'https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-2'


try:
    with urllib.request.urlopen(url1) as response:
        url1_data = json.loads(response.read().decode('utf-8'))
        print("Successfully loaded JSON data from URL1.")
except Exception as e:
    print("Error loading JSON data from URL1:", e)

try:
    with urllib.request.urlopen(url2) as response:
        url2_data = json.loads(response.read().decode('utf-8'))
        print("Successfully loaded JSON data from URL2.")
except Exception as e:
    print("Error loading JSON data from URL2:", e)


url1_results = url1_data["data"]["results"]

# 解析第二個 JSON 檔案
url2_results = url2_data["data"]

'''
巢狀迴圈寫法
# 將資料組織成想要的格式
grouped_data = {}

for item1 in url1_results:
    for item2 in url2_results:
        if item1["SERIAL_NO"] == item2["SERIAL_NO"]:
            if item2["MRT"] not in grouped_data:
                grouped_data[item2["MRT"]] = []
            grouped_data[item2["MRT"]].append(item1["stitle"])

'''
# 建立字典來存儲 url2_results 中的資料: MRT 的 seial no.
serial_to_mrt = {item["SERIAL_NO"]: item["MRT"] for item in url2_results}
 
# 建立字典來組織資料
grouped_data = {}
for item1 in url1_results:
    serial_no = item1["SERIAL_NO"]
    mrt = serial_to_mrt.get(serial_no)
    if mrt:
        if mrt not in grouped_data:
            grouped_data[mrt] = []
        grouped_data[mrt].append(item1["stitle"])


# 將組織好的資料輸出到 CSV 檔案中
with open('mrt.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['MRT', 'stitle']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    for MRT, stitles in grouped_data.items():
        writer.writerow({'MRT': MRT, 'stitle': ','.join(stitles)})


#建立 spot.csv，優先處理 district的問題
#用正則表達式去對比 Serial No. 取區

serial_to_district = {item["SERIAL_NO"]: re.search(r"(\S{2}區)", item["address"]).group(1) for item in url2_results}

rows = []
for item in url1_results: 
    #資料型態 {"data":{"limit":1000 ,"offset":0,"count":58,"sort":"","results":[{"info":"新北投）
    #表示取 my_data 是字典，取 ['data']key 中 ['results']key的value值
    spot_title = item.get('stitle', '')
    district = serial_to_district.get(item1["SERIAL_NO"], "")
    longitude = item.get('longitude', '')
    latitude = item.get('latitude', '')
    image_urls = item.get('filelist', '').split('https://')  # 根據URL的分隔符進行分割
    image_url = 'https://' + image_urls[1] if len(image_urls) > 1 else ''  # 選擇第一个URL作为ImageURL，因為https//分隔符前面沒有東西，所以image_urls[0]=''
    rows.append([spot_title, district, longitude, latitude, image_url])
#print(rows)

# 3 write
if __name__ == "__main__":
    with open('spot.csv', 'w', encoding='utf-8', newline=None) as file: #newline ="", None 有不同意思
        writer = csv.writer(file)
        #writer.writerow(['SpotTitle', 'District', 'Longitude', 'Latitude', 'ImageURL'])  # adding name row by row
        writer.writerows(rows)