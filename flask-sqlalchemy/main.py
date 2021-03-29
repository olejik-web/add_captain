from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = 'captain'
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = 'scott_chief@mars.org'

    user2 = User()
    user2.surname = "Олег"
    user2.name = "Еремичев"
    user2.age = 21
    user2.position = 'captain'
    user2.speciality = "research engineer"
    user2.address = "module_1"
    user2.email = 'oleg_eremichew@mars.org'

    user3 = User()
    user3.surname = "Олег2"
    user3.name = "Еремичев2"
    user3.age = 21
    user3.position = 'captain'
    user3.speciality = "research engineer"
    user3.address = "module_1"
    user3.email = 'oleg_eremichew2@mars.org'

    user4 = User()
    user4.surname = "Олег3"
    user4.name = "Еремичев3"
    user4.age = 21
    user4.position = 'captain'
    user4.speciality = "research engineer"
    user4.address = "module_1"
    user4.email = 'oleg_eremichew3@mars.org'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.add(user4)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()
