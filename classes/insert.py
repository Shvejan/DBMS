import os
from cls import *
from flask import Flask,session
import csv
import random
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL3")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    os.chdir("C:/my files/II.II/DBMS/DBMS project/DBMS")
    """user = open("csv/users.csv")
    reader = csv.reader(user)
    for n,p in reader:
        x = users(name =n,password=p)
        print(x.name,x.password)
        db.session.add(x)
        db.session.commit()
    user.close()"""

    """event = open("csv/events.csv")
    reader = csv.reader(event)
    for a in reader:
        x=events(name=a[0])
        db.session.add(x)
        db.session.commit()
    event.close()"""

    """participant = open("csv/participants.csv")
    reader = csv.reader(participant)
    for n,c,co,m,e in reader:
        ev = random.randint(1,8)
        print(n,c,co,m,e,ev)
        x = participants(name =n ,city =c ,college =co ,mobile =m ,email =e ,e_id =ev )
        db.session.add(x)
        db.session.commit()
    participant.close()"""



if __name__ == '__main__':
    with app.app_context():
        main()
