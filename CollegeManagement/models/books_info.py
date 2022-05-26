from odoo import fields, api, models, _


class BooksInfo(models.Model):
    _name = 'books.info'
    _rec_name = 'books_name'
    _description = 'info of all the books'

    books_name = fields.Char('Books')
    author = fields.Char('Author')
    generous = fields.Char('generous')
