from odoo import http, _
from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.exceptions import AccessError, MissingError
from odoo.fields import Command
from collections import OrderedDict
from odoo.http import request
from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models


class WeblearnsPortal(CustomerPortal):

    # -------------------------------------------
    # Contador de equipamentos da mesma empresa
    # -------------------------------------------
    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        partner = request.env.user.partner_id.parent_id.id
        if 'equipamento_count' in counters:
            equipamento_count = request.env['nr.equipamento'].search_count([('cliente_propri.id', '=', partner)]) \
                if request.env['nr.equipamento'].check_access_rights('read', raise_exception=False) else 0
            values['equipamento_count'] = equipamento_count
        return values

    # -------------------------------------------
    # lista os equipamentos de cada tipo juntamente com a empresa correspondente
    # ERROR: Não foi possível criar uma função a ser chamada quando é clicado em cada tipo de url e
    # mandar uma variavel que mudaria dependendo do tipo de equipamento que foi clicado
    # e assim listar exatamente aquele tipo de equipamento e empresa
    # -------------------------------------------
    @http.route(['/my/equip/vaso', '/my/equip/vaso/page/<int:page>'], type='http', website=True)
    def weblearnsEquipVasoListView(self, page=1, sortby=None, **kw):
        equipamento_obj = request.env['nr.equipamento']
        partner = request.env.user.partner_id.parent_id.id

        sorted_list = {
            'id': {'label': _('ID'), 'order': 'equipamento_id asc'},
            'name': {'label': _('Nome'), 'order': 'name'},
            'tipo_equip': {'label': _('TAG'), 'order': 'tipo_equip asc'},
        }
        if not sortby:
            sortby = 'id'
        default_order_by = sorted_list[sortby]['order']

        total_equipamentos = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'vaso_de_pressao')])
        page_detail = pager(url='/my/equip/vaso',
                            total=total_equipamentos,
                            page=page,
                            url_args={'sortby': sortby},
                            step=5)
        equipamentos_vaso = equipamento_obj.search(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'vaso_de_pressao')], limit=5, order=default_order_by, offset=page_detail['offset'])

        vals = {
            'equipamentos': equipamentos_vaso,
            'sortby': sortby,
            'searchbar_sortings': sorted_list,
            'page_name': 'equipamento_list_view',
            'pager': page_detail,
        }
        return request.render("NREspecialista.wb_equipamento_list_view_portal", vals)

    @http.route(['/my/equip/caldeira', '/my/equip/caldeira/page/<int:page>'], type='http', website=True)
    def weblearnsEquipCaldeiraListView(self, page=1, sortby=None, **kw):
        equipamento_obj = request.env['nr.equipamento']
        partner = request.env.user.partner_id.parent_id.id

        sorted_list = {
            'id': {'label': _('ID'), 'order': 'equipamento_id asc'},
            'name': {'label': _('Nome'), 'order': 'name'},
            'tipo_equip': {'label': _('TAG'), 'order': 'tipo_equip asc'},
        }
        if not sortby:
            sortby = 'id'
        default_order_by = sorted_list[sortby]['order']

        total_equipamentos = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'caldeira')])
        page_detail = pager(url='/my/equip/vaso',
                            total=total_equipamentos,
                            page=page,
                            url_args={'sortby': sortby},
                            step=5)
        equipamentos_caldeira = equipamento_obj.search(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'caldeira')], limit=5, order=default_order_by, offset=page_detail['offset'])

        vals = {
            'equipamentos': equipamentos_caldeira,
            'sortby': sortby,
            'searchbar_sortings': sorted_list,
            'page_name': 'equipamento_list_view',
            'pager': page_detail,
        }
        return request.render("NREspecialista.wb_equipamento_list_view_portal", vals)

    @http.route(['/my/equip/tubulacao', '/my/equip/tubulacao/page/<int:page>'], type='http', website=True)
    def weblearnsEquipTubulacaoListView(self, page=1, sortby=None, **kw):
        equipamento_obj = request.env['nr.equipamento']
        partner = request.env.user.partner_id.parent_id.id

        sorted_list = {
            'id': {'label': _('ID'), 'order': 'equipamento_id asc'},
            'name': {'label': _('Nome'), 'order': 'name'},
            'tipo_equip': {'label': _('TAG'), 'order': 'tipo_equip asc'},
        }
        if not sortby:
            sortby = 'id'
        default_order_by = sorted_list[sortby]['order']

        total_equipamentos = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'tubulacao')])
        page_detail = pager(url='/my/equip/vaso',
                            total=total_equipamentos,
                            page=page,
                            url_args={'sortby': sortby},
                            step=5)
        equipamentos_tubulacao = equipamento_obj.search(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'tubulacao')], limit=5, order=default_order_by, offset=page_detail['offset'])

        vals = {
            'equipamentos': equipamentos_tubulacao,
            'sortby': sortby,
            'searchbar_sortings': sorted_list,
            'page_name': 'equipamento_list_view',
            'pager': page_detail,
        }
        return request.render("NREspecialista.wb_equipamento_list_view_portal", vals)

    @http.route(['/my/equip/tanque', '/my/equip/tanque/page/<int:page>'], type='http', website=True)
    def weblearnsEquipTanqueListView(self, page=1, sortby=None, **kw):
        equipamento_obj = request.env['nr.equipamento']
        partner = request.env.user.partner_id.parent_id.id

        sorted_list = {
            'id': {'label': _('ID'), 'order': 'equipamento_id desc'},
            'name': {'label': _('Nome'), 'order': 'name'},
            'tipo_equip': {'label': _('TAG'), 'order': 'tipo_equip asc'},
        }
        if not sortby:
            sortby = 'id'
        default_order_by = sorted_list[sortby]['order']

        total_equipamentos = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'tanque')])
        page_detail = pager(url='/my/equip/vaso',
                            total=total_equipamentos,
                            page=page,
                            url_args={'sortby': sortby},
                            step=5)
        equipamentos_tanque = equipamento_obj.search(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'tanque')], limit=5, order=default_order_by, offset=page_detail['offset'])

        vals = {
            'equipamentos': equipamentos_tanque,
            'sortby': sortby,
            'searchbar_sortings': sorted_list,
            'page_name': 'equipamento_list_view',
            'pager': page_detail,
        }
        return request.render("NREspecialista.wb_equipamento_list_view_portal", vals)
    # -------------------------------------------
    # Fim da Repetição de função desnecessaria
    # -------------------------------------------

    # -------------------------------------------
    # DashBoard
    # Conta quantos de cada equipmaneto existe na mesma empresa
    # -------------------------------------------

    @http.route(['/my/equip'], type='http', website=True)
    def weblearnsEquipDashboardView(self, ** kw):
        equipamento_obj = request.env['nr.equipamento']
        partner = request.env.user.partner_id.parent_id.id

        total_equipamentos_vaso = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'vaso_de_pressao')])
        total_equipamentos_caldeira = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'caldeira')])
        total_equipamentos_tubulacao = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'tubulacao')])
        total_equipamentos_tanque = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'tanque')])

        vals = {
            'total_equipamentos_vaso': total_equipamentos_vaso,
            'total_equipamentos_caldeira': total_equipamentos_caldeira,
            'total_equipamentos_tubulacao': total_equipamentos_tubulacao,
            'total_equipamentos_tanque': total_equipamentos_tanque,
            'page_name': 'equipamento_list_dashboard_view',
        }
        return request.render("NREspecialista.wb_equipamento_dashboard_view_portal", vals)

    # ----------------------------------------------------------------------------------------------------------
    # Abre uma pagina para cada equipamento, além de "tentar" fazer um token de acesso para pessoas especificas
    # A parte de token parece não estar funcionando, pode estar faltando algum codigo de funcionalidade
    # ----------------------------------------------------------------------------------------------------------
    @http.route(['/my/equip/vaso/<int:equipamento_id>',
                 '/my/equip/caldeira/<int:equipamento_id>',
                 '/my/equip/tanque/<int:equipamento_id>',
                 '/my/equip/tubulacao/<int:equipamento_id>'], auth="public", type='http', website=True)
    def weblearnsEquipFormView(self, equipamento_id, access_token=None, **kw):
        try:
            order_sudo = self._document_check_access(
                'nr.equipamento', equipamento_id, access_token=access_token)
        except (AccessError, MissingError):
            return request.redirect('/my')

        try:
            equipamento_obj = request.env['nr.equipamento']
            equipamentos = equipamento_obj.search([])
            partner = request.env.user.partner_id.parent_id.id

            for equipamento_sourch in equipamentos:
                if equipamento_sourch.equipamento_id == str(equipamento_id):
                    if equipamento_sourch.tipo_equip == 'vaso_de_pressao':
                        equipamento_records = request.env['nr.equipamento'].search(
                            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'vaso_de_pressao')])
                        tipo_equip = 'vaso'
                    elif equipamento_sourch.tipo_equip == 'caldeira':
                        equipamento_records = request.env['nr.equipamento'].search(
                            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'caldeira')])
                        tipo_equip = 'caldeira'
                    elif equipamento_sourch.tipo_equip == 'tanque':
                        equipamento_records = request.env['nr.equipamento'].search(
                            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'tanque')])
                        tipo_equip = 'tanque'
                    elif equipamento_sourch.tipo_equip == 'tubulacao':
                        equipamento_records = request.env['nr.equipamento'].search(
                            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'tubulacao')])
                        tipo_equip = 'tubulacao'
                    equipamento_ids = equipamento_records.ids
                    equipamento_index = equipamento_ids.index(equipamento_id)
                    vals = {"id": equipamento_id,
                            'nr_equipamento': order_sudo,
                            'token': access_token,
                            "equipamentos": equipamento_sourch,
                            'page_name': 'equipamento_form_view',
                            }
                    if equipamento_index != 0 and equipamento_ids[equipamento_index-1]:
                        vals['prev_record'] = '/my/equip/{}/{}'.format(
                            tipo_equip, equipamento_ids[equipamento_index-1])
                    if equipamento_index < len(equipamento_ids) - 1 and equipamento_ids[equipamento_index+1]:
                        vals['next_record'] = '/my/equip/{}/{}'.format(
                            tipo_equip, equipamento_ids[equipamento_index+1])
                    return request.render("NREspecialista.wb_equipamento_form_view_portal", vals)
        except Exception as e:
            return request.redirect('/my')
