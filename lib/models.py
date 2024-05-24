from sqlalchemy import String, Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///school.db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


# creation of tables


class Student(Base):
    __tablename__ = 'students'

    student_id = Column(Integer, primary_key=True)
    student_first_name = Column(String(15))
    student_second_name = Column(String(10))
    student_surname = Column(String(10))
    school_code = Column(String)
    unique_code = Column(String)


class Parent(Base):
    __tablename__ = 'parents'

    parent_id = Column(Integer, primary_key=True)
    parent_name = Column(String)
    parent_phone = Column(String)
    student_code = Column(String)
    parent_log_in = Column(String)


class Student_behaviour(Base):
    __tablename__ = 'misbehaviours'

    misbehaviour_id = Column(Integer, primary_key=True)
    student_unique_code = Column(String)
    student_misbehave = Column(String)
    school_code = Column(String)


class Student_results(Base):
    __tablename__ = 'results'

    result_id = Column(Integer, primary_key=True)
    result_points = Column(Integer)
    student_unique_code = Column(String)
    student_perfomance = Column(Integer)


class Other_user(Base):
    __tablename__ = 'other_users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(20))
    user_password = Column(String)
    company_name = Column(String)
    company_code = Column(String)


class Principal(Base):
    __tablename__ = 'principals'

    principal_id = Column(Integer, primary_key=True)
    principal_reg = Column(Integer)
    principal_school = Column(String(10))
    principal_name = Column(String)
    principal_phone_number = Column(Integer)


"""
Creates all the tables and fields if the file is called 
"""
Base.metadata.create_all(engine)
