__author__ = "Aji Ari Adam"
__copyright__ = "Copyright 2020, ArindyProject or AdamLabs"
__version__ = "0.0.1"

import json
from pathlib import Path

# read json tables
_json_tables = open('../json/tables.json').read()
_json_tables = json.loads(_json_tables)

# read temlate reacjs index / tabs
_react_create = open('../templates/reactjs/create/create_default.js').read()


def react_make_create(name):
    for i in _json_tables:
        _temp_create = _react_create
        if(i['name'] == name):  # check table name
            # nama class index
            _temp_create = _temp_create.replace(
                "name_class", 'Create' + i['name'].capitalize())
            # nama
            _temp_create = _temp_create.replace(
                "//name",  i['name'].capitalize())
            # name id
            _temp_create = _temp_create.replace(
                '@nameid', 'create' + i['name'].lower())
            # make file index
            # ================================================================================================
            with open('../../resources/js/pages/' + i['name'].lower() + '/Create' + i['name'].capitalize() + '.js', "w") as file_write:
                file_write.write(_temp_create)
                file_write.close()
