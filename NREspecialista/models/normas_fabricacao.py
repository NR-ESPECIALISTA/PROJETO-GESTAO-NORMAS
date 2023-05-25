from odoo import api, fields, models


class NormasFabricacao(models.Model):
    _name = 'normas.fabricacao'

    normas_id = fields.Integer()
    name = fields.Char(String='Normas de Fabricação')