from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'

    name = fields.Char(string='Title', required=True) [cite: 9]
    tag_ids = fields.Many2many('todo.tag', string='Tags') [cite: 10]
    start_date = fields.Datetime(string='Start Date', required=True) [cite: 12, 13]
    end_date = fields.Datetime(string='End Date', required=True) [cite: 12, 13]
    
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete')
    ], string='Status', default='draft', readonly=True) [cite: 14]

    # Required: Record attendees linked to res.users [cite: 61]
    attendee_ids = fields.Many2many('res.users', string='Attendees') [cite: 61]
    
    # Required: Record Todo items [cite: 29]
    item_ids = fields.One2many('todo.item', 'list_id', string='Items') [cite: 29]

    # Required: End Date must be later than Start Date [cite: 12]
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.end_date <= record.start_date:
                raise ValidationError("The End Date must be later than the Start Date.") [cite: 12]

    # Required: Button to transition from Draft to In Progress [cite: 15]
    def action_confirm(self):
        self.status = 'in_progress' [cite: 15]

    # Required: Change status to Complete when items are done 
    def action_done(self):
        self.status = 'complete' [cite: 85]