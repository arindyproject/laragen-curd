__author__ = "Aji Ari Adam"
__copyright__ = "Copyright 2020, ArindyProject or AdamLabs"
__version__ = "0.0.1"


from pathlib import Path  # python3 only
from dotenv import load_dotenv
import os
import mysql.connector
import json


# load file .env to get database connetion
env_path = Path('../../') / '.env'
load_dotenv(dotenv_path=env_path)
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# table json
table_json = []

# connect to database
mydb = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    passwd=DB_PASSWORD,
    database=DB_DATABASE
)
cursor = mydb.cursor()
cursor_reff = mydb.cursor(buffered=True)
cursor_reff_val = mydb.cursor(buffered=True)
cursor.execute("SHOW TABLES")  # get all tables
tables = cursor.fetchall()  # var all tables
for i in tables:
    # not including table "failed_jobs", "migrations", "password_resets", "users"
    if i[0] not in ["failed_jobs", "migrations", "password_resets", "users"]:
        print("+----------------------------------------------------------+")
        print("|  " + i[0])
        print("+----------------------------------------------------------+")
        cursor.execute("DESC " + i[0])
        table = cursor.fetchall()

        # --------------------------------------------------
        print("| references :")
        cursor_reff.execute(
            "SELECT CONCAT(table_name, '.', column_name) AS 'foreign key', CONCAT(referenced_table_name, '.', referenced_column_name) AS 'references', constraint_name AS 'constraint name' FROM information_schema.key_column_usage WHERE referenced_table_name IS NOT NULL AND TABLE_NAME='" + i[0] + "' AND TABLE_SCHEMA='"+DB_DATABASE+"'")
        ref = cursor_reff.fetchall()
        for j in ref:
            print("| " + str(j))
        # --------------------------------------------------

        tbl = {"name": i[0], "show": True, "auth": True,
               "template": 'default', "action": ["view", "edit", "delete"], "ref": len(ref)}
        rows = []

        print("+----------------------------------------------------------+")
        for item in table:
            print("| " + str(item))
            value = item[0]
            ref_tab = ""
            for ref_i in ref:
                if(i[0] in ref_i[0].split('.')[:1] and item[0] in ref_i[0].split('.')[1:]):
                    ref_tab = ref_i[1].split('.')
                    cursor_reff_val.execute("DESCRIBE " + ref_tab[0])
                    value = cursor_reff_val.fetchall()[1][0] # [1] is position colunm name
            rows.append({"row": item[0], "show": True,
                         "value": value, "ref": ref_tab})

        tbl["rows"] = rows
        table_json.append(tbl)
        print("+----------------------------------------------------------+\n")

sorted_string = json.dumps(table_json, indent=4, sort_keys=True)
# print(sorted_string)
with open('../json/tables.json', "w") as file_write:
    # write json data into file
    json.dump(table_json, file_write)
