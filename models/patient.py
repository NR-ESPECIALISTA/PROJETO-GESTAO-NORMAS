from odoo import api, fields, models


# ------------------------------------------------------------------------------
# Ele não atualiza esse arquivo se apresentar um erro na declaração de variavel!
# Precisa Desinstalar esse modulo, logo em seguida derrubar o serviço e subir.
# ------------------------------------------------------------------------------


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    imagem_equip = fields.Image(string="Image")
    name = fields.Char(string="Nome do Equipamento",
                       required=True, copy=False, index=True)  # tracking=True
    state = fields.Selection([
        ('em_adequacao', 'EM ADEQUAÇÃO'),
        ('aprovado', 'APROVADO'),
        ('reprovado', 'REPROVADO'),
        ('desativado', 'DESATIVADO'),
        ('desenquadrado', 'DESENQUADRADO')], default='em_adequacao', string='Status', required=True)
    # age = fields.Integer(string="Age")
    # image = fields.Char(string='image')
    # gender = fields.Selection(
    #    [('male', 'Male'), ('female', 'Female')], string='Gender')

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
    # normas_fabri_ids = fields.Many2many()
    # normas_calibracao_ids = fields.Many2many()
    # fabricante_id = fields.Many2one()
    ano_fabri = fields.Integer(string="Ano de Fabricação")
    num_serie = fields.Integer(string="Número de Série")
    lote = fields.Integer(string="Lote")

    # --------------------------
    # | Informações do Contato |
    # --------------------------
    cliente_propri = fields.Many2one(
        'res.company', string="Cliente Proprietario")  # Saber como configura o dominio de um may2one
    # nome_contato = fields._Relational()
    # email_contato = fields._Relational();
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

    # equip_vinculado = fields.Many2one()

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
    # equip_cal_material_fabri_ids = fields.Many2many()
    equip_cal_ambiente_instalacao = fields.Selection(
        [('aberto', 'Aberto'),
         ('fechado', 'Fechado')], string="Ambiente de instalação")
    # equip_cal_tipo_fluido_id = fields.Many2one(string="Tipo de Fluido")

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
        string="Temperatura de Projeto (Cº)")
    equip_vaso_casco_temp_operacao = fields.Char(
        string="Temperatura de Operação (Cº)")
    equip_vaso_casco_compri_altura = fields.Float(
        string="Comprimento/Altura (mm)")
    equip_vaso_casco_diametro = fields.Float(string="Diâmetro (mm)")
    equip_vaso_casco_volume = fields.Float(string="Volume (m³)")
    # equip_vaso_casco_mat_fabricacao_id = fields.Many2one(string="Material de Fabricação")
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
    # equip_vaso_casco_cal_pxv = fields.Char(string="Calculo PxV")  # Tem que calcular o valor do PxV para esse campo
    # equip_vaso_casco_pxv_class = fields.Float(string="PxV Classificação")  # Tem que calcular o valor de PxV para esse campo
    # equip_vaso_casco_grupo_risco = fields.Char(string="Grupo Potencial de Risco")  # Tem que calcular o valor dos dois campos de cima
    # equip_vaso_casco_classe_fluido = fields.Char(string="Classe do Fluido ")  # Tem que Calcular a Classe do Fluido
    equip_vaso_casco_categoria = fields.Selection([
        ('cat_1', 'CAT I'),
        ('cat_2', 'CAT II'),
        ('cat_3', 'CAT III'),
        ('cat_4', 'CAT IV'),
        ('cat_5', 'CAT V'),
        ('n_a', 'N/A')], string="Categoria")

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
        string="Temperatura de Projeto (Cº)")
    equip_vaso_tubo_temp_operacao = fields.Char(
        string="Temperatura de Operação (Cº)")
    equip_vaso_tubo_volume = fields.Float(string="Volume (m³)")
    # equip_vaso_tubo_mat_fabricacao_id = fields.Many2one(string="Material de Fabricação")
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
    # equip_vaso_tubo_cal_pxv = fields.Char(string="Calculo PxV")  # Tem que calcular o valor do PxV para esse campo
    # equip_vaso_tubo_pxv_class = fields.Float(string="PxV Classificação")  # Tem que calcular o valor de PxV para esse campo
    # equip_vaso_tubo_grupo_risco = fields.Char(string="Grupo Potencial de Risco")  # Tem que calcular o valor dos dois campos de cima
    # equip_vaso_tubo_classe_fluido = fields.Char(string="Classe do Fluido ")  # Tem que Calcular a Classe do Fluido
    equip_vaso_tubo_categoria = fields.Selection([
        ('cat_1', 'CAT I'),
        ('cat_2', 'CAT II'),
        ('cat_3', 'CAT III'),
        ('cat_4', 'CAT IV'),
        ('cat_5', 'CAT V'),
        ('n_a', 'N/A')], string="Categoria")

    # -------------------------------
    # | Dados Técnicos da Tubulação |
    # -------------------------------
    # equip_tubu_linhas_ramais_ids = fields.Many2many(string="Linhas e Ramais")
    equip_tubu_pmta = fields.Float(string="PMTA(kgf/cm²)")
    equip_tubu_press_trabalho = fields.Float(
        string="Pressão de Trabalho (kgf/cm²):")
    equip_tubu_press_teste = fields.Float(string="Pressão de Teste (kgf/cm²):")
    equip_tubu_temp_projeto = fields.Char(string="Temperatura de Projeto (ºC)")
    equip_tubu_temp_operacao = fields.Char(
        string="Temperatura de Operação (ºC)")
    equip_tubu_volume = fields.Float(string="Tubulação - Volume (m³)")
    # equip_tubu_mat_fabricacao_id = fields.Many2one(string="Material de Fabricação")
    # equip_tubu_tipo_fluido_id = fields.Many2one(string="Tipo de Fluido")
    equip_tubu_isolamento = fields.Selection([
        ('sim', 'Sim'),
        ('nao', 'Não')], string="Possui isolamento?")

    # ----------------------------
    # | Dados Técnicos do Tanque |
    # ----------------------------
    equip_tanque_press_trabalho = fields.Float(
        string="Pressão de Trabalho (kgf/cm²):")
    equip_tanque_temp_projeto = fields.Char(
        string="Temperatura de Projeto (ºC)")
    equip_tanque_temp_operacao = fields.Char(
        string="Temperatura de Operação (ºC)")
    equip_tanque_volume = fields.Float(string="Volume(m³)")
    equip_tanque_altura = fields.Float(string="Altura (mm)")
    equip_tanque_diametro_interno = fields.Float(
        string="Diâmetro interno (mm)")
    # equip_tanque_mat_fabricacao_id = fields.Many2one(string="Material de Fabricação")
    # equip_tanque_tipo_fluido_id = fields.Many2one(string="Tipo de Fluido")

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
    # equip_psv_mat_fabricacao_id = fields.Many2one(string="Material de Fabricação")
    # equip_psv_tipo_fluido_id = fields.Many2one(string="Tipo de Fluido")

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
    # equip_pi_tipo_fluido_id = fields.Many2one(string="Tipo de Fluido")

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
    equip_doc_cald_livro_iamge = fields.Image(string="Imagem do Livro")

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
    # equip_doc_tubu_art_pdf = fields.One2many(string="Histórico de ART")

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
