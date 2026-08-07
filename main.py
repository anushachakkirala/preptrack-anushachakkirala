print("=" * 50)
print("              PREPTRACK APPLICATION")
print("=" * 50)

# Student Name Validation
student_name=input("Enter the student name:")
if len(student_name)==0:
    print("Invalid input!Please enter a valid name.")
else:
    print(student_name)

# Registration Number
registration_number = input("Enter registration number: ")

# Graduation Year
graduation_year = int(input("Enter graduation year: "))
graduation_eligible = (
    graduation_year >= 2025
    and graduation_year <= 2027)
if not graduation_eligible:
    print("You are not eligible for graduation.")
# Attendance Validation
while True:
    attendance = float(input("Enter attendance percentage: "))

    if 0 <= attendance <= 100:
        print("Attendance accepted.")
        break

    print("Invalid attendance. Enter a value between 0 and 100.")

# Project Completion Input
while True:
    project_input = input(
        "Has the student completed the required project?\nEnter yes or no: "
    ).lower()

    if project_input == "yes":
        project_completed = True
        break
    elif project_input == "no":
        project_completed = False
        break
    else:
        print("Invalid input. Enter only yes or no.")

# Profile Verification Input
while True:
    profile_input = input(
        "Is the student profile verified?\nEnter yes or no: "
    ).lower()

    if profile_input == "yes":
        profile_verified = True
        break
    elif profile_input == "no":
        profile_verified = False
        break
    else:
        print("Invalid input. Enter only yes or no.")

# Initialize Variables
total_score = 0

attempted_days = 0
absent_days = 0
passed_days = 0
failed_days = 0

strong_days = 0
satisfactory_days = 0
improvement_days = 0
critical_days = 0

highest_score = 0
highest_score_day = 0

lowest_score = 0
lowest_score_day = 0

first_attempt_found = False

critical_score_found = False
first_critical_day = 0
first_critical_score = 0
# Process Seven Practice Days
for day in range(1, 8):

    while True:
        score = int(
            input(
                f"Enter Day {day} score from 0 to 100, or -1 for absent: "
            )
        )

        if score == -1 or (0 <= score <= 100):
            break

        print("Invalid score. Enter -1 or a value between 0 and 100.")

    # Handle Absent Days
    if score == -1:
        absent_days += 1
        print(f"Day {day} Result: Absent")
        continue

    attempted_days += 1
    total_score += score

    # Highest and Lowest Score
    if not first_attempt_found:
        highest_score = score
        highest_score_day = day

        lowest_score = score
        lowest_score_day = day

        first_attempt_found = True
    else:
        if score > highest_score:
            highest_score = score
            highest_score_day = day

        if score < lowest_score:
            lowest_score = score
            lowest_score_day = day

    # Classification
    if 75 <= score <= 100:
        print(f"Day {day} Result: Strong")
        strong_days += 1

    elif 60 <= score <= 74:
        print(f"Day {day} Result: Satisfactory")
        satisfactory_days += 1

    elif 40 <= score <= 59:
        print(f"Day {day} Result: Needs Improvement")
        improvement_days += 1

    else:
        print(f"Day {day} Result: Critical")
        critical_days += 1

        if not critical_score_found:
            critical_score_found = True
            first_critical_day = day
            first_critical_score = score

    # Pass / Fail Count
    if score >= 60:
        passed_days += 1
    else:
        failed_days += 1

# Average Calculation
if attempted_days > 0:
    average_score = total_score / attempted_days
else:
    average_score = 0

# Placement Readiness Conditions
graduation_eligible = (
    graduation_year >= 2025 and graduation_year <= 2027
)

attendance_eligible = attendance >= 75
practice_count_eligible = attempted_days >= 6
average_eligible = average_score >= 70
critical_score_clear = not critical_score_found
passed_days_eligible = passed_days >= 4

placement_ready = (
    graduation_eligible
    and attendance_eligible
    and practice_count_eligible
    and average_eligible
    and critical_score_clear
    and passed_days_eligible
    and project_completed
    and profile_verified
)

# Final Status Priority
if attempted_days == 0:
    final_status = "Practice Not Evaluated"
    blocker = "No practice attempted"
    next_action = "Attempt the required coding practices"

elif critical_score_found:
    final_status = "Critical Support Required"
    blocker = "Critical score found"
    next_action = "Revise the concepts from the first critical day"

elif attempted_days < 6:
    final_status = "Practice Incomplete"
    blocker = "Fewer than six practices attempted"
    next_action = "Complete at least six practice days"

elif passed_days < 4:
    final_status = "Insufficient Passed Practices"
    blocker = "Fewer than four practices passed"
    next_action = "Pass at least four coding practices"

elif average_score < 70:
    final_status = "Practice Improvement Required"
    blocker = "Average score below 70"
    next_action = "Improve the average score to at least 70"

elif attendance < 75:
    final_status = "Attendance Improvement Required"
    blocker = "Attendance below 75"
    next_action = "Improve attendance to at least 75 percent"

elif not graduation_eligible:
    final_status = "Graduation Criteria Not Met"
    blocker = "Graduation year not eligible"
    next_action = "Check the eligible graduation-year requirement"

elif not project_completed:
    final_status = "Application On Hold"
    blocker = "Project incomplete"
    next_action = "Complete the required project"

elif not profile_verified:
    final_status = "Application On Hold"
    blocker = "Profile not verified"
    next_action = "Complete profile verification"

else:
    final_status = "Ready for Mock Interview"
    blocker = "None"
    next_action = "Proceed to placement mock interviews"

# Values when no practice attempted
if attempted_days == 0:
    highest_score_display = "Not Available"
    highest_day_display = "Not Available"
    lowest_score_display = "Not Available"
    lowest_day_display = "Not Available"
else:
    highest_score_display = highest_score
    highest_day_display = highest_score_day
    lowest_score_display = lowest_score
    lowest_day_display = lowest_score_day

if critical_score_found:
    first_critical_day_display = first_critical_day
    first_critical_score_display = first_critical_score
else:
    first_critical_day_display = "Not Applicable"
    first_critical_score_display = "Not Applicable"

# Final Report
print("\n" + "=" * 50)
print("                 PREPTRACK REPORT")
print("=" * 50)

print("\nSTUDENT PROFILE\n")

print(f"Student Name             : {student_name}")
print(f"Registration Number      : {registration_number}")
print(f"Graduation Year          : {graduation_year}")
print(f"Attendance               : {attendance}")
print(f"Project Completed        : {project_completed}")
print(f"Profile Verified         : {profile_verified}")

print("\nPRACTICE SUMMARY\n")

print("Total Practice Days      : 7")
print(f"Attempted Days           : {attempted_days}")
print(f"Absent Days              : {absent_days}")
print(f"Passed Days              : {passed_days}")
print(f"Failed Days              : {failed_days}")

print(f"Strong Days              : {strong_days}")
print(f"Satisfactory Days        : {satisfactory_days}")
print(f"Needs Improvement Days   : {improvement_days}")
print(f"Critical Days            : {critical_days}")

print("\nPERFORMANCE ANALYSIS\n")

print(f"Total Score              : {total_score}")
print(f"Average Score            : {average_score:.2f}")
print(f"Highest Score            : {highest_score_display}")
print(f"Highest Score Day        : {highest_day_display}")
print(f"Lowest Score             : {lowest_score_display}")
print(f"Lowest Score Day         : {lowest_day_display}")

print("\nCRITICAL SCORE INFORMATION\n")

print(f"Critical Score Found     : {critical_score_found}")
print(f"First Critical Day       : {first_critical_day_display}")
print(f"First Critical Score     : {first_critical_score_display}")

print("\nFINAL DECISION\n")

print(f"Final Status             : {final_status}")
print(f"Primary Blocker          : {blocker}")
print(f"Next Action              : {next_action}")

print("\n" + "=" * 50)
