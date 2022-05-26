from odoo import fields, api, models, _


class LibraryInfo(models.Model):
    _name = 'library.info'
    _rec_name = 'student_name'
    _description = 'info of all the library'

    student_name = fields.Many2one('students.info', 'Student Name')
    # One2many fields
    book_ids = fields.One2many('library.info.line', 'book_id', 'Book ids')


class LibraryInfoLine(models.Model):
    _name = 'library.info.line'

    book_id = fields.Many2one('library.info', 'Book id')
    book_name_id = fields.Many2one('books.info','Books Name')
    issue_date = fields.Date('Issue Date')
