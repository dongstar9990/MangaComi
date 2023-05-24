from source import app

from source.main.function.handleGroups import *

app.add_url_rule('/group',
                 methods=['GET', 'POST', "PATCH", "DELETE"], view_func=handleNotesGroup)
app.add_url_rule('/group/create',
                 methods=['POST'], view_func=createGroup)
app.add_url_rule('/group/add/<string:idGr>',
                 methods=['POST'], view_func=addMembers)
app.add_url_rule('/group/quit/<string>',
                 methods=['delete'], view_func=quitMembers)
