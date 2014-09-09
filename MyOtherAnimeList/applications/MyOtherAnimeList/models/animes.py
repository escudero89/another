# We define a new table for storing the Anime List
db = DAL('sqlite://webform.sqlite')
db.define_table('animes',
    Field('mal_id', requires=IS_NOT_EMPTY()),
    Field('name', requires=IS_NOT_EMPTY()),
    Field('score', requires=IS_NOT_EMPTY()))

