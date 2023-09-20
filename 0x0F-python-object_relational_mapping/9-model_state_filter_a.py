#!/usr/bin/python3

"""lists all State objects that contain the letter a from the database."""

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

    state = session.query(State).filter(
                            State.name.like('%a%')
                    ).order_by(State.id).all()

    for i in state:
        print(f"{i.id}: {i.name}")

    session.close()
