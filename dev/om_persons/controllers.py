from odoo import http
from odoo.http import request


class PersonsController(http.Controller):
    @http.route("/persons", type="http", auth="public", website=True)
    def persons_page(self, **kwargs):
        Persons = request.env["custom_module.persons"]
        persons = Persons.search([], limit=5, order="create_date desc")
        return http.request.render("custom_module.persons_template", {"persons": persons})
