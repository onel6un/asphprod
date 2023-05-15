from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session


engine = create_engine("sqlite+pysqlite:///db.db", echo=True)


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
    def filter_add_price(asphalt_id='NULL', asphalt_name='NULL', send='NULL',
                         breakstone='NULL', bitumen='NULL', climat_id='NULL',
                         category_id='NULL', durable='NULL'):
        with Session(engine) as s:
            query = '''
                SELECT *
                FROM factory
                    JOIN asph_price USING(factory_id)
                    JOIN asphalt
                        ON asph_price.asphalt_id = asphalt.asphalt_id
                    JOIN category
                        ON category.category_id = asphalt.category_id
                WHERE (:asphalt_id = "NULL"
                        or asphalt.asphalt_id = :asphalt_id)
                    AND (:asphalt_name = "NULL"
                         or asphalt_name = :asphalt_name)
                    AND (:send = "NULL" or send = :send)
                    AND (:breakstone = "NULL" or send = :send)
                    AND (:bitumen = "NULL" or bitumen = :bitumen)
                    AND (:climat_id = "NULL" or asphalt.climat_id = :climat_id)
                    AND (:category_id = "NULL"
                        or asphalt.category_id = :category_id)
                    AND (:durable = "NULL" or durable > :durable)
                ORDER BY price
            '''
        return s.execute(
                text(query),
                {'asphalt_name': asphalt_name, 'send': send,
                 'bitumen': bitumen, 'breakstone': breakstone,
                 'category_id': category_id, 'climat_id': climat_id,
                 'asphalt_id': asphalt_id, 'durable': durable}
            )

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

    @staticmethod
    def create(factory_name):
        with Session(engine) as s:
            query = '''
                INSERT INTO factory(factory_name)
                VALUES (:factory_name)
            '''

            s.execute(text(query), {'factory_name': factory_name})
            s.commit()


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

    @staticmethod
    def create(category_name, durable):
        with Session(engine) as s:
            query = '''
                INSERT INTO category(category_name, durable)
                VALUES (:category_name, :durable)
            '''

            s.execute(
                text(query),
                {'category_name': category_name, 'durable': durable}
            )
            s.commit()


class Climat:
    @staticmethod
    def all():
        with Session(engine) as s:
            query = '''
                SELECT *
                FROM climat
            '''

            return s.execute(text(query))

    @staticmethod
    def create(climat_name):
        with Session(engine) as s:
            query = '''
                INSERT INTO climat(climat_name)
                VALUES (:climat_name)
            '''

            s.execute(text(query), {'climat_name': climat_name})
            s.commit()


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
