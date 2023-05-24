from flask import Flask
from flask_cors import CORS
from function.favorteManga import addFavoriteManga
from function.listFavoriteManga import getListFavoriteManga
from function.createUser import createUser
from function.addChapterReaded import addChapterReaded
from function.listChapterReaded import getListChapterReader
from function.listLast200Readed import getList200Reader
from function.addLinkAvatar import createAvatarUser
from function.addCreateCommentUser import addCommentUser
from function.listLast200Comment import List200commentUser
from function.listCommentUser import listCommentuser
from function.getTimeOnline import getTimeOnline
from function.checkOnline import checkOnline
from function.getListOnline import checkListOnline
from function.addCommentChapter import addCommentChapter
from function.listCommentChapter import listCommentChapter
from function.listLast200CommentChapter import List200commentChapter
app = Flask(__name__)
CORS(app)

app.add_url_rule("/mangaComi/createFavorite" ,methods=["POST","GET"],view_func=addFavoriteManga)
app.add_url_rule("/mangaComi/listFavoriteManga/idUser<int:iduser>" , methods=["GET"] , view_func=getListFavoriteManga)
app.add_url_rule("/mangaComi/createUser" , methods=["POST","GET"] , view_func=createUser)
app.add_url_rule("/mangaComi/createChapterReaded" , methods=["POST","GET"] , view_func=addChapterReaded)
app.add_url_rule("/mangaComi/listChapterReader/idUser<int:iduser>" , methods=["GET"] , view_func=getListChapterReader)
app.add_url_rule("/mangaComi/list200LastChapters/idUser" , methods=["GET"] , view_func=getList200Reader)
app.add_url_rule("/mangaComi/CreateAvatar/idUser" , methods=["GET","POST"] , view_func=createAvatarUser)
app.add_url_rule("/mangaComi/createCommentUser" ,methods=["POST","GET"],view_func= addCommentUser)
app.add_url_rule("/mangaComi/list200comment_user/idUser" , methods=["GET"] , view_func=List200commentUser)
app.add_url_rule("/mangaComi/listCommentUser/idUser<int:iduser>" , methods=["GET"] , view_func=listCommentuser)
app.add_url_rule("/mangaComi/timeOnline" , methods=["GET","POST"] , view_func=getTimeOnline)
app.add_url_rule("/mangaComi/checkOnline/idUser<int:iduser>" , methods=["GET"] , view_func=checkOnline)
app.add_url_rule("/mangaComi/checkListOnline" , methods=["GET"] , view_func=checkListOnline)
app.add_url_rule("/mangaComi/addCommentChapter" , methods=["GET","POST"] , view_func=addCommentChapter)
app.add_url_rule("/mangaComi/listCommentChapter/idUser<int:iduser>" , methods=["GET"] , view_func=listCommentChapter)
app.add_url_rule("/mangaComi/list200CommentChapter/idUser" , methods=["GET"] , view_func=List200commentChapter)
if __name__ == '__main__':
    app.run(host="0.0.0.0",port="9999")
