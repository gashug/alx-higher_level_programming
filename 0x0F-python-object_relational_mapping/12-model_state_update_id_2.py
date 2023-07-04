#!/usr/bin/python3
# Changes the name of the State object with id = 2 to
# New Mexico in the database hbtn_0e_6_usa.
# Usage: ./12-model_state_update_id_2.py <mysql username> /
#                                        <mysql password> /
#                                        <database name>
if __name__ == "__main__":
    import sys
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = 'New Mexico'
        session.commit()
