__author__ = "Aji Ari Adam"
__copyright__ = "Copyright 2020, ArindyProject or AdamLabs"
__version__ = "0.0.1"

import json


def run():

    # read template from /templates/lara/Controller.php
    _temp_controller = open('../templates/lara/Controller.php', 'r').read()

    print('         +-------------------------------------------+')
    print('         |           Make Resource Controller        |')
    print('         +-------------------------------------------+')

    '''----------------------------------------------------------------------------------
    make table
    ----------------------------------------------------------------------------------'''

    # auth template
    _auth_text = """/**
        * Create a new controller instance.
        *
        * @return void
        */
        public function __construct(){
            $this->middleware('auth');
        }
        """

    # route web template
    _route_text = ""

    # read json tables
    _json_tables = open('../json/tables.json').read()
    _json_tables = json.loads(_json_tables)

    '''-------------------------------------------------------------------------------------
    make cotroller file
    make index controller
    -------------------------------------------------------------------------------------'''
    for i in _json_tables:
        _cont_name = i['name'].capitalize() + "Controller"
        _temp_cont = _temp_controller.replace(
            '@controllername', _cont_name)  # make controller class name

        '''-------------------------------------------------------------------------------------
        reset file Controller.php
        -------------------------------------------------------------------------------------'''
        # make file controller php
        with open('../../app/Http/Controllers/' + _cont_name + '.php', "w") as file_write:
            file_write.write(_temp_cont)
            file_write.close()

        # check if this controller use auth
        if(i['auth']):
            _temp_cont = _temp_cont.replace(
                '//auth', _auth_text)  # make __construct auth

        '''-------------------------------------------------------------------------------------
        membuat table / index Controller.php
        -------------------------------------------------------------------------------------'''
        if("table" in i["action"]):  # check make table or not
            # make index controller
            if i['ref'] > 0:
                _index_text = "$" + i['name'] + \
                    " = DB::table('" + i['name'] + "')\n"
                _select_text = "\t\t->select('" + i['name'] + ".*'"
                for ref_i in i["rows"]:
                    if(ref_i['ref'] != ""):
                        _select_text += ",'" + \
                            ref_i['ref'][0] + "." + ref_i['value'] + \
                            " as " + ref_i['row'] + "'"
                        _index_text += "\t\t->leftjoin('" + ref_i['ref'][0] + "', '" + i['name'] + "." + ref_i['row'] + \
                            "', '=', '" + ref_i['ref'][0] + \
                            "." + ref_i['ref'][1] + "')\n"
                _select_text += ")"
                _index_text += _select_text
                _index_text += "\n\t\t->orderBy('id','DESC')->get();\n\t\t"
            else:
                # make variabel data from database
                _index_text = "$" + i['name'] + \
                    " = DB::table('" + i['name'] + "')->get(); \n\t\t"

            # make return to json
            _index_text += "return response()->json([" + "'" + \
                i['name'] + "'=>" + "$" + i['name'] + "," + "]);"
            _temp_cont = _temp_cont.replace('//index', _index_text)

        '''-------------------------------------------------------------------------------------
        membuat create / store Controller.php
        -------------------------------------------------------------------------------------'''
        if("create" in i["action"]):  # check make create and store or not

            _create_text = ""
            _create_text_return = ""

            _store_text = ""
            _validation_text = "$request->validate(["
            _store_db_text = "\t\t$" + i['name'] + \
                " = DB::table('" + i['name'] + "')->insertGetId(["

            # membuat store method
            for ref_i_s in i["rows"]:
                # membuat validasi
                if ref_i_s['row'] not in ["id", "created_at", "updated_at"]:
                    _val_requred = 'nullable'
                    if ref_i_s['item'][1] == "NO":
                        _val_requred = 'required'
                    _validation_text += "\n\t\t\t'" + \
                        ref_i_s['row'] + "' => '" + _val_requred + "',"

                # membuat db insert
                    _store_db_text += "\n\t\t\t'" + ref_i_s['row'] + \
                        "' => $request->" + ref_i_s['row'] + ","
                if ref_i_s['row'] in ["created_at", "updated_at"]:
                    _store_db_text += "\n\t\t\t'" + \
                        ref_i_s['row']+"' => date('Y-m-d H:i:s'),"

            # membuat create method
            if i['ref'] > 0:  # cek jika punya table refrensi
                for ref_i in i["rows"]:
                    if(ref_i['ref'] != ""):
                        # membuat create method
                        _create_text += "$" + \
                            ref_i['ref'][0] + \
                            " = DB::table('" + \
                            ref_i['ref'][0] + \
                            "')->select('id as value', '" + \
                            ref_i['value'] + " as name')->get(); \n\t\t"
                        _create_text_return += "'" + \
                            ref_i['ref'][0] + "' => $" + ref_i['ref'][0] + ","
                        # end membuat create method

            # make return to json
            _create_text += "return response()->json([" + \
                _create_text_return+"]);"
            _temp_cont = _temp_cont.replace('//create', _create_text)

            # membuat store dan create method
            _validation_text += "\n\t\t]);\n"
            _store_db_text += "\n\t\t]);\n"
            _store_db_text += "\n\t\t$data = DB::table('" + \
                i['name'] + "')->where('id', $"+i['name']+")->first();"
            _store_db_text += "\n\t\treturn response()->json(['" + \
                i['name']+"' => $data]);"
            _temp_cont = _temp_cont.replace(
                '//store', _validation_text + _store_db_text)

        '''-------------------------------------------------------------------------------------
        membuat show / view Controller.php
        -------------------------------------------------------------------------------------'''
        if("view" in i["action"]):  # check make show
            _show_text = "$" + \
                i['name'] + " =  DB::table('"+i['name'] + \
                "')->where('id', $id)->first(); \n"
            _show_text += "\t\treturn response()->json([" + "'" + \
                i['name'] + "'=>" + "$" + i['name'] + "," + "]);"

            _temp_cont = _temp_cont.replace(
                '//show', _show_text)

        '''-------------------------------------------------------------------------------------
        membuat edit / update Controller.php
        -------------------------------------------------------------------------------------'''
        if("edit" in i["action"]):  # check make edit
            # edit method
            _edit_text = ""
            _edit_text += "$" + i['name'] + " = DB::table('" + \
                i['name'] + "')->where('id', $id) -> first(); \n\t\t"
            _edit_text_return = "'" + i['name'] + "' => $" + i['name'] + ","

            if i['ref'] > 0:  # cek jika punya table refrensi
                for ref_i in i["rows"]:
                    if(ref_i['ref'] != ""):
                        # membuat create method
                        _edit_text += "$" + \
                            ref_i['ref'][0] + \
                            " = DB::table('" + \
                            ref_i['ref'][0] + \
                            "')->pluck('" + ref_i['value'] + "','id'); \n\t\t"
                        _edit_text_return += "'" + \
                            ref_i['ref'][0] + "' => $" + ref_i['ref'][0] + ","

            # make edit return
            _edit_text += "return response()->json(["+_edit_text_return+"]);"
            _temp_cont = _temp_cont.replace('//edit', _edit_text)

            # update method
            _update_db_text = "\t\t$" + \
                i['name'] + " = DB::table('" + i['name'] + \
                "')->where('id', $id)\n\t\t\t->update(["
            _validation_text = "$request->validate(["
            for ref_i_s in i["rows"]:
                # membuat validasi
                if ref_i_s['row'] not in ["id", "created_at", "updated_at"]:
                    _val_requred = 'nullable'
                    if ref_i_s['item'][1] == "NO":
                        _val_requred = 'required'
                    _validation_text += "\n\t\t\t'" + \
                        ref_i_s['row'] + "' => '" + _val_requred + "',"

                # membuat db insert
                    _update_db_text += "\n\t\t\t\t'" + ref_i_s['row'] + \
                        "' => $request->" + ref_i_s['row'] + ","

                if ref_i_s['row'] in ["updated_at"]:
                    _update_db_text += "\n\t\t\t\t'" + \
                        ref_i_s['row']+"' => date('Y-m-d H:i:s'),"

            _validation_text += "\n\t\t]);\n"

            # membuat return update
            _update_db_text += "\n\t\t\t]);"
            _update_db_text += "\n\t\treturn response()->json(['" + \
                i['name']+"' => $"+i['name']+"]);"
            _temp_cont = _temp_cont.replace(
                '//update', _validation_text + _update_db_text)

        '''-------------------------------------------------------------------------------------
        membuat destroy / delete Controller.php
        -------------------------------------------------------------------------------------'''
        if("delete" in i["action"]):  # check make destroy
            _delete_text = "$" + i['name'] + " =  DB::table('"+i['name'] + \
                "')->where('id', $id)->delete(); \n"
            _delete_text += "\n\t\treturn response()->json(['" + \
                i['name']+"' => $"+i['name']+"]);"
            # membuat delete / destroy method
            _temp_cont = _temp_cont.replace('//destroy', _delete_text)

        '''-------------------------------------------------------------------------------------
        membuat file Controller.php
        -------------------------------------------------------------------------------------'''
        # make file controller php
        with open('../../app/Http/Controllers/' + _cont_name + '.php', "w") as file_write:
            file_write.write(_temp_cont)
            file_write.close()

        '''-------------------------------------------------------------------------------------
        membuat route
        -------------------------------------------------------------------------------------'''
        # make resourse route web
        _route_text += "\nRoute::resource('gen/" + i['name'] + \
            "', '" + _cont_name + "'); //by LaraGen_CURD"

        print("generate... " + _cont_name)

    '''-------------------------------------------------------------------------------------
    menambahkan route controller ke file web.php
    -------------------------------------------------------------------------------------'''
    # make file routes web
    _read_route_web = open('../../routes/web.php',
                           "r").read()  # read route web
    _route_web = open('../../routes/web.php', "a")  # apped route web
    if _route_text not in _read_route_web:  # check if new route not in web.php file
        _route_web.write(_route_text)  # apped new route into web.php
    _route_web.close()
