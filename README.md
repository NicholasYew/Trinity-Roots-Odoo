# Todo List Management Module

## Overview
This Odoo module provides a comprehensive Todo List Management system for internal users. It is designed to allow users to create, manage, and track todo lists, items, tags, and attendees, with full CRUD permissions and status workflows.

## Features
- **Todo List Creation:** Users can create todo lists with a required title, start and end dates, and assign tags and attendees.
- **Tag Management:** Default tags (Work, Event, Life achievement) are provided via data files. Users can add additional tags as needed.
- **Date Validation:** The module enforces that the end date must be later than the start date.
- **Status Tracking:** Each todo list tracks its status (Draft, In Progress, Complete) and provides buttons to transition between states.
- **Todo Items:** Each list can have multiple items, each with a name, description, and a checkbox to mark as finished. Inline editing is supported.
- **Attendees:** Users can assign internal users as attendees to each todo list.
- **Menu Structure:** The module provides three sub-menus: All Todo Lists, Incomplete Lists, and Complete Lists.
- **Permissions:** Full read, write, create, and delete permissions are granted to internal users via the access control file.

## Code Structure
- **models/todo_list.py:**
  - Defines the `todo.list` model with fields for title, tags, dates, status, attendees, and items.
  - Implements constraints to ensure valid date ranges.
  - Provides methods for status transitions and a computed field to check if all items are done.
- **models/todo_item.py:**
  - Defines the `todo.item` model for individual checklist items, including name, description, and completion status.
- **models/todo_tag.py:**
  - Defines the `todo.tag` model for tagging todo lists, with a name and color index.
- **views/todo_list_views.xml:**
  - Configures the form and tree views for todo lists, including status buttons, field visibility, and menu actions for filtered views.
- **views/todo_item_views.xml:**
  - Configures the form and tree views for todo items, supporting inline editing and linking to parent lists.
- **security/ir.model.access.csv:**
  - Grants full access rights to internal users for all models in the module.
- **data/todo_tag_data.xml:**
  - Provides default tag records for initial module setup.

## Testing and Limitations
Due to technical constraints, I was unable to test this module on Odoo 18 Community Edition. Despite my attempts to update the `addons_path` in the `odoo.conf` file and restarting the Odoo service, the module did not appear in the Apps list. All code and configuration have been reviewed for correctness and completeness, but functional testing could not be performed in the target environment.

