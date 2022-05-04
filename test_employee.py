import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp1=Employee('pooja','mourya',1000)
        emp2=Employee('jess','smith',5000)

        self.assertEqual(emp1.email,'pooja.mourya@email.com')
        self.assertEqual(emp2.email,'jess.smith@email.com')

        emp1.first = 'John'
        emp2.first = 'Jane'

        self.assertEqual(emp1.email,'John.mourya@email.com')
        self.assertEqual(emp2.email,'Jane.smith@email.com')

    def test_fullname(self):
        emp1=Employee('pooja','mourya',1000)
        emp2=Employee('jess','smith',5000)

        self.assertEqual(emp1.fullname,'pooja mourya')
        self.assertEqual(emp2.fullname,'jess smith')

        emp1.first = 'John'
        emp2.first = 'Jane'

        self.assertEqual(emp1.fullname,'John mourya')
        self.assertEqual(emp2.fullname,'Jane smith')

    def test_apply_raise(self):
        emp1=Employee('pooja','mourya',50000)
        emp2=Employee('jess','smith',60000)

        emp1.apply_raise()
        emp2.apply_raise()
        self.assertEqual(emp1.pay,52500)
        self.assertEqual(emp2.pay,63000)



if __name__=='__main__':
    unittest.main()