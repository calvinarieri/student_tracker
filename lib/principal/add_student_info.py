from models import Student_results,Student_behaviour, session
GREEN = '\033[92m'
RESET = "\033[0m"

# add new result
def add_new_result(unique_cod):
    print(GREEN+"Happy to know the exams are done. Please enter the results below to start the computation"+RESET)

    # get the results details
    r_id = None
    r_p = int(input("Perfomance in terms of points: ")) 

    # gets the average to find the percentage perfomance
    the_avg = (r_p / 84)*100 

    # Adds new result to the database
    new_result = Student_results(result_id = r_id, result_points = r_p, student_unique_code = unique_cod, student_perfomance= the_avg)
    session.add(new_result)
    session.commit()
    print(GREEN+ f"The results have been added successfully. The student has {the_avg}%"+RESET)

# add misbehaviour case for the principal only
def add_misbehave(school_id, uniqu_cod):
    
    # Gets misbehaviour
    print('Please fill the detail below')
    m_id = None
    s_m_b = input('The mistake: ')

    # Adds new misbehaviour in the database
    new_misbehave = Student_behaviour(misbehaviour_id = m_id, student_unique_code = uniqu_cod, student_misbehave = s_m_b, school_code = school_id )
    session.add(new_misbehave)
    session.commit()
    print(GREEN+'You have successfully added the misbehaviour of the student'+RESET)