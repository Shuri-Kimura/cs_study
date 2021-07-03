-- Keep a log of any SQL queries you execute as you solve the mystery.
--犯罪が起こった場所の確認
select * from crime_scene_reports;
--インタビューに情報アリ
select * from interviews;
--裁判所のセキュリティの10:15から10分以内に情報アリ
select * from courthouse_security_logs;

260 | 2020 | 7 | 28 | 10 | 16 | exit | 5P2BI95
261 | 2020 | 7 | 28 | 10 | 18 | exit | 94KL13X
262 | 2020 | 7 | 28 | 10 | 18 | exit | 6P58WS2
263 | 2020 | 7 | 28 | 10 | 19 | exit | 4328GD8
264 | 2020 | 7 | 28 | 10 | 20 | exit | G412CB7
265 | 2020 | 7 | 28 | 10 | 21 | exit | L93JTIZ
266 | 2020 | 7 | 28 | 10 | 23 | exit | 322W7JE
267 | 2020 | 7 | 28 | 10 | 23 | exit | 0NTHK55
268 | 2020 | 7 | 28 | 10 | 35 | exit | 1106N58

--列を確認
PRAGMA table_info(people);
--それぞれ、セキュリティで出てきた人を確認
SELECT * FROM people WHERE license_plate in ("5P2BI95","94KL13X","6P58WS2","4328GD8","G412CB7","L93JTIZ","322W7JE","0NTHK55","1106N58");
id | name | phone_number | passport_number | license_plate
221103 | Patrick | (725) 555-4692 | 2963008352 | 5P2BI95
243696 | Amber | (301) 555-4174 | 7526138472 | 6P58WS2
396669 | Elizabeth | (829) 555-5269 | 7049073643 | L93JTIZ
398010 | Roger | (130) 555-0289 | 1695452385 | G412CB7
449774 | Madison | (286) 555-6063 | 1988161715 | 1106N58
467400 | Danielle | (389) 555-5198 | 8496433585 | 4328GD8
514354 | Russell | (770) 555-1861 | 3592750733 | 322W7JE
560886 | Evelyn | (499) 555-9472 | 8294398571 | 0NTHK55
686048 | Ernest | (367) 555-5533 | 5773159633 | 94KL13X

--29日の飛行機、朝一番は
select * from flights WHERE day = 29;
id | origin_airport_id | destination_airport_id | year | month | day | hour | minute
36 | 8 | 4 | 2020 | 7 | 29 | 8 | 20

--列を確認
PRAGMA table_info(passengers);
--乗客に上記の奴らはいるか(id 36フライト)
SELECT * FROM passengers WHERE passport_number in ("2963008352","7526138472","7049073643","1695452385","1988161715","8496433585","3592750733","8294398571","5773159633");

36 | 1695452385 | 3B
36 | 5773159633 | 4A
36 | 8294398571 | 6C
36 | 1988161715 | 6D
36 | 8496433585 | 7B
人は
398010 | Roger | (130) 555-0289 | 1695452385 | G412CB7
686048 | Ernest | (367) 555-5533 | 5773159633 | 94KL13X
560886 | Evelyn | (499) 555-9472 | 8294398571 | 0NTHK55
449774 | Madison | (286) 555-6063 | 1988161715 | 1106N58
467400 | Danielle | (389) 555-5198 | 8496433585 | 4328GD8



SELECT * FROM atm_transactions WHERE atm_location = "Fifer Street" and day = 28 and transaction_type = "withdraw";
id | account_number | year | month | day | atm_location | transaction_type | amount
246 | 28500762 | 2020 | 7 | 28 | Fifer Street | withdraw | 48
264 | 28296815 | 2020 | 7 | 28 | Fifer Street | withdraw | 20
266 | 76054385 | 2020 | 7 | 28 | Fifer Street | withdraw | 60
267 | 49610011 | 2020 | 7 | 28 | Fifer Street | withdraw | 50
269 | 16153065 | 2020 | 7 | 28 | Fifer Street | withdraw | 80
288 | 25506511 | 2020 | 7 | 28 | Fifer Street | withdraw | 20
313 | 81061156 | 2020 | 7 | 28 | Fifer Street | withdraw | 30
336 | 26013199 | 2020 | 7 | 28 | Fifer Street | withdraw | 35

--人確認
SELECT * FROM bank_accounts WHERE account_number in (28500762, 28296815, 76054385, 49610011, 16153065, 25506511, 81061156, 26013199);
49610011 | 686048 | 2010
26013199 | 514354 | 2012
16153065 | 458378 | 2012
28296815 | 395717 | 2014
25506511 | 396669 | 2014
28500762 | 467400 | 2014
76054385 | 449774 | 2015
81061156 | 438727 | 2018

この三人の誰か
686048 | Ernest | (367) 555-5533 | 5773159633 | 94KL13X
449774 | Madison | (286) 555-6063 | 1988161715 | 1106N58
467400 | Danielle | (389) 555-5198 | 8496433585 | 4328GD8



--列を確認
PRAGMA table_info(phone_calls);
--共犯者に電話したと考え、電話番号検索（上記より飛行機を使っていないAmberはない）
SELECT * FROM phone_calls WHERE caller in ("(367) 555-5533", "(286) 555-6063", "(389) 555-5198") and day = 28;
id | caller | receiver | year | month | day | duration
233 | (367) 555-5533 | (375) 555-8161 | 2020 | 7 | 28 | 45
236 | (367) 555-5533 | (344) 555-9601 | 2020 | 7 | 28 | 120
245 | (367) 555-5533 | (022) 555-4052 | 2020 | 7 | 28 | 241
254 | (286) 555-6063 | (676) 555-6554 | 2020 | 7 | 28 | 43
284 | (286) 555-6063 | (310) 555-8568 | 2020 | 7 | 28 | 235
285 | (367) 555-5533 | (704) 555-5790 | 2020 | 7 | 28 | 75
1分未満
233 | (367) 555-5533 | (375) 555-8161 | 2020 | 7 | 28 | 45
254 | (286) 555-6063 | (676) 555-6554 | 2020 | 7 | 28 | 43


--共犯者の候補リスト
SELECT * FROM people WHERE phone_number in ("(375) 555-8161","(676) 555-6554");
id | name | phone_number | passport_number | license_plate
250277 | James | (676) 555-6554 | 2438825627 | Q13SVG6
864400 | Berthold | (375) 555-8161 |  | 4V16VO0

--場所
SELECT * FROM airports;
4 | LHR | Heathrow Airport | London