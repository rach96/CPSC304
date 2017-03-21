create table customer1
    (cusID int not null,
     cusName char(20) null,
     cusPhoneNumber int null,
     primary key (cusID));

insert into customer1
    values('1234','Henry',9239203928);

create table customer2
    (cusName char(20) not null,
     cusPhoneNumber int null,
     cusBirthday text null,
     cusAddress char(20) null,
     primary key (cusName));

insert into customer2
    values('3928','Alice',9283784938);

create table athlete
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


create table member
    (memberID int not null,
     memberRenewalTime text not null,
     memberType char(20) not null,
     primary key (memberID),
     foreign key (memberID) references customer1);

insert into member
    values(654321,'03:23:49');
insert into athlete
    values(392837,'02:03:39');

create table Equipment_checkIn_reserveOrcancel_return1
    (EquipType char(20) not null,
     EquipRate double not null,
     EquipDamageFee double not null,
     primary key (EquipType));

insert into Equipment_checkIn_reserveOrcancel_return1
    values('TennisRacket', 30.20, 39.12);

insert into Equipment_checkIn_reserveOrcancel_return1
    values('TennisRacket', 30.20, 39.12);

create table Equipment_checkIn_reserveOrcancel_return2
    (EquipID int not null,
     EquipType char(20) not null,
     EquipCustID int not null,
     primary key (EquipID),
     foreign key (EquipCustID) references customer1);

create table room1
    (roomID int not null,
     roomType char(20),
     primary key (roomID));

create table room2
    (roomType char(20),
     roomRate int null,
     roomSlots int null,
     roomDamageFee int null,
     primary key (roomType));

create table returnRooms
    (roomID int not null,
     customerID int not null,
     roomType char(20),
     roomSlots int null,
     roomDamageFee int null,
     primary key (roomID),
     foreign key (roomID) references room1);

create table returnOrCancelRoom
    (roomID int not null,
     customerID int not null,
     roomType char(20),
     roomSlots int null,
     roomDamageFee int null,
     foreign key (roomID) references room1,
     foreign key (customerID) references customer1);

create table checkInRoom
    (roomID int not null,
     customerID int not null,
     foreign key (roomID) references room1,
     foreign key (customerID) references customer1);

create table createOrUpdateAccount
    (customerID int not null,
     accountUsername char(20) null,
     accountPassword char(20) null,
     foreign key (customerID) references customer1);

create table recordsTransactionHistory
  (customerID int not null,
   accountUsername char(20), null,
   THReason char(20), null,
   THDate text, NULL,
   foreign key (accountUsername) references createOrUpdateAccount);

create table employee
    (emmployeeSSN int not null,
     employeeName char(20) null,
     employeeGender char(20) null,
     employeeBirthday int null,
     primary key (employeeSSN));

create table clean
    (employeeRoomID int not null,
     employeeTime int null,
     employeeID int not null,
     primary key (employeeRoomID));

