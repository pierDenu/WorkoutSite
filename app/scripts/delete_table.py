from sqlalchemy import Table, MetaData
from app import create_app, db

app = create_app()


def drop_table_by_name(table_name):
    with app.app_context():
        metadata = MetaData()
        metadata.reflect(bind=db.engine)
        table = Table(table_name, metadata, autoload_with=db.engine)
        table.drop(db.engine)
        print(f"Table '{table_name}' dropped successfully.")


if __name__ == "__main__":
    drop_table_by_name("muscle_groups")
