from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


engine = create_engine("sqlite+pysqlite:///db.db")


class Price:
    @staticmethod
    def all():
        with Session(engine) as s:
            query = '''
                SELECT *
                FROM asph_price
                    join factory USING(factory_id)
                    join asphalt USING(asphalt_id)
            '''

            return s.execute(text(query))

    @staticmethod
    def create(asphalt_id, factory_id, price):
        with Session(engine) as s:
            query = '''
                INSERT INTO asph_price(asphalt_id, factory_id, price)
                VALUES (:asphalt_id,
                    :factory_id,
                    :price)
            '''

            s.execute(
                text(query),
                {'asphalt_id': asphalt_id, 'factory_id': factory_id,
                 'price': price}
            )
            s.commit()

    @staticmethod
    def delete(price_id):
        with Session(engine) as s:
            query = '''
                DELETE FROM asph_price
                WHERE price_id = :price_id
            '''

            s.execute(
                text(query),
                {'price_id': price_id}
            )
            s.commit()


class Asphalt:
    @staticmethod
    def all():
        with Session(engine) as s:
            query = '''
                SELECT *
                FROM asphalt
                    join climat USING(climat_id)
                    join category USING(category_id)
            '''

            return s.execute(text(query))

    @staticmethod
    def delete(asphalt_id):
        with Session(engine) as s:
            query = '''
                DELETE FROM asphalt
                WHERE asphalt_id = :asphalt_id
            '''

            s.execute(
                text(query),
                {'asphalt_id': asphalt_id}
            )
            s.commit()

    @staticmethod
    def create(asphalt_name, send, bitumen, breakstone, category_id,
               climat_id):
        with Session(engine) as s:
            query = '''
                INSERT INTO asphalt(
                    asphalt_name,
                    send,
                    bitumen,
                    breakstone,
                    category_id,
                    climat_id
                )
                VALUES (
                    :asphalt_name,
                    :send,
                    :bitumen,
                    :breakstone,
                    :category_id,
                    :climat_id
                )
            '''

            s.execute(
                text(query),
                {'asphalt_name': asphalt_name, 'send': send,
                 'bitumen': bitumen, 'breakstone': breakstone,
                 'category_id': category_id, 'climat_id': climat_id}
            )
            s.commit()

    @staticmethod
    def last():
        with Session(engine) as s:
            query = '''
                SELECT *
                FROM asphalt
                ORDER BY asphalt_id DESC
                LIMIT 1
            '''

            return s.execute(text(query))

    @staticmethod
    def update(asphalt_id, asphalt_name, send, bitumen, breakstone,
               category_id, climat_id):
        with Session(engine) as s:
            query = '''
                UPDATE asphalt
                    SET asphalt_name = :asphalt_name,
                        send = :send,
                        bitumen = :bitumen,
                        breakstone = :breakstone,
                        category_id = :category_id,
                        climat_id = :climat_id
                    WHERE asphalt_id = :asphalt_id
            '''

        s.execute(
                text(query),
                {'asphalt_name': asphalt_name, 'send': send,
                 'bitumen': bitumen, 'breakstone': breakstone,
                 'category_id': category_id, 'climat_id': climat_id,
                 'asphalt_id': asphalt_id}
            )
        s.commit()

    @staticmethod
    def del_supp(asphalt_id):
        with Session(engine) as s:
            query = '''
                DELETE FROM asph_supp
                WHERE asphalt_id = :asphalt_id
            '''

            s.execute(
                text(query),
                {'asphalt_id': asphalt_id}
            )
            s.commit()


class Factory:
    @staticmethod
    def all():
        with Session(engine) as s:
            query = '''
                SELECT *
                FROM factory
            '''

            return s.execute(text(query))


class Supplement:
    @staticmethod
    def all():
        with Session(engine) as s:
            query = '''
                SELECT *
                FROM supplement
            '''

            return s.execute(text(query))

    @staticmethod
    def filter(asphalt_id):
        with Session(engine) as s:
            query = '''
                SELECT supplement_id, supplement_name, amount
                FROM asph_supp
                    JOIN supplement USING(supplement_id)
                WHERE asphalt_id = :asphalt_id
            '''

            return s.execute(text(query), {'asphalt_id': asphalt_id})


class Category:
    @staticmethod
    def all():
        with Session(engine) as s:
            query = '''
                SELECT *
                FROM category
            '''

            return s.execute(text(query))


class Climat:
    @staticmethod
    def all():
        with Session(engine) as s:
            query = '''
                SELECT *
                FROM climat
            '''

            return s.execute(text(query))


class AsphSupp:
    @staticmethod
    def create(asphalt_id, supplement_id, amount):
        with Session(engine) as s:
            query = '''
                INSERT INTO asph_supp(
                    asphalt_id,
                    supplement_id,
                    amount
                )
                VALUES (
                    :asphalt_id,
                    :supplement_id,
                    :amount
                )
            '''

            s.execute(
                text(query),
                {'asphalt_id': asphalt_id,
                 'supplement_id': supplement_id,
                 'amount': amount}
            )
            s.commit()
