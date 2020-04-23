from django.test import TestCase
from .models import Calculation


class CfpTestCase(TestCase):
    def setup(self):
        Calculation.objects.create(
            name="test_1_dead_person_0_CFP_expected",
            email="test@test.test",
            # need irina with test input and outputs.
            offset=0,
            a1=0, a2=0, a3=0, a4=0, a5=0,
            b1=0, b2=0, b3=0,
            c1=0, c2=0, c3=0, c4=0, c5=0, c6=0, c7=0, c8=0,
            d1=0, d2=0, d3=0, d4=0, d5=0, d6=0, d7=0, d8=0, d9=0, da=0, db=0,
            e1=0, e2=0, e3=0, e4=0, e5=0, e6=0,
            f1=0, f2=0, f3=0, f4=0, f5=0,
        )

        Calculation.objects.create(
            name="test_2_cool_vegan_low_CFP_expected",
            email="test@test.test",
            # need irina with test input and outputs.
            offset=0,
            a1=0, a2=0, a3=0, a4=0, a5=0,
            b1=0, b2=0, b3=0,
            c1=0, c2=0, c3=0, c4=0, c5=0, c6=0, c7=0, c8=0,
            d1=0, d2=0, d3=0, d4=0, d5=0, d6=0, d7=0, d8=0, d9=0, da=0, db=0,
            e1=0, e2=0, e3=0, e4=0, e5=0, e6=0,
            f1=0, f2=0, f3=0, f4=0, f5=0,
        )

        Calculation.objects.create(
            name="test_3_meat_eater_high_CFP_expected",
            email="test@test.test",
            # need irina with test input and outputs.
            offset=0,
            a1=0, a2=0, a3=0, a4=0, a5=0,
            b1=0, b2=0, b3=0,
            c1=0, c2=0, c3=0, c4=0, c5=0, c6=0, c7=0, c8=0,
            d1=0, d2=0, d3=0, d4=0, d5=0, d6=0, d7=0, d8=0, d9=0, da=0, db=0,
            e1=0, e2=0, e3=0, e4=0, e5=0, e6=0,
            f1=0, f2=0, f3=0, f4=0, f5=0,
        )

        Calculation.objects.create(
            name="test_4_frequent_flier_very_high_CFP_expected",
            email="test@test.test",
            # need irina with test input and outputs.
            offset=0,
            a1=0, a2=0, a3=0, a4=0, a5=0,
            b1=0, b2=0, b3=0,
            c1=0, c2=0, c3=0, c4=0, c5=0, c6=0, c7=0, c8=0,
            d1=0, d2=0, d3=0, d4=0, d5=0, d6=0, d7=0, d8=0, d9=0, da=0, db=0,
            e1=0, e2=0, e3=0, e4=0, e5=0, e6=0,
            f1=0, f2=0, f3=0, f4=0, f5=0,
        )

    def test_cfp_works(self):
        test_1 = Calculation.objects.get(
            name="test_1_dead_person_0_CFP_expected")
        test_2 = Calculation.objects.get(
            name="test_2_cool_vegan_low_CFP_expected")
        test_3 = Calculation.objects.get(
            name="test_3_meat_eater_high_CFP_expected")
        test_4 = Calculation.objects.get(
            name="test_4_frequent_flier_very_high_CFP_expected")
        self.assertEqual(test_1.cfp, 0)
        self.assertTrue(test_2.cfp <= 1)
        self.assertTrue(test_3.cfp > 1)
        self.assertTrue(test_3.cfp <= 10)
        self.assertTrue(test_4.cfp > 10)
        self.assertTrue(test_4.cfp <= 1000)
