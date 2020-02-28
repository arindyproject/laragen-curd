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
            # //itemcolumns
            _item_columns = ""

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

            # read item rows
            for row in i['rows']:
                if row['show']:
                    _type_item_filter = ""
                    if row['ref'] == "":  # not refrerence / no select
                            # check type filter
                            if 'varchar' in row['item'][0]:
                                _type_item_filter = "filter: textFilter()"
                            elif 'int' in row['item'][0]:
                                _type_item_filter = "filter: numberFilter()"
                            elif 'date' in row['item'][0]:
                                _type_item_filter = "filter: dateFilter()"
                            elif 'text' in row['item'][0]:
                                _type_item_filter = "filter: textFilter()"
                            else :
                                _type_item_filter = ""
                    else:
                        pass
                    _item_columns += "\n\t\t\t{\n\t\t\t\tdataField : '" + \
                        row['row'] + "',\n"
                    _item_columns += "\t\t\t\ttext : '" + \
                        row['row'].capitalize() + "',\n"
                    _item_columns += "\t\t\t\tsort: true,\n"
                    _item_columns += "\t\t\t\t" + _type_item_filter + "\n"
                    _item_columns += "\n\t\t\t},"
            # itemcolumns
            _temp_table = _temp_table.replace(
                "//itemcolumns", _item_columns)
            # make file index
            # ================================================================================================
            with open('../../resources/js/pages/' + i['name'].lower() + '/Table' + i['name'].capitalize() + '.js', "w") as file_write:
                file_write.write(_temp_table)
                file_write.close()
