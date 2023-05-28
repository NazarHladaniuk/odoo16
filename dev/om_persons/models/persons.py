from datetime import date

from odoo import models, fields, api


class Persons(models.Model):
    _name = "custom_module.persons"
    _description = "Records of persons"

    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    full_name = fields.Char(string="Full Name", compute="_compute_full_name")
    birthday = fields.Date(string="Birthday")
    age = fields.Integer(string="Age", compute="_compute_age")
    sex = fields.Selection(
        [
            ("male", "Male"),
            ("female", "Female"),
            ("non_binary", "Non-Binary")
        ],
        string="Sex"
    )
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        default=lambda self: self.env.user.company_id,
        required=True
    )

    @api.depends("first_name", "last_name")
    def _compute_full_name(self):
        for person in self:
            if person.first_name and person.last_name:
                person.full_name = f"{person.first_name} {person.last_name}"
            else:
                person.full_name = "Enter first name and last name"

    @api.depends("birthday")
    def _compute_age(self):
        today = date.today()
        for person in self:
            if person.birthday:
                birth_date = person.birthday
                age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            else:
                age = 0
            person.age = age
