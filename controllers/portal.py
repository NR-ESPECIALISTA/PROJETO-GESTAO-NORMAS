from odoo import http, _
from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.exceptions import AccessError, MissingError
from collections import OrderedDict
from odoo.http import request
from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models


class WeblearnsPortal(CustomerPortal):

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

    @http.route(['/my/equip', '/my/equip/page/<int:page>'], type='http', website=True)
    def weblearnsEquipListView(self, page=1, **kw):
        equipamento_obj = request.env['nr.equipamento']
        partner = request.env.user.partner_id.parent_id.id
        total_equipamentos = equipamento_obj.search_count(
            [('cliente_propri.id', '=', partner)])
        page_detail = pager(url='/my/equip',
                            total=total_equipamentos,
                            page=page,
                            step=5)
        equipamentos = equipamento_obj.search(
            [], limit=5, offset=page_detail['offset'])
        vals = {'equipamentos': equipamentos,
                'page_name': 'equipamento_list_view',
                'pager': page_detail}
        return request.render("NREspecialista.wb_equipamento_list_view_portal", vals)

    # @http.route(['/my/equip/<int:equipamento_id>'], auth="public", type='http', website=True)
    # def weblearnsEquipFormView(self, equipamento_id, **kw):
    #     equipamento_obj = request.env['nr.equipamento']
    #     equipamentos = equipamento_obj.search([])
    #     for equipamento_sourch in equipamentos:
    #         if equipamento_sourch.equipamento_id == str(equipamento_id):
    #             vals = {"id": equipamento_id,
    #                     "equipamentos": equipamento_sourch,
    #                     'page_name': 'equipamento_form_view',
    #                     }
    #             return request.render("NREspecialista.wb_equipamento_form_view_portal", vals)
    @http.route(['/my/equip/<int:equipamento_id>'], auth="public", type='http', website=True)
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
                [('cliente_propri.id', '=', partner)])
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
                        vals['prev_record'] = '/my/equip/{}'.format(
                            equipamento_ids[equipamento_index-1])
                    if equipamento_index < len(equipamento_ids) - 1 and equipamento_ids[equipamento_index+1]:
                        vals['next_record'] = '/my/equip/{}'.format(
                            equipamento_ids[equipamento_index+1])
                    # if order_sudo.state in ('draft', 'sent', 'cancel'):
                    #     history = request.session.get('my_quotations_history', [])
                    # else:
                    #     history = request.session.get('my_orders_history', [])
                    # values.update(get_records_pager(history, order_sudo))
                    return request.render("NREspecialista.wb_equipamento_form_view_portal", vals)
        except Exception as e:
            return request.redirect('/my')
