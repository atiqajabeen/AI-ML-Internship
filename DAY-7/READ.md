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

- `hostel_system.py` — everything: the `Hostel`/`Student`/`Room`
  classes, the console menu, AND the Gradio web UI, all in one file
- `requirements.txt` — just `gradio`, needed for the web UI
- `sample_data/students.json`, `sample_data/rooms.json` — example data
- `sample_data/report.txt` — example report output

## Console vs. Web UI

Both versions live in `hostel_system.py` and use the exact same
`Hostel` class underneath — nothing is duplicated.

- `run_console()` — the terminal menu (type numbers 1-9)
- `run_gradio()` — the Gradio web UI (click buttons in the browser)

At the bottom of the file:

```python
if __name__ == "__main__":
    run_gradio()
```

By default it launches the **web UI**. If you want the plain terminal
version instead, just change that one line to `run_console()`.

## Running it in VS Code

1. Install gradio (only needed for the web UI):
   ```bash
   pip install -r requirements.txt
   ```
2. Open `hostel_system.py` in VS Code and hit Run (or
   `python3 hostel_system.py` in the terminal).
3. It'll print a local URL like `http://127.0.0.1:7860` — open that in
   your browser (VS Code also usually shows an "open in browser"
   popup).

The web UI has one tab per feature (register, add room, allocate,
checkout, available/occupied rooms, search, report) — same behavior
as the console menu, just with forms and buttons. Either way, data
saves to the same `students.json` and `rooms.json` files.

## Possible improvements

- Let students have room-type preferences (AC/non-AC, single/shared)
- Add a waiting list for when no rooms are free
- Track fees/payments per student
- Move from JSON files to a real database once data grows large