#!/usr/bin/python3

"""prints the State object with the name passed as argument."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, orm


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{database}'
            )

    Base.metadata.bind = engine

    DBSession = orm.sessionmaker(bind=engine)
    session = DBSession()

    state = session.query(State).filter(State.name == state_name).first()

    if state is not None:
        print(state.id)
    else:
        print('Not found')

    session.close()
