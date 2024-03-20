#!/usr/bin/python3
""" Prints the State object with the name passed as argument from the database """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./script.py <username> <password> <database> <state_name>")
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        instance = session.query(State).filter(State.name == sys.argv[4]).first()
        if instance:
            print(instance.id)
        else:
            print("Not found")
    except NoResultFound:
        print("Not found")

    session.close()
