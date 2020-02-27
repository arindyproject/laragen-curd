__author__ = "Aji Ari Adam"
__copyright__ = "Copyright 2020, ArindyProject or AdamLabs"
__version__ = "0.0.1"

import json
from pathlib import Path

# read json tables
_json_tables = open('../json/tables.json').read()
_json_tables = json.loads(_json_tables)

# read temlate reacjs index / tabs
_react_table = open('../templates/reactjs/table/table_default.js').read()


def react_make_table(name):
    for i in _json_tables:
        _temp_table = _react_table
        if(i['name'] == name):  # check table name
            # nama class index
            _temp_table = _temp_table.replace(
                "name_class", 'Table' + i['name'].capitalize())
            # nama
            _temp_table = _temp_table.replace(
                "//name",  i['name'].capitalize())
            # name id
            _temp_table = _temp_table.replace(
                '@nameid', 'table' + i['name'].lower())
            # get url
            _temp_table = _temp_table.replace(
                "//url", "gen/" + i['name'].lower())
            # data name
            _temp_table = _temp_table.replace(
                "//dataname",  i['name'].lower())
            # make file index
            # ================================================================================================
            with open('../../resources/js/pages/' + i['name'].lower() + '/Table' + i['name'].capitalize() + '.js', "w") as file_write:
                file_write.write(_temp_table)
                file_write.close()
