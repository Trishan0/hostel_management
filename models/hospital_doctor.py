from odoo import models, fields

class Doctor(models.Model):
    _name = 'hospital.doctor'  # New model for doctors
    _inherits = {'res.partner': 'partner_id'}  # Delegation inheritance
    
    partner_id = fields.Many2one('res.partner', required=True, ondelete='cascade')  # Reference to parent
    specialization = fields.Char(string="Specialization")
    license_number = fields.Char(string="Medical License No.")
