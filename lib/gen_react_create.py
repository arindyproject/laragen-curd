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
        _item_form = ""
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
            # item form
            for _item in i['rows']:
                if(_item['row'] not in ['created_at', 'updated_at']):
                    if(_item['item'][4] != "auto_increment"):
                        # open
                        _item_form += '<Col sm="12" md="6" lg="4" xl="3"> \n<Form.Group controlId="form' + \
                            _item['row'].capitalize()+'">\n'
                        # label
                        _item_form += '<Form.Label>' + \
                            _item['row'].capitalize()+'</Form.Label>'
                        # input / select
                        # check required
                        _required_item = ""
                        if _item['item'][1] == "NO":
                            _required_item = "required"
                        if _item['ref'] == "":  # not refrerence / no select
                            # check type
                            _type_item = ""
                            if 'varchar' in _item['item'][0]:
                                _type_item = "text"
                            elif 'int' in _item['item'][0]:
                                _type_item = "number"
                            elif 'date' in _item['item'][0]:
                                _type_item = "date"

                            _item_form += '<Form.Control type="'+_type_item+'" placeholder="' + \
                                _item['row'].capitalize()+'" ' + \
                                _required_item+' />\n'
                        else:
                            _item_form += '<Form.Control as="select" '+_required_item+' >\n'
                            _item_form += '<option>1</option><option>2</option><option>3</option>\n'
                            _item_form += '</Form.Control>\n'
                        # close
                        _item_form += "</Form.Group> \n</Col>\n\n"
            # create form
            _temp_create = _temp_create.replace(
                '//item', _item_form)
            # make file index
            # ================================================================================================
            with open('../../resources/js/pages/' + i['name'].lower() + '/Create' + i['name'].capitalize() + '.js', "w") as file_write:
                file_write.write(_temp_create)
                file_write.close()
