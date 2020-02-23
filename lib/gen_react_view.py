__author__ = "Aji Ari Adam"
__copyright__ = "Copyright 2020, ArindyProject or AdamLabs"
__version__ = "0.0.1"

import json
from pathlib import Path


def run():
    import gen_react_tables
    import gen_react_create
    print('         +-------------------------------------------+')
    print('         |           Make Ui with ReactJs            |')
    print('         +-------------------------------------------+')

    # read app.js
    _app = open('../../resources/js/app.js', 'r').read()

    # read json tables
    _json_tables = open('../json/tables.json').read()
    _json_tables = json.loads(_json_tables)

    # read temlate reacjs index / tabs
    _react_index = open('../templates/reactjs/index/index_default.js').read()

    for i in _json_tables:
        _temp_index = _react_index
        _tabs_item = ""
        _import_item = ""
        # membuat tabs / Index
        # ================================================================================================
        Path("../../resources/js/pages/" +
             i['name'].lower()).mkdir(parents=True, exist_ok=True)  # make directory in resources reactjs
        print(i['name'].lower() + " " + ("=" * (65 - len(i['name']))))
        print('--> make dir "/pages/' + i['name'].lower() + '"')
        print('--> generate class table or file "Index' +
              i['name'].capitalize() + '.js"')
        # check if need view / table
        # ================================================================================================
        if("table" in i["action"]):
            # create table class and file
            gen_react_tables.react_make_table(i['name'])
            print('--> generate class table or file "Table' +
                  i['name'].capitalize() + '.js"')
            # add item tabs table
            _tabs_item += '\t\t\t\t<Tab eventKey="table" title="Table"><Table' + \
                i['name'].capitalize()+' /></Tab>\n'
            # import class table
            _import_item += "\nimport Table" + \
                i['name'].capitalize() + " from './Table" + \
                i['name'].capitalize() + "';"

        # check if need create / add
        # ================================================================================================
        if("create" in i["action"]):
            # create create class and file
            gen_react_create.react_make_create(i['name'])
            print('--> generate class create or file "Create' +
                  i['name'].capitalize() + '.js"')
            # add item tabs create
            _tabs_item += '\t\t\t\t<Tab eventKey="create" title="Add New ' + \
                i['name'].capitalize()+'"><Create' + \
                i['name'].capitalize()+' /></Tab>\n'
            # import class create
            _import_item += "\nimport Create" + \
                i['name'].capitalize() + " from './Create" + \
                i['name'].capitalize() + "';"

        # make file index
        # ================================================================================================
        with open('../../resources/js/pages/' + i['name'].lower() + '/Index' + i['name'].capitalize() + '.js', "w") as file_write:
            # nama class index
            _temp_index = _temp_index.replace(
                "name_class", 'Index' + i['name'].capitalize())
            # nama
            _temp_index = _temp_index.replace(
                "//name",  i['name'].capitalize())
            # name id
            _temp_index = _temp_index.replace(
                '@nameid', 'index' + i['name'].lower())
            # add tabs items
            _temp_index = _temp_index.replace(
                '//tabitem', _tabs_item)
            # import class
            _temp_index = _temp_index.replace(
                '//import', _import_item)
            file_write.write(_temp_index)
            file_write.close()

        # edit file app.js
        # ================================================================================================
        _app_text = "require('./pages/" + \
            i['name'].lower() + "/Index"+i['name'].capitalize()+"');\n"
        print('__> add require "./pages/' +
              i['name'].lower() + "/Index"+i['name'].capitalize()+'" in app.s')
        if _app_text not in _app:
            _app_new = open('../../resources/js/app.js', "a")
            _app_new.write(_app_text)
            _app_new.close()

        _temp_index = ""

    print("Done")
