__author__ = "Aji Ari Adam"
__copyright__ = "Copyright 2020, ArindyProject or AdamLabs"
__version__ = "0.0.1"

import json

#read template from /templates/lara/Controller.php
_temp_controller = open('../templates/lara/Controller.php','r').read()


'''----------------------------------------------------------------------------------
make table 
----------------------------------------------------------------------------------'''

#auth template
_auth_text= """/**
	* Create a new controller instance.
	*
	* @return void
	*/
	public function __construct(){
		$this->middleware('auth');
	}
	"""

#route web template
_route_text = ""

#read json tables
_json_tables = open('../json/tables.json').read()
_json_tables = json.loads(_json_tables)

for i in _json_tables:
	if(i['show']): #check make table or not
		_cont_name = i['name'].capitalize() + "Controller"
		_temp_cont = _temp_controller.replace('@controllername', _cont_name) #make controller class name

		#check if this controller use auth
		if(i['auth']):
			_temp_cont = _temp_cont.replace('//auth', _auth_text) #make __construct auth
		
		#make index controller
		_index_text = "$" + i['name'] + " = DB::table('" + i['name'] + "')->get(); \n\t\t" #make variabel data from database
		_index_text += "return response()->json([" + "'" + i['name'] + "'=>" + "$" + i['name'] + ","+ "]);" #make return to json 
		_temp_cont = _temp_cont.replace('//index', _index_text)

		#make file controller php
		with open('../../app/Http/Controllers/'+ _cont_name +'.php', "w") as file_write:
			file_write.write(_temp_cont)
			file_write.close()

		#make resourse route web
		_route_text += "\nRoute::resource('" + i['name'] + "', '" + _cont_name + "'); //by LaraGen_CURD"

		print("generate... "+ _cont_name)
	
#make file routes web
_read_route_web = open('../../routes/web.php', "r").read() #read route web
_route_web = open('../../routes/web.php', "a") #apped route web
if _route_text not in _read_route_web: #check if new route not in web.php file
	_route_web.write(_route_text) #apped new route into web.php
_route_web.close()


