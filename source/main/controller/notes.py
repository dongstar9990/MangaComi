from source import app

from source.main.function.handleNotes import handleNotes
from source.main.function.handleNotes import delTruncNote
from source.main.function.handleNotes import trashGet
from source.main.function.handleNotes import trashRestore
from source.main.function.handleNotes import tickerBox
from source.main.function.handleNotes import getLastNote
from source.main.function.handleNotes import openLock
from source.main.function.handleNotes import getOnlyNote

app.add_url_rule('/notes/<string:param>',
                 methods=['GET', 'POST', "PATCH", "DELETE"], view_func=handleNotes)
app.add_url_rule('/only/<string:idNote>',
                 methods=['GET'], view_func=getOnlyNote)

app.add_url_rule('/open-note/<string:idNote>',
                 methods=["POST"], view_func=openLock)
app.add_url_rule('/trunc-notes/<string:id>',
                 methods=["DELETE"], view_func=delTruncNote)
app.add_url_rule('/trash/<string:idUser>',
                 methods=["GET"], view_func=trashGet)
app.add_url_rule('/trash-res/<string:id>',
                 methods=["POST"], view_func=trashRestore)

app.add_url_rule('/tick/<string:idData>',
                 methods=["PATCH"], view_func=tickerBox)
app.add_url_rule('/last-note',
                 methods=["GET"], view_func=getLastNote)
