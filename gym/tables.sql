drop table if exists customer1;
drop table if exists customer2;
drop table if exists athlete;
drop table if exists Equipment_checkIn_reserveOrcancel_return1;
drop table if exists employee;
drop table if exists Equipment_checkIn_reserveOrcancel_return2;
drop table if exists room1;
drop table if exists room2;
drop table if exists recordsTransactionHistory;
drop table if exists returnOrCancelRoom;
drop table if exists checkInRoom;
drop table if exists clean;
drop table if exists createOrUpdateAccount;
drop table if exists member;

create table if not exists customer1
    (cusID int not null,
     cusName char(20) null,
     cusPhoneNumber int null,
     primary key (cusID));

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


-- need to populate information for member:




create table if not exists customer2
    (cusName char(20) not null,
     cusPhoneNumber int null,
     cusBirthday text null,
     cusAddress char(20) null,
     primary key (cusName));

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


--need to popular information for member:





create table if not exists athlete
    (athleteTeam char(20) not null,
     athleteID int not null,
     primary key (athleteID),
     foreign key (athleteID) references customer1);

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
     foreign key (memberID) references customer1);

 insert into member
     values(654321,'1978/04/24', 'monthly');
 insert into member
     values(392837,'1988/04/25','week');
insert into member
     values(654124,'1984/05/12','yearly');
 insert into member
     values(392764,'1977/03/02','monthly');
insert into member
     values(625678,'1990/08/17','week');


create table if not exists Equipment_checkIn_reserveOrcancel_return1
    (EquipType char(20) not null,
     EquipRate double not null,
     EquipDamageFee double not null,
     primary key (EquipType));

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

create table if not exists Equipment_checkIn_reserveOrcancel_return2
    (EquipID int not null,
     EquipType char(20) not null,
     EquipCustID int not null,
     primary key (EquipID),
     foreign key (EquipCustID) references customer1);

 insert into Equipment_checkIn_reserveOrcancel_return2
     values(2355, 'TennisRacket', 129382);
 insert into Equipment_checkIn_reserveOrcancel_return2
     values(5432, 'Badminton', 392837);
 insert into Equipment_checkIn_reserveOrcancel_return2
     values(3463, 'Ping Pong', 472839);
 insert into Equipment_checkIn_reserveOrcancel_return2
     values(2563, 'Badminton', 42345);
 insert into Equipment_checkIn_reserveOrcancel_return2
     values(7643, 'Ping Pong', 22345);

create table if not exists room1
    (roomID int not null,
     roomType char(20),
     primary key (roomID));

create table if not exists room2
    (roomType char(20),
     roomRate int null,
     roomSlots int null,
     roomDamageFee int null,
     primary key (roomType));

create table if not exists returnRooms
    (roomID int not null,
     customerID int not null,
     roomType char(20),
     roomSlots int null,
     roomDamageFee int null,
     primary key (roomID),
     foreign key (roomID) references room1);

create table if not exists returnOrCancelRoom
    (roomID int not null,
     customerID int not null,
     roomType char(20),
     roomSlots int null,
     roomDamageFee int null,
     foreign key (roomID) references room1,
     foreign key (customerID) references customer1);

create table if not exists checkInRoom
    (roomID int not null,
     customerID int not null,
     foreign key (roomID) references room1,
     foreign key (customerID) references customer1);

create table if not exists createOrUpdateAccount
    (customerID int not null,
     accountUsername char(20) null,
     accountPassword char(20) null,
     foreign key (customerID) references customer1);

create table if not exists recordsTransactionHistory
  (customerID int not null,
   accountUsername char(20) not null,
   THReason char(20) null,
   THDate text null,
   foreign key (accountUsername) references createOrUpdateAccount);

create table if not exists employee
    (employeeSSN int not null,
     employeeName char(20) null,
     employeeGender char(20) null,
     employeeBirthday int null,
     primary key (employeeSSN));

create table if not exists clean
    (employeeRoomID int not null,
     employeeTime int null,
     employeeID int not null,
     primary key (employeeRoomID));

