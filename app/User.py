''' User Model '''
from config.database import Model


class User(Model):
    ''' User Model '''

    __fillable__ = ['name', 'email', 'password', 'is_admin', 'bio',
                    'website', 'facebook', 'twitter', 'github', 'gitlab', ]

    __auth__ = 'email'
