# coding: UTF-8

import peewee

_db = peewee.SqliteDatabase('db/db.db')


class Test(peewee.Model):
    description = peewee.TextField()

    def to_dict(self):
        return {'id': self.id,
                'title': self.description}

    class Meta:
        database = _db