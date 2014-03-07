# -*- coding: utf-8 -*-
import sys

__author__ = 'wangting'

from flask import Flask, abort, jsonify, Response, json, request

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
engine = create_engine('mysql://root:@localhost:3308/pomodoro')
Session = sessionmaker(bind=engine)
session = Session()

# -------- DB Model -----


Base = declarative_base()


class EverydayTodo(Base):
    __tablename__ = 'everyday_todos'

    id = Column(Integer, primary_key=True)
    date = Column(String)
    def __repr__(self):
        return "<EverydayTodo(date='%s')>" % (self.date)


# -------- web app -----

app = Flask(__name__)

@app.route("/api/v1/everyday-todo/<date>", methods=['PUT'])
def create(date):

    everyday_todo = EverydayTodo(date=date)
    global session
    try:
        session.add(everyday_todo)
        session.commit()
    except:
        session.rollback()
        print "Unexpected error:", sys.exc_info()[0]
        abort(500)
    if not everyday_todo:
        abort(500)
    return Response("ok", 201)

@app.route("/api/v1/everyday-todo/<date>", methods=['POST'])
def update(date):
    # get everyday-todo
    # update the everyday-todo
    post_date = request.form['date']
    everyday_todo = session.query(EverydayTodo).filter(EverydayTodo.date == date)
    if not everyday_todo:
        abort(500)
    everyday_todo.date = post_date
    #session.
    pass




if __name__ == "__main__":
    app.run(debug=True)
