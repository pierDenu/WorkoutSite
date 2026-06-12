import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from sqlalchemy import Table, MetaData
from app import db
from app.run import app


def drop_table_by_name(table_name):
    with app.app_context():
        metadata = MetaData()
        metadata.reflect(bind=db.engine)
        table = Table(table_name, metadata, autoload_with=db.engine)
        table.drop(db.engine)
        print(f"Table '{table_name}' dropped successfully.")


if __name__ == "__main__":
    drop_table_by_name("muscle_groups")
