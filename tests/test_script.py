import unittest

from script import main

class TestScript(unittest.TestCase):
    def test_main(self):
        # Verificar que el script se ejecute sin errores
        main()

if __name__ == "__main__":
    unittest.main()