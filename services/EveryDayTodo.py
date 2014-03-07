# -*- coding: utf-8 -*-
__author__ = 'wangting'
from models.EveryDayTodo import TodoItem
from models.EveryDayTodo import EveryDayTodo


class EveryDayTodoService:

    @staticmethod
    def create(date):
        everyDayTodo = EveryDayTodo(date)
        return everyDayTodo

    @staticmethod
    def addNewItem(everDayTodoId, itemText):
        everyDayTodo = EveryDayTodoMapper.get(everDayTodoId)
        everyDayTodo.add(TodoItem(itemText))

    @staticmethod
    def addPomodoroClock(itemId):
        todoItem = TodoItemMapper.get(itemId)
        todoItem.increasePomodoroClock()


class EveryDayTodoMapper:

    @staticmethod
    def get(id):
        return EveryDayTodo('2014-3-5')

    @staticmethod
    def create(date):
        return EveryDayTodo(date)


class TodoItemMapper:

    @staticmethod
    def get(id):
        return TodoItem(id)

