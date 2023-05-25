from odoo import api, fields, models


class EquipDocumentacao(models.Model):
    _name = "equip.documentacao"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Documentações do Equipamento"

    tittle = fields.Char(string="TAG")
    validade = fields.Char(string="Validade")
    ndocumento = fields.Char(string="Nº do Documento")
    
    equip_doc_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF ?")
    equip_doc_image = fields.Image(
        string="Foto da documentação")
    equip_doc_pdf = fields.Binary(
        string='PDF da documentação')


    # ------------------------------------------
    # | Tipo Documentação                      |
    # ------------------------------------------
    tipo_documentacao = fields.Selection([
        ('relatorios', 'Relatórios e Laudos'),
        ('databook', 'Prontuário ou Databook'),
        ('teste_hidrostatico', 'Teste Hidrostático'),
        ('liquido_penetrante', 'Líquido Penetrante'),
        ('projeto_instalacao', 'Projeto de Instalação'),
        ('projeto_alteracao_reparo', 'Projeto de Alteração ou Reparo (PAR)'),
        ('certificado_treinamento', 'Certificados de Treinamentos'),
        ('livro_registro', 'Livro de Registros'),
        ('certificados_psv', 'Certificado Calibração PSV'),
        ('certificados_pi', 'Certificado Calibração PI'),
        ('art', 'A.R.T.'),

    ], string='Tipo de Documentação')

    # ------------------------------------------
    # | validade documentação                  |
    # ------------------------------------------

    documentacao_validade_date = fields.Date(
        string="Validade"
    )
