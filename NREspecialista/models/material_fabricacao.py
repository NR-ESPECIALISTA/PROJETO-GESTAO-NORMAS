from odoo import api, fields, models


class MaterialFabricacao(models.Model):
    _name = 'material.fabricacao'

    normas_id = fields.Integer()
    name = fields.Char(String='Material de Fabricação')