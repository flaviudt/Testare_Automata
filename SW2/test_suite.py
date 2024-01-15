"""
SUITE DE TESTE

- Suitele de teste sunt utile din doua puncte de vedere:

1. Sa putem sa rulam mai multe clase in acelasi timp
2. Sa specificam configuratia pentru raportul de executie

- Suita de executie va contine toate clasele de test pe care ne dorim sa le executam intr-o rulare.

- Din punct de vedere TEHNIC:
    -- Suita de teste trebuie facuta intr-o clasa numita TestSuite care sa mosteneasca unittest.TestCase:
class TestSuite(unittest.TestCase):

    -- In interiorul acestei clase vom avea o metoda numita test_suite care sa contina un obiect instantiat din clasa TestSuite:

            test_de_rulat = unittest.TestSuite()

    -- Prin intermediul acestui obiect vom apela metoda addTests care va primi drept parametru
o lista de clase de test care se doreste a fi executate.

teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(Firefox)]
"""
import unittest
import HtmlTestRunner

from SW2.test_elefant_page import TestElefantPage
from SW2.test_carturesti_page import TestCarturestiPage
from SW2.test_herokuapp_page import TestHeroukappPage


class TestSuite(unittest.TestCase):

    def test_suite(self):

        teste_de_rulat = unittest.TestSuite()

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestElefantPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCarturestiPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestHeroukappPage)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='Tests Results',
            report_title='TestReport'
        )

        runner.run(teste_de_rulat)


"""
Generarea RAPORTULUI DE TESTE

- In interiorul metodei definite anterior, va trebui sa definim un runner care sa contina parametrii de configurare
ai raportului de executie:

runner = HtmlTestRunner.HTMLTestRunner\
        (
            combine_reports=True, # daca avem mai multe clase de test, rezultatele vor fi puse in acelasi raport de executie
            report_title='TestReport',
            report_name='Smoke Test Result'
        )

- Pentru a putea avea acest runner functional trebuie sa instalam libraria html-testRunner
(pip install html-testRunner) si sa importam (import HtmlTestRunner).
- Dupa cum observati, runner este un obiect instantiat din clasa HTMLTestRunner care a primit drept argumente valorile
combine_reports, report_title si report_name.
- Ultimul pas va fi sa apelam runnerul care va primi drept argument lista de teste de rulat:
 
runner.run(test_de_rulat)

- Observati cum dupa rulare in meniul din stanga a aparut raportul de executie.
- Experimentati putin cu diverse teste si observati cum se schimba raportul de executie.
"""