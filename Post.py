# -*- coding: utf-8 -*-

import peewee

_db = peewee.SqliteDatabase('db.db')

class Post(peewee.Model):
    title = peewee.CharField()
    content = peewee.TextField()
    emitDate = peewee.TextField()
    expireDate = peewee.TextField()

    def to_dict(self):
        return {'id':self.id,
                'title':self.title,
                'content':self.content,
                'emitDate':self.emitDate,
                'expireDate':self.expireDate}

    class Meta:
        database = _db