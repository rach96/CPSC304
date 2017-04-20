drop table if exists member;
drop table if exists athlete;
drop table if exists customer2;
drop table if exists customer1;
DROP TABLE if EXISTS Equipment;
drop table if exists Equipment_checkIn_reserveOrcancel_return1;
drop table if exists employee;
drop table if exists Equipment_checkIn_reserveOrcancel_return2;
drop table if exists room1;
drop table if exists room2;
drop table if exists recordsTransactionHistory;
drop table if exists reservedRoom;
drop table if exists checkInRoom;
drop table if exists clean;
drop table if exists createOrUpdateAccount;

drop table if exists returnRooms;


create table if not exists customer2
    (cusName char(20) not null,
     cusPhoneNumber int null,
     cusBirthday text null,
     cusAddress char(20) null,
     primary key (cusName, cusPhoneNumber));

insert into customer2
    values('Henry Sze',6043269284,'1978/05/08', '12-321 Beautiful road, Vancouver');
insert into customer2
    values('John Wai',7788343845,'1967/08/08', '53-1345 Strong str., Vancouver');
insert into customer2
    values('Kelly Yeung',6042351345,'1988/11/06', '7234 Big House Road, Surrey');
insert into customer2
    values('Nick Mellon',7782349764,'1977/07/19', '874 Rich People Road, Surrey');
insert into customer2
    values('Mark Mitchel',6042453267,'1977/12/29', '235 Older Guy Str. Vancouver');

--  below are the athele informations:

 insert into customer2
     values('Rachel Sand', 7783652753, '1985/08/04', '324 Hungry road, Vancouver');
 insert into customer2
     values('Tiffany Pan', 6049863782, '1976/07/28', '234 Sushi Str, Surrey');
 insert into customer2
     values('Yoshi Yamamoto', 7786536286, '1980/09/10', '7624 Pancake Lane, Richmond');
 insert into customer2
     values('Andy Yeung', 6048592478, '1975/04/31', '234-2942 Blueberry Road, Vancouver');
 insert into customer2
     values('John Doe', 7789374052, '1980/05/25', '1245 East str, Vancouver');

--member:

INSERT INTO customer2
      VALUES ('Herb Derp', 6049873452, '1987/07/29', '135 Highberry Road, Vancouver');
INSERT INTO customer2
      VALUES ('Tiffany Lin', 6049818652, '1990/08/03', '532 Willow Lane, Surrey');
INSERT INTO customer2
      VALUES ('Rachel Hi', 6043597522, '1977/07/03', '972-123 GingerBread Road, Vancouver');
INSERT INTO customer2
      VALUES ('Andy Ball', 6049826738, '1985/09/09', '972-3435 Amber Drive, New Westminister');
INSERT INTO customer2
      VALUES ('Tim Fan', 6047489452, '1975/12/28', '2315 HighLand Ave, Vancouver');


create table if not exists customer1
     (cusID int not null,
     cusName char(20) null,
     cusPhoneNumber int null,
     UNIQUE (cusName,cusPhoneNumber) ON CONFLICT REPLACE,
     primary key (cusID),
     foreign key (cusName, cusPhoneNumber) REFERENCES customer2(cusName,cusPhoneNumber));

 insert into customer1
     values(12345,'Henry Sze',6043269284);
 insert into customer1
     values(22345,'John Wai',7788343845);
 insert into customer1
     values(32345,'Kelly Yeung',6042351345);
 insert into customer1
     values(42345,'Nick Mellon',7782349764);
 insert into customer1
     values(52345,'Mark Mitchel',6042453267);

--  below are the athele informations:
 insert into customer1
     values(129382, 'Rachel Sand', 7783652753);
 insert into customer1
     values(239483, 'Tiffany Pan', 6049863782);
 insert into customer1
     values(472839, 'Yoshi Yamamoto', 7786536286);
 insert into customer1
     values(123456, 'Andy Yeung', 6048592478);
 insert into customer1
     values(123457, 'John Doe', 7789374052);

--member:
  INSERT INTO customer1
      VALUES (654321, 'Herb Derp', 6049873452);
INSERT INTO customer1
      VALUES (392837, 'Tiffany Lin', 6049818652);
INSERT INTO customer1
      VALUES (654124, 'Rachel Hi', 6043597522);
INSERT INTO customer1
      VALUES (392764, 'Andy Ball', 6049826738);
INSERT INTO customer1
      VALUES (625678, 'Tim Fan', 6047489452);


create table if not exists athlete
    (athleteTeam char(20) not null,
     athleteID int not null,
     primary key (athleteID),
     foreign key (athleteID) references customer1(cusID)
     ON DELETE RESTRICT);

 insert into athlete
     values('Rangers',129382);
 insert into athlete
     values('Eagle',239483);
 insert into athlete
     values('Thunder',472839);
 insert into athlete
     values('Tuutuus',123456);
 insert into athlete
     values('Tuutuus',123457);

create table if not exists member
    (memberID int not null,
     memberRenewalTime text not null,
     memberType char(20) not null,
     primary key (memberID),
     foreign key (memberID) references customer1(cusID)
     ON DELETE CASCADE );

 insert into member
     values(654321,'2017/04/24', 'monthly');
 insert into member
     values(392837,'2017/04/25','week');
insert into member
     values(654124,'2018/05/12','yearly');
 insert into member
     values(392764,'2017/03/02','monthly');
insert into member
     values(625678,'2017/08/17','week');


create table if not exists Equipment_checkIn_reserveOrcancel_return1
    (EquipType char(20) not null,
     EquipRate double not null,
     EquipDamageFee double not null,
     primary key (EquipType),
     CHECK(EquipRate > 0 AND EquipRate < 100));

 insert into Equipment_checkIn_reserveOrcancel_return1
     values('TennisRacket', 10.00, 39.12);
 insert into Equipment_checkIn_reserveOrcancel_return1
     values('TennisBall', 3.00, 39.12);
 insert into Equipment_checkIn_reserveOrcancel_return1
     values('Basketball', 15.00, 30.25);
 insert into Equipment_checkIn_reserveOrcancel_return1
     values('Badminton', 10.00, 50.75);
 insert into Equipment_checkIn_reserveOrcancel_return1
     values('Ping Pong', 2.00, 5.25);

CREATE TABLE IF NOT EXISTS Equipment
    (EquipID int not null,
     EquipType char(20) not null,
     PRIMARY KEY (EquipID));

INSERT INTO Equipment
    VALUES (2355, 'TennisRacket');
INSERT INTO Equipment
    VALUES (2341, 'Basketball');
INSERT INTO Equipment
    VALUES (2563, 'Badminton');

create table if not exists Equipment_checkIn_reserveOrcancel_return2
    (EquipID int not null,
     EquipTIME int null,
     EquipType char(20) not null,
     EquipCustID int not null,
     primary key (EquipID, EquipCustID),
     FOREIGN KEY (EquipID) REFERENCES Equipment(EquipID),
     foreign key (EquipCustID) references customer1(cusID));

 insert into Equipment_checkIn_reserveOrcancel_return2
     values(2355, 8, 'TennisRacket', 129382);
insert into Equipment_checkIn_reserveOrcancel_return2
     values(2341, 9, 'Basketball', 129382);
 insert into Equipment_checkIn_reserveOrcancel_return2
     values(2341, 15, 'Basketball', 392764);
insert into Equipment_checkIn_reserveOrcancel_return2
     values(2563, 20,'Badminton', 129382);

insert into Equipment_checkIn_reserveOrcancel_return2
     values(2355, 10,'TennisRacket', 22345);
insert into Equipment_checkIn_reserveOrcancel_return2
     values(2341, 9,'Basketball', 42345);
insert into Equipment_checkIn_reserveOrcancel_return2
     values(2563, 13,'Badminton', 472839);
insert into Equipment_checkIn_reserveOrcancel_return2
     values(2563, 16,'Badminton', 625678);
insert into Equipment_checkIn_reserveOrcancel_return2
     values(2563, 17,'Badminton', 654124);

--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 12345);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 22345);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 32345);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 42345);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 52345);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 239483);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 472839);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 123456);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 123457);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 654321);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 392837);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 654124);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 392764);
--  insert into Equipment_checkIn_reserveOrcancel_return2
--      values(2563, 'Badminton', 625678);


create table if not exists room1
    (roomID int not null,
     roomType char(20),
     primary key (roomID));

INSERT INTO room1
    VALUES (8452, 'Large Gym Room');
INSERT INTO room1
    VALUES (8453, 'Small Gym Room');
INSERT INTO room1
    VALUES (8454, 'Basketball Room');
INSERT INTO room1
    VALUES (8455, 'Tennis Room');
INSERT INTO room1
    VALUES (8456, 'Large Gym Room');

create table if not exists room2
    (roomType char(20),
     roomRate double null,
     roomSlots int null,
     roomDamageFee double null,
     primary key (roomType),
    CHECK(roomRate > 0 AND roomRate < 100));

INSERT INTO room2
    VALUES ('Large Gym Room', 5.00, 15, 10.00);
INSERT INTO room2
    VALUES ('Small Gym Room', 5.00, 10, 10.00);
INSERT INTO room2
    VALUES ('Tennis Room', 7.00, 4, 20.00);
INSERT INTO room2
    VALUES ('Basketball Room', 5.00, 10, 20.00);
INSERT INTO room2
    VALUES ('Table Tennis Room', 2.00, 6, 20.00);

create table if not exists returnRooms
    (roomID int not null,
     customerID int not null,
     primary key (roomID, customerID),
     foreign key (roomID) references room1,
     foreign key (customerID) REFERENCES customer1);

INSERT INTO returnRooms
    VALUES (8452, 32345);
INSERT INTO returnRooms
    VALUES (8453, 12345);
INSERT INTO returnRooms
    VALUES (8454, 123456);
INSERT INTO returnRooms
    VALUES (8455, 22345);
INSERT INTO returnRooms
    VALUES (8456, 129382);


create table if not exists reservedRoom
    (roomID int not null,
     customerID int not null,
     time text NOT NULL,
     PRIMARY KEY (roomID,customerID),
     foreign key (roomID) references room1(roomID),
     foreign key (customerID) references customer1(cusID));

INSERT INTO reservedRoom
   VALUES (8452, 32345, 'Monday');
INSERT INTO reservedRoom
   VALUES (8453, 42345, 'Monday');
INSERT INTO reservedRoom
   VALUES (8454, 123456, 'Saturday');
INSERT INTO reservedRoom
   VALUES (8455, 22345, 'Sunday');
INSERT INTO reservedRoom
   VALUES (8456, 129382, 'Sunday');


--may nt need this table (no query)
create table if not exists checkInRoom
    (roomID int not null,
     customerID int not null,
     foreign key (roomID) references room1,
     foreign key (customerID) references customer1);


--may nt need this table(no query)
create table if not exists createOrUpdateAccount
    (customerID int not null,
     accountUsername char(20) null,
     accountPassword char(20) null,
     foreign key (customerID) references customer1);

--may nt need this table(no query)
create table if not exists recordsTransactionHistory
  (customerID int not null,
   accountUsername char(20) not null,
   THReason char(20) null,
   THDate text null,
   foreign key (accountUsername) references createOrUpdateAccount);



create table if not exists employee
    (employeeSSN int not null,
     employeeID int not null,
     employeeName char(20) null,
     employeeGender char(20) null,
     employeeBirthday text null,
     primary key (employeeID));

INSERT INTO employee
    VALUES (123984, 8147564912, 'Amy Tang', 'female', '1966/06/04');
INSERT INTO employee
    VALUES (1273462, 8147135912, 'Ralph Sui', 'male', '1984/06/12');
INSERT INTO employee
    VALUES (12743264, 8147346712, 'Robert King', 'male', '1977/09/20');
INSERT INTO employee
    VALUES (12472374, 8147564346, 'Nichol Smith', 'female', '1990/05/15');
INSERT INTO employee
    VALUES (1264264, 8147534667, 'Sean Mendez', 'male', '1979/07/09');


create table if not exists clean
    (RoomID int not null,
     CleanTime int null,
     employeeID int not null,
     primary key (RoomID, employeeID),
     foreign key (RoomID) references room1(roomID),
     foreign key (employeeID) REFERENCES employee(employeeID));


INSERT INTO clean
    VALUES (8452, 8, 8147564912);
INSERT INTO clean
    VALUES (8454, 10, 8147135912);
INSERT INTO clean
    VALUES (8453, 11, 8147346712);
INSERT INTO clean
    VALUES (8455, 8, 8147564346);
INSERT INTO clean
    VALUES (8456, 6, 8147534667);