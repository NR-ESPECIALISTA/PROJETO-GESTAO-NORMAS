from odoo import api, fields, models


class TipoFluido(models.Model):
    _name = 'tipo.fluido'

    normas_id = fields.Integer()
    name = fields.Char(String='Tipo de Fluído')