from database import get_connection
from students import find_student

def add_result():
    roll = input("Roll number: ").strip()
    student = find_student(roll)
    if not student:
        print("Student not found."); return
    subject = input("Subject: ").strip()
    try:
        marks = float(input("Marks (0-100): "))
        if not subject or not 0 <= marks <= 100:
            raise ValueError
        with get_connection() as conn:
            conn.execute("INSERT INTO results(student_id,subject,marks) VALUES(?,?,?)",
                         (student[0],subject,marks))
            conn.commit()
        print("Result added.")
    except ValueError:
        print("Marks must be between 0 and 100.")
    except Exception as e:
        print("Could not add result:", e)

def grade(marks):
    if marks >= 90: return "A+"
    if marks >= 80: return "A"
    if marks >= 70: return "B"
    if marks >= 60: return "C"
    if marks >= 50: return "D"
    return "F"

def show_result():
    roll = input("Roll number: ").strip()
    student = find_student(roll)
    if not student:
        print("Student not found."); return
    with get_connection() as conn:
        rows = conn.execute("SELECT subject,marks FROM results WHERE student_id=? ORDER BY subject",
                            (student[0],)).fetchall()
    if not rows:
        print("No results found."); return
    total = sum(m for _,m in rows)
    percentage = total / len(rows)
    print(f"\n{student[2]} | Roll: {student[1]} | {student[3]} Semester {student[4]}")
    print("-"*45)
    for subject,marks in rows:
        print(f"{subject:<20} {marks:>6.2f}  Grade: {grade(marks)}")
    print("-"*45)
    print(f"Total: {total:.2f}/{len(rows)*100:.0f}")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Overall Result: {'PASS' if all(m >= 40 for _,m in rows) else 'FAIL'}")

def all_results():
    with get_connection() as conn:
        rows = conn.execute("""SELECT s.roll_no,s.name,r.subject,r.marks
                               FROM results r JOIN students s ON s.id=r.student_id
                               ORDER BY s.roll_no,r.subject""").fetchall()
    if not rows:
        print("No results found."); return
    for roll,name,subject,marks in rows:
        print(f"{roll} | {name} | {subject} | {marks:.2f} | {grade(marks)}")
