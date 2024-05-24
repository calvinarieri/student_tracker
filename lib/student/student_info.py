from models import session, Student_results as StudentResults, Student_behaviour as StudentBehaviour
from tabulate import tabulate


# calculates the student rating through the results and the discipline of the student
def student_rating(unique_cod):
    the_results = session.query(StudentResults).filter(StudentResults.student_unique_code == unique_cod).all()
    result_sum = 0
    number_of_exams = 0
    for result in the_results:
        number_of_exams += 1
        result_sum = result_sum + result.student_perfomance
    the_average = result_sum / number_of_exams
    the_children = session.query(StudentBehaviour).filter(StudentBehaviour.student_unique_code == unique_cod).count()

    # finds the rate percentage.
    if the_children < 2:
        rate = 100
    elif 2 < the_children < 5:
        rate = 75
    elif the_children > 5 and the_children > 7:
        rate = 50
    elif 9 < the_children < 11:
        rate = 25
    else:
        rate = 0

    # calculates the student ratings
    the_rating_of = (the_average + rate) / 2

    # Finds recommendation msg
    if 101 > the_rating_of >= 75:
        msg = "Good and well behaved student"
    elif 75 > the_rating_of >= 50:
        msg = "The student is an average student in terms of behaviour and results"
    elif 50 > the_rating_of >= 25:
        msg = "Good but requires supervision "
    else:
        msg = "Cannot recommend him"
    print(tabulate([['Academic performance in %', 'Discipline percentage', 'Average rating',
                     'What to say about rating'],
                    [the_average, rate, the_rating_of, msg]], headers='firstrow', tablefmt='github'))
