#!/usr/bin/env python3

import uuid
import argparse
import random
import datetime
import csv
import sys

def generate_vehicle_data(vehicle_count, frequency, duration):
    end_time = datetime.datetime.now()
    start_time = end_time - datetime.timedelta(minutes=duration)

    vehicle_data = []

    for i in range(vehicle_count):
        vehicle_subject_id = str(uuid.uuid4())  # <-- Use UUID for unique ID

        vehicle_data.append((vehicle_subject_id, "type", "vehicle"))
        vehicle_data.append((vehicle_subject_id, "vehicle_id", i))

        current_time = start_time
        while current_time <= end_time:
            drivetrain_subject_id = str(uuid.uuid4())  # <-- Use UUID for unique ID
            chassis_subject_id = str(uuid.uuid4())     # <-- Use UUID for unique ID

            vehicle_data.append((vehicle_subject_id, "timestamp", current_time.strftime('%Y-%m-%d %H:%M:%S')))
            vehicle_data.append((vehicle_subject_id, "has_drivetrain", drivetrain_subject_id))
            vehicle_data.append((vehicle_subject_id, "has_chassis", chassis_subject_id))

            vehicle_data.append((drivetrain_subject_id, "type", "drivetrain"))
            vehicle_data.append((drivetrain_subject_id, "fuel_level", random.randint(0, 100)))
            vehicle_data.append((drivetrain_subject_id, "battery_level", random.randint(0, 100)))
            vehicle_data.append((drivetrain_subject_id, "engine_temperature", random.randint(80, 120)))

            vehicle_data.append((chassis_subject_id, "type", "chassis"))
            vehicle_data.append((chassis_subject_id, "speed", random.randint(0, 120)))
            vehicle_data.append((chassis_subject_id, "brake_status", random.choice([True, False])))

            current_time += datetime.timedelta(minutes=frequency)

    return vehicle_data

def write_to_stdout(data):
    csvwriter = csv.writer(sys.stdout)
    csvwriter.writerow(["Subject", "Predicate", "Object"])  # CSV headers
    for row in data:
        csvwriter.writerow(row)

def main():
    parser = argparse.ArgumentParser(description="Generate VSS conform test data in triples format.")
    parser.add_argument("-v", "--vehicles", type=int, required=True, help="Number of vehicles to simulate.")
    parser.add_argument("-f", "--frequency", type=int, required=True, help="Frequency of observations in minutes.")
    parser.add_argument("-d", "--duration", type=int, required=True, help="Duration from the first to the last observation in minutes.")

    args = parser.parse_args()

    data = generate_vehicle_data(args.vehicles, args.frequency, args.duration)
    write_to_stdout(data)

if __name__ == "__main__":
    main()
