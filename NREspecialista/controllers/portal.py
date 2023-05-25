from odoo import http, _
from odoo.addons.portal.controllers.portal import CustomerPortal, pager
from odoo.exceptions import AccessError, MissingError
from odoo.fields import Command
from collections import OrderedDict
from odoo.http import request
from odoo.exceptions import UserError, ValidationError
from odoo import api, fields, models
from operator import itemgetter
from markupsafe import Markup
from odoo.tools import groupby as groupbyelem
from odoo.osv.expression import OR, AND
from odoo.addons.web.controllers.main import HomeStaticTemplateHelpers

'''
from odoo import conf, http, _ -->esperar
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager
from odoo.tools import groupby as groupbyelem
'''
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
    def weblearnsEquipVasoListView(self, page=1, search=None, search_in=None, sortby=None, **kw): #adicionado equipamento, search, search in e group
        equipamento_obj = request.env['nr.equipamento']
        partner = request.env.user.partner_id.parent_id.id
        #domain = [('equipamento_id', '=', equipamento.id)]
        #values = self._prepare_portal_layout_values() #novo input
        #searchbar_sortings = self._task_get_searchbar_sortings() #novo input
        #searchbar_inputs = self._task_get_searchbar_inputs() #novo input
        #searchbar_groupby = self._task_get_searchbar_groupby() #novo input

        sorted_list = {
            'id': {'label': _('ID'), 'order': 'equipamento_id asc'},
            'name': {'label': _('Nome'), 'order': 'name'},
            'tipo_equip': {'label': _('TAG'), 'order': 'tipo_equip asc'},
        }
        if not sortby:
            sortby = 'id'
            #order = searchbar_sortings[sortby]['order']
        default_order_by = sorted_list[sortby]['order']
        
        #------------------------------------#
        # novos inputs de pesquisa           #
        #------------------------------------#
        #if not groupby:
        #    groupby = 'tipo_equip'

        #if date_begin and date_end:
        #    domain += [('create_date', '>', date_begin), ('create_date', '<=', date_end)]

        # search
        if search and search_in:
            domain += self._task_get_search_domain(search_in, search)

        #------------------------------------#
        # fim dos novos inputs de pesquisa   #
        #------------------------------------#
        
        
        total_equipamentos = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'vaso_de_pressao')])
        page_detail = pager(url='/my/equip/vaso',
                            total=total_equipamentos,
                            page=page,
                            url_args={'sortby': sortby},
                            step=5)
        equipamentos_vaso = equipamento_obj.search(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'vaso_de_pressao')], limit=5, order=default_order_by, offset=page_detail['offset'])
        ##order = self._task_get_order(order, groupby) #novo input
        vals = {
            'equipamentos': equipamentos_vaso,
            'sortby': sortby,
            'search': search,
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
    
    @http.route(['/my/equip/psv', '/my/equip/psv/page/<int:page>'], type='http', website=True)
    def weblearnsEquipPsvListView(self, page=1, sortby=None, **kw):
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
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'psv')])
        page_detail = pager(url='/my/equip/psv',
                            total=total_equipamentos,
                            page=page,
                            url_args={'sortby': sortby},
                            step=5)
        equipamentos_psv = equipamento_obj.search(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'psv')], limit=5, order=default_order_by, offset=page_detail['offset'])

        vals = {
            'equipamentos': equipamentos_psv,
            'sortby': sortby,
            'searchbar_sortings': sorted_list,
            'page_name': 'equipamento_list_view',
            'pager': page_detail,
        }
        return request.render("NREspecialista.wb_equipamento_list_view_portal", vals)
    
    
    @http.route(['/my/equip/pi', '/my/equip/pi/page/<int:page>'], type='http', website=True)
    def weblearnsEquipPiListView(self, page=1, sortby=None, **kw):
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
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'pi')])
        page_detail = pager(url='/my/equip/pi',
                            total=total_equipamentos,
                            page=page,
                            url_args={'sortby': sortby},
                            step=5)
        equipamentos_pi = equipamento_obj.search(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'pi')], limit=5, order=default_order_by, offset=page_detail['offset'])

        vals = {
            'equipamentos': equipamentos_pi,
            'sortby': sortby,
            'searchbar_sortings': sorted_list,
            'page_name': 'equipamento_list_view',
            'pager': page_detail,
        }
        return request.render("NREspecialista.wb_equipamento_list_view_portal", vals)
    
    
    @http.route(['/my/equip/outros', '/my/equip/outros/page/<int:page>'], type='http', website=True)
    def weblearnsEquipOutrosListView(self, page=1, sortby=None, **kw):
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
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'outros')])
        page_detail = pager(url='/my/equip/outros',
                            total=total_equipamentos,
                            page=page,
                            url_args={'sortby': sortby},
                            step=5)
        equipamentos_outros = equipamento_obj.search(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'outros')], limit=5, order=default_order_by, offset=page_detail['offset'])

        vals = {
            'equipamentos': equipamentos_outros,
            'sortby': sortby,
            'searchbar_sortings': sorted_list,
            'page_name': 'equipamento_list_view',
            'pager': page_detail,
        }
        return request.render("NREspecialista.wb_equipamento_list_view_portal", vals)
    
    @http.route(['/my/equip/todos', '/my/equip/todos/page/<int:page>'], type='http', website=True)
    def weblearnsEquipTodosListView(self, page=1, sortby=None, **kw):
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
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'todos')])
        page_detail = pager(url='/my/equip/todos',
                            total=total_equipamentos,
                            page=page,
                            url_args={'sortby': sortby},
                            step=5)
        equipamentos_todos = equipamento_obj.search(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '!=', 'Null')], limit=5, order=default_order_by, offset=page_detail['offset'])

        vals = {
            'equipamentos': equipamentos_todos,
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
        total_equipamentos_psv = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'psv')])
        total_equipamentos_pi = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'pi')])
        total_equipamentos_outros = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'outros')])
        total_equipamentos_todos = equipamento_obj.search_count(
            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '!=', 'Null')])

        vals = {
            'total_equipamentos_vaso': total_equipamentos_vaso,
            'total_equipamentos_caldeira': total_equipamentos_caldeira,
            'total_equipamentos_tubulacao': total_equipamentos_tubulacao,
            'total_equipamentos_tanque': total_equipamentos_tanque,
            'total_equipamentos_psv': total_equipamentos_psv,
            'total_equipamentos_pi': total_equipamentos_pi,
            'total_equipamentos_outros': total_equipamentos_outros,
            'total_equipamentos_todos': total_equipamentos_todos,
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
                 '/my/equip/tubulacao/<int:equipamento_id>',
                 '/my/equip/psv/<int:equipamento_id>',
                 '/my/equip/pi/<int:equipamento_id>',
                 '/my/equip/outros/<int:equipamento_id>'], auth="public", type='http', website=True)
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
                    elif equipamento_sourch.tipo_equip == 'psv':
                        equipamento_records = request.env['nr.equipamento'].search(
                            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'psv')])
                        tipo_equip = 'psv'
                    elif equipamento_sourch.tipo_equip == 'pi':
                        equipamento_records = request.env['nr.equipamento'].search(
                            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'pi')])
                        tipo_equip = 'pi'
                    elif equipamento_sourch.tipo_equip == 'outros':
                        equipamento_records = request.env['nr.equipamento'].search(
                            ['&', ('cliente_propri.id', '=', partner), ('tipo_equip', '=', 'outros')])
                        tipo_equip = 'outros'            
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
        
# =========================
# defs 
#--------------------------
#def _task_get_search_domain(self, search_in, search):
        #search_domain = []
        #if search_in in ('state', 'all'):
        #    search_domain.append([('name', 'ilike', search)])
        #    search_domain.append([('description', 'ilike', search)])
        #if search_in in ('customer', 'all'):
        #    search_domain.append([('partner_id', 'ilike', search)])
        #if search_in in ('message', 'all'):
        #    search_domain.append([('message_ids.body', 'ilike', search)])
        #if search_in in ('stage', 'all'):
        #    search_domain.append([('stage_id', 'ilike', search)])
        #if search_in in ('project', 'all'):
        #    search_domain.append([('project_id', 'ilike', search)])
        #if search_in in ('ref', 'all'):
        #    search_domain.append([('id', 'ilike', search)])
        #if search_in in ('users', 'all'):
        #    user_ids = request.env['res.users'].sudo().search([('name', 'ilike', search)])
        #    search_domain.append([('user_ids', 'in', user_ids.ids)])
        #if search_in in ('priority', 'all'):
        #    search_domain.append([('priority', 'ilike', search == 'normal' and '0' or '1')])
        #if search_in in ('status', 'all'):
        #    search_domain.append([
        #        ('kanban_state', 'ilike', 'normal' if search == 'In Progress' else 'done' if search == 'Ready' else 'blocked' if search == 'Blocked' else search)
        #    ])
        #return OR(search_domain)
        
#def _task_get_searchbar_inputs(self):
        #values = {
            #'all': {'input': 'all', 'label': _('Search in All'), 'order': 1},
            #'content': {'input': 'content', 'label': Markup(_('Search <span class="nolabel"> (in Content)</span>')), 'order': 1},
            #'ref': {'input': 'ref', 'label': _('Search in Ref'), 'order': 1},
            #'project': {'input': 'project', 'label': _('Search in Project'), 'order': 2},
            #'users': {'input': 'users', 'label': _('Search in Assignees'), 'order': 3},
            #'state': {'input': 'state', 'label': _('Search in Stages'), 'order': 2},
            #'status': {'input': 'status', 'label': _('Search in Status'), 'order': 5},
            #'priority': {'input': 'priority', 'label': _('Search in Priority'), 'order': 6},
            #'message': {'input': 'message', 'label': _('Search in Messages'), 'order': 10},
        #}
        #return dict(sorted(values.items(), key=lambda item: item[1]["order"]))
# =========================
# fim dos defs 
#--------------------------