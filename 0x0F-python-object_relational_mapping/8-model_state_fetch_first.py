#!/usr/bin/python3

"""prints the first State object from the database hbtn_0e_6_usa."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, orm


if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
            f'mysql://{username}:{password}@localhost:3306/{database}'
            )

    Base.metadata.bind = engine

    DBSession = orm.sessionmaker(bind=engine)
    session = DBSession()

    state = session.query(State).order_by(State.id).first()

    if state is not None:
        print(f'{state.id}: {state.name}')
    else:
        print('Nothing')

    session.close()
