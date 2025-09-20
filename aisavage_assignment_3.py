full_name= "Aiyana Savage"
student_email= "aisavage@ncat.edu"
hometown= "Baltimore, MD"
graduation_semester = "Spring 2029"
major= "Computer Engineering"
current_course_list= ["COMP 163", "MATH 131", "ENG 100", "ECEN 101", "GEEN 100", "GEEN 101"]
completed_course_list= ["N/A"]
credit_hour_list= [3, 4, 3, 3, 2, 1]
gpa_history_list= ["N/A"]
emergency_contact= ("Mom", "Shilonda Savage", "704-555-0199")
home_address= ("456 Oak Street", "Baltimore, MD", 21206)
instagram_info=  ("Instagram", "@aiyanaaaaa.__", 1,701)
twitter_info= ("Twitter", "@ineedpinkricks", 27)
birthday= ("Birthday", 1, 8, 2007)
current_skills= {"Python basics", "Problem solving", "Time management"}
skills_to_learn= {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests={"Software development", "Web development", "Data science", "Game development"}
hobbies= {"Dancing", "Shopping", "Cheerleading", "Music"}
entertainment_backlog= {"Empire", "Power", "BMF", "The CHI"}
course_credits= {"COMP 163": 3, "MATH 131": 4, "ENG 100": 3, "ECEN 101": 3, "GEEN 100": 2, "GEEN 111": 1}
course_professors={"COMP 163": "Prof. Rhodes", "MATH 131": "Prof. "Chen", "ENG 100": "Prof. Rush", "ECEN 101": "Prof. Horne", "GEEN 100": "Prof. Alford", "GEEN 111": "Dr. Parrish"}
course_rooms= { "COMP 163": "M-Eric 300", "MATH 103": "Marteena 201", "ENG 100": "Crosby 121", "ECEN 101": "MCNAIR 210","GEEN 100": "GRAHAM 210", "GEEN 111": "MCNAIR 210" } 
monthly_budget= {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_hours_per= {"Programming": 10, "Math": 8, "English": 4, "History": 3}
contact_directory= {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}
total_credits= sum(credit_hour_list)
entertainment_budget= monthly_budget["Entertainment"]
cumalative_gpa= (sum(gpa_history_list))/3
total_courses= len(completed_course_list)
total_study_hours= sum(study_hours_per.values())
academic_load= (total_credits + total_study_hours)
total_monthly_budget= sum(monthly_budget.values())
current_skill_amount= len(current_skills)
new_skill_amount= len(skills_to_learn)
food_amount= 450
daily_food_budget= (f"{(food_amount/30):.1f}")
annual_budget= (total_monthly_budget * 12)
book_budget= monthly_budget["Books"]
hourly_study_cost= (f"{(book_budget/total_study_hours):.2f}")
total_followers= (instagram_info[2]+ twitter_info[2])
backlog_count= len(entertainment_backlog)
print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print("Student:", full_name , "| Email:", student_email)
print("From:", hometown ,"| Graduating:", graduation_semester)
print("Major:", major)
print("")
print("=== ACADEMIC PROFILE ===")
print("Current Semester:", total_credits, "credits across 4 courses")
print("Cumulative GPA: 4.0")
print("Weekly Study Time:", total_study_hours, "hours")
print("Academic Investment:", "$5.0 per study hour")
print("")
print("Current Courses:")
print("COMP 163 -", course_credits["COMP 163"], "credits -", course_professors["COMP 163"], "-", course_rooms["COMP 163"])
print("MATH 150 -", course_credits["MATH 103"], "credits -", course_professors["MATH 150"], "-", course_rooms["MATH 150"])
print("ENG 101 -", course_credits["ENG 100"], "credits -", course_professors["ENG 101"], "-", course_rooms["ENG 101"])
print("ECEN 101 -", course_credits["ECEN 101"], "credits -", course_professors["ECEN 101"], "-", course_rooms["ECEN 101"])
print("GEEN 100 -", course_credits["GEEN 100"], "credits -", course_professors["GEEN 100"], "-", course_rooms["GEEN 100"])
print("GEEN 111 -", course_credits["GEEN 111"], "credits -", course_professors["GEEN 111"], "-", course_rooms["GEEN 111"])
print("")
print("=== PERSONAL DEVELOPMENT ===")
print("Current Skills:", current_skills)
print("Learning Goals:", skills_to_learn)
print("Career Interests:", career_interests)
print("Skills Currently Have:", current_skill_amount)
print("Skills Want to Learn:", new_skill_amount)
print("")
print("=== FINANCIAL OVERVIEW ===")
print("Monthly Budget:", f"${total_monthly_budget}")
print("Food:", f"${food_amount}", f"(${daily_food_budget}/day)")
print("Entertainment:", f"${entertainment_budget}")
print("Books:", f"${monthly_budget["Books"]}")
print("Transportation:", f"${monthly_budget["Transportation"]}")
print("Annual Projection:", f"${annual_budget}")
print("")
print("=== CONNECTIONS & CONTACTS ===")
print("Emergency Contact:", emergency_contact[1], f"({emergency_contact[0]}) -", emergency_contact[2])
print("Home Address:", f"{home_address[0]}, {home_address[1]} {home_address[2]})")
print("Social Media Presence:", total_followers, "followers across 2 platforms")
print("Key Contacts:", len(contact_directory), "people in directory")
print("")
print("=== LIFE STATISTICS ===")
print("Total Courses Completed:", total_courses)
print("Current Academic Load:", academic_load, "weekly commitments")
print("Entertainment Backlog:", backlog_count, "items")
print("Current Hobbies:", len(hobbies), "activities")
print("================================================================")
