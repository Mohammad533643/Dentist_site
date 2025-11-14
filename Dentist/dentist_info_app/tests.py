from django.test import TestCase, SimpleTestCase
from .models import Dentist
from .forms import Contact_Form
from datetime import datetime
from django.urls import reverse, resolve


# region:testing Concat form


class TestConcatForm(SimpleTestCase):
    def test_form_with_valid_data(self):
        form = Contact_Form(data={
            "Gmail": "reza@gmail.com",
            "Message": "This is a test."
        })
        self.assertTrue(form.is_valid())
# endregion

# region :testing __str__ methode in Dentist model


class TestDentistModel(SimpleTestCase):
    def test_model_with_valid_data(self):
        instance = Dentist(Full_name="Michael", User_id="12345",
                           Speciality="Orthodontist", City="Canberra")

        self.assertTrue(str(instance), "Michael")
# endregion
