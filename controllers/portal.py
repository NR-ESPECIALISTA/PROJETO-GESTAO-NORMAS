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
        # equipamento_obj = request.env['nr.equipamento']
        # equipamentos = equipamento_obj.search([()])
        # for equipamento_sourch in equipamentos:
        #     if equipamento_sourch.cliente_propri == partner:
        #         equipamento_count = equipamento_count + 1
        if 'equipamento_count' in counters:
            equipamento_count = request.env['nr.equipamento'].search_count([('cliente_propri.id', '=', partner)]) \
                if request.env['nr.equipamento'].check_access_rights('read', raise_exception=False) else 0
            values['equipamento_count'] = equipamento_count
        return values
    # -------------------------------------------
    # lista os equipamentos do tipo vaso da mesma empresa
    # -------------------------------------------

    @http.route(['/my/equip/vaso', '/my/equip/vaso/page/<int:page>'], type='http', website=True)
    def weblearnsEquipVasoListView(self, page=1, sortby=None, **kw):
        equipamento_obj = request.env['nr.equipamento']
        partner = request.env.user.partner_id.parent_id.id

        sorted_list = {
            'id': {'label': _('ID'), 'order': 'equipamento_id desc'},
            'name': {'label': _('Nome'), 'order': 'name'},
            'tipo_equip': {'label': _('TAG'), 'order': 'tipo_equip asc'},
        }
        if not sortby:
            sortby = 'tipo_equip'
        default_order_by = sorted_list[sortby]['order']

        total_equipamentos = equipamento_obj.search_count(
            [('cliente_propri.id', '=', partner) and ('tipo_equip', '=', 'vaso_de_pressao')])
        page_detail = pager(url='/my/equip/vaso',
                            total=total_equipamentos,
                            page=page,
                            url_args={'sortby': sortby},
                            step=5)
        equipamentos = equipamento_obj.search(
            [('cliente_propri.id', '=', partner) and ('tipo_equip', '=', 'vaso_de_pressao')], limit=5, order=default_order_by, offset=page_detail['offset'])

        vals = {
            'equipamentos': equipamentos,
            'sortby': sortby,
            'searchbar_sortings': sorted_list,
            'page_name': 'equipamento_list_vaso_view',
            'pager': page_detail
        }
        return request.render("NREspecialista.wb_equipamento_list_vaso_view_portal", vals)

    # -------------------------------------------
    # DashBoard
    # -------------------------------------------
    @http.route(['/my/equip'], type='http', website=True)
    def weblearnsEquipListView(self, ** kw):
        equipamento_obj = request.env['nr.equipamento']
        partner = request.env.user.partner_id.parent_id.id
        total_equipamentos = equipamento_obj.search_count(
            [('cliente_propri.id', '=', partner) and ('tipo_equip', '=', 'vaso_de_pressao')])

        vals = {
            'total_equipamentos': total_equipamentos,
            'page_name': 'equipamento_list_dashboard_view',
        }
        return request.render("NREspecialista.wb_equipamento_dashboard_view_portal", vals)

    # ----------------------------------------------------------------------------------------------------------
    # Abre uma pagina para cada equipamento, além de "tentar" fazer um token de acesso para pessoas especificas
    # ----------------------------------------------------------------------------------------------------------
    @http.route(['/my/equip/vaso/<int:equipamento_id>'], auth="public", type='http', website=True)
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
            equipamento_records = request.env['nr.equipamento'].search(
                [('cliente_propri.id', '=', partner) and ('tipo_equip', '=', 'vaso_de_pressao')])
            equipamento_ids = equipamento_records.ids
            equipamento_index = equipamento_ids.index(equipamento_id)

            for equipamento_sourch in equipamentos:
                if equipamento_sourch.equipamento_id == str(equipamento_id):
                    vals = {"id": equipamento_id,
                            'nr_equipamento': order_sudo,
                            'token': access_token,
                            "equipamentos": equipamento_sourch,
                            'page_name': 'equipamento_form_view',
                            }
                    if equipamento_index != 0 and equipamento_ids[equipamento_index-1]:
                        vals['prev_record'] = '/my/equip/vaso/{}'.format(
                            equipamento_ids[equipamento_index-1])
                    if equipamento_index < len(equipamento_ids) - 1 and equipamento_ids[equipamento_index+1]:
                        vals['next_record'] = '/my/equip/vaso/{}'.format(
                            equipamento_ids[equipamento_index+1])
                    # if order_sudo.state in ('draft', 'sent', 'cancel'):
                    #     history = request.session.get('my_quotations_history', [])
                    # else:
                    #     history = request.session.get('my_orders_history', [])
                    # values.update(get_records_pager(history, order_sudo))
                    return request.render("NREspecialista.wb_equipamento_form_view_portal", vals)
        except Exception as e:
            return request.redirect('/my')
