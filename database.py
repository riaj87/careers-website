import sqlalchemy
from sqlalchemy import create_engine, text
import os

my_secret = os.environ['DB_CONNECTION_STRING']

engine = create_engine(my_secret)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(sqlalchemy.text("select * from jobs"))
        jobs = []
        for row in result.all():
            jobs.append(row._asdict())
        return jobs
