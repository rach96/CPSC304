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
     values('1234','Henry',9239203928);

create table if not exists customer2
    (cusName char(20) not null,
     cusPhoneNumber int null,
     cusBirthday text null,
     cusAddress char(20) null,
     primary key (cusName));

insert into customer2
    values('Alice',9283784938,'04:30:9382', 'MontgomeryLane');

create table if not exists athlete
    (athleteTeam char(20) not null,
     athleteID int not null,
     primary key (athleteID),
     foreign key (athleteID) references customer1);

 insert into athlete
     values('Rangers',129382);
 insert into athlete
     values('Rangers',239483);
 insert into athlete
     values('Rangers',472839);
 insert into athlete
     values('Tuutuus',123456);


create table if not exists member
    (memberID int not null,
     memberRenewalTime text not null,
     memberType char(20) not null,
     primary key (memberID),
     foreign key (memberID) references customer1);

 insert into member
     values(654321,'03:23:49','Party');
 insert into member
     values(392837,'02:03:39','Party');

create table if not exists Equipment_checkIn_reserveOrcancel_return1
    (EquipType char(20) not null,
     EquipRate double not null,
     EquipDamageFee double not null,
     primary key (EquipType));

 insert into Equipment_checkIn_reserveOrcancel_return1
     values('TennisRacket', 30.20, 39.12);

 insert into Equipment_checkIn_reserveOrcancel_return1
     values('TennisBall', 30.20, 39.12);

create table if not exists Equipment_checkIn_reserveOrcancel_return2
    (EquipID int not null,
     EquipType char(20) not null,
     EquipCustID int not null,
     primary key (EquipID),
     foreign key (EquipCustID) references customer1);

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

