from models import Student_behaviour, Student_results, session
from tabulate import tabulate

# fetching the student indiscipline cases of the parents child
def parent_get_student_behaviour(unque_cod):
    the_children = session.query(Student_behaviour).filter(Student_behaviour.student_unique_code == unque_cod).all()
    the_mistakes = []
    num = 0
    for mis in the_children:
        num += 1
        the_mistakes.append([num , mis.student_misbehave])
    print(tabulate(the_mistakes , headers=['Number of mistakes', 'The misbehave']))         

# fetching the students result
def parent_get_student_result(unique_cod):
    the_results = session.query(Student_results).filter(Student_results.student_unique_code == unique_cod).all()
    num = 0
    table = []
    for result in the_results:
        num +=1
        data = [num , result.result_id,result.result_points, result.student_perfomance]
        table.append(data)
    print(tabulate(table, headers=['Number of exam' , 'Exam id', 'Student points', 'student percentage '], tablefmt='github'))  