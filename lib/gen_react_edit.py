__author__ = "Aji Ari Adam"
__copyright__ = "Copyright 2020, ArindyProject or AdamLabs"
__version__ = "0.0.1"

import json
from pathlib import Path

# read json tables
_json_tables = open('../json/tables.json').read()
_json_tables = json.loads(_json_tables)

# read temlate reacjs index / tabs
_react_edit = open('../templates/reactjs/edit/edit_default.js').read()


def react_make_edit(name):
    for i in _json_tables:
        _temp_edit = _react_edit
        _item_form = ""
        _state_item = ""
        _handle_item_function = ""
        _bind_item_function = ""
        _data_item = ""
        _item_value = ""
        _state_item_options = ""
        _componentdidmount = ""
        if(i['name'] == name):  # check table name
            # nama class index
            _temp_edit = _temp_edit.replace(
                "name_class", 'Edit' + i['name'].capitalize())
            # nama
            _temp_edit = _temp_edit.replace(
                "//name",  i['name'].capitalize())
            # name id
            _temp_edit = _temp_edit.replace(
                '@nameid', 'edit' + i['name'].lower())
            # item form
            for _item in i['rows']:

                if(_item['row'] not in ['created_at', 'updated_at']):
                    if(_item['item'][4] != "auto_increment"):
                        # make state item
                        _state_item += "\t\t\t" + \
                            _item['row'].lower() + " : '',\n"
                        # make bind function item
                        _bind_item_function += "\t\tthis.handle" + \
                            _item['row'].capitalize()+" = this.handle" + \
                            _item['row'].capitalize()+".bind(this);\n"
                        # make function handle item form
                        _handle_item_function += "\thandle" + \
                            _item['row'].capitalize() + "(e){\n"
                        _handle_item_function += "\t\tthis.setState({\n\t\t\t" + _item['row'].lower(
                        ) + " : e.target.value \n\t\t})\n"
                        _handle_item_function += "\t}\n"
                        # data item
                        _data_item += "\t\t\t" + \
                            _item['row'].lower() + " : this.state." + \
                            _item['row'].lower() + ",\n"
                        # //valueofitem
                        _item_value += "\n\t\t\t\t" + \
                            _item['row'].lower() + " : response.data." + \
                            i['name'].lower() + "." + _item['row'].lower() + ","
                        # open
                        _item_form += '<Col sm="12" md="6" lg="4" xl="3"> \n<Form.Group controlId="form' + \
                            _item['row'].capitalize()+'">\n'

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
                            elif 'text' in _item['item'][0]:
                                _type_item = "textarea"

                            # label
                            _item_form += '<Form.Label>' + \
                                _item['row'].capitalize()+'</Form.Label>\n'

                            _item_form += '<Form.Control onChange={this.handle'+_item['row'].capitalize()+'} value={this.state.'+_item['row'].lower()+'} type="'+_type_item+'" placeholder="' + \
                                _item['row'].capitalize()+'" ' + \
                                _required_item+' />\n'
                        else:
                            # label
                            _item_form += '<Form.Label> <a href="' + \
                                _item['ref'][0].lower(
                                )+'">+ '+_item['row'].capitalize()+'</a></Form.Label>\n'
                            # _componentdidmount
                            _componentdidmount = "this.getOptions();"
                            # make state item
                            _state_item += "\t\t\t" + \
                                _item['row'].lower() + "Options : [],\n"
                            _item['row'].lower() + " : '',\n"
                            # make state item options
                            _state_item_options += "\t\t" + \
                                _item['row'].lower() + "Options : response.data." + \
                                _item['ref'][0].lower() + ",\n"
                            # make select form
                            _item_form += '<Form.Control onChange={this.handle'+_item['row'].capitalize(
                            )+'} value={this.state.'+_item['row'].lower()+'} as="select" '+_required_item+' >\n'
                            _item_form += "{this.state."+_item['row'].lower(
                            ) + "Options.map((data)=> <option key={data.value} value={data.value}>{data.name}</option>)}\n"
                            _item_form += '</Form.Control>\n'
                        # close
                        _item_form += "</Form.Group> \n</Col>\n\n"
            # edit form
            _temp_edit = _temp_edit.replace(
                '//item', _item_form)
            # make state item
            _temp_edit = _temp_edit.replace(
                '//stateitem', _state_item)
            # make state options item
            _temp_edit = _temp_edit.replace(
                '//stateoptionsitems', _state_item_options)
            # make bind function item
            _temp_edit = _temp_edit.replace(
                '//binditem', _bind_item_function)
            # data item
            _temp_edit = _temp_edit.replace(
                '//dataitem', _data_item)
            # url update
            _temp_edit = _temp_edit.replace(
                '//url', 'gen/' + i['name'].lower())
            # url data
            _temp_edit = _temp_edit.replace(
                '//dataurl', i['name'].lower())
            # //valueofitem
            _temp_edit = _temp_edit.replace("//valueofitem", _item_value)

            # edit handle function
            _temp_edit = _temp_edit.replace(
                '//handleitem', _handle_item_function)
            # _componentdidmount
            _temp_edit = _temp_edit.replace(
                '//componentdidmount', _componentdidmount)
            # make file index
            # ================================================================================================
            with open('../../resources/js/pages/' + i['name'].lower() + '/Edit' + i['name'].capitalize() + '.js', "w") as file_write:
                file_write.write(_temp_edit)
                file_write.close()
