### Task2
* Create a new database named website.
    ```sql=
    CREATE DATABASE website;
    ```
    ![螢幕快照 2024-05-04 上午7.34.48](https://hackmd.io/_uploads/B1mnElQf0.png)
* Create a new table named member, in the website database, designed as below:

    ```sql=
    CREATE TABLE `member` (
    id bigint AUTO_INCREMENT PRIMARY KEY UNIQUE COMMENT 'Unique ID',
    name varchar(255) NOT NULL COMMENT 'Name',
    username varchar(255) NOT NULL COMMENT 'Username',
    password varchar(255) NOT NULL COMMENT 'Password',
    follower_count int unsigned NOT NULL DEFAULT 0 COMMENT 'Follower Count',
    time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Signup Time'
    );
    ```
    ![task2-1](https://hackmd.io/_uploads/B1pqIlQfA.png)

<br/>

### Task3: SQL CRUD
* INSERT a new row to the member table where name, username and password must be set to test. INSERT additional 4 rows with arbitrary data.
    ```sql=
    INSERT INTO `member` (name, username, password)
    VALUES 
  ('test', 'test', 'test');
    ```
    ![task3-1](https://hackmd.io/_uploads/H1r9vlmGR.png)
    
    ```sql=
    INSERT INTO `member` (name, username, password)
    VALUES 
    ('Yanbo', 'ybchen', '1'),
    ('A', 'a', '2'),
    ('B', 'b', '3'),
    ('C', 'c', '4');
    ```
    ![task3-2](https://hackmd.io/_uploads/Bkr-_lmf0.png)

* SELECT all rows from the member table.
    ```sql=
    SELECT * FROM `member`;
    ```
    (上一張圖有一起印出結果了)
    
* SELECT all rows from the member table, in descending order of time.
    ```sql=
    SELECT * FROM `member` ORDER BY time DESC;
    ```
    ![task3-3](https://hackmd.io/_uploads/HJBHKgXMC.png)

* SELECT total 3 rows, second to fourth, from the member table, in descending order of time. Note: it does not mean SELECT rows where id are 2, 3, or 4.
    ```sql=
    SELECT * FROM `member` ORDER BY time DESC LIMIT 3 OFFSET 1;
    ```
    ![螢幕快照 2024-05-04 上午7.57.21](https://hackmd.io/_uploads/Byvxce7fC.png)

* SELECT rows where username equals to test.
    ```sql=
    SELECT * FROM `member` WHERE username = 'test';
    ```
    ![task3-5](https://hackmd.io/_uploads/H1iHcx7fA.png)

    
* SELECT rows where name includes the es keyword.
    ```sql=
    SELECT * FROM `member` WHERE name LIKE '%es%';
    ```
    這邊用 like 不用  ＝ 是因為模糊比對
    
    ![task3-6](https://hackmd.io/_uploads/r1Ko5l7GA.png)

* SELECT rows where both username and password equal to test.
    ```sql=
    SELECT * FROM `member` WHERE username = 'test' AND password = 'test';
    SELECT * FROM `memeber` WHERE (username, password) = ('test', 'test');
    ```
    ![task3-7](https://hackmd.io/_uploads/SJAHse7fA.png)

* UPDATE data in name column to test2 where username equals to test.
    ```sql=
    UPDATE `member` SET name = 'test2' WHERE username = 'test';
    ```
    ![task3-8](https://hackmd.io/_uploads/rkDm3lXzR.png)

<br/>

### Task4: SQL Aggregation Functions
* SELECT how many rows from the member table.
    ```sql=
    SELECT COUNT(*) AS row_count FROM `member`;
    SELECT COUNT(*) INTO row_count FROM `member`;
    ```
    有上面兩種語法，差別在於要不要儲存變數
    
    ![task4-1](https://hackmd.io/_uploads/HyUZDb7z0.png)

* SELECT the sum of follower_count of all the rows from the member table.
    
    接下來計算 follower 的總數，先設定值：
    ```sql=
    UPDATE `member`
    SET follower_count = 
    CASE name
        WHEN 'test2' THEN 1
        WHEN 'Yanbo' THEN 5
        WHEN 'A' THEN 10
        WHEN 'B' THEN 8
        WHEN 'C' THEN 7
    END;
    
    /* 上面因為之前我們有設定不為0, 但default0 如果確實有一個是0（也就是沒有改變，可以用以下語法：*/
    
    UPDATE `member`
    SET follower_count = 
    CASE name
        WHEN 'Yanbo' THEN 5
        WHEN 'A' THEN 10
        WHEN 'B' THEN 8
        WHEN 'C' THEN 7
        ELSE follower_count -- 如果沒有匹配到任何條件，保持原值
    END
    WHERE name IN ('test2', 'Yanbo', 'A', 'B', 'C');
    
    ```
    再來用 sum 語法來計算總數：
    ```sql=
    SELECT SUM(follower_count) AS total_followers FROM `member`;
    ```
    ![task4-2](https://hackmd.io/_uploads/r1p_cZmM0.png)

* SELECT the average of follower_count of all the rows from the member table.
    ```sql=
    SELECT AVG(follower_count) AS average_followers From `member`;
    ```
    ![task4-3](https://hackmd.io/_uploads/HJ9GsbXzC.png)

* SELECT the average of follower_count of the first 2 rows, in descending order of follower_count, from the member table.
    
    先按照follower_count降冪排序，之後計算前兩個平均
    ```sql=
    SELECT AVG(follower_count) AS average_followers
    FROM (
    SELECT follower_count
    FROM `member`
    ORDER BY follower_count DESC 
    LIMIT 2
    ) AS querycount;
    ```
    降冪排列取前兩項的結果
    
    ![task4-4](https://hackmd.io/_uploads/HyP4hWmfC.png)

    計算這兩項的平均值
    
    ![task4-5](https://hackmd.io/_uploads/S1ZPn-7GA.png)
<br/>

### Task5: SQL JOIN
* Create a new table named message, in the website database. designed as below:
    ```sql=
    CREATE TABLE `message` (
    id bigint AUTO_INCREMENT PRIMARY KEY UNIQUE COMMENT 'Unique ID',
    member_id bigint NOT NULL COMMENT 'Member ID for Message Sender',
    content varchar(255) NOT NULL COMMENT 'Content',
    like_count int unsigned NOT NULL COMMENT 'Password',
    follower_count int unsigned NOT NULL DEFAULT 0 COMMENT 'Like Count',
    time datetime NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Publish Time',
    FOREIGN KEY (member_id) REFERENCES `member`(id)
    );
    ```
    ![task5-1](https://hackmd.io/_uploads/B1tdgM7MR.png)

    
* SELECT all messages, including sender names. We have to JOIN the member table to get that.

    先 key 進一些值
    ```sql=
    -- 第一次插入
    INSERT INTO `message` (member_id, content, like_count)
    VALUES (1, 'You are Good!', 3);
    -- 第二次插入
    INSERT INTO `message` (member_id, content, like_count)
    VALUES (2, 'I don''t have the same opinion.', 2);
    -- 第三次插入
    INSERT INTO `message` (member_id, content, like_count)
    VALUES (3, 'lol lol lol lol lol', 12);
    -- 第四次插入
    INSERT INTO `message` (member_id, content, like_count)
    VALUES (4, 'pretty nice author and insightful words', 15);
    -- 第五次插入
    INSERT INTO `message` (member_id, content, like_count)
    VALUES (5, '...', 1);
    ```
    ![task5-2](https://hackmd.io/_uploads/r1aHWGXzC.png)

    ```sql=
    SELECT message.*, member.name 
    --這個排列順序決定 資料表的呈現順序
    FROM message
    JOIN `member` ON message.member_id = member.id;
    -- JOIN 同 INNER JOIN 前面有設定 member_id是message表單的 FK 對應到 member 表單的 id
    ```
    ![task5-3](https://hackmd.io/_uploads/HyQrzf7zR.png)

* SELECT all messages, including sender names, where sender username equals to test. We have to JOIN the member table to filter and get that.
    
    方法一：照上面按表操課
    ```sql=
    SELECT message.*, member.username
    FROM message
    JOIN `member` ON message.member_id = member.id
    WHERE member.username = 'test';
    ```
    ![task5-5.0](https://hackmd.io/_uploads/HkyHrfXGA.png)

    

    方法二：先成立一個新的表單，然後SELECT
    ```sql=
    CREATE TABLE joint_table AS
    SELECT message.*, member.username
    FROM message
    JOIN `member` ON message.member_id = member.id;
    
    SELECT * FROM joint_table WHERE member.username = 'test';
    ```
    ![task5-5](https://hackmd.io/_uploads/rJhHHz7MR.png)

    
* Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages where sender username equals to test.
    ```sql=
    SELECT AVG(joint_table.like_count) AS average_like_count
    FROM joint_table
    WHERE joint_table.username = 'test';
    ```
    ![task5-6](https://hackmd.io/_uploads/SyhlLMQf0.png)
    
    按老師題意的做法：
    ```sql=
    SELECT AVG(message.like_count) AS average_like_count
    FROM message
    JOIN `member` ON message.member_id = member_id
    WHERE member.username ='test';
    ```
    ![task5-7](https://hackmd.io/_uploads/r1-guzQfA.png)


* Use SELECT, SQL Aggregation Functions with JOIN statement, get the average like count of messages GROUP BY sender username.

    為了看出差別：再新增 id:4 的一個comment
    
    ```sql=
    INSERT INTO `message` (member_id, content, like_count)
    VALUES (4, 'excellent recommendation', 10);
    ```
    ![task5-8](https://hackmd.io/_uploads/BkpBufmG0.png)
    
    再用 group 去處理
    ```sql=
    SELECT member.username, AVG(message.like_count) AS Group_average_like_count
    FROM message
    JOIN `member` ON message.member_id = member.id
    GROUP BY member.username;
    ```
    ![task5-9](https://hackmd.io/_uploads/SkJn_MQGC.png)
    
    有注意到 username: b, 是兩個按讚數：(15 + 10 )/2 = 12.5 
