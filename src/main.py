import analyze
import chartHandler
from ptt import GetPttPost
from db import DB


db = DB()
db.create()

datas = GetPttPost(10)
for data in datas:
    if db.get(data['title']).fetchall():
        db.update(db.get_id(data['title']).fetchall()[0][0], data['url'], data['author'], data['date'], data['push'])
    else:
        analyze_data = analyze.nlp(data['title'].replace('Re: ', '').replace('[新聞] ', '').replace('[爆卦] ', '').replace('[問卦] ', '').replace('[協尋]', ''))
        db.store(data['title'], data['url'], data['author'], data['date'], data['push'], analyze_data)


chartHandler.handle_data(db.get_all())
chartHandler.handle_push(db.get_all())
