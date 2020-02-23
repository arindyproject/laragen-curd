__author__ = "Aji Ari Adam"
__copyright__ = "Copyright 2020, ArindyProject or AdamLabs"
__version__ = "0.0.1"

import json
from pathlib import Path


def run():

    print('         +-------------------------------------------+')
    print('         |           Make View Controller            |')
    print('         +-------------------------------------------+')

    # read template from /templates/lara/Controller.php
    _temp_controller = open('../templates/lara/ViewController.php', 'r').read()

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
        _cont_name = i['name'].capitalize() + "ViewController"
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
                '//auth', _auth_text)  # make __construct //auth

        '''-------------------------------------------------------------------------------------
        membuat  index ViewController.php
        -------------------------------------------------------------------------------------'''
        _temp_cont = _temp_cont.replace(
            '//index', "return View('"+i['name'].lower()+".index');")  # index dir views
        '''-------------------------------------------------------------------------------------
        membuat route
        -------------------------------------------------------------------------------------'''
        # make resourse route web
        _route_text += "\nRoute::get('" + i['name'] + \
            "', '" + _cont_name + "@index'); //by LaraGen_CURD"

        print("generate... " + _cont_name)

        '''-------------------------------------------------------------------------------------
        membuat file blade view
        -------------------------------------------------------------------------------------'''
        Path("../../resources/views/" +
             i['name'].lower()).mkdir(parents=True, exist_ok=True)  # check directory
        with open('../../resources/views/' + i['name'].lower() + '/index.blade.php', "w") as file_write:
            _text_view = "@extends('layouts.app') \n@section('content')\n<div class='container'>"
            _text_view += '<div id="index'+i['name'].lower()+'"></div>\n'
            _text_view += '</div>\n@endsection'
            file_write.write(_text_view)
            file_write.close()

        '''-------------------------------------------------------------------------------------
        membuat file Controller.php
        -------------------------------------------------------------------------------------'''
        # make file controller php
        with open('../../app/Http/Controllers/' + _cont_name + '.php', "w") as file_write:
            file_write.write(_temp_cont)
            file_write.close()

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
