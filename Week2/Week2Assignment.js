// Assignment1
function findAndPrint(messages, currentStation) {
    const mapDifference = {};

    for (const [name, msg] of Object.entries(messages)) {
        let distance = [];
        const listsToCheck = currentStation === "Xiaobitan" ? [list2, list3] : [list1, list2, list3];

        for (const sublist of listsToCheck) {
            if (sublist.includes(currentStation)) {
                const distances = sublist.filter(item => msg.includes(item)).map(item => Math.abs(sublist.indexOf(item) - sublist.indexOf(currentStation)));
                distance = distance.concat(distances);
            }
        }

        if (distance.length > 0) {
            mapDifference[name] = distance;
        }
    }

    const shortestDistance = Math.min(...Object.values(mapDifference).flat());
    const closestFriend = Object.keys(mapDifference).filter(key => mapDifference[key].includes(shortestDistance));

    console.log(closestFriend);
    return;
}

const messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
};

// 先分出三個線路
const list1 = ["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing",
    "Songjiang Nanjing","Zhongshan","Beimen","Ximen","Xiaonanmen",
    "Chiang Kai-Shek Memorial Hall","Guting","Taipower Building",
    "Guongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xindian City Hall","Xindian"
]; //main line

const list2 = ["Songshan","Nanjing Sanmin","Taipei Arena","Nanjing Fuxing","Songjiang Nanjing",
    "Zhongshan","Beimen","Ximen","Xiaonanmen","Chiang Kai-Shek Memorial Hall","Guting",
    "Taipower Building","Guongguan","Wanlong","Jingmei","Dapinglin","Qizhang","Xiaobitan"
]; //branch line-1

const list3 = ["Xiaobitan","Qizhang","Xindian City Hall","Xindian"]; //branch line-2

// Test cases
console.log("<Assignment1>");
findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian

//Assignment2
function book(consultants, hour, duration, criteria) {
    // Step 1: 確認所有顧問的BookedTime
    for (const consultant of consultants) {
        if (!consultant.hasOwnProperty("BookedTime")) {
            consultant["BookedTime"] = [];
        }
    }

    // Step 2: 判斷預定時間是否與現有預定重疊，並取出時間上可以的顧問
    let availableConsultants = []; // 預設目前沒有可以供預訂的顧問
    for (const consultant of consultants) {
        let isOverlap = false; // 預設一開始顧問的時間都沒有重疊
        for (const existingTime of consultant["BookedTime"]) {
            if (checkOverlap(existingTime, [hour, hour + duration])) {
                isOverlap = true;
                break; // 如果已經有查到重複的時間段，就跳出，不需要查完全部的時間段
            }
        }
        if (!isOverlap) {
            availableConsultants.push(consultant);
        }
    }

    // Step 3: 如果所有顧問時間都有重疊，輸出 "No Service" 後返回
    if (availableConsultants.length === 0) {
        console.log("No Service");
        return;
    }

    // Step 4 & 5: 根據 criteria 選擇最小或最大值
    let selectedConsultant;
    if (criteria === "price") {
        selectedConsultant = availableConsultants.reduce((min, curr) => (curr["price"] < min["price"]) ? curr : min);
    } else if (criteria === "rate") {
        selectedConsultant = availableConsultants.reduce((max, curr) => (curr["rate"] > max["rate"]) ? curr : max);
    }

    // print
    console.log(selectedConsultant["name"]);

    // Step 6: 將預定時間添加到所選顧問的 BookedTime 中
    selectedConsultant["BookedTime"].push([hour, hour + duration]);
    selectedConsultant["BookedTime"].sort((a, b) => a[0] - b[0]);
    // 合併相鄰的時間範圍
    for (let i = 0; i < selectedConsultant["BookedTime"].length - 1;) {
        if (selectedConsultant["BookedTime"][i][1] === selectedConsultant["BookedTime"][i + 1][0]) {
            selectedConsultant["BookedTime"][i] = [selectedConsultant["BookedTime"][i][0], selectedConsultant["BookedTime"][i + 1][1]];
            selectedConsultant["BookedTime"].splice(i + 1, 1);
        } else {
            i++;
        }
    }
}

// 檢查時間重疊的函式
function checkOverlap(existingTime, newTime) {
    return existingTime[0] < newTime[1] && existingTime[1] > newTime[0];
}

// 執行
const consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800}
];
console.log("");
console.log("<Assignment2>");
book(consultants, 15, 1, "price");  // Jenny
book(consultants, 11, 2, "price");  // Jenny
book(consultants, 10, 2, "price");  // John
book(consultants, 20, 2, "rate");   // John
book(consultants, 11, 1, "rate");   // Bob
book(consultants, 11, 2, "rate");   // No Service
book(consultants, 14, 3, "price");  // John

//Assignment3

function func(...data) {
    for (const name of data) {
        // 提取中間名
        let middleName = "";
        if (name.length === 2 || name.length === 3) {
            middleName = name[1];
        } else if (name.length === 4 || name.length === 5) {
            middleName = name[2];
        }

        // 檢查中間名是否唯一
        let unique = true;
        for (const otherName of data) {
            if (name !== otherName) {
                let otherMiddleName = "";
                if (otherName.length === 2 || otherName.length === 3) {
                    otherMiddleName = otherName[1];
                } else if (otherName.length === 4 || otherName.length === 5) {
                    otherMiddleName = otherName[2];
                }

                if (middleName === otherMiddleName) {
                    unique = false;
                    break;
                }
            }
        }

        // 如果中間名唯一就印出
        if (unique) {
            console.log(name);
            return;
        }
    }

    // 如果沒有唯一的中間名就印出"沒有"
    console.log("沒有");
}

// 測試
console.log("");
console.log("<Assignment3>");
func("彭大牆", "陳王明雅", "吳明");  // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花");  // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花");  // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆");  // print 夏曼藍波安

//Assignment4
function getNumber(n) {
    const groupIndex = Math.floor(n / 3); // 求商表示所在的組的索引
    const remainder = n % 3; // 求餘表示在組內的位置
    return 7 * groupIndex + 4 * remainder;
}

// 測試案例
console.log("");
console.log("<Assignment4>");
console.log(getNumber(1));   // print 4
console.log(getNumber(5));   // print 15
console.log(getNumber(10));  // print 25
console.log(getNumber(30));  // print 70
