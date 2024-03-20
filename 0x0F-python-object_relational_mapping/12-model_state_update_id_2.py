#!/usr/bin/python3
"""Changes the name of a State object from the database hbtn_0e_6_usa."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query State object with id=2
    state = session.query(State).filter_by(id=2).first()

    if state:
        # Change the name of the State object
        state.name = "New Mexico"
        # Commit the changes to the database
        session.commit()
        print("Name of State with id=2 changed to 'New Mexico'")
    else:
        print("State with id=2 not found")

    # Close the session
    session.close()
