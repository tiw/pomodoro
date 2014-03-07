# -*- coding: utf-8 -*-
__author__ = 'wangting'


class EveryDayTodo:
    def __init__(self, date):
        self.date = date
        self.items = []

    def addTodoItem(self, item):
        self.items.append(item)

    def getTodoItems(self):
        return self.items


class TodoItem:

    def __init__(self, text):
        self.text = text

    def setText(self, text):
        self.text = text

    def getText(self):
        return self.text

    def increasePomodoroClock(self):
        self.pomodoroClock =+ 1

    def addExternalInterrupt(self, interrupt):
        self.externalInterrupts.add(interrupt)

    def addInternalInterrupt(self, interrupt):
        self.internalInterrupts.add(interrupt)


class UnplannedTodoItems:
    def __init__(self):
        self.items = set()

    def addItem(self, item):
        self.items.add(item)

    def deleteItem(self, item):
        self.items.remove(item)


class PomodoroClock:
    pass


class ExternalInterrupt:
    pass


class InternalInterrupt:
    pass


