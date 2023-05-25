from odoo import api, fields, models


class EquipVinculo(models.Model):
    _name = "equip.vinculo"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Vinculos do Equipamento"

    tittle = fields.Char(string='TAG')
    #equip_vinculo_press_trabalho = fields.Many2one(
    #    string="Pressão de Trabalho (kgf/cm²)")
    #equip_vinculo_pmta = fields.Float(string="PMTA (kgf/cm²)")
    #equip_vinculo_psv_press_ajuste = fields.Float(string="Pressão de Ajuste (kgf/cm²)")
    #equip_vinculo_pi_escala = fields.Float(string="Escala")
        
    # --------------------------
    # | Informações do Contato |
    # --------------------------
    #cliente_propri = fields.Many2one(
    #    'res.partner', string="Cliente Proprietario")
    #nome_contato = fields.Char(
    #    string="Nome do Contato", related="cliente_propri.child_ids.name")
    #email_contato = fields.Char(
    #    string="Email do Contato", related="cliente_propri.child_ids.email_formatted")
    #depar_respon = fields.Char(string="Departamento do Responsável")
    #local_instalacao = fields.Char(string="Local de Instalação")

    # ------------------------------------------
    # | Tipo de Equipamento                    |
    # ------------------------------------------
    #tipo_equipamento = fields.Selection([
    #    ('caldeira', 'Caldeira'),
    #    ('vaso_de_pressao', 'Vaso de Pressão'),
    #    ('tubulacao', 'Tubulação'),
    #    ('tanque', 'Tanque'),
    #    ('psv', 'PSV'),
    #    ('pi', 'PI'),

    #], string='Tipo de Equipamento')

    # ------------------------------------------
    # | validade documentação                  |
    # ------------------------------------------

    #documentacao_validade_date = fields.Date(
    #    string="Validade"
    #)
