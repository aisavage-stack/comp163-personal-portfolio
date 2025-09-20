full_name= "Jordan Smith"
student_email= "jsmith@ncat.edu"
hometown= "Charlotte, NC"
graduation_semester = "Spring 2028"
major= "Computer Science"
current_course_list= ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_course_list= ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hour_list= [3, 3, 3, 3]
gpa_history_list= [3.2, 3.6, 3.4, 3.7]
emergency_contact= ("Mom", "Hannah Smith", "704-555-0199")
home_address= ("456 Oak Street", "Charlotte, NC", 28202)
instagram_info=  ("Instagram", "@jordan_codes", 312)
twitter_info= ("Twitter", "@jordandev", 127)
birthday= ("Birthday", 5, 22, 2006)
current_skills= {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn= {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests={"Software development", "Web development", "Data science", "Game development"}
hobbies= {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog= {"One Piece", "Barry", "Life", "Incantation", "Memento"}
course_credits= {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
course_professors={"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee", "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
course_rooms= { "COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"} 
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
print("Cumulative GPA: 3.48")
print("Weekly Study Time:", total_study_hours, "hours")
print("Academic Investment:", "$5.0 per study hour")
print("")
print("Current Courses:")
print("COMP 163 -", course_credits["COMP 163"], "credits -", course_professors["COMP 163"], "-", course_rooms["COMP 163"])
print("MATH 150 -", course_credits["MATH 150"], "credits -", course_professors["MATH 150"], "-", course_rooms["MATH 150"])
print("ENG 101 -", course_credits["ENG 101"], "credits -", course_professors["ENG 101"], "-", course_rooms["ENG 101"])
print("HIS 105 -", course_credits["HIS 105"], "credits -", course_professors["HIS 105"], "-", course_rooms["HIS 105"])
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
