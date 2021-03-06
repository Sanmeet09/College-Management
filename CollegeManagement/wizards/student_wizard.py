from odoo import fields, api, models, _
from odoo.exceptions import ValidationError


class StudentGraceWizard(models.TransientModel):
    _name = 'student.grace.wizard'
    _description = 'for adding grace marks'

    add_grace = fields.Integer('Add Grace')

    @api.onchange('add_grace')
    def on_change_marks(self):
        for rec in self:
            if rec.add_grace >= 20:
                raise ValidationError(_('20 se jyada umeed mat rkho'))

    @api.model
    def default_get(self, fields):
        res = super(StudentGraceWizard, self).default_get(fields)
        active_model = self.env.context.get('active_id')
        grace_id = self.env['students.info'].search([('id', '=', active_model)])
        res.update({
            'add_grace': grace_id.grace
        })
        return res

    def change_grace(self):
        active_model = self.env.context.get('active_id')
        students_id = self.env['students.info'].search([('id', '=', active_model)])
        students_id.update({
            'grace': self.add_grace
        })
