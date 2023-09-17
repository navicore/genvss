Vehicle Signal Specification Test Data Generator
===============

See https://covesa.github.io/vehicle_signal_specification

Generates data "inspired by" the spec - I've not confirmed compliance.  I'm
using this to test general purpose IOT data wrangling tools.

Install
--------

after cloning the repo...

```bash
python3 -m venv venv
source ./venv/bin/activate
```

Usage
--------

```bash
./genvss.py -h
```

```bash
usage: genvss.py [-h] -v VEHICLES -f FREQUENCY -d DURATION

Generate VSS conform test data in triples format.

options:
  -h, --help            show this help message and exit
  -v VEHICLES, --vehicles VEHICLES
                        Number of vehicles to simulate.
  -f FREQUENCY, --frequency FREQUENCY
                        Frequency of observations in minutes.
  -d DURATION, --duration DURATION
                        Duration from the first to the last observation in minutes.
```

Example
--------

```bash
./genvss.py -v 3 -f 10 -d 100  
```

```bash
Subject,Predicate,Object
a4402fd9-53b4-49b2-993a-502eb21ffe36,type,vehicle
a4402fd9-53b4-49b2-993a-502eb21ffe36,vehicle_id,0
a4402fd9-53b4-49b2-993a-502eb21ffe36,timestamp,2023-09-17 11:43:22
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_drivetrain,cadfb8ea-6295-4f21-a113-07ab1cdb02e5
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_chassis,3b939b06-80c1-4fc8-8a6e-c3c469df7dbc
cadfb8ea-6295-4f21-a113-07ab1cdb02e5,type,drivetrain
cadfb8ea-6295-4f21-a113-07ab1cdb02e5,fuel_level,74
cadfb8ea-6295-4f21-a113-07ab1cdb02e5,battery_level,31
cadfb8ea-6295-4f21-a113-07ab1cdb02e5,engine_temperature,107
3b939b06-80c1-4fc8-8a6e-c3c469df7dbc,type,chassis
3b939b06-80c1-4fc8-8a6e-c3c469df7dbc,speed,97
3b939b06-80c1-4fc8-8a6e-c3c469df7dbc,brake_status,False
a4402fd9-53b4-49b2-993a-502eb21ffe36,timestamp,2023-09-17 11:53:22
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_drivetrain,fa55282f-6967-4390-a487-34a242d39a9c
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_chassis,604cc378-4fa6-4dd2-a6f7-7f86a345f238
fa55282f-6967-4390-a487-34a242d39a9c,type,drivetrain
fa55282f-6967-4390-a487-34a242d39a9c,fuel_level,6
fa55282f-6967-4390-a487-34a242d39a9c,battery_level,92
fa55282f-6967-4390-a487-34a242d39a9c,engine_temperature,83
604cc378-4fa6-4dd2-a6f7-7f86a345f238,type,chassis
604cc378-4fa6-4dd2-a6f7-7f86a345f238,speed,29
604cc378-4fa6-4dd2-a6f7-7f86a345f238,brake_status,False
a4402fd9-53b4-49b2-993a-502eb21ffe36,timestamp,2023-09-17 12:03:22
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_drivetrain,4655fc69-039d-4523-aa92-094bd93d25f2
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_chassis,f68b42e4-109b-4486-82d6-5f479db98493
4655fc69-039d-4523-aa92-094bd93d25f2,type,drivetrain
4655fc69-039d-4523-aa92-094bd93d25f2,fuel_level,100
4655fc69-039d-4523-aa92-094bd93d25f2,battery_level,29
4655fc69-039d-4523-aa92-094bd93d25f2,engine_temperature,96
f68b42e4-109b-4486-82d6-5f479db98493,type,chassis
f68b42e4-109b-4486-82d6-5f479db98493,speed,2
f68b42e4-109b-4486-82d6-5f479db98493,brake_status,False
a4402fd9-53b4-49b2-993a-502eb21ffe36,timestamp,2023-09-17 12:13:22
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_drivetrain,5f3bff9f-44c7-469c-92c7-1c8b16e68437
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_chassis,c39d69a2-bfda-4267-a042-4715fbffccf8
5f3bff9f-44c7-469c-92c7-1c8b16e68437,type,drivetrain
5f3bff9f-44c7-469c-92c7-1c8b16e68437,fuel_level,54
5f3bff9f-44c7-469c-92c7-1c8b16e68437,battery_level,81
5f3bff9f-44c7-469c-92c7-1c8b16e68437,engine_temperature,118
c39d69a2-bfda-4267-a042-4715fbffccf8,type,chassis
c39d69a2-bfda-4267-a042-4715fbffccf8,speed,89
c39d69a2-bfda-4267-a042-4715fbffccf8,brake_status,False
a4402fd9-53b4-49b2-993a-502eb21ffe36,timestamp,2023-09-17 12:23:22
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_drivetrain,7a2a9335-5c1c-4df4-a720-86231f578eb7
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_chassis,91c1dcca-3884-4d01-a22d-9931713af1e6
7a2a9335-5c1c-4df4-a720-86231f578eb7,type,drivetrain
7a2a9335-5c1c-4df4-a720-86231f578eb7,fuel_level,22
7a2a9335-5c1c-4df4-a720-86231f578eb7,battery_level,68
7a2a9335-5c1c-4df4-a720-86231f578eb7,engine_temperature,81
91c1dcca-3884-4d01-a22d-9931713af1e6,type,chassis
91c1dcca-3884-4d01-a22d-9931713af1e6,speed,59
91c1dcca-3884-4d01-a22d-9931713af1e6,brake_status,True
a4402fd9-53b4-49b2-993a-502eb21ffe36,timestamp,2023-09-17 12:33:22
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_drivetrain,e2639c19-97d0-49a3-8292-7153912d8c7c
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_chassis,f1ca92ad-c039-41ad-9389-f4247db07991
e2639c19-97d0-49a3-8292-7153912d8c7c,type,drivetrain
e2639c19-97d0-49a3-8292-7153912d8c7c,fuel_level,57
e2639c19-97d0-49a3-8292-7153912d8c7c,battery_level,77
e2639c19-97d0-49a3-8292-7153912d8c7c,engine_temperature,80
f1ca92ad-c039-41ad-9389-f4247db07991,type,chassis
f1ca92ad-c039-41ad-9389-f4247db07991,speed,49
f1ca92ad-c039-41ad-9389-f4247db07991,brake_status,False
a4402fd9-53b4-49b2-993a-502eb21ffe36,timestamp,2023-09-17 12:43:22
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_drivetrain,6cd3ca75-0c51-4c98-9f1c-c860d796d7d8
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_chassis,7285d5f3-2ddc-432b-870e-fb3d3a1f405a
6cd3ca75-0c51-4c98-9f1c-c860d796d7d8,type,drivetrain
6cd3ca75-0c51-4c98-9f1c-c860d796d7d8,fuel_level,58
6cd3ca75-0c51-4c98-9f1c-c860d796d7d8,battery_level,17
6cd3ca75-0c51-4c98-9f1c-c860d796d7d8,engine_temperature,113
7285d5f3-2ddc-432b-870e-fb3d3a1f405a,type,chassis
7285d5f3-2ddc-432b-870e-fb3d3a1f405a,speed,85
7285d5f3-2ddc-432b-870e-fb3d3a1f405a,brake_status,True
a4402fd9-53b4-49b2-993a-502eb21ffe36,timestamp,2023-09-17 12:53:22
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_drivetrain,02d514ed-f9c7-4148-9100-9280b32a0274
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_chassis,b6f72d93-17f4-4579-9ad3-2db885445ea8
02d514ed-f9c7-4148-9100-9280b32a0274,type,drivetrain
02d514ed-f9c7-4148-9100-9280b32a0274,fuel_level,84
02d514ed-f9c7-4148-9100-9280b32a0274,battery_level,84
02d514ed-f9c7-4148-9100-9280b32a0274,engine_temperature,106
b6f72d93-17f4-4579-9ad3-2db885445ea8,type,chassis
b6f72d93-17f4-4579-9ad3-2db885445ea8,speed,79
b6f72d93-17f4-4579-9ad3-2db885445ea8,brake_status,True
a4402fd9-53b4-49b2-993a-502eb21ffe36,timestamp,2023-09-17 13:03:22
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_drivetrain,01e896e9-0402-4f5a-9697-20d0936f8f5b
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_chassis,2f684d89-b4a4-4f0e-8ee6-54c7ed1b6680
01e896e9-0402-4f5a-9697-20d0936f8f5b,type,drivetrain
01e896e9-0402-4f5a-9697-20d0936f8f5b,fuel_level,55
01e896e9-0402-4f5a-9697-20d0936f8f5b,battery_level,79
01e896e9-0402-4f5a-9697-20d0936f8f5b,engine_temperature,96
2f684d89-b4a4-4f0e-8ee6-54c7ed1b6680,type,chassis
2f684d89-b4a4-4f0e-8ee6-54c7ed1b6680,speed,67
2f684d89-b4a4-4f0e-8ee6-54c7ed1b6680,brake_status,False
a4402fd9-53b4-49b2-993a-502eb21ffe36,timestamp,2023-09-17 13:13:22
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_drivetrain,1387b946-9b50-4ce2-91b9-93466191a088
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_chassis,1cd264e2-b504-472f-9220-488ed6625aae
1387b946-9b50-4ce2-91b9-93466191a088,type,drivetrain
1387b946-9b50-4ce2-91b9-93466191a088,fuel_level,15
1387b946-9b50-4ce2-91b9-93466191a088,battery_level,51
1387b946-9b50-4ce2-91b9-93466191a088,engine_temperature,93
1cd264e2-b504-472f-9220-488ed6625aae,type,chassis
1cd264e2-b504-472f-9220-488ed6625aae,speed,65
1cd264e2-b504-472f-9220-488ed6625aae,brake_status,True
a4402fd9-53b4-49b2-993a-502eb21ffe36,timestamp,2023-09-17 13:23:22
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_drivetrain,bcda99be-b79c-4f61-99e1-e32ccf7ebd28
a4402fd9-53b4-49b2-993a-502eb21ffe36,has_chassis,6d6bbac8-e6c6-4ad3-afef-4d26a58a28a6
bcda99be-b79c-4f61-99e1-e32ccf7ebd28,type,drivetrain
bcda99be-b79c-4f61-99e1-e32ccf7ebd28,fuel_level,92
bcda99be-b79c-4f61-99e1-e32ccf7ebd28,battery_level,14
bcda99be-b79c-4f61-99e1-e32ccf7ebd28,engine_temperature,109
6d6bbac8-e6c6-4ad3-afef-4d26a58a28a6,type,chassis
6d6bbac8-e6c6-4ad3-afef-4d26a58a28a6,speed,4
6d6bbac8-e6c6-4ad3-afef-4d26a58a28a6,brake_status,True
94d9039f-1bb3-4a35-803d-c5823c41c351,type,vehicle
94d9039f-1bb3-4a35-803d-c5823c41c351,vehicle_id,1
94d9039f-1bb3-4a35-803d-c5823c41c351,timestamp,2023-09-17 11:43:22
94d9039f-1bb3-4a35-803d-c5823c41c351,has_drivetrain,29387484-f554-4735-a87b-fb969912690b
94d9039f-1bb3-4a35-803d-c5823c41c351,has_chassis,0f454e03-0dfd-49c6-9acc-8d7dcd3ce38b
29387484-f554-4735-a87b-fb969912690b,type,drivetrain
29387484-f554-4735-a87b-fb969912690b,fuel_level,49
29387484-f554-4735-a87b-fb969912690b,battery_level,18
29387484-f554-4735-a87b-fb969912690b,engine_temperature,102
0f454e03-0dfd-49c6-9acc-8d7dcd3ce38b,type,chassis
0f454e03-0dfd-49c6-9acc-8d7dcd3ce38b,speed,16
0f454e03-0dfd-49c6-9acc-8d7dcd3ce38b,brake_status,True
94d9039f-1bb3-4a35-803d-c5823c41c351,timestamp,2023-09-17 11:53:22
94d9039f-1bb3-4a35-803d-c5823c41c351,has_drivetrain,3a988811-5fe3-4852-9ba6-4d45bb4ed05e
94d9039f-1bb3-4a35-803d-c5823c41c351,has_chassis,4e02e395-c0a8-4401-956c-f110e78de154
3a988811-5fe3-4852-9ba6-4d45bb4ed05e,type,drivetrain
3a988811-5fe3-4852-9ba6-4d45bb4ed05e,fuel_level,3
3a988811-5fe3-4852-9ba6-4d45bb4ed05e,battery_level,4
3a988811-5fe3-4852-9ba6-4d45bb4ed05e,engine_temperature,97
4e02e395-c0a8-4401-956c-f110e78de154,type,chassis
4e02e395-c0a8-4401-956c-f110e78de154,speed,81
4e02e395-c0a8-4401-956c-f110e78de154,brake_status,True
94d9039f-1bb3-4a35-803d-c5823c41c351,timestamp,2023-09-17 12:03:22
94d9039f-1bb3-4a35-803d-c5823c41c351,has_drivetrain,ebf095d7-01db-4293-ad84-846ae86cabcb
94d9039f-1bb3-4a35-803d-c5823c41c351,has_chassis,69a95a5e-8d74-4fcf-b1f6-a4c5d9001d01
ebf095d7-01db-4293-ad84-846ae86cabcb,type,drivetrain
ebf095d7-01db-4293-ad84-846ae86cabcb,fuel_level,13
ebf095d7-01db-4293-ad84-846ae86cabcb,battery_level,56
ebf095d7-01db-4293-ad84-846ae86cabcb,engine_temperature,119
69a95a5e-8d74-4fcf-b1f6-a4c5d9001d01,type,chassis
69a95a5e-8d74-4fcf-b1f6-a4c5d9001d01,speed,61
69a95a5e-8d74-4fcf-b1f6-a4c5d9001d01,brake_status,False
94d9039f-1bb3-4a35-803d-c5823c41c351,timestamp,2023-09-17 12:13:22
94d9039f-1bb3-4a35-803d-c5823c41c351,has_drivetrain,3b351401-0832-43fc-9b67-26ee51d2ec2e
94d9039f-1bb3-4a35-803d-c5823c41c351,has_chassis,776f2062-8741-4548-9c81-a0551378b7d2
3b351401-0832-43fc-9b67-26ee51d2ec2e,type,drivetrain
3b351401-0832-43fc-9b67-26ee51d2ec2e,fuel_level,2
3b351401-0832-43fc-9b67-26ee51d2ec2e,battery_level,100
3b351401-0832-43fc-9b67-26ee51d2ec2e,engine_temperature,107
776f2062-8741-4548-9c81-a0551378b7d2,type,chassis
776f2062-8741-4548-9c81-a0551378b7d2,speed,79
776f2062-8741-4548-9c81-a0551378b7d2,brake_status,True
94d9039f-1bb3-4a35-803d-c5823c41c351,timestamp,2023-09-17 12:23:22
94d9039f-1bb3-4a35-803d-c5823c41c351,has_drivetrain,97dc9622-476c-405a-8159-94fc47d54ed3
94d9039f-1bb3-4a35-803d-c5823c41c351,has_chassis,0de1ea87-e81f-48b0-be77-066df9bac670
97dc9622-476c-405a-8159-94fc47d54ed3,type,drivetrain
97dc9622-476c-405a-8159-94fc47d54ed3,fuel_level,7
97dc9622-476c-405a-8159-94fc47d54ed3,battery_level,79
97dc9622-476c-405a-8159-94fc47d54ed3,engine_temperature,89
0de1ea87-e81f-48b0-be77-066df9bac670,type,chassis
0de1ea87-e81f-48b0-be77-066df9bac670,speed,56
0de1ea87-e81f-48b0-be77-066df9bac670,brake_status,False
94d9039f-1bb3-4a35-803d-c5823c41c351,timestamp,2023-09-17 12:33:22
94d9039f-1bb3-4a35-803d-c5823c41c351,has_drivetrain,f798f053-d9e4-4659-b8d2-622d1d5e1c0d
94d9039f-1bb3-4a35-803d-c5823c41c351,has_chassis,8220aaac-a2e4-4e52-b258-272b7a6c4c5e
f798f053-d9e4-4659-b8d2-622d1d5e1c0d,type,drivetrain
f798f053-d9e4-4659-b8d2-622d1d5e1c0d,fuel_level,89
f798f053-d9e4-4659-b8d2-622d1d5e1c0d,battery_level,33
f798f053-d9e4-4659-b8d2-622d1d5e1c0d,engine_temperature,120
8220aaac-a2e4-4e52-b258-272b7a6c4c5e,type,chassis
8220aaac-a2e4-4e52-b258-272b7a6c4c5e,speed,50
8220aaac-a2e4-4e52-b258-272b7a6c4c5e,brake_status,False
94d9039f-1bb3-4a35-803d-c5823c41c351,timestamp,2023-09-17 12:43:22
94d9039f-1bb3-4a35-803d-c5823c41c351,has_drivetrain,069f2469-f31c-41d6-9128-91253e13fad3
94d9039f-1bb3-4a35-803d-c5823c41c351,has_chassis,e63842f2-de8f-4cda-86e4-a70ed7ed4455
069f2469-f31c-41d6-9128-91253e13fad3,type,drivetrain
069f2469-f31c-41d6-9128-91253e13fad3,fuel_level,96
069f2469-f31c-41d6-9128-91253e13fad3,battery_level,78
069f2469-f31c-41d6-9128-91253e13fad3,engine_temperature,107
e63842f2-de8f-4cda-86e4-a70ed7ed4455,type,chassis
e63842f2-de8f-4cda-86e4-a70ed7ed4455,speed,85
e63842f2-de8f-4cda-86e4-a70ed7ed4455,brake_status,True
94d9039f-1bb3-4a35-803d-c5823c41c351,timestamp,2023-09-17 12:53:22
94d9039f-1bb3-4a35-803d-c5823c41c351,has_drivetrain,34d5a568-bab8-44cd-9791-562f9275d1cf
94d9039f-1bb3-4a35-803d-c5823c41c351,has_chassis,f8f84fa1-34a9-40b0-b098-100756db9b80
34d5a568-bab8-44cd-9791-562f9275d1cf,type,drivetrain
34d5a568-bab8-44cd-9791-562f9275d1cf,fuel_level,35
34d5a568-bab8-44cd-9791-562f9275d1cf,battery_level,100
34d5a568-bab8-44cd-9791-562f9275d1cf,engine_temperature,96
f8f84fa1-34a9-40b0-b098-100756db9b80,type,chassis
f8f84fa1-34a9-40b0-b098-100756db9b80,speed,17
f8f84fa1-34a9-40b0-b098-100756db9b80,brake_status,False
94d9039f-1bb3-4a35-803d-c5823c41c351,timestamp,2023-09-17 13:03:22
94d9039f-1bb3-4a35-803d-c5823c41c351,has_drivetrain,7ea85e5e-42d7-4cbb-a8fc-9d093bcbdd31
94d9039f-1bb3-4a35-803d-c5823c41c351,has_chassis,c502863d-60fd-4d7c-ad94-0e48c65e27bb
7ea85e5e-42d7-4cbb-a8fc-9d093bcbdd31,type,drivetrain
7ea85e5e-42d7-4cbb-a8fc-9d093bcbdd31,fuel_level,80
7ea85e5e-42d7-4cbb-a8fc-9d093bcbdd31,battery_level,100
7ea85e5e-42d7-4cbb-a8fc-9d093bcbdd31,engine_temperature,119
c502863d-60fd-4d7c-ad94-0e48c65e27bb,type,chassis
c502863d-60fd-4d7c-ad94-0e48c65e27bb,speed,61
c502863d-60fd-4d7c-ad94-0e48c65e27bb,brake_status,False
94d9039f-1bb3-4a35-803d-c5823c41c351,timestamp,2023-09-17 13:13:22
94d9039f-1bb3-4a35-803d-c5823c41c351,has_drivetrain,f4f526f0-7fcb-4d83-b5a0-acfeb5d1cb32
94d9039f-1bb3-4a35-803d-c5823c41c351,has_chassis,c05ad015-4d65-4e67-b4ef-05b98567a5ef
f4f526f0-7fcb-4d83-b5a0-acfeb5d1cb32,type,drivetrain
f4f526f0-7fcb-4d83-b5a0-acfeb5d1cb32,fuel_level,85
f4f526f0-7fcb-4d83-b5a0-acfeb5d1cb32,battery_level,99
f4f526f0-7fcb-4d83-b5a0-acfeb5d1cb32,engine_temperature,96
c05ad015-4d65-4e67-b4ef-05b98567a5ef,type,chassis
c05ad015-4d65-4e67-b4ef-05b98567a5ef,speed,63
c05ad015-4d65-4e67-b4ef-05b98567a5ef,brake_status,True
94d9039f-1bb3-4a35-803d-c5823c41c351,timestamp,2023-09-17 13:23:22
94d9039f-1bb3-4a35-803d-c5823c41c351,has_drivetrain,093102ce-7f65-48d0-87d8-cfe40fbf08de
94d9039f-1bb3-4a35-803d-c5823c41c351,has_chassis,f8a12745-2a78-42e2-bf33-d8b053bf2ca6
093102ce-7f65-48d0-87d8-cfe40fbf08de,type,drivetrain
093102ce-7f65-48d0-87d8-cfe40fbf08de,fuel_level,79
093102ce-7f65-48d0-87d8-cfe40fbf08de,battery_level,28
093102ce-7f65-48d0-87d8-cfe40fbf08de,engine_temperature,101
f8a12745-2a78-42e2-bf33-d8b053bf2ca6,type,chassis
f8a12745-2a78-42e2-bf33-d8b053bf2ca6,speed,107
f8a12745-2a78-42e2-bf33-d8b053bf2ca6,brake_status,True
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,type,vehicle
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,vehicle_id,2
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,timestamp,2023-09-17 11:43:22
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_drivetrain,394c3b85-1f4a-457a-83bc-5d343a7ece08
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_chassis,75a03070-04c6-4a9c-9481-f33fee5c6cfc
394c3b85-1f4a-457a-83bc-5d343a7ece08,type,drivetrain
394c3b85-1f4a-457a-83bc-5d343a7ece08,fuel_level,92
394c3b85-1f4a-457a-83bc-5d343a7ece08,battery_level,52
394c3b85-1f4a-457a-83bc-5d343a7ece08,engine_temperature,84
75a03070-04c6-4a9c-9481-f33fee5c6cfc,type,chassis
75a03070-04c6-4a9c-9481-f33fee5c6cfc,speed,117
75a03070-04c6-4a9c-9481-f33fee5c6cfc,brake_status,True
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,timestamp,2023-09-17 11:53:22
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_drivetrain,5728b942-bac8-4704-b623-eb1e98247e44
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_chassis,cdd286ab-997f-437e-b32f-0822d94be58e
5728b942-bac8-4704-b623-eb1e98247e44,type,drivetrain
5728b942-bac8-4704-b623-eb1e98247e44,fuel_level,78
5728b942-bac8-4704-b623-eb1e98247e44,battery_level,52
5728b942-bac8-4704-b623-eb1e98247e44,engine_temperature,98
cdd286ab-997f-437e-b32f-0822d94be58e,type,chassis
cdd286ab-997f-437e-b32f-0822d94be58e,speed,33
cdd286ab-997f-437e-b32f-0822d94be58e,brake_status,False
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,timestamp,2023-09-17 12:03:22
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_drivetrain,b5e847bb-f755-4826-8d5d-4f7d34d8b5c3
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_chassis,a0454f53-9f22-49d4-ad96-cb664bcc22fd
b5e847bb-f755-4826-8d5d-4f7d34d8b5c3,type,drivetrain
b5e847bb-f755-4826-8d5d-4f7d34d8b5c3,fuel_level,53
b5e847bb-f755-4826-8d5d-4f7d34d8b5c3,battery_level,2
b5e847bb-f755-4826-8d5d-4f7d34d8b5c3,engine_temperature,92
a0454f53-9f22-49d4-ad96-cb664bcc22fd,type,chassis
a0454f53-9f22-49d4-ad96-cb664bcc22fd,speed,26
a0454f53-9f22-49d4-ad96-cb664bcc22fd,brake_status,False
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,timestamp,2023-09-17 12:13:22
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_drivetrain,b9a4137a-5328-4e44-8f30-4cc4694394d9
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_chassis,5b32fadb-0c90-46ce-8eb3-0755591fab9c
b9a4137a-5328-4e44-8f30-4cc4694394d9,type,drivetrain
b9a4137a-5328-4e44-8f30-4cc4694394d9,fuel_level,21
b9a4137a-5328-4e44-8f30-4cc4694394d9,battery_level,72
b9a4137a-5328-4e44-8f30-4cc4694394d9,engine_temperature,112
5b32fadb-0c90-46ce-8eb3-0755591fab9c,type,chassis
5b32fadb-0c90-46ce-8eb3-0755591fab9c,speed,62
5b32fadb-0c90-46ce-8eb3-0755591fab9c,brake_status,True
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,timestamp,2023-09-17 12:23:22
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_drivetrain,42083192-41de-4828-b5c7-c608159495e9
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_chassis,8fc8f8bc-9fa6-42fc-a338-ec68c8c6c0c4
42083192-41de-4828-b5c7-c608159495e9,type,drivetrain
42083192-41de-4828-b5c7-c608159495e9,fuel_level,48
42083192-41de-4828-b5c7-c608159495e9,battery_level,46
42083192-41de-4828-b5c7-c608159495e9,engine_temperature,118
8fc8f8bc-9fa6-42fc-a338-ec68c8c6c0c4,type,chassis
8fc8f8bc-9fa6-42fc-a338-ec68c8c6c0c4,speed,84
8fc8f8bc-9fa6-42fc-a338-ec68c8c6c0c4,brake_status,True
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,timestamp,2023-09-17 12:33:22
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_drivetrain,4655489c-81a1-409c-8bef-ac961c9d30bb
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_chassis,ec121d33-7831-4e37-ad98-91e90a0a5b94
4655489c-81a1-409c-8bef-ac961c9d30bb,type,drivetrain
4655489c-81a1-409c-8bef-ac961c9d30bb,fuel_level,58
4655489c-81a1-409c-8bef-ac961c9d30bb,battery_level,45
4655489c-81a1-409c-8bef-ac961c9d30bb,engine_temperature,90
ec121d33-7831-4e37-ad98-91e90a0a5b94,type,chassis
ec121d33-7831-4e37-ad98-91e90a0a5b94,speed,104
ec121d33-7831-4e37-ad98-91e90a0a5b94,brake_status,True
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,timestamp,2023-09-17 12:43:22
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_drivetrain,addfe497-be65-4c7f-a1be-ddb037c76a92
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_chassis,66f5c556-4747-4ba7-859a-6e32cdeecfe7
addfe497-be65-4c7f-a1be-ddb037c76a92,type,drivetrain
addfe497-be65-4c7f-a1be-ddb037c76a92,fuel_level,26
addfe497-be65-4c7f-a1be-ddb037c76a92,battery_level,98
addfe497-be65-4c7f-a1be-ddb037c76a92,engine_temperature,91
66f5c556-4747-4ba7-859a-6e32cdeecfe7,type,chassis
66f5c556-4747-4ba7-859a-6e32cdeecfe7,speed,5
66f5c556-4747-4ba7-859a-6e32cdeecfe7,brake_status,True
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,timestamp,2023-09-17 12:53:22
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_drivetrain,1dd41ef4-cdf7-42d6-81ab-73fe990bf0fe
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_chassis,b9826eee-988a-48ee-9c92-f9f4604f3c17
1dd41ef4-cdf7-42d6-81ab-73fe990bf0fe,type,drivetrain
1dd41ef4-cdf7-42d6-81ab-73fe990bf0fe,fuel_level,4
1dd41ef4-cdf7-42d6-81ab-73fe990bf0fe,battery_level,45
1dd41ef4-cdf7-42d6-81ab-73fe990bf0fe,engine_temperature,117
b9826eee-988a-48ee-9c92-f9f4604f3c17,type,chassis
b9826eee-988a-48ee-9c92-f9f4604f3c17,speed,63
b9826eee-988a-48ee-9c92-f9f4604f3c17,brake_status,False
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,timestamp,2023-09-17 13:03:22
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_drivetrain,59aae361-6504-401c-b948-89965bd340fb
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_chassis,2e456379-85ff-443a-9cf8-ce6bcc0ae699
59aae361-6504-401c-b948-89965bd340fb,type,drivetrain
59aae361-6504-401c-b948-89965bd340fb,fuel_level,31
59aae361-6504-401c-b948-89965bd340fb,battery_level,26
59aae361-6504-401c-b948-89965bd340fb,engine_temperature,87
2e456379-85ff-443a-9cf8-ce6bcc0ae699,type,chassis
2e456379-85ff-443a-9cf8-ce6bcc0ae699,speed,114
2e456379-85ff-443a-9cf8-ce6bcc0ae699,brake_status,False
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,timestamp,2023-09-17 13:13:22
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_drivetrain,74adc39c-6952-45af-b318-488fe1ead760
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_chassis,6ec21426-f3d4-421c-b142-b5687686c841
74adc39c-6952-45af-b318-488fe1ead760,type,drivetrain
74adc39c-6952-45af-b318-488fe1ead760,fuel_level,17
74adc39c-6952-45af-b318-488fe1ead760,battery_level,47
74adc39c-6952-45af-b318-488fe1ead760,engine_temperature,84
6ec21426-f3d4-421c-b142-b5687686c841,type,chassis
6ec21426-f3d4-421c-b142-b5687686c841,speed,89
6ec21426-f3d4-421c-b142-b5687686c841,brake_status,True
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,timestamp,2023-09-17 13:23:22
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_drivetrain,6754befd-36c4-4555-a8b6-d514f1c7d656
a8106416-0ea8-42b1-bf28-a0bc44d2ff18,has_chassis,1ea6e00d-5609-4697-97a4-4809b9322463
6754befd-36c4-4555-a8b6-d514f1c7d656,type,drivetrain
6754befd-36c4-4555-a8b6-d514f1c7d656,fuel_level,91
6754befd-36c4-4555-a8b6-d514f1c7d656,battery_level,41
6754befd-36c4-4555-a8b6-d514f1c7d656,engine_temperature,84
1ea6e00d-5609-4697-97a4-4809b9322463,type,chassis
1ea6e00d-5609-4697-97a4-4809b9322463,speed,65
1ea6e00d-5609-4697-97a4-4809b9322463,brake_status,True
```
