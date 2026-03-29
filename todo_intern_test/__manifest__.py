{
    'name': 'Todo List Management',
    'version': '1.0',
    'category': 'Extra Tools',
    'summary': 'Module for managing internal tasks',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'data/todo_tag_data.xml',
        'views/todo_list_views.xml',
    ],
    'installable': True,
    'application': True,
}
