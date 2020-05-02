from django.test import TestCase
from .models import Calculation


class CfpTestCase(TestCase):
    def test_dead_person(self):
        test_1 = Calculation.objects.create(
            name="test_1_dead",
            email="test@test.test",
            offset=0,
            a1=0, a2=0, a3=0, a4=0, a5=0,
            b1=0, b2=0, b3=0,
            c1=0, c2=1, c3=0, c4=1, c5=0, c6=1, c7=0, c8=1,
            d1=0, d2=0, d3=0, d4=0, d5=0, d6=0, d7=0, d8=0, d9=100, da=0, db=0,
            e1=100, e2=0, e3=800, e4=1, e5=1, e6=1,
            f1=0, f2=1, f3=0, f4=0, f5=1
        )
        self.assertAlmostEqual(test_1.cfp, 0, places=1)

    def test_vegan(self):
        test_2 = Calculation.objects.create(
            name="test_2_vegan",
            email="test@test.test",
            offset=0,
            a1=0, a2=0, a3=0, a4=0, a5=0,
            b1=0, b2=0, b3=0,
            c1=0, c2=1, c3=0, c4=1, c5=0, c6=1, c7=0, c8=1,
            d1=0, d2=0, d3=0, d4=0, d5=0, d6=0, d7=0, d8=2100, d9=100, da=0, db=0,
            e1=100, e2=0, e3=800, e4=1, e5=1, e6=1,
            f1=0, f2=1, f3=0, f4=0, f5=1
        )
        self.assertLessEqual(test_2.cfp, 1)

    def test_meat_eater(self):
        test_3 = Calculation.objects.create(
            name="test_3_meat_eater",
            email="test@test.test",
            offset=0,
            a1=1000, a2=100, a3=1200, a4=1200, a5=3650,
            b1=60, b2=24, b3=3,
            c1=12, c2=1, c3=3, c4=2, c5=1, c6=1, c7=1, c8=2,
            d1=400, d2=400, d3=400, d4=400, d5=200, d6=700, d7=14, d8=2100, d9=50, da=25, db=25,
            e1=0, e2=80, e3=800, e4=2, e5=8, e6=3,
            f1=100, f2=5, f3=20, f4=1000, f5=2
        )
        self.assertGreater(test_3.cfp, 1)
        self.assertLessEqual(test_3.cfp, 7)

    def test_frequent_flier(self):
        test_4 = Calculation.objects.create(
            name="test_4_frequent_flier",
            email="test@test.test",
            offset=0,
            a1=40000, a2=100, a3=1200, a4=1200, a5=3650,
            b1=60, b2=24, b3=3,
            c1=12, c2=1, c3=3, c4=2, c5=1, c6=1, c7=1, c8=2,
            d1=400, d2=400, d3=400, d4=400, d5=200, d6=700, d7=14, d8=2100, d9=50, da=25, db=25,
            e1=0, e2=80, e3=800, e4=2, e5=8, e6=3,
            f1=1000, f2=5, f3=20, f4=100, f5=2
        )
        self.assertGreater(test_4.cfp, 7)
        self.assertLessEqual(test_4.cfp, 20)
