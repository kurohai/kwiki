from sqlalchemy.orm import scoped_session, sessionmaker
from kwiki import app, Base, User, session, engine, log
import time


def initdb():
    Base.metadata.create_all(bind=engine)
    log.info('tables created')
    mkusr()
    log.info('user created')


def deldb():
    Base.metadata.drop_all(bind=engine)


def mkusr():
    u = User()
    u.id = 1
    u.email = 'kurohai@gmail.com'
    u.username = 'kurohai'
    u.name = 'Kurohai'
    u.password = 'lol'
    u.admin = True


    session.add(u)
    session.commit()

# def mkusr2():
#     log.debug('making user2 obj')
#     u = User()

#     log.debug('user2 email')
#     u.email = 'derp@gmail.com'
#     log.debug('user2 username')
#     u.username = 'derp'
#     log.debug('user2 name')
#     u.name = 'Herp Derp'
#     log.debug('user2 password')
#     u.password = 'herp'

#     log.debug('user2 Game')
#     g = Game()
#     log.debug('user2 user into game')
#     g.user = u

#     g.building.append(make_icemine())
#     g.building.append(make_metalmine())

#     session.add(g)
#     session.commit()


if __name__ == '__main__':
    deldb()
    initdb()
