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
                {'asphalt_id': asphalt_id, 'factory_id': factory_id, 'price': price}
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


class Factory:
    @staticmethod
    def all():
        with Session(engine) as s:
            query = '''
                SELECT *
                FROM factory
            '''

            return s.execute(text(query))
