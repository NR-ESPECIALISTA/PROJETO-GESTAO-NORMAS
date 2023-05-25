# -*- coding: utf-8 -*-
{
    'name': "NrEspecialista",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Modulo para controle, gestão e inspeção de equipamentos de alta pressão.
    """,

    'author': "Equipe Nr-Especialista",
    'website': "https://metainspecoes.com.br/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Gestão',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail', 'portal', 'board', 'project'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/equipamento.xml',
        'views/portal_template.xml',
        'data/sequence.xml',
        'views/linhas_ramais.xml',
        'views/material_fabricacao.xml',
        'views/normas_calibracao.xml',
        'views/normas_fabricacao.xml',
        'views/tipo_fluido.xml',
        #'views/css_loader.xml'
        # 'views/views.xml',
        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'assets':{
        'web.assets_backend':[
            'NREspecialista/static/src/css/style_dashboard_portal.css'
        ],
    },
    'license': 'GPL-3',
}
