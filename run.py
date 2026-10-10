from crawler import PLdataUpdate
from import_to_db import update_data

run = update_data()
run.upsert_all()