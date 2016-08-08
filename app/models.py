from . import db


class Comment(db.Model):
    __tablename__ = 'comments'
    com_id = db.Column(db.String(32), primary_key=True)
    com_time = db.Column(db.String(32))
    good = db.Column(db.Unicode(64))
    f_pic = db.Column(db.UnicodeText)
    f_rate = db.Column(db.UnicodeText)
    s_pic = db.Column(db.UnicodeText)
    s_rate = db.Column(db.UnicodeText)

    @staticmethod
    def generate_data():
        from sqlalchemy.exc import IntegrityError
        import os.path,json

        data_txt = open(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data.txt')), 'r')
        for item in data_txt:
            item=eval(item)
            c = Comment(com_id=item['id'],
                        com_time=item['gmtCreateTime'],
                        good=item['auctionSku'],
                        f_pic=str(item['pics']),
                        f_rate=item['rateContent'],
                        s_pic=str(item['appendPics']),
                        s_rate=item['appendComment'])
            db.session.add(c)
            try:
                db.session.commit()
            except ImportError:
                db.session.rollback()
        data_txt.close()
