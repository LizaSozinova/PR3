from django.test import TestCase
from django.urls import reverse

class BudgetTests(TestCase):
    def test_status_ok(self):
        response = self.client.get("/status/")
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, {"status": "ok"})

    def test_balance_flow(self):
        self.client.get("/add/?kind=income&amount=1000")
        self.client.get("/add/?kind=expense&amount=300")
        r = self.client.get("/balance/")
        self.assertJSONEqual(r.content, {"balance": 700})
