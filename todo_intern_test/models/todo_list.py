from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'

    name = fields.Char(string='Title', required=True)  # [cite: 9]
    tag_ids = fields.Many2many('todo.tag', string='Tags')  # [cite: 10]
    start_date = fields.Datetime(string='Start Date', required=True)  # [cite: 12, 13]
    end_date = fields.Datetime(string='End Date', required=True)  # [cite: 12, 13]
    
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete')
    ], string='Status', default='draft', readonly=True)  # [cite: 14]

    attendee_ids = fields.Many2many('res.users', string='Attendees')  # [cite: 61]
    item_ids = fields.One2many('todo.item', 'list_id', string='Items')  # [cite: 29]
    all_items_done = fields.Boolean(string='All Items Done', compute='_compute_all_items_done', store=True)

    @api.depends('item_ids.is_done')
    def _compute_all_items_done(self):
        for record in self:
            record.all_items_done = all(item.is_done for item in record.item_ids) if record.item_ids else False

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.end_date <= record.start_date:
                raise ValidationError("The End Date must be later than the Start Date.")  # [cite: 12]

    def action_confirm(self):
        self.status = 'in_progress'  # [cite: 15]

    def action_done(self):
        self.status = 'complete'  # [cite: 85]
