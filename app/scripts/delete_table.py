from sqlalchemy import Table, MetaData, inspect
from app import db
from app.run import app


def drop_table_by_name(table_name):
    with app.app_context():  # Створення контексту програми
        # Створення метаданих
        metadata = MetaData()
        metadata.reflect(bind=db.engine)

        # Пошук таблиці за іменем
        table = Table(table_name, metadata, autoload_with=db.engine)

        # Видалення таблиці
        table.drop(db.engine)
        print(f"Таблиця '{table_name}' успішно видалена.")


# Використання
drop_table_by_name("muscle_groups")

