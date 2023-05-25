from odoo import api, fields, models


class LinhasRamais(models.Model):
    _name = 'linhas.ramais'

    normas_id = fields.Integer()
    name = fields.Char(String='Linhas e Ramais')