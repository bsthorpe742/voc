from .. utils import TranspileTestCase, BuiltinFunctionTestCase


class DictTests(TranspileTestCase):
    pass


class BuiltinDictFunctionTests(BuiltinFunctionTestCase, TranspileTestCase):
    functions = ["dict"]

    not_implemented = [
        'test_bytearray',
        'test_bytes',
        'test_class',
        'test_list',
        'test_str',
    ]
