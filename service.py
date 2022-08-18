from models import *
from config import db
import json


def insert_data(model, input_data):
    """
    Заполняет таблицы
    """

    for row in input_data:
        db.session.add(
            model(
                **row
            )
        )

    db.session.commit()


def get_all(model):
    """
    Возвращает запрашиваемую таблицу
    """
    result = []
    for row in db.session.query(model).all():
        result.append(row.to_dict())
    return result


def get_by_pk(model, pk):
    """
    Возвращает значения по id
    """
    try:
        return db.session.query(model).get(pk).to_dict()
    except Exception:
        return "Пользователя с таким id не существует"


def get_all_union(model, model2, pk):
    """
    Функция объединения данных из 2х таблиц Offer и User
    """
    data = db.session.query(model, model2).join(model2).filter(model.id == pk).all()
    if len(data) == 0:
        return "Пользователя с таким id не существует"
    else:
        data = data[0]
        result = data[0].to_dict()
        result.update(data[1].to_dict())
        return result


def update_values(model, pk, values):
    """
    Обновляем данные по id
    """
    try:
        db.session.query(model).filter(model.id == pk).update(values)
        db.session.commit()
    except Exception:
        return "Пользователя с таким id не существует"


def delete_by_pk(model, pk):
    """
    Удаляем данныые по id
    """
    try:
        db.session.query(model).filter(model.id == pk).delete()
        db.session.commit()
    except Exception as e:
        print(e)
        return "Пользователя с таким id не существует"


def init_db():
    """
    Создаём db
    """
    db.drop_all()
    db.create_all()

    with open("fixtures/users.json", encoding='utf-8') as file:
        insert_data(User, json.load(file))

    with open("fixtures/orders.json", encoding='utf-8') as file:
        insert_data(Order, json.load(file))

    with open("fixtures/offers.json", encoding='utf-8') as file:
        insert_data(Offer, json.load(file))

