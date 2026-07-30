import json
import os
from datetime import datetime
STUDENTS_FILE = "students.json"
ROOMS_FILE = "rooms.json"
class Student:
    def __init__(self, student_id, name, cnic, contact, room_id=None):
        self.student_id = student_id
        self.name = name
        self.cnic = cnic
        self.contact = contact
        self.room_id = room_id
class Room:
    def __init__(self, room_id, room_number, capacity, occupants=None):
        self.room_id = room_id
        self.room_number = room_number
        self.capacity = capacity
        self.occupants = occupants if occupants else []
class Hostel:
    def __init__(self):
        self.students = []   
        self.rooms = []      
        self.load_data()
    def load_data(self):
        if os.path.exists(STUDENTS_FILE):
            with open(STUDENTS_FILE, "r") as f:
                data = json.load(f)
                for d in data:
                    self.students.append(Student(d["student_id"], d["name"], d["cnic"],
                                                  d["contact"], d["room_id"]))
        if os.path.exists(ROOMS_FILE):
            with open(ROOMS_FILE, "r") as f:
                data = json.load(f)
                for d in data:
                    self.rooms.append(Room(d["room_id"], d["room_number"], d["capacity"],
                                            d["occupants"]))
    def save_data(self):
        student_list = []
        for s in self.students:
            student_list.append({
                "student_id": s.student_id,
                "name": s.name,
                "cnic": s.cnic,
                "contact": s.contact,
                "room_id": s.room_id
            })
        with open(STUDENTS_FILE, "w") as f:
            json.dump(student_list, f, indent=2)
        room_list = []
        for r in self.rooms:
            room_list.append({
                "room_id": r.room_id,
                "room_number": r.room_number,
                "capacity": r.capacity,
                "occupants": r.occupants
            })
        with open(ROOMS_FILE, "w") as f:
            json.dump(room_list, f, indent=2)
    def find_student(self, student_id):
        for s in self.students:
            if s.student_id == student_id:
                return s
        return None
    def find_room(self, room_id):
        for r in self.rooms:
            if r.room_id == room_id:
                return r
        return None
    def register_student(self, name, cnic, contact):
        for s in self.students:
            if s.cnic == cnic:
                raise ValueError(f"This CNIC is already registered under {s.name} ({s.student_id})")
        new_id = "STU" + str(len(self.students) + 1).zfill(3)
        student = Student(new_id, name, cnic, contact)
        self.students.append(student)
        self.save_data()
        return student
    def add_room(self, room_number, capacity):
        new_id = "RM" + str(len(self.rooms) + 1).zfill(3)
        room = Room(new_id, room_number, capacity)
        self.rooms.append(room)
        self.save_data()
        return room
    def allocate_room(self, student_id, room_id=None):
        student = self.find_student(student_id)
        if not student:
            raise ValueError("Student not found.")
        if student.room_id:
            raise ValueError("This student already has a room. Check out first.")
        if room_id:
            room = self.find_room(room_id)
            if not room:
                raise ValueError("Room not found.")
            if len(room.occupants) >= room.capacity:
                raise ValueError("This room is already full.")
        else:
            room = None
            for r in self.rooms:
                if len(r.occupants) < r.capacity:
                    room = r
                    break
            if not room:
                raise ValueError("No rooms available right now.")
        room.occupants.append(student.student_id)
        student.room_id = room.room_id
        self.save_data()
        return room
    def checkout_student(self, student_id):
        student = self.find_student(student_id)
        if not student:
            raise ValueError("Student not found.")
        if not student.room_id:
            raise ValueError("Student doesn't have a room to check out of.")
        room = self.find_room(student.room_id)
        if room and student_id in room.occupants:
            room.occupants.remove(student_id)
        old_room = student.room_id
        student.room_id = None
        self.save_data()
        return old_room
    def search_student(self, query):
        results = []
        for s in self.students:
            if s.student_id == query or query.lower() in s.name.lower():
                results.append(s)
        return results
    def available_rooms(self):
        return [r for r in self.rooms if len(r.occupants) < r.capacity]
    def occupied_rooms(self):
        return [r for r in self.rooms if len(r.occupants) > 0]
    def generate_report(self):
        total_students = len(self.students)
        total_rooms = len(self.rooms)
        occupied = len(self.occupied_rooms())
        available = total_rooms - occupied
        if total_rooms > 0:
            occupancy = (occupied / total_rooms) * 100
        else:
            occupancy = 0
        report = (
            "----- SUMMARY REPORT -----\n"
            f"Total Students   : {total_students}\n"
            f"Total Rooms      : {total_rooms}\n"
            f"Occupied Rooms   : {occupied}\n"
            f"Available Rooms  : {available}\n"
            f"Occupancy Rate   : {occupancy:.2f}%\n"
        )
        with open("report.txt", "w") as f:
            f.write(report)
        return report
def print_student(s):
    room = s.room_id if s.room_id else "Not allocated"
    print(f"{s.student_id} | {s.name} | CNIC: {s.cnic} | Contact: {s.contact} | Room: {room}")
def print_room(r):
    print(f"{r.room_id} | Room {r.room_number} | Capacity: {r.capacity} | "
          f"Occupied: {len(r.occupants)} | Free: {r.capacity - len(r.occupants)}")
def main():
    hostel = Hostel()
    menu = """
1. Register student
2. Add room
3. Allocate room
4. Checkout student
5. View available rooms
6. View occupied rooms
7. Search student
8. Generate report
9. Exit
"""
    while True:
        print(menu)
        choice = input("Enter choice: ").strip()
        try:
            if choice == "1":
                name = input("Name: ").strip()
                cnic = input("CNIC: ").strip()
                contact = input("Contact number: ").strip()
                student = hostel.register_student(name, cnic, contact)
                print("Registered! Student ID:", student.student_id)
            elif choice == "2":
                number = input("Room number: ").strip()
                capacity = int(input("Capacity: ").strip())
                room = hostel.add_room(number, capacity)
                print("Room added! Room ID:", room.room_id)
            elif choice == "3":
                student_id = input("Student ID: ").strip().upper()
                room_id = input("Room ID (leave blank for auto-allocate): ").strip().upper()
                room = hostel.allocate_room(student_id, room_id if room_id else None)
                print(f"Allocated room {room.room_number} to {student_id}")
            elif choice == "4":
                student_id = input("Student ID: ").strip().upper()
                old_room = hostel.checkout_student(student_id)
                print(f"{student_id} checked out of {old_room}")
            elif choice == "5":
                for r in hostel.available_rooms():
                    print_room(r)
            elif choice == "6":
                for r in hostel.occupied_rooms():
                    print_room(r)
            elif choice == "7":
                query = input("Enter Student ID or Name: ").strip()
                results = hostel.search_student(query)
                if not results:
                    print("No student found.")
                for s in results:
                    print_student(s)
            elif choice == "8":
                print(hostel.generate_report())
            elif choice == "9":
                print("Goodbye!")
                break
            else:
                print("Invalid choice, pick a number from 1-9.")
        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("Something went wrong:", e)
if __name__ == "__main__":
    main()