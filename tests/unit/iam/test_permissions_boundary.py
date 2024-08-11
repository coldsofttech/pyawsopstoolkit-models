import unittest

from pyawsopstoolkit_models.iam.permissions_boundary import PermissionsBoundary


class TestPermissionsBoundary(unittest.TestCase):
    def setUp(self) -> None:
        self.maxDiff = None
        self.params = {
            'type': 'Policy',
            'arn': 'arn:aws:iam::123456789012:policy/ExamplePolicy'
        }
        self.permissions_boundary = PermissionsBoundary(self.params['type'], self.params['arn'])

    def test_initialization(self):
        self.assertEqual(self.permissions_boundary.type, self.params['type'])
        self.assertEqual(self.permissions_boundary.arn, self.params['arn'])

    def test_initialization_empty(self):
        with self.assertRaises(TypeError):
            PermissionsBoundary()

    def test_setters(self):
        new_params = {
            'type': 'ManagedPolicy',
            'arn': 'arn:aws:iam::987654321012:policy/SomeNewPolicy'
        }

        self.permissions_boundary.type = new_params['type']
        self.permissions_boundary.arn = new_params['arn']

        self.assertEqual(self.permissions_boundary.type, new_params['type'])
        self.assertEqual(self.permissions_boundary.arn, new_params['arn'])

    def test_invalid_types(self):
        from pyawsopstoolkit_validators.exceptions import ValidationError

        invalid_params = {
            'type': 123,
            'arn': 'invalid-arn'
        }

        with self.assertRaises(TypeError):
            PermissionsBoundary(invalid_params['type'], self.params['arn'])
        with self.assertRaises(ValidationError):
            PermissionsBoundary(self.params['type'], invalid_params['arn'])

        with self.assertRaises(TypeError):
            self.permissions_boundary.type = invalid_params['type']
        with self.assertRaises(ValidationError):
            self.permissions_boundary.arn = invalid_params['arn']

    def test_to_dict(self):
        expected_dict = {
            "type": self.params['type'],
            "arn": self.params['arn']
        }
        self.assertDictEqual(self.permissions_boundary.to_dict(), expected_dict)


if __name__ == "__main__":
    unittest.main()
