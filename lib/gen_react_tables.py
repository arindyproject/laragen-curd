__author__ = "Aji Ari Adam"
__copyright__ = "Copyright 2020, ArindyProject or AdamLabs"
__version__ = "0.0.1"

import json
from pathlib import Path

# read json tables
_json_tables = open('../json/tables.json').read()
_json_tables = json.loads(_json_tables)

for i in _json_tables:
    if(i['show']):  # check if tables to show
        Path("../../resources/js/components/" +
             i['name'].lower()).mkdir(parents=True, exist_ok=True)  # make directory in resources reactjs

        # make file table
        with open('../../resources/js/components/' + i['name'].lower() + '/' + i['name'].capitalize() + 'Table.js', "w") as file_write:
            file_write.write("hallo")
            file_write.close()
