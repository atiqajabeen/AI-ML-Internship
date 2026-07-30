# Smart Hostel Room Allocation System

A simple console app to manage hostel students and rooms. Run it with:

```bash
python3 hostel_system.py
```

## What it does

- Register students (auto-generates a Student ID like `STU001`)
- Add rooms with a capacity
- Allocate a room to a student (auto-picks the first room with space,
  or you can type a specific Room ID)
- Stops overbooking — checks capacity before every allocation
- Checkout a student to free up their room
- View available / occupied rooms
- Search by Student ID or Name
- Generate a summary report (also saved to `report.txt`)
- Everything saves to `students.json` and `rooms.json` so data is
  still there next time you run it

## How it works (in plain terms)

**Classes:** `Student` and `Room` just hold data. `Hostel` does
everything else — registering, allocating, saving/loading files, etc.

**Student IDs:** `STU` + however many students exist so far + 1.
So the 5th student registered becomes `STU005`.

**Duplicate students:** checked using CNIC, since names can repeat but
CNIC can't. If someone tries to register with a CNIC that's already
in the system, it's rejected.

**Room allocation:** if you don't pick a room yourself, the app just
loops through the room list and gives the student the first room that
still has space. Simple first-fit, nothing fancy.

**Overbooking:** before adding a student to a room, it checks
`len(room.occupants) >= room.capacity`. If true, it refuses.

**Saving data:** every time something changes (register, allocate,
checkout, add room), the whole students/rooms list gets written to
its JSON file. So you never lose anything, and there's no separate
"save" button to remember.

**Errors:** anything that shouldn't happen (duplicate CNIC, full room,
student not found, etc.) raises a `ValueError`, and the menu just
prints `Error: ...` instead of crashing.

## Files

- `hostel_system.py` — the whole app
- `sample_data/students.json`, `sample_data/rooms.json` — example data
- `sample_data/report.txt` — example report output

## Possible improvements

- Let students have room-type preferences (AC/non-AC, single/shared)
- Add a waiting list for when no rooms are free
- Track fees/payments per student
- Move from JSON files to a real database once data grows large