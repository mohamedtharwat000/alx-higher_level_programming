#!/usr/bin/python3

"""changes the name of a State object from the database."""

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

    state_to_update = session.query(State).filter_by(id=2).first()

    if state_to_update is not None:
        state_to_update.name = "New Mexico"
        session.commit()

    session.close()
