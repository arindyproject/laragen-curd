import py_tables_json
import make_controller
import gen_react_view
import make_view


# read json tables
try:
    _json_tables = open('../json/tables.json').read()
    print('File tables.json ditemukan apakah anda ingin mengedit file tersebut atau lanjut?')
    _a = str(input('pencet "y" untuk lanjut / "r" untuk reset file : '))
    if _a.lower() == 'y':
        # make resourece controller
        make_controller.run()
        # make view react.js
        gen_react_view.run()
        # make view controller
        make_view.run()
    elif _a.lower() == 'r':
        # read database
        py_tables_json.run()
        # make resourece controller
        make_controller.run()
        # make view react.js
        gen_react_view.run()
        # make view controller
        make_view.run()
    else:
        print('silahkan edit file di "/json/tables.json".')
        exit()
except IOError:
    print("File tables.json ditemukan, membuat file....")
    py_tables_json.run()
    print('File tables.json ditemukan apakah anda ingin mengedit file tersebut atau lanjut?')
    _a = str(input('pencet "y" untuk lanjut / "n" untuk edit dulu : '))
    if _a.lower() == 'y':
        # make resourece controller
        make_controller.run()
        # make view react.js
        gen_react_view.run()
        # make view controller
        make_view.run()
    else:
        print('silahkan edit file di "/json/tables.json".')
        exit()
