#!/usr/bin/python3

"""script that adds the State object “Louisiana” to the database."""

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

    new_state = State(name="Louisiana")

    session.add(new_state)
    session.commit()

    print(new_state.id)

    session.close()
