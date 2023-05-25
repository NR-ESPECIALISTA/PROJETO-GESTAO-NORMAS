from odoo import api, fields, models


class NormasCalibracao(models.Model):
    _name = 'normas.calibracao'

    normas_id = fields.Integer()
    name = fields.Char(String='Normas de Calibração')