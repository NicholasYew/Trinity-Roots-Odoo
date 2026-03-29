from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'

    # 1. Title: Ability to specify a Todo List name (Required)
    name = fields.Char(string='Title', required=True)
    # 2. Tags: Ability to specify tags (default tags via data files, can add more)
    tag_ids = fields.Many2many('todo.tag', string='Tags')
    # 3. Dates: Start Date and End Date (End Date must be later than Start Date, Required)
    start_date = fields.Datetime(string='Start Date', required=True)
    end_date = fields.Datetime(string='End Date', required=True)
    # 4. Status Tracking: Track statuses: Draft / In Progress / Complete
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete')
    ], string='Status', default='draft', readonly=True)
    # 7. Attendees: Record attendees for the Todo List (linked to res.users)
    attendee_ids = fields.Many2many('res.users', string='Attendees')
    # 6. Todo Items: Record Todo items (see todo_item.py for details)
    item_ids = fields.One2many('todo.item', 'list_id', string='Items')
    # 8. Computed field: All items marked as complete
    all_items_done = fields.Boolean(string='All Items Done', compute='_compute_all_items_done', store=True)

    # 8. Compute if all items are done
    @api.depends('item_ids.is_done')
    def _compute_all_items_done(self):
        for record in self:
            record.all_items_done = all(item.is_done for item in record.item_ids) if record.item_ids else False

    # 3. Dates: Constraint to ensure End Date > Start Date
    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.start_date and record.end_date and record.end_date <= record.start_date:
                raise ValidationError("The End Date must be later than the Start Date.")

    # 5. State Transition: Button to transition from Draft to In Progress
    def action_confirm(self):
        self.status = 'in_progress'

    # 8. Button to change status to Complete when all items are done
    def action_done(self):
        self.status = 'complete'
