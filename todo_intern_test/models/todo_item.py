from odoo import models, fields

class TodoItem(models.Model):
    _name = 'todo.item'
    _description = 'Todo Item'

    # 6. Todo Items:
    # a. Item Name
    name = fields.Char(string='Item Name', required=True)
    # b. Description
    description = fields.Text(string='Description')
    # c. Checkbox to mark items as finished (visible only when status is In Progress, handled in view)
    is_done = fields.Boolean(string='Done')
    # d. When status is Complete, all records/items become non-editable (handled in view)
    # e. Inline editing supported in tree view (handled in view)
    # Relation to parent Todo List
    list_id = fields.Many2one('todo.list', string='Todo List')
