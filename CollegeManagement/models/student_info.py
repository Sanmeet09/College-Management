from odoo import fields, api, models, _
from _datetime import date
from dateutil.relativedelta import relativedelta


class StudentsInfo(models.Model):
    _name = 'students.info'
    _rec_name = 'first_name'
    _description = 'Module of student details'

    first_name = fields.Char('First Name')
    last_name = fields.Char('Last Name')
    full_name = fields.Char('Full name')
    roll_no = fields.Integer('Roll No')
    gender = fields.Selection(selection=[('M', 'Male'), ('F', 'Female')], default='M')
    dob = fields.Date('Date of birth')
    age = fields.Integer('Age', compute='_cal_age', store=True)
    phone = fields.Char('Phone No', size=10)
    email = fields.Char('Email-Id')

    # notebook
    reading = fields.Boolean('Reading')
    Swim = fields.Boolean('Swimming')
    dance = fields.Boolean('Dancing')

    # educational details
    chemistry = fields.Integer('Chemistry', required=True)
    physics = fields.Integer('Physics', required=True)
    maths = fields.Integer('Maths', required=True)
    english = fields.Integer('English', required=True)
    total = fields.Integer('Total', compute='total_marks', store=True)
    percentage = fields.Integer('Percentage')
    status = fields.Char('Status', compute='status_of_marks', store=True)
    check_status = fields.Boolean('check status', compute='check_status_info', store=True)
    grace = fields.Integer('Add Grace')

    # subject
    many_books = fields.Many2many(comodel_name='books.info', string='Books')

    # state for selecting
    state = fields.Selection(selection=[('draft', 'Draft'), ('confirm', 'Confirm'), ('cancel', 'Cancel')],
                             default='draft')

    # full name program
    @api.onchange('first_name', 'last_name')
    def fill_full_name(self):
        for rec in self:
            if rec.first_name and rec.last_name:
                rec.full_name = rec.first_name + ' ' + rec.last_name

    # total of all the marks
    @api.depends('chemistry', 'physics', 'maths', 'english', 'grace')
    def total_marks(self):
        for rec in self:
            if rec.chemistry and rec.physics and rec.maths and rec.english:
                rec.total = rec.chemistry + rec.physics + rec.maths + rec.english + rec.grace
                rec.percentage = (rec.total / 400) * 100

    # @api.onchange('total')
    # def percentage_of_subjects(self):
    #     for rec in self:
    #         if rec.total:

    @api.depends('percentage')
    def status_of_marks(self):
        for rec in self:
            if rec.percentage:
                if rec.percentage > 40:
                    rec.status = 'Pass'
                else:
                    rec.status = 'Fail'

    @api.depends('status')
    def check_status_info(self):
        for rec in self:
            if rec.status:
                if rec.status == 'Fail':
                    rec.check_status = True
                else:
                    rec.check_status = False

    @api.depends('dob')
    def _cal_age(self):
        for i in self:
            today = date.today()
            i.age = relativedelta(today, i.dob).years

    def action_confirm(self):
        for rec in self:
            rec.state = 'confirm'

    def action_cancel(self):
        for rec in self:
            rec.state = 'cancel'

    def action_url(self):
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': 'https://www.youtube.com/'
        }
