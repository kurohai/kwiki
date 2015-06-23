from sqlalchemy.orm import scoped_session, sessionmaker
from sched.app import db, app, Base


engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

Base.query = db_session.query_property()


def initdb():
    Base.metadata.create_all(bind=engine)

def deldb():
    Base.metadata.drop_all(bind=engine)


if __name__ == '__main__':
    deldb()
    initdb()
