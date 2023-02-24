from odoo import api, fields, models


# ------------------------------------------------------------------------------
# Ele não atualiza esse arquivo se apresentar um erro na declaração de variavel!
# Precisa Desinstalar esse modulo, logo em seguida derrubar o serviço e subir.
# ------------------------------------------------------------------------------

class NrEquipamento(models.Model):
    _name = "nr.equipamento"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Nr-Especialista | Gestão de Equipamentos e Inspeções"

    @api.model
    def create(self, vals):
        vals['equipamento_id'] = self.env['ir.sequence'].next_by_code(
            'equip.sequence')
        return super(NrEquipamento, self).create(vals)

    imagem_equip = fields.Image(string="Image")
    name = fields.Char(string="Nome do Equipamento",
                       required=True, copy=False, index=True)  # tracking=True
    equipamento_id = fields.Char(string="ID")
    state = fields.Selection([
        ('em_adequacao', 'EM ADEQUAÇÃO'),
        ('aprovado', 'APROVADO'),
        ('reprovado', 'REPROVADO'),
        ('desativado', 'DESATIVADO'),
        ('desenquadrado', 'DESENQUADRADO')], default='em_adequacao', string='Status', required=True)

    responsavel_id = fields.Many2one(
        'res.partner', string="Responsável")
    contrato_id = fields.Many2one(
        'res.company', string="Contrato")

    nr13 = fields.Boolean(string="NR-13")
    nr12 = fields.Boolean(string="NR-12")
    nr11 = fields.Boolean(string="NR-11")
    nr10 = fields.Boolean(string="NR-10")

    tipo_equip = fields.Selection(
        [('caldeira', 'CALDEIRA'),
         ('vaso_de_pressao', 'VASO DE PRESSÃO'),
         ('tubulacao', 'TUBULAÇÃO'),
         ('tanque', 'TANQUE'),
         ('psv', 'PSV'),
         ('pi', 'PI')], string='Tipo de Equipamento')

    # ------------------------------
    # | Informações do Equipamento |
    # ------------------------------
    desc_equip = fields.Char(string="Descrição do Equipamento")
    normas_fabri_ids = fields.Many2many(
        'x_normas_fabricacao', string="Normas de Fabricação")
    normas_calibracao_ids = fields.Many2many(
        'x_normas_calibracao', string="Normas de Calibração")
    fabricante_id = fields.Many2one('res.partner', string="Fabricante")
    ano_fabri = fields.Integer(string="Ano de Fabricação")
    num_serie = fields.Integer(string="Número de Série")
    lote = fields.Integer(string="Lote")

    # --------------------------
    # | Informações do Contato |
    # --------------------------
    cliente_propri = fields.Many2one(
        'res.partner', string="Cliente Proprietario")
    nome_contato = fields.Char(
        string="Nome do Contato", related="cliente_propri.child_ids.name")
    email_contato = fields.Char(
        string="Email do Contato", related="cliente_propri.child_ids.email_formatted")
    depar_respon = fields.Char(string="Departamento do Responsável")
    local_instalacao = fields.Char(string="Local de Instalação")

    # -------------------------
    # | Equipamento Vinculado |
    # -------------------------
    equip_instrumen_psv = fields.Selection(
        [('sim', 'Sim'),
         ('nao', 'Não')], string="Tem PSV ou qualquer dispositivo de segurança?"
    )
    equip_instrumen_pi = fields.Selection(
        [('sim', 'Sim'),
         ('nao', 'Não')], string="Tem PI ou qualquer dispositivo para monitorar pressão?"
    )

    equip_relacional_ids = fields.Many2many(
        'nr.equipamento', 'equipamento_name', 'name', string="Informe uma Tag relacionada")

    # ------------------------------
    # | Dados Técnicos da Caldeira |
    # ------------------------------
    equip_cal_capacidade = fields.Float(
        string="Caldeira - Capacidade (ton/hora)")
    equip_cal_pmta = fields.Float(string="Caldeira - PMTA (kgf/cm²)")
    equip_cal_press_trabalho = fields.Float(
        string="Caldeira - Pressão de Trabalho (kgf/cm²)")
    equip_cal_press_teste = fields.Float(
        string="Caldeira - Pressão de Teste (kgf/cm²)")
    equip_cal_temp_projeto = fields.Char(
        string="Caldeira - Temperatura de Projeto (ºC)")
    equip_cal_temp_operacao = fields.Char(
        string="Caldeira - Temperatura de Operação (ºC)")
    equip_cal_volume = fields.Float(string="Caldeira - Volume(m³)")
    equip_cal_material_fabri_ids = fields.Many2many(
        'x_material_fabricacao', 'name', string="Material de Fabricação")
    equip_cal_ambiente_instalacao = fields.Selection(
        [('aberto', 'Aberto'),
         ('fechado', 'Fechado')], string="Ambiente de instalação")
    equip_cal_tipo_fluido_id = fields.Many2one(
        'x_tipo_fluido', string="Tipo de Fluido")

    # ---------------------------------------
    # | Dados Técnicos do Vaso - Lado Casco |
    # ---------------------------------------
    equip_vaso_casco_tubo = fields.Boolean(string="Casco e Tubo?")
    equip_vaso_casco_press_trabalho = fields.Float(
        string="Pressão de Trabalho (kgf/cm²)")
    equip_vaso_casco_pmta = fields.Float(string="PMTA (kgf/cm²)")
    equip_vaso_casco_press_teste = fields.Float(
        string="Pressão de Teste (kgf/cm²)")
    equip_vaso_casco_temp_projeto = fields.Char(
        string="Temperatura de Projeto (ºC)")
    equip_vaso_casco_temp_operacao = fields.Char(
        string="Temperatura de Operação (ºC)")
    equip_vaso_casco_compri_altura = fields.Float(
        string="Comprimento/Altura (mm)")
    equip_vaso_casco_diametro = fields.Float(string="Diâmetro (mm)")
    equip_vaso_casco_volume = fields.Float(string="Volume (m³)")
    equip_vaso_casco_mat_fabricacao_ids = fields.Many2many(
        'x_material_fabricacao', 'name', string="Material de Fabricação")
    equip_vaso_casco_tipo_fluidos = fields.Selection([
        ('acido_sulfurico', 'ÁCIDO SULFÚRICO'),
        ('ar_comprimido', 'AR COMPRIMIDO'),
        ('agua', 'ÁGUA'),
        ('tinta', 'TINTA'),
        ('desengraxante', 'DESENGRAXANTE'),
        ('clorato_de_sodio', 'CLORATO DE SÓDIO'),
        ('peroxido_de_hidrogenio', 'PERÓXIDO DE HIDROGÊNIO'),
        ('mother_liquor_eletrolito', 'MOTHER LIQUOR - ELETRÓLITO'),
        ('helio', 'HÉLIO'),
        ('nitrogenio', 'NITROGÊNIO'),
        ('hidrogenio', 'HIDROGÊNIO'),
        ('vapor_de_agua', 'VAPOR DE ÁGUA'),
        ('eletrolito', 'ELETRÓLITO'),
        ('dioxido_de_cloro', 'DIÓXIDO DE CLORO'),
        ('soda_caustica', 'SODA CAUSTICA'),
        ('diesel', 'DIESEL'),
        ('ar_oleo', 'AR/ÓLEO')], string="Tipo de Fluido")
    equip_vaso_casco_cal_pxv = fields.Char(
        string="Calculo PxV", compute="casco_cal_pxv")
    equip_vaso_casco_pxv_class = fields.Float(
        string="PxV Classificação", compute="casco_pxv_classificacao")
    equip_vaso_casco_grupo_risco = fields.Char(
        string="Grupo Potencial de Risco", compute="casco_cal_grupo_risco")
    equip_vaso_casco_classe_fluido = fields.Char(
        string="Classe do Fluido ", compute="casco_cal_classe_fluido")
    equip_vaso_casco_categoria = fields.Selection([
        ('cat_1', 'CAT I'),
        ('cat_2', 'CAT II'),
        ('cat_3', 'CAT III'),
        ('cat_4', 'CAT IV'),
        ('cat_5', 'CAT V'),
        ('n_a', 'N/A')], string="Categoria")

    @api.depends('equip_vaso_casco_press_trabalho', 'equip_vaso_casco_volume')
    def casco_cal_pxv(self):
        for rec in self:
            rec.equip_vaso_casco_cal_pxv = round(
                rec.equip_vaso_casco_press_trabalho * 98.068 * rec.equip_vaso_casco_volume, 2)

    @api.depends('equip_vaso_casco_press_trabalho', 'equip_vaso_casco_volume')
    def casco_pxv_classificacao(self):
        for rec in self:
            rec.equip_vaso_casco_pxv_class = round(
                rec.equip_vaso_casco_press_trabalho * 0.09806 * rec.equip_vaso_casco_volume, 2)

    @api.depends('equip_vaso_casco_pxv_class')
    def casco_cal_grupo_risco(self):
        for rec in self:
            if rec.equip_vaso_casco_pxv_class < 1:
                rec.equip_vaso_casco_grupo_risco = "GRUPO 5"
            elif rec.equip_vaso_casco_pxv_class >= 1 and rec.equip_vaso_casco_pxv_class < 2.5:
                rec.equip_vaso_casco_grupo_risco = "GRUPO 4"
            elif rec.equip_vaso_casco_pxv_class >= 2.5 and rec.equip_vaso_casco_pxv_class < 30:
                rec.equip_vaso_casco_grupo_risco = "GRUPO 3"
            elif rec.equip_vaso_casco_pxv_class >= 30 and rec.equip_vaso_casco_pxv_class < 100:
                rec.equip_vaso_casco_grupo_risco = "GRUPO 2"
            elif rec.equip_vaso_casco_pxv_class >= 100:
                rec.equip_vaso_casco_grupo_risco = "GRUPO 1"

    @api.depends('equip_vaso_casco_tipo_fluidos')
    def casco_cal_classe_fluido(self):
        for rec in self:
            if rec.equip_vaso_casco_tipo_fluidos == "acido_sulfurico":
                rec.equip_vaso_casco_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_casco_tipo_fluidos == "ar_comprimido":
                rec.equip_vaso_casco_classe_fluido = "CLASSE C"
            elif rec.equip_vaso_casco_tipo_fluidos == "agua":
                rec.equip_vaso_casco_classe_fluido = "CLASSE D"
            elif rec.equip_vaso_casco_tipo_fluidos == "tinta":
                rec.equip_vaso_casco_classe_fluido = "CLASSE "
            elif rec.equip_vaso_casco_tipo_fluidos == "desengraxante":
                rec.equip_vaso_casco_classe_fluido = "CLASSE "
            elif rec.equip_vaso_casco_tipo_fluidos == "clorato_de_sodio":
                rec.equip_vaso_casco_classe_fluido = "CLASSE D"
            elif rec.equip_vaso_casco_tipo_fluidos == "peroxido_de_hidrogenio":
                rec.equip_vaso_casco_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_casco_tipo_fluidos == "mother_liquor_eletrolito":
                rec.equip_vaso_casco_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_casco_tipo_fluidos == "helio":
                rec.equip_vaso_casco_classe_fluido = "CLASSE C"
            elif rec.equip_vaso_casco_tipo_fluidos == "nitrogenio":
                rec.equip_vaso_casco_classe_fluido = "CLASSE C"
            elif rec.equip_vaso_casco_tipo_fluidos == "hidrogenio":
                rec.equip_vaso_casco_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_casco_tipo_fluidos == "vapor_de_agua":
                rec.equip_vaso_casco_classe_fluido = "CLASSE C"
            elif rec.equip_vaso_casco_tipo_fluidos == "eletrolito":
                rec.equip_vaso_casco_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_casco_tipo_fluidos == "dioxido_de_cloro":
                rec.equip_vaso_casco_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_casco_tipo_fluidos == "soda_caustica":
                rec.equip_vaso_casco_classe_fluido = "CLASSE D"
            elif rec.equip_vaso_casco_tipo_fluidos == "diesel":
                rec.equip_vaso_casco_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_casco_tipo_fluidos == "ar_oleo":
                rec.equip_vaso_casco_classe_fluido = "CLASSE B"
            else:
                rec.equip_vaso_casco_classe_fluido = "Nenhum Fluido Selecionado!"
    # --------------------------------------
    # | Dados Técnicos do Vaso - Lado Tubo |
    # --------------------------------------
    equip_vaso_tubo_press_trabalho = fields.Float(
        string="Pressão de Trabalho (kgf/cm²)")
    equip_vaso_tubo_pmta = fields.Float(
        string="PMTA (kgf/cm²)")
    equip_vaso_tubo_press_teste = fields.Float(
        string="Pressão de Teste (kgf/cm²)")
    equip_vaso_tubo_temp_projeto = fields.Char(
        string="Temperatura de Projeto (ºC)")
    equip_vaso_tubo_temp_operacao = fields.Char(
        string="Temperatura de Operação (ºC)")
    equip_vaso_tubo_volume = fields.Float(string="Volume (m³)")
    equip_vaso_tubo_mat_fabricacao_ids = fields.Many2many(
        'x_material_fabricacao', 'name', string="Material de Fabricação")
    equip_vaso_tubo_tipo_fluido = fields.Selection([
        ('acido_sulfurico', 'ÁCIDO SULFÚRICO'),
        ('ar_comprimido', 'AR COMPRIMIDO'),
        ('agua', 'ÁGUA'),
        ('tinta', 'TINTA'),
        ('desengraxante', 'DESENGRAXANTE'),
        ('clorato_de_sodio', 'CLORATO DE SÓDIO'),
        ('peroxido_de_hidrogenio', 'PERÓXIDO DE HIDROGÊNIO'),
        ('mother_liquor_eletrolito', 'MOTHER LIQUOR - ELETRÓLITO'),
        ('helio', 'HÉLIO'),
        ('nitrogenio', 'NITROGÊNIO'),
        ('hidrogenio', 'HIDROGÊNIO'),
        ('vapor_de_agua', 'VAPOR DE ÁGUA'),
        ('eletrolito', 'ELETRÓLITO'),
        ('dioxido_de_cloro', 'DIÓXIDO DE CLORO'),
        ('soda_caustica', 'SODA CAUSTICA'),
        ('diesel', 'DIESEL'),
        ('ar_oleo', 'AR/ÓLEO')], string="Tipo de Fluido")
    equip_vaso_tubo_cal_pxv = fields.Char(
        string="Calculo PxV", compute="tubo_calc_pxv")
    equip_vaso_tubo_pxv_class = fields.Float(
        string="PxV Classificação", compute="tubo_calc_pxv_class")
    equip_vaso_tubo_grupo_risco = fields.Char(
        string="Grupo Potencial de Risco", compute="tubo_calc_grupo_risco")
    equip_vaso_tubo_classe_fluido = fields.Char(
        string="Classe do Fluido", compute="tubo_calc_classe_fluido")
    equip_vaso_tubo_categoria = fields.Selection([
        ('cat_1', 'CAT I'),
        ('cat_2', 'CAT II'),
        ('cat_3', 'CAT III'),
        ('cat_4', 'CAT IV'),
        ('cat_5', 'CAT V'),
        ('n_a', 'N/A')], string="Categoria")

    @api.depends('equip_vaso_tubo_press_trabalho', 'equip_vaso_tubo_volume')
    def tubo_calc_pxv(self):
        for rec in self:
            rec.equip_vaso_tubo_cal_pxv = round(
                rec.equip_vaso_tubo_press_trabalho * 98.068 * rec.equip_vaso_tubo_volume, 2)

    @api.depends('equip_vaso_tubo_press_trabalho', 'equip_vaso_tubo_volume')
    def tubo_calc_pxv_class(self):
        for rec in self:
            rec.equip_vaso_tubo_pxv_class = round(
                rec.equip_vaso_tubo_press_trabalho * 0.09806 * rec.equip_vaso_tubo_volume, 2)

    @api.depends('equip_vaso_tubo_pxv_class')
    def tubo_calc_grupo_risco(self):
        for rec in self:
            if rec.equip_vaso_tubo_pxv_class < 1:
                rec.equip_vaso_tubo_grupo_risco = "GRUPO 5"
            elif rec.equip_vaso_tubo_pxv_class >= 1 and rec.equip_vaso_tubo_pxv_class < 2.5:
                rec.equip_vaso_tubo_grupo_risco = "GRUPO 4"
            elif rec.equip_vaso_tubo_pxv_class >= 2.5 and rec.equip_vaso_tubo_pxv_class < 30:
                rec.equip_vaso_tubo_grupo_risco = "GRUPO 3"
            elif rec.equip_vaso_tubo_pxv_class >= 30 and rec.equip_vaso_tubo_pxv_class < 100:
                rec.equip_vaso_tubo_grupo_risco = "GRUPO 2"
            elif rec.equip_vaso_tubo_pxv_class >= 100:
                rec.equip_vaso_tubo_grupo_risco = "GRUPO 1"

    @api.depends('equip_vaso_tubo_tipo_fluido')
    def tubo_calc_classe_fluido(self):
        for rec in self:
            if rec.equip_vaso_tubo_tipo_fluido == "acido_sulfurico":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_tubo_tipo_fluido == "ar_comprimido":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE C"
            elif rec.equip_vaso_tubo_tipo_fluido == "agua":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE D"
            elif rec.equip_vaso_tubo_tipo_fluido == "tinta":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE "
            elif rec.equip_vaso_tubo_tipo_fluido == "desengraxante":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE "
            elif rec.equip_vaso_tubo_tipo_fluido == "clorato_de_sodio":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE D"
            elif rec.equip_vaso_tubo_tipo_fluido == "peroxido_de_hidrogenio":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_tubo_tipo_fluido == "mother_liquor_eletrolito":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_tubo_tipo_fluido == "helio":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE C"
            elif rec.equip_vaso_tubo_tipo_fluido == "nitrogenio":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE C"
            elif rec.equip_vaso_tubo_tipo_fluido == "hidrogenio":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_tubo_tipo_fluido == "vapor_de_agua":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE C"
            elif rec.equip_vaso_tubo_tipo_fluido == "eletrolito":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_tubo_tipo_fluido == "dioxido_de_cloro":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_tubo_tipo_fluido == "soda_caustica":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE D"
            elif rec.equip_vaso_tubo_tipo_fluido == "diesel":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE A"
            elif rec.equip_vaso_tubo_tipo_fluido == "ar_oleo":
                rec.equip_vaso_tubo_classe_fluido = "CLASSE B"
            else:
                rec.equip_vaso_tubo_classe_fluido = "Selecione um tipo de fluido!"
    # -------------------------------
    # | Dados Técnicos da Tubulação |
    # -------------------------------
    equip_tubu_linhas_ramais_ids = fields.Many2many(
        'x_linhas_ramais', string="Linhas e Ramais")
    equip_tubu_pmta = fields.Float(string="PMTA(kgf/cm²)")
    equip_tubu_press_trabalho = fields.Float(
        string="Pressão de Trabalho (kgf/cm²)")
    equip_tubu_press_teste = fields.Float(string="Pressão de Teste (kgf/cm²)")
    equip_tubu_temp_projeto = fields.Char(string="Temperatura de Projeto (ºC)")
    equip_tubu_temp_operacao = fields.Char(
        string="Temperatura de Operação (ºC)")
    equip_tubu_volume = fields.Float(string="Tubulação - Volume (m³)")
    equip_tubu_mat_fabricacao_ids = fields.Many2many(
        'x_material_fabricacao', 'name', string="Material de Fabricação")
    equip_tubu_tipo_fluido_id = fields.Many2one(
        'x_tipo_fluido', string="Tipo de Fluido")
    equip_tubu_isolamento = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Possui isolamento?")

    # ----------------------------
    # | Dados Técnicos do Tanque |
    # ----------------------------
    equip_tanque_press_trabalho = fields.Float(
        string="Pressão de Trabalho (kgf/cm²)")
    equip_tanque_temp_projeto = fields.Char(
        string="Temperatura de Projeto (ºC)")
    equip_tanque_temp_operacao = fields.Char(
        string="Temperatura de Operação (ºC)")
    equip_tanque_volume = fields.Float(string="Volume(m³)")
    equip_tanque_altura = fields.Float(string="Altura (mm)")
    equip_tanque_diametro_interno = fields.Float(
        string="Diâmetro interno (mm)")
    equip_tanque_mat_fabricacao_ids = fields.Many2many(
        'x_material_fabricacao', 'name', string="Material de Fabricação")
    equip_tanque_tipo_fluido_id = fields.Many2one(
        'x_tipo_fluido', string="Tipo de Fluido")

    # -------------------------
    # | Dados Técnicos da PSV |
    # -------------------------
    equip_psv_press_ajuste = fields.Float(string="Pressão de Ajuste (kgf/cm²)")
    equip_psv_temp_operacao = fields.Float(
        string="Temperatura de Operação (ºC)")
    equip_psv_diametro_entrada = fields.Char(string="Diâmetro de entrada (mm)")
    equip_psv_diametro_saida = fields.Char(string="Diâmetro de saída (mm)")
    equip_psv_tipo_conexao = fields.Selection([
        ('flangeada', 'Flangeada'),
        ('roscada', 'Roscada')], string="Tipo de conexão")
    equip_psv_alavanca = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Com alavanca?")
    equip_psv_castelo = fields.Selection([
        ('aberto', 'Aberto'),
        ('fechado', 'Fechado'),
        ('nao_possui', 'Não Possui')], string="Castelo")
    equip_psv_mat_fabricacao_ids = fields.Many2many(
        'x_material_fabricacao', 'name', string="Material de Fabricação")
    equip_psv_tipo_fluido_id = fields.Many2one(
        'x_tipo_fluido', string="Tipo de Fluido")

    # ------------------------
    # | Dados Técnicos do PI |
    # ------------------------
    equip_pi_tipo_manometro = fields.Selection([
        ('simples', 'SIMPLES'),
        ('pressao_absoluta', 'PRESSÃO ABSOLUTA'),
        ('duplo', 'DUPLO'),
        ('diferencial', 'DIFERENCIAL'),
        ('manovacuometro', 'MANOVACUÔMETRO')], string="Tipo de manômetro")
    equip_pi_escala_pressao = fields.Char(string="Escala de Pressão (kgf/cm²)")
    equip_pi_diametro_caixa = fields.Char(string="Diâmetro da Caixa (mm)")
    equip_pi_material_caixa = fields.Selection([
        ('plastico_abs', 'PLÁSTICO ABS'),
        ('aco_carbono', 'AÇO CARBONO'),
        ('latao_forjado', 'LATÃO FORJADO'),
        ('aco_inox', 'AÇO INOX')], string="Material da Caixa")
    equip_pi_visor = fields.Selection([
        ('vidro', 'VIDRO'),
        ('policarbonato', 'POLICARBONATO')], string="Visor")
    equip_pi_enchimento = fields.Selection([
        ('glicerina', 'GLICERINA'),
        ('silicone', 'SILICONE'),
        ('nenhum', 'NENHUM')], string="Enchimento")
    equip_pi_posicao = fields.Selection([
        ('vertical', 'VERTICAL'),
        ('horizontal', 'HORIZONTAL')], string="Posição")
    equip_pi_conexao = fields.Selection([
        ('npt_conica', 'NPT (cônica)'),
        ('bspt_conica', 'BSPT (cônica)'),
        ('bsp_paralela', 'BSP (paralela)'),
        ('metrica_paralela', 'MÉTRICA (paralela)'),
        ('unf_refrigeracao', 'UNF (Refrigeração)')], string="Conexão")
    equip_pi_temp_trabalho = fields.Float(
        string="Temperatura de Trabalho (ºC)")
    equip_pi_tipo_fluido_id = fields.Many2one(
        'x_tipo_fluido', string="Tipo de Fluido")

    # ------------------------
    # | Documentação do Vaso |
    # | RELATÓRIOS E LAUDOS  |
    # ------------------------
    equip_doc_vaso_exame_externo_relatorio = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Vaso tem relatório de exame externo?")
    equip_doc_vaso_exame_externo_validade_date = fields.Date(
        string="Próximo vencimento Exame Externo do Vaso")
    equip_doc_vaso_exame_externo_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF ?")
    equip_doc_vaso_exame_externo_image = fields.Image(
        string="Foto Relatório - Externo")
    # equip_doc_vaso_exame_externo_pdf_ids = fields.One2many(string="Histórico de Relatórios Externos")

    equip_doc_vaso_exame_interno_relatorio = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Vaso tem relatório de exame interno?")
    equip_doc_vaso_exame_interno_substituido = fields.Selection([
        ('nao', 'Não'),
        ('sim', 'Sim, Conforme item 13.5.4.6 Vasos de pressão que não permitam acesso visual para o exame interno ou externo por impossibilidade física devem ser submetidos alternativamente a outros exames não destrutivos e metodologias de avaliação da integridade, a critério do PH, baseados em normas e códigos aplicáveis à identificação de mecanismos de deterioração.')], string="Foi Substituído?")
    equip_doc_vaso_exame_interno_validade_date = fields.Date(
        string="Próximo vencimento Exame Interno do Vaso")
    equip_doc_vaso_exame_interno_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF ?")
    equip_doc_vaso_exame_interno_image = fields.Image(
        string="Foto do relatório - Interno")
    # equip_doc_vaso_exame_interno_pdf_ids = fields.One2many(string="Histórico de Relatórios Internos")

    # ----------------------------
    # | Documentação do Vaso     |
    # | PRONTUÁRIO OU DATA-BOOK  |
    # ----------------------------
    equip_doc_vaso_prontuario_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe prontuário do vaso?")
    equip_doc_vaso_prontuario_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF ?")
    equip_doc_vaso_prontuario_image = fields.Image(
        string="Imagem do Prontuário")
    # equip_doc_vaso_prontuario_pdf_ids = fields.One2many(string="Prontuários")

    # ----------------------------
    # | Documentação do Vaso     |
    # | TESTE HIDROSTÁTICO       |
    # ----------------------------
    equip_doc_vaso_th_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe certificado de TH do Vaso?")
    equip_doc_vaso_th_substituido = fields.Selection([
        ('nao', 'Não'),
        ('sim', 'Sim, Conforme item 13.5.4.3.1 "alínea b" para os vasos de pressão em operação antes da vigência da Portaria MTE º 594, de 28 de abril de 2014, a execução do TH fica a critério do PH e, caso seja necessária à sua realização, o TH deve ser realizado até a próxima inspeção de segurança periódica interna. Portanto o mesmo foi substituído por ensaio não destrutivo B-Scan')], string="Foi Substituído?")
    equip_doc_vaso_th_possui_validade = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="O TH tem validade?")
    equip_doc_vaso_th_validade_date = fields.Date(
        string="Validade do certificado de TH")
    equip_doc_vaso_th_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF ?")
    equip_doc_vaso_th_image = fields.Image(string="Foto Certificado de T.H.")
    # equip_doc_vaso_th_pdf_ids = fields.One2many(string="Histórico de TH")

    # ----------------------------
    # | Documentação do Vaso     |
    # | A.R.T.                   |
    # ----------------------------
    equip_doc_vaso_art_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe ART Vigente?")
    equip_doc_vaso_art_validade_date = fields.Date(string="Validade da ART")
    # equip_doc_vaso_art_pdf_ids = fields.One2many(string="Histórico de ART")

    # ------------------------------------------
    # | Documentação do Vaso                   |
    # | PROJETO DE ALTERAÇÃO E REPARO (PAR)    |
    # ------------------------------------------
    equip_doc_vaso_par_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe projeto de alteração e reparo?")
    equip_doc_vaso_par_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF ?")
    equip_doc_vaso_par_image = fields.Image(string="Foto do PAR")
    # equip_doc_vaso_par_pdf_ids = fields.One2many(string="Histórico de PAR")

    # -------------------------------
    # | Documentação do Vaso        |
    # | TREINAMENTOS                |
    # -------------------------------
    equip_doc_vaso_operador_possui_treinamento = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Operadores tem treinamento e certificação?")
    # equip_doc_vaso_certificado_treinamento = fields.One2many(string="Lista de Certificados")

    # ---------------------------------------
    # | Documentação do Vaso                |
    # | REGISTRO DE SEGURANÇA (LIVRO)       |
    # ---------------------------------------
    equip_doc_vaso_livro_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Registro de Segurança do Vaso existente?")
    equip_doc_vaso_livro_image = fields.Image(string="Imagem do Livro")

    # ---------------------------------------
    # | Documentação da Caldeira            |
    # | Relatórios e Laudos                 |
    # ---------------------------------------
    equip_doc_cald_relatorio_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Caldeira tem relatório de inspeção válido?")
    equip_doc_cald_relatorio_validade_date = fields.Date(
        string="Validade da Inspeção da Caldeira")
    equip_doc_cald_relatorio_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF ?")
    equip_doc_cald_relatorio_image = fields.Image(string="Foto do Relatório")
    # equip_doc_cald_relatorio_pdf_ids = fields.One2many(string="Histórico de Relatórios")

    # ------------------------------------------
    # | Documentação da Caldeira               |
    # | Prontuário ou Databook                 |
    # ------------------------------------------
    equip_doc_cald_prontuario_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe prontuário da caldeira?")
    equip_doc_cald_prontuario_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF?")
    equip_doc_cald_prontuario_image = fields.Image(string="Foto do Prontuario")
    # equip_doc_cald_prontuario_pdf_ids = fields.One2many(string="Prontuário / Data-Book")

    # ------------------------------------------
    # | Documentação da Caldeira               |
    # | Teste Hidrostático                     |
    # ------------------------------------------
    equip_doc_cald_th_certificado_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe certificado de TH da caldeira?")
    equip_doc_cald_th_possui_validade = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="O TH tem validade?")
    equip_doc_cald_th_validade_date = fields.Date(
        string="Validade do certificado de TH")
    equip_doc_cald_th_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir PDF ?")
    equip_doc_cald_th_image = fields.Image(string="Foto do Certificado T.H.")
    # equip_doc_cald_th_pdf_ids = fields.One2many(string="Histórico de TH")

    # ------------------------------------------
    # | Documentação da Caldeira               |
    # | A.R.T.                                 |
    # ------------------------------------------
    equip_doc_cald_art_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe ART vigente da caldeira?")
    equip_doc_cald_art_validade_date = fields.Date(string="Validade da ART")
    # equip_doc_cald_art_historico_ids = fields.One2many(string="Histórico de ART")

    # ------------------------------------------
    # | Documentação da Caldeira               |
    # | Projeto de Instalação                  |
    # ------------------------------------------
    equip_doc_cald_projeto_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe projeto de instalação da caldeira?")
    equip_doc_cald_projeto_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF?")
    equip_doc_cald_projeto_image = fields.Image(
        string="Foto do Projeto de Instalação")
    # equip_doc_cald_projeto_instalacao_ids = fields.One2many(string="Projeto de Instalação")

    # ------------------------------------------
    # | Documentação da Caldeira               |
    # | Projeto de Alteração e Reparo (PAR)    |
    # ------------------------------------------
    equip_doc_cald_par_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe projeto de alteração e reparo da caldeira?")
    equip_doc_cald_par_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF ?")
    equip_doc_cald_par_image = fields.Image(string="Foto do PAR")
    # equip_doc_cald_par_historico_ids = fields.One2many(string="Histórico de PAR")

    # ------------------------------------------
    # | Documentação da Caldeira               |
    # | Treinamentos                           |
    # ------------------------------------------
    equip_doc_cald_treinamento_possui_certificado = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Operadores tem treinamento e certificação?")
    # equip_doc_cald_treinamento_certificados_ids = fields.One2many(string="Lista de Certificados")

    # ------------------------------------------
    # | Documentação da Caldeira               |
    # | Registro de Segurança (Livro)          |
    # ------------------------------------------
    equip_doc_cald_livro_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Registro de Segurança da Caldeira existente?")
    equip_doc_cald_livro_image = fields.Image(string="Imagem do Livro")

    # ------------------------------------------
    # | Documentação da Tubulação              |
    # | Relatórios e Laudos                    |
    # ------------------------------------------
    equip_doc_tubu_relatorio_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Tubulação tem relatório de inspeção válido?")
    equip_doc_tubu_relatorio_validade_date = fields.Date(
        string="Validade da inspeção da Tubulação")
    equip_doc_tubu_relatorio_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF?")
    equip_doc_tubu_relatorio_image = fields.Image(string="Foto do Relatório")
    # equip_doc_tubu_relatorio_pdf_ids = fields.One2many(string="Histórico de Relatórios")

    # ------------------------------------------
    # | Documentação da Tubulação              |
    # | Prontuário ou Isométrico               |
    # ------------------------------------------
    equip_doc_tubu_prontuario_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe isométrico, prontuário especificações aplicáveis?")
    equip_doc_tubu_prontuario_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF ?")
    equip_doc_tubu_prontuario_image = fields.Image(string="Foto do Prontuário")
    # equip_doc_tubu_prontuario_pdf_ids = fields.One2many(string="Isométrico e Especificações aplicáveis")

    # ------------------------------------------
    # | Documentação da Tubulação              |
    # | Fluxograma                             |
    # ------------------------------------------
    equip_doc_tubu_fluxograma_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe fluxograma da tubulação?")
    equip_doc_tubu_fluxograma_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF ?")
    equip_doc_tubu_fluxograma_image = fields.Image(string="Foto do Fluxograma")
    # equip_doc_tubu_fluxograma_pdf_ids = fields.One2many(string="Fluxograma")

    # ------------------------------------------
    # | Documentação da Tubulação              |
    # | A.R.T.                                 |
    # ------------------------------------------
    equip_doc_tubu_art_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe ART vigente?")
    equip_doc_tubu_art_validade_date = fields.Date(string="Validade da ART")
    # equip_doc_tubu_art_pdf_ids = fields.One2many(string="Histórico de ART")

    # ------------------------------------------
    # | Documentação da Tubulação              |
    # | Projeto de Alteração e Reparo (PAR)    |
    # ------------------------------------------
    equip_doc_tubu_par_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe projeto de alteração e reparo?")
    equip_doc_tubu_par_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF ?")
    equip_doc_tubu_par_iamge = fields.Image(string="Foto do PAR")
    # equip_doc_tubu_par_pdf = fields.One2many(string="Histórico de PAR")

    # ------------------------------------------
    # | Documentação da Tubulação              |
    # | Registro de Segurança (Livro)          |
    # ------------------------------------------
    equip_doc_tubu_livro_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Registro de Segurança da Tubulação existente?")
    equip_doc_tubu_livro_image = fields.Image(string="Imagem do Livro")

    # ------------------------------------------
    # | Documentação do Tanque                 |
    # | Relatórios e Laudos                    |
    # ------------------------------------------
    equip_doc_tanque_relatorio_exame_externo_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Tanque tem relatório de Exame Externo ?")
    equip_doc_tanque_relatorio_exame_externo_validade_date = fields.Date(
        string="Próximo vencimento Exame Externo do Tanque")
    equip_doc_tanque_relatorio_exame_externo_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF?")
    equip_doc_tanque_relatorio_exame_externo_image = fields.Image(
        string="Foto Relatório Externo")
    # equip_doc_tanque_relatorio_exame_externo_pdf_ids = fields.One2many(string="Histórico de relatórios")
    equip_doc_tanque_relatorio_exame_interno_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Tanque tem relatório de exame interno?")
    equip_doc_tanque_relatorio_exame_interno_validade_date = fields.Date(
        string="Próximo vencimento Exame Interno do Tanque")
    equip_doc_tanque_relatorio_exame_interno_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF?")
    equip_doc_tanque_relatorio_exame_interno_image = fields.Image(
        string="Foto Relatório Interno")
    # equip_doc_tanque_relatorio_exame_interno_pdf_ids = fields.One2many(string="Histórico de relatórios")

    # ------------------------------------------
    # | Documentação do Tanque                 |
    # | Prontuário ou Data-Book                |
    # ------------------------------------------
    equip_doc_tanque_prontuario_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe folha de dados ou prontuário do tanque?")
    equip_doc_tanque_prontuario_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF?")
    equip_doc_tanque_prontuario_image = fields.Image(
        string="Foto do Prontuário")
    # equip_doc_tanque_prontuario_pdf_ids = fields.One2many(string="Prontuário ou Data-Book")

    # ------------------------------------------
    # | Documentação do Tanque                 |
    # | Projeto / Desenho                      |
    # ------------------------------------------
    equip_doc_tanque_projeto_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe desenho / projeto do tanque?")
    equip_doc_tanque_projeto_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF?")
    equip_doc_tanque_projeto_image = fields.Image(
        string="Foto do Projeto / Desenho")
    # equip_doc_tanque_projeto_pdf_ids = fields.One2many(string="Desenhos e Projetos")

    # ------------------------------------------
    # | Documentação do Tanque                 |
    # | A.R.T.                                 |
    # ------------------------------------------
    equip_doc_tanque_art_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe ART vigente?")
    # equip_doc_tanque_art_pdf_ids = fields.One2many(string="Histórico de ART")

    # ------------------------------------------
    # | Documentação do Tanque                 |
    # | Projeto de Alteração e Reparo (PAR)    |
    # ------------------------------------------
    equip_doc_tanque_par_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe projeto de alteração e reparo?")
    equip_doc_tanque_par_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF?")
    equip_doc_tanque_par_image = fields.Image(string="Foto do PAR")
    # equip_doc_tanque_par_pdf_ids = fields.One2many(string="Histórico de PAR")

    # ------------------------------------------
    # | Documentação do Tanque                 |
    # | Registro de Segurança (Livro)          |
    # ------------------------------------------
    equip_doc_tanque_livro_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Registro de Segurança do Tanque existente?")
    equip_doc_tanque_livro_image = fields.Image(string="Imagem do Livro")

    # ------------------------------------------
    # | Documentação do PI                     |
    # ------------------------------------------
    equip_doc_pi_possui_certificado = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="PI tem certificado de calibração válido?")
    equip_doc_pi_validade_date = fields.Date(
        string="Validade da calibração do PI")
    equip_doc_pi_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF?")
    equip_doc_pi_image = fields.Image(string="Foto do Certificado")
    # equip_doc_pi_pdf_ids = fields.One2many(string="Histórico de certificados")

    # ------------------------------------------
    # | Documentação da PSV                    |
    # ------------------------------------------
    equip_doc_psv_possui_certificado = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="PSV tem certificado de calibração válido?")
    equip_doc_psv_validade_date = fields.Date(
        string="Validade da calibração da PSV")
    equip_doc_psv_foto_pdf = fields.Selection([
        ('foto', 'Foto'),
        ('pdf', 'PDF')], string="Deseja tirar foto ou subir o PDF?")
    equip_doc_psv_image = fields.Image(string="Foto do Certificado")
    # equip_doc_psv_pdf_ids = fields.One2many(string="Histórico de certificados")

    # ------------------------------------------
    # | Documentação NR-11                     |
    # | RELATÓRIOS E LAUDOS                    |
    # ------------------------------------------
    equip_doc_nr11_relatorio_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe Relatório de Inspeção?")
    equip_doc_nr11_relatorio_inspecao_date = fields.Date(
        string="PRÓXIMA INSPEÇÃO")
    # equip_doc_nr11_relatorio_pdf_ids = fields.One2many(string="Histórico de Laudos e Relatórios")

    # ------------------------------------------
    # | Documentação NR-11                     |
    # | MANUAIS E INSTRUÇÕES                   |
    # ------------------------------------------
    equip_doc_nr11_manual_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe manual do equipamento?")
    # equip_doc_nr11_manual_pdf_ids = fields.One2many(string="Histórico de Manuais e Instruções")

    # ------------------------------------------
    # | Documentação NR-11                     |
    # | MEMORIAL DE CÁLCULO                    |
    # ------------------------------------------
    equip_doc_nr11_memorial_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe Memorial de Cálculo?")
    # equip_doc_nr11_memorial_pdf_ids = fields.One2many(string="Histórico de Memorial de Cálculo")

    # ------------------------------------------
    # | Documentação NR-11                     |
    # | PROJETOS E DESENHOS                    |
    # ------------------------------------------
    equip_doc_nr11_projeto_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe projeto ou desenho?")
    # equip_doc_nr11_projeto_pdf_ids = fields.One2many(string="Histórico de Projetos e Desenhos")

    # ------------------------------------------
    # | Documentação NR-11                     |
    # | A.R.T.                                 |
    # ------------------------------------------
    equip_doc_nr11_art_existe = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Existe ART vigente?")
    # equip_doc_nr11_art_pdf_ids = fields.One2many(string="Histórico de ARTs")

    # ------------------------------------------
    # | Inspeção do Vaso de Pressão            |
    # | Exame Externo e Interno                |
    # ------------------------------------------
    insp_vaso_ex_externo = fields.Boolean(string="Exame Externo")
    insp_vaso_ex_interno = fields.Boolean(string="Exame Interno")
    insp_vaso_med_espessura = fields.Boolean(
        string="Medição de Espessura por Ultrassom")
    insp_vaso_th = fields.Boolean(string="Teste Hidrostático")
    insp_vaso_lp = fields.Boolean(string="Líquido Penetrante")

    insp_vaso_1_1 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='1.1 Placa de Identificação indelével, fixada no corpo, em local de fácil acesso e visível com informações mínimas conforme item 13.5.1.4')
    insp_vaso_1_2 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='1.2 Vaso identificado com a respectiva categoria conforme anexo IV e número ou código de identificação, ambos em local visível, conforme item 13.5.1.5')

    insp_vaso_2_1 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='2.1 Drenos, respiros, bocas de visita, indicadores de nível, pressão e temperatura em boas condições físicas e em local de fácil acesso, conforme item 13.5.2.1')
    insp_vaso_2_2 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='2.2 Possui duas saídas amplas, desobstruídas e dispostas em direções distintas, conforme item 13.5.2.2. - alínea "a"')
    insp_vaso_2_3 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='2.3 Possui acesso fácil e seguro para as atividades de manutenção, operação e inspeção, sendo que, para guarda-corpos vazados, os vãos devem ter dimensões que impeçam a queda de pessoas, conforme item 13.5.2.2. - alínea "b"')
    insp_vaso_2_4 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='2.4 Possui ventilação permanente com entradas de ar que não possam ser bloqueadas, conforme item 13.5.2.2. - alínea "c"')
    insp_vaso_2_5 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='2.5 Possui iluminação conforme normas vigente, conforme item 13.5.2.2. - alínea "d"')
    insp_vaso_2_6 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='2.6 Possui sistema de iluminação de emergência, conforme item 13.5.2.2. - alínea "e"')

    insp_vaso_3_1 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='3.1 Dispositivos de segurança livres de bloqueios que possam neutralizar seu funcionamento em operação, conforme item 13.5.1.3 alínea "c"')
    insp_vaso_3_2 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='3.2 Para vasos categorias "I" e "II", possuem Manual de Operação Próprio ou Instruções de Operação no Manual de Operação da Unidade, conforme item 13.5.3.1')

    insp_vaso_4_1 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='4.1 Escada, Passarela e Plataformas em boas condições físicas')
    insp_vaso_4_2 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='4.2 Fundações, Suportes e Apoios em boas condições físicas')
    insp_vaso_4_3 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='4.3 Dispositivos de Aterramento em boas condições físicas')
    insp_vaso_4_4 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='4.4 Pintura em boa condição de conservação')
    insp_vaso_4_5 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='4.5 Costado e Tampos em boas condições físicas')
    insp_vaso_4_6 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='4.6 Válvulas de Controle, Bocais e Conexões em boas condições físicas')
    insp_vaso_4_7 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='4.7 Parafusos, Porcas, Prisioneiros, Chumbadores e Fixadores em boas condições físicas')
    insp_vaso_4_8 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='4.8 Revestimento ou Isolamento Térmico em boas condições físicas')
    insp_vaso_4_9 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='4.9 Medidor de Nível em boas condições físicas')
    insp_vaso_4_10 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='4.10 Dispositivos de segurança em boas condições operacionais')
    insp_vaso_4_11 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                      string='4.11 Dispositivos de monitoramento de pressão em boas condições operacionais')
    insp_vaso_4_12 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='4.12 Elementos de Travamento em boas condições físicas')

    insp_vaso_ex_externo_img_1 = fields.Image(
        string="Exame Externo - Imagem 1")
    insp_vaso_ex_externo_img_2 = fields.Image(
        string="Exame Externo - Imagem 2")
    insp_vaso_ex_externo_img_3 = fields.Image(
        string="Exame Externo - Imagem 3")
    insp_vaso_ex_externo_img_4 = fields.Image(
        string="Exame Externo - Imagem 4")
    insp_vaso_ex_externo_img_5 = fields.Image(
        string="Exame Externo - Imagem 5")
    insp_vaso_ex_externo_img_6 = fields.Image(
        string="Exame Externo - Imagem 6")

    insp_vaso_5_1 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='5.1 Existência de trincas, corrosão, escavações no costado / tampos')
    insp_vaso_5_2 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='5.2 Integridade do revestimento interno')
    insp_vaso_5_3 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='5.3 Indicações de poros ou deformações')
    insp_vaso_5_4 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='5.4 Integridade dos cordões de solda internos')
    insp_vaso_5_5 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='5.5 Integridade dos medidores de nível, pescadores, etc')
    insp_vaso_5_6 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='5.6 Integridade dos bocais, luvas e demais conexões e acessórios')

    insp_vaso_ex_interno_img_1 = fields.Image(
        string="Exame Interno - Imagem 1")
    insp_vaso_ex_interno_img_2 = fields.Image(
        string="Exame Interno - Imagem 2")
    insp_vaso_ex_interno_img_3 = fields.Image(
        string="Exame Interno - Imagem 3")
    insp_vaso_ex_interno_img_4 = fields.Image(
        string="Exame Interno - Imagem 4")
    # ------------------------------------------
    # | Inspeção da Caldeira                   |
    # | Exame Externo e Interno                |
    # ------------------------------------------
    insp_tipo_inspecao = fields.Selection([
        ('inicial', 'Inicial'),
        ('periodica', 'Periódica'),
        ('extraordinaria', 'Extraordinária')], string="Tipo de Inspeção")
    insp_cal_ex_externo_interno = fields.Boolean(
        string="Exame Externo e Interno")
    insp_cal_med_espessura = fields.Boolean(
        string="Medição de Espessura por Ultrassom")
    insp_cal_th = fields.Boolean(string="Teste Hidrostático")
    insp_cal_lp = fields.Boolean(string="Líquido Penetrante")

    insp_cal_1_1 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='1.1 Caldeira Identificada com tag e categoria, conforme item 13.4.1.5 da NR-13')
    insp_cal_1_2 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='1.2 Placa de identificação indelével afixada no corpo da caldeira e em local de fácil acesso, conforme item 13.4.1.4 da NR-13')

    insp_cal_2_1 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.1 Caldeira está afastada no mínimo 3 metros de outras instalações conforme o item 13.4.2.3 alinea "a"')
    insp_cal_2_2 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.2 Possui duas saídas amplas, desobstruídas sinalizadas e dispostas em direções distintas, conforme item 13.4.2.3 alinea "b"')
    insp_cal_2_3 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.3 Possui acesso fácil e seguro para atividades de manutenção, operação e inspeção, conforme item 13.4.2.3 alinea "c"')
    insp_cal_2_4 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.4 Possui sistema de captação e lançamento dos gases e material particulado, provenientes da combustão, para fora da área de operação conforme item 13.4.2.3 alinea "d"')
    insp_cal_2_5 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.5 Possui iluminação conforme normas vigente, conforme item 13.4.2.3 alinea "e"')
    insp_cal_2_6 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.6 Possui sistema de iluminação de emergência caso opere a noite, conforme item 13.4.2.3 alinea "f"')

    insp_cal_2_7 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.7 Caldeira deve estar afastada de no mínimo 3 metros de outras instalações e instalada em prédio separado construído de material resistente a fogo conforme item 13.4.2.4 alinea "a" ')
    insp_cal_2_8 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.8 Possui duas saídas amplas, desobstruídas sinalizadas e dispostas em direções distintas, conforme item 13.4.2.4 alinea "b"')
    insp_cal_2_9 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.9 Possui ventilação permanente com entradas de ar que não possam ser bloqueadas conforme item 13.4.2.4 alinea "c')
    insp_cal_2_10 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.10 Possui sensor para detecção de vazamento de gás conforme item 13.4.2.4 alinea "d"')
    insp_cal_2_11 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.11 Possui acesso fácil e seguro para atividades de manutenção, operação e inspeção, conforme item 13.4.2.4 alinea "c"')
    insp_cal_2_12 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.12 Possui sistema de captação e lançamento dos gases e material particulado, provenientes da combustão, para fora da área de operação conforme item 13.4.2.4 alinea "d"')
    insp_cal_2_13 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.13 Possui iluminação conforme normas vigente, conforme item 13.4.2.4 alinea "e"')
    insp_cal_2_14 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.14 Possui sistema de iluminação de emergência caso opere a noite, conforme item 13.4.2.4 alinea "f"')

    insp_cal_3_1 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='3.1 Dispositivo que indique a pressão do vapor acumulado (Manômetro) em boas condições físicas conforme item 13.4.1.3 alinea "b" da NR-13')
    insp_cal_3_2 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='3.2 Válvula de Segurança instalada diretamente na caldeira ou no sistema que a inclui em boas condições físicas conforme item 13.4.1.3 alinea "a" da NR-13')
    insp_cal_3_3 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='3.3 Sistemas de controle de segurança livres de bloqueios que possam neutralizar seu funcionamento em operação conforme item 13.3.1 alinea "c" da NR-13')
    insp_cal_3_4 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='3.4 Dispositivo de controle de pressão (Manômetro) e válvula de segurança calibrados conforme item 13.4.1.3 e 13.4.3.2 da NR-13')
    insp_cal_3_5 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='3.5 Sistema automático de controle do nível de água com intertravamento que evite o superaquecimento por alimentação deficiente conforme item 13.4.1.3 alinea "e"')
    insp_cal_3_6 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='3.6 Dispositivo de controle do nível de água da Caldeira conforme item 13.4.1.3 alinea "e" da NR-13')
    insp_cal_3_7 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='3.7 Qualidade da água controlada para compatibilizar sua propriedades físico-químicas com os parâmetros de operação da caldeira conforme item 13.4.3.3 da NR-13')

    insp_cal_4_1 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='4.1 Os reparos e ou alterações realizados na caldeira respeitam o código de projeto e construção e as prescrições do fabricante, conforme item 13.3.3. da NR-13')
    insp_cal_4_2 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='4.2 Realizado Projeto de Alteração ou Reparo caso haja modificação das condições de projeto ou reparos que possam comprometer a segurança, conforme item 13.3.6 da NR-13')
    insp_cal_4_3 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='4.3 Projeto de Alteração ou Reparo realizado por Profissional Habilitado, possuindo dados técnicos e divulgado para profissionais envolvidos com a caldeira, conforme item 13.3.7.')
    insp_cal_4_4 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='4.4 Após reparos por soldagem em partes sujeitas à pressão foi realizado Teste Hidrostático, conforme item 13.3.8 da NR-13')
    insp_cal_4_5 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='4.5 Sistemas de controle e segurança submetidos a manutenção preventiva ou preditiva, conforme item 13.3.9. da -NR-13')

    insp_cal_ex_externo_interno_img_1 = fields.Image(
        string="Exame Externo e Interno - Imagem 1")
    insp_cal_ex_externo_interno_img_2 = fields.Image(
        string="Exame Externo e Interno - Imagem 2")
    insp_cal_ex_externo_interno_img_3 = fields.Image(
        string="Exame Externo e Interno - Imagem 3")
    insp_cal_ex_externo_interno_img_4 = fields.Image(
        string="Exame Externo e Interno - Imagem 4")
    insp_cal_ex_externo_interno_img_5 = fields.Image(
        string="Exame Externo e Interno - Imagem 5")
    insp_cal_ex_externo_interno_img_6 = fields.Image(
        string="Exame Externo e Interno - Imagem 6")

    # ------------------------------------------
    # | Inspeção                               |
    # | Medição de Espessura por Ultrassom     |
    # ------------------------------------------
    insp_med_esp_esquerdo_0 = fields.Float(string="Ponto 1 (0º)")
    insp_med_esp_esquerdo_90 = fields.Float(string="Ponto 2 (90º)")
    insp_med_esp_esquerdo_180 = fields.Float(string="Ponto 2 (180º)")
    insp_med_esp_esquerdo_270 = fields.Float(string="Ponto 4 (270º)")

    insp_med_esp_direito_0 = fields.Float(string="Ponto 4 (0º)")
    insp_med_esp_direito_90 = fields.Float(string="Ponto 4 (90º)")
    insp_med_esp_direito_180 = fields.Float(string="Ponto 4 (180º)")
    insp_med_esp_direito_270 = fields.Float(string="Ponto 4 (270º)")

    insp_med_esp_tubo_0 = fields.Float(string="Ponto 1 (0º)")
    insp_med_esp_tubo_90 = fields.Float(string="Ponto 2 (90º)")
    insp_med_esp_tubo_180 = fields.Float(string="Ponto 3 (180º)")
    insp_med_esp_tubo_270 = fields.Float(string="Ponto 4 (270º)")

    insp_med_esp_costado_0 = fields.Float(string="Ponto 1 (0º)")
    insp_med_esp_costado_90 = fields.Float(string="Ponto 2 (90º)")
    insp_med_esp_costado_180 = fields.Float(string="Ponto 3 (180º)")
    insp_med_esp_costado_270 = fields.Float(string="Ponto 4 (270º)")

    # ------------------------------------------
    # | Inspeção                               |
    # | Teste Hidrostático                     |
    # ------------------------------------------
    insp_th_fluido_teste = fields.Selection([
        ('agua', 'Água')], string="Fluído de Teste")
    insp_th_press_trabalho = fields.Float(
        string="Pressão de Trabalho (Kgf/cm²)")
    insp_th_press_teste = fields.Float(string="Pressão de Teste (kgf/cm²)")
    insp_th_desenho = fields.Char(string="Desenho n°")
    insp_th_manometro = fields.Selection([
        ('MN-001', 'MN-001'),
        ('MN-002', 'MN-002'),
        ('MN-003', 'MN-003')], string="Manômetros Nº")
    insp_th_croqui = fields.Char(
        string="Croqui / Fluxograma do Sistema de Teste")
    insp_th_img_1 = fields.Image(string="Teste Hidrostático - Imagem 1")
    insp_th_img_2 = fields.Image(string="Teste Hidrostático - Imagem 2")
    insp_th_img_3 = fields.Image(string="Teste Hidrostático - Imagem 3")
    insp_th_img_4 = fields.Image(string="Teste Hidrostático - Imagem 4")
    insp_th_img_5 = fields.Image(string="Teste Hidrostático - Imagem 5")
    insp_th_laudo = fields.Selection([
        ('aprovado', 'Aprovado'),
        ('reprovado', 'Reprovado')], string="Laudo")

    # ------------------------------------------
    # | Inspeção                               |
    # | Líquido Penetrante                     |
    # ------------------------------------------
    # insp_cal_lp_mate_fabricacao_id = fields.Many2one(string="Material de Fabricação")
    insp_lp_equip_peca = fields.Char(
        string="Equipamento, Peça ou Componente")
    insp_lp_desenho_referencia = fields.Char(
        string="Desenho de Referencia nº")
    insp_lp_condicao_superficie = fields.Selection([
        ('bruta', 'Bruta'),
        ('esmerilhada_escovada_lixada', 'Esmerilhada / Escovada / Lixada'),
        ('usinada', 'Usinada')], string="Condição da Superfície")
    insp_lp_trata_termico = fields.Selection([
        ('antes_t_t', 'Antes do T.T.'),
        ('depois_t_t', 'Após do T.T.'),
        ('nao_aplicavel', 'Não Aplicável')], string="Tratamento Térmico")

    # insp_cal_lp_penetrante_fabricante_ids = fields.Many2many(string="Fabricante")
    insp_lp_penetrante_modelo = fields.Char(string="Modelo")
    insp_lp_penetrante_validade_date = fields.Date(string="Validade")
    insp_lp_penetrante_lote = fields.Char(string="Lote")
    insp_lp_penetrante_tempo = fields.Integer(
        string="Tempo de Ação do Penetrante (minutos)")

    # insp_cal_lp_revelador_fabricante_ids = fields.Many2many(string="Fabricante")
    insp_lp_revelador_modelo = fields.Char(string="Modelo")
    insp_lp_revelador_validade_date = fields.Date(string="Validade")
    insp_lp_revelador_lote = fields.Char(string="Lote")
    insp_lp_revelador_tempo = fields.Integer(
        string="Tempo de Avaliação  (minutos)")

    insp_lp_removedor_tipo = fields.Selection([
        ('agua', 'Água'),
        ('solvente', 'Solvente')], string="Tipo")
    insp_lp_removedor_validade_date = fields.Date(string="Validade")
    insp_lp_removedor_lote = fields.Char(string="Lote")
    insp_lp_removedor_temperatura = fields.Char(string="Temperatura")

    insp_lp_obs_comentarios = fields.Char(
        string="Observações / Comentários")

    insp_lp_img_1 = fields.Image(string="Liquido Penetrante - Imagem 1")
    insp_lp_img_2 = fields.Image(string="Liquido Penetrante - Imagem 2")
    insp_lp_img_3 = fields.Image(string="Liquido Penetrante - Imagem 3")
    insp_lp_img_4 = fields.Image(string="Liquido Penetrante - Imagem 4")
    insp_lp_img_5 = fields.Image(string="Liquido Penetrante - Imagem 5")
    insp_lp_img_6 = fields.Image(string="Liquido Penetrante - Imagem 6")
    insp_lp_img_7 = fields.Image(string="Liquido Penetrante - Imagem 7")
    insp_lp_img_8 = fields.Image(string="Liquido Penetrante - Imagem 8")
    insp_lp_img_9 = fields.Image(string="Liquido Penetrante - Imagem 9")
    insp_lp_img_10 = fields.Image(string="Liquido Penetrante - Imagem 10")
    insp_lp_img_11 = fields.Image(string="Liquido Penetrante - Imagem 11")
    insp_lp_img_12 = fields.Image(string="Liquido Penetrante - Imagem 12")
    insp_lp_img_13 = fields.Image(string="Liquido Penetrante - Imagem 13")
    insp_lp_img_14 = fields.Image(string="Liquido Penetrante - Imagem 14")
    insp_lp_img_15 = fields.Image(string="Liquido Penetrante - Imagem 15")

    insp_lp_revelador_img_1 = fields.Image(string="Revelador - Imagem 1")
    insp_lp_revelador_img_2 = fields.Image(string="Revelador - Imagem 2")
    insp_lp_revelador_img_3 = fields.Image(string="Revelador - Imagem 3")
    insp_lp_revelador_img_4 = fields.Image(string="Revelador - Imagem 4")
    insp_lp_revelador_img_5 = fields.Image(string="Revelador - Imagem 5")
    insp_lp_revelador_img_6 = fields.Image(string="Revelador - Imagem 6")
    insp_lp_revelador_img_7 = fields.Image(string="Revelador - Imagem 7")
    insp_lp_revelador_img_8 = fields.Image(string="Revelador - Imagem 8")
    insp_lp_revelador_img_9 = fields.Image(string="Revelador - Imagem 9")
    insp_lp_revelador_img_10 = fields.Image(string="Revelador - Imagem 10")
    insp_lp_revelador_img_11 = fields.Image(string="Revelador - Imagem 11")
    insp_lp_revelador_img_12 = fields.Image(string="Revelador - Imagem 12")
    insp_lp_revelador_img_13 = fields.Image(string="Revelador - Imagem 13")
    insp_lp_revelador_img_14 = fields.Image(string="Revelador - Imagem 14")
    insp_lp_revelador_img_15 = fields.Image(string="Revelador - Imagem 15")

    # ------------------------------------------
    # | Inspeção da Tubulação                  |
    # | Exame Externo                          |
    # ------------------------------------------
    insp_tubu_ex_externo = fields.Boolean(string="Exame Externo")
    insp_tubu_th = fields.Boolean(string="Teste Hidrostático")
    insp_tubu_lp = fields.Boolean(string="Líquido Penetrante")

    insp_tubu_7_1 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='7.1. As tubulações ou sistemas de tubulação devem possuir dispositivos de segurança conforme os critérios do código de projeto utilizado, ou em atendimento às recomendações de estudo de análises de cenários de falhas, conforme item 13.6.1.2 da NR-13')
    insp_tubu_7_2 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='7.2. As tubulações ou sistemas de tubulação devem possuir indicador de pressão de operação, conforme definido no projeto de processo e instrumentação, conforme item 13.6.1.3 da NR-13.')
    insp_tubu_7_3 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='7.3. A empresa possui plano de manutenção preventiva das tubulações.')
    insp_tubu_7_4 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='7.4. O equipamento esta isento de vibrações, colisões e aquecimentos. ')

    insp_tubu_9_1 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='9.1. Os dispositivos indicadores de pressão da tubulação devem ser mantidos em boas condições operacionais.')
    insp_tubu_9_2 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='9.2. As tubulações de vapor e seus acessórios devem ser mantidos em boas condições operacionais, de acordo com um plano de manutenção elaborado pelo estabelecimento.')
    insp_tubu_9_3 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                     string='9.3. As tubulações e sistemas de tubulação devem ser identificáveis segundo padronização formalmente instituída pelo estabelecimento, e sinalizadas conforme a NR-26.')

    insp_tubu_10_1 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='10.1. Integridade da tubulação quanto a pontos de corrosão.')
    insp_tubu_10_2 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='10.2. Pintura em boa condição de conservação.')
    insp_tubu_10_3 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='10.3. Válvulas de Controle e Conexões em boas condições físicas.')
    insp_tubu_10_4 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='10.4. Fixadores em boas condições físicas.')
    insp_tubu_10_5 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='10.5. Suportes e Apoios em boas condições físicas.')

    insp_tubu_img_1 = fields.Image(string="Exame Externo - Imagem 1")
    insp_tubu_img_2 = fields.Image(string="Exame Externo - Imagem 2")
    insp_tubu_img_3 = fields.Image(string="Exame Externo - Imagem 3")
    insp_tubu_img_4 = fields.Image(string="Exame Externo - Imagem 4")
    insp_tubu_img_5 = fields.Image(string="Exame Externo - Imagem 5")
    insp_tubu_img_6 = fields.Image(string="Exame Externo - Imagem 6")

    # ------------------------------------------
    # | Inspeção do Tanque                     |
    # | Exame Externo e Interno                |
    # ------------------------------------------
    insp_tanque_ex_externo = fields.Boolean(string="Exame Externo")
    insp_tanque_ex_interno = fields.Boolean(string="Exame Interno")
    insp_tanque_med_espessura = fields.Boolean(string="Medição de Espessura")
    insp_tanque_th = fields.Boolean(string="Teste Hidrostático")
    insp_tanque_lp = fields.Boolean(string="Líquido Penetrante")

    insp_tanque_1_1 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                       string='1.1 Placa de Identificação indelével, fixada no corpo, em local de fácil acesso e visível com informações mínimas conforme item 13.7.1.1, alinea "b";')
    insp_tanque_1_2 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                       string='1.2 Tanque identificado com a respectiva categoria e número ou código de identificação, ambos em local visível, conforme item 13.7.2.3;')

    insp_tanque_2_1 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                       string='2.1 Tampo superior/esquerdo em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão.')
    insp_tanque_2_2 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                       string='2.2 Tampo inferior/direito em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão.')
    insp_tanque_2_3 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                       string='2.3 Base de concreto do tanque em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão')
    insp_tanque_2_4 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                       string='2.4 Flanges em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão.')
    insp_tanque_2_5 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='2.5 Chumbadores e Fixadores em boas condições físicas.')
    insp_tanque_2_6 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                       string='2.6 Bocas de visita em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão.')
    insp_tanque_2_7 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='2.7 Válvulas de Controle, Bocais e Conexões em boas condições físicas.')
    insp_tanque_2_8 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='2.8 Pintura do tanque em boas condições de conservação.')
    insp_tanque_2_9 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                       string='2.9 Tanque identificado com o respectivo número ou código de identificação, em local visível.')
    insp_tanque_2_10 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='2.10 Parafusos, Porcas, Estojos e Prisioneiros em boas condições físicas.')
    insp_tanque_2_11 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='2.11 Fundações, Suportes, Berços e Apoios em boas condições físicas')
    insp_tanque_2_12 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='2.12 Revestimento em boas condições físicas.')
    insp_tanque_2_13 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='2.13 Bacia de contenção e seus acessórios em boas condições.')
    insp_tanque_2_14 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')],
                                        string='2.14 Escada marinheiro e escada de acesso ao lado interno da bacia de contenção em boas condições físicas.')
    insp_tanque_2_15 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='2.15 Aterramento elétrico em boas condições.')
    insp_tanque_2_16 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.16 Tubulações em boas condições.')
    insp_tanque_2_17 = fields.Selection(
        [('a', 'A'), ('r', 'R'), ('ar', 'AR'), ('na', 'NA')], string='2.17 Instrumentos em boas condições.')
    insp_tanque_2_18 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='2.18 Sistema de bombeamento em boas condições.')

    insp_tanque_img_1 = fields.Image(string="Imagem 1")
    insp_tanque_img_2 = fields.Image(string="Imagem 2")
    insp_tanque_img_3 = fields.Image(string="Imagem 3")
    insp_tanque_img_4 = fields.Image(string="Imagem 4")
    insp_tanque_img_5 = fields.Image(string="Imagem 5")
    insp_tanque_img_6 = fields.Image(string="Imagem 6")
    insp_tanque_img_7 = fields.Image(string="Imagem 7")
    insp_tanque_img_8 = fields.Image(string="Imagem 8")
    insp_tanque_img_9 = fields.Image(string="Imagem 9")
    insp_tanque_img_10 = fields.Image(string="Imagem 10")

    insp_tanque_interno_1_1 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='1.1 Costado em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão.')
    insp_tanque_interno_1_2 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='1.2 Teto superior/esquerdo em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão.')
    insp_tanque_interno_1_3 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='1.3 Fundo em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão.')
    insp_tanque_interno_1_4 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='1.4 Bocais do tanque em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão.')
    insp_tanque_interno_1_5 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='1.5 Pescador em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão.')
    insp_tanque_interno_1_6 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='1.6 Bocas de visita em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão.')
    insp_tanque_interno_1_7 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='1.7 Revestimento interno em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão.')
    insp_tanque_interno_1_8 = fields.Selection([('a', 'A'), ('r', 'R'), ('ar', 'AR'), (
        'na', 'NA')], string='1.8 Acessórios internos (serpentina e suportação) em boas condições físicas e sem apresentação de trincas, vazamentos e corrosão.')

    insp_tanque_interno_img_1 = fields.Image(string="Imagem 1")
    insp_tanque_interno_img_2 = fields.Image(string="Imagem 2")
    insp_tanque_interno_img_3 = fields.Image(string="Imagem 3")
    insp_tanque_interno_img_4 = fields.Image(string="Imagem 4")
    insp_tanque_interno_img_5 = fields.Image(string="Imagem 5")
    insp_tanque_interno_img_6 = fields.Image(string="Imagem 6")
    insp_tanque_interno_img_7 = fields.Image(string="Imagem 7")
    insp_tanque_interno_img_8 = fields.Image(string="Imagem 8")
    insp_tanque_interno_img_9 = fields.Image(string="Imagem 9")
    insp_tanque_interno_img_10 = fields.Image(string="Imagem 10")

    # ------------------------------------------
    # | Inspeção do PI                         |
    # |                                        |
    # ------------------------------------------
    # insp_pi_dados_padrao_smp_pi_ids = fields.Many2many(string="Dados dos Padrões Utilizados (SMP) (PI)")

    # insp_pi_smp_padrao_ids = fields.Many2many(string="SMP - Padrão")
    # insp_pi_smc_calibrado_ids = fields.Many2many(string="SMC - Calibrado")

    # ------------------------------------------
    # | Inspeção do PSV                        |
    # |                                        |
    # ------------------------------------------
    insp_psv_inspecao_visual = fields.Boolean(string="Inspeção Visual")
    insp_psv_manutencao = fields.Boolean(string="Manutenção")
    insp_psv_servicos_exe = fields.Boolean(string="Serviços Executados")

    # ------------------------------------------
    # | Inspeção do PSV                        |
    # | Inspeção Visual                        |
    # ------------------------------------------
    insp_psv_erosao_disco = fields.Boolean(string="Erosão Disco Local")
    insp_psv_esmaga_disco = fields.Boolean(string="Esmagamento Disco Local")
    insp_psv_oxidacao_corpo = fields.Boolean(string="Oxidação do Corpo")
    insp_psv_oxidacao_mola = fields.Boolean(string="Oxidação da Mola")
    insp_psv_mola_quebrada = fields.Boolean(string="Mola Quebrada")
    insp_psv_mola_desgastes = fields.Boolean(string="Mola com Desgastes")
    insp_psv_sede_danificada = fields.Boolean(string="Sede Danificada")
    insp_psv_juntas_rompidas = fields.Boolean(string="Juntas Rompidas")

    insp_psv_rosca_bocal = fields.Boolean(string="Rosca do Bocal")
    insp_psv_haste_empenada = fields.Boolean(string="Haste Empenada")
    insp_psv_parafuso_ajuste_dani = fields.Boolean(
        string="Parafuso de Ajuste Danificado")
    insp_psv_parafuso_trava_dani = fields.Boolean(
        string="Parafuso de Trava Danificado")
    insp_psv_parafuso_mola_dani = fields.Boolean(
        string="Parafuso da Mola Danificado")
    insp_psv_oxidacao_flange = fields.Boolean(
        string="Oxidação na Abertura da Flange")
    insp_psv_erosao_flange = fields.Boolean(
        string="Erosão na Abertura de Flange")
    insp_psv_oxidacao_parafusos = fields.Boolean(
        string="Oxidação de Parafusos e Porcas")

    # ------------------------------------------
    # | Inspeção do PSV                        |
    # | Manutenção                             |
    # ------------------------------------------
    insp_psv_manu_retirado_processo = fields.Boolean(
        string="Retirado do Processo")
    insp_psv_manu_desmontagem = fields.Boolean(string="Desmontagem")
    insp_psv_manu_neutralizacao = fields.Boolean(string="Neutralização")
    insp_psv_manu_limpeza = fields.Boolean(string="Limpeza")
    insp_psv_manu_jateamento = fields.Boolean(string="Jateamento")
    insp_psv_manu_usinagem = fields.Boolean(string="Usinagem")
    insp_psv_manu_retifica = fields.Boolean(string="Retifica")
    insp_psv_manu_lapidacao = fields.Boolean(string="Lapidação")
    insp_psv_manu_repintura = fields.Boolean(string="Repintura")
    insp_psv_manu_montagem = fields.Boolean(string="Montagem")
    insp_psv_manu_calibracao = fields.Boolean(string="Calibração")
    insp_psv_manu_instalacao = fields.Boolean(string="Instalação")
    insp_psv_manu_acompanhamento = fields.Boolean(
        string="Acompanhamento da Partida")

    # ------------------------------------------
    # | Inspeção do PSV                        |
    # | Serviços Executados                    |
    # ------------------------------------------
    insp_psv_serv_exe_pintura = fields.Boolean(string="Pintura")
    insp_psv_serv_exe_plaqueta = fields.Boolean(string="Plaqueta")
    insp_psv_serv_exe_lacre = fields.Boolean(string="Lacre")
    insp_psv_serv_exe_protecao = fields.Boolean(
        string="Proteção dos Bocais e Roscas")

    # ------------------------------------------
    # | Fim da Pagina                          |
    # |                                        |
    # ------------------------------------------
    insp_ass_inspetor = fields.Image(string="Assinatura do Inspetor")
    insp_ass_engenheiro = fields.Image(string="Assinatura do Engenheiro")

    # insp_atividade_ids = fields.Many2many(string="Atividade")
