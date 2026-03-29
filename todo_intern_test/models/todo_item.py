from odoo import models, fields

class TodoItem(models.Model):
    _name = 'todo.item'
    _description = 'Todo Item'

    list_id = fields.Many2one('todo.list', string='Todo List')
    name = fields.Char(string='Item Name', required=True) # [cite: 30]
    description = fields.Text(string='Description') # [cite: 31]
    is_done = fields.Boolean(string='Done')  # [cite: 32]
