from odoo import api, fields, models

class EquipInspecao(models.Model):
    _name = "equip.inspecao"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Inspeção de Equipamentos"

    tittle = fields.Char(string="TAG")
    validade = fields.Char(string="Validade")

    # ------------------------------------------
    # | Inspeção da Caldeira                   |
    # | Exame Externo e Interno                |
    # ------------------------------------------
    insp_cal_tipo_inspecao = fields.Selection([
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
    # | Inspeção da Caldeira                   |
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
    # | Inspeção da Caldeira                   |
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
    # | Inspeção da Caldeira                   |
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