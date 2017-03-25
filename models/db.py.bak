# -*- coding: utf-8 -*-
db = DAL("sqlite://storage.sqlite")

db.define_table('faces',
                Field('user_id', 'integer', unique=False),
                Field('pic_num', 'integer'),
                Field('file', 'upload'),
                format = '%(user_id)s')
