from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class BytesTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = b'hello, world'
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)

    def test_capitalize(self):
        self.assertCodeExecution(r"""
            print(b'hello, world'.capitalize())
            print(b'helloWORLD'.capitalize())
            print(b'HELLO WORLD'.capitalize())
            print(b'2015638687'.capitalize())
            print(b'\xc8'.capitalize())
        """)

    def test_repr(self):
        self.assertCodeExecution(r"""
            print(repr(b'\xc8'))
            print(repr(b'abcdef \xc8 abcdef'))
            print(repr(b'abcdef \xc8 abcdef\n\r\t'))
            print(b'abcdef \xc8 abcdef\n\r\t')
        """)

    def test_iter(self):
        self.assertCodeExecution("""
            print([b for b in b''])
            print([b for b in b'hello world'])
        """)

    def test_getitem(self):

        self.assertCodeExecution("""
            x = b'0123456789'
            print("x[0] = ", x[0])
            print("x[-10] = ", x[-10])
            print("x[9] = ", x[9])
            #Start/Stop Empty w/Step +/-
            print("x[:] = ", x[:])
            print("x[::1] = ", x[::1])
            print("x[::2] = ", x[::2])
            print("x[::3] = ", x[::3])
            print("x[::-1] = ", x[::-1])
            print("x[::-2] = ", x[::-2])
            print("x[::-3] = ", x[::-3])
            #Empty Start Tests With Stop Bounds checks
            print("x[:9:1] = ", x[:9:1])
            print("x[:10:1] = ", x[:10:1])
            print("x[:11:1] = ", x[:11:1])
            print("x[:-9:1] = ", x[:-9:1])
            print("x[:-10:1] = ", x[:-10:1])
            print("x[:-11:1] = ", x[:-11:1])
            print("x[:9:2] = ", x[:9:2])
            print("x[:10:2] = ", x[:10:2])
            print("x[:11:2] = ", x[:11:2])
            print("x[:-9:2] = ", x[:-9:2])
            print("x[:-10:2] = ", x[:-10:2])
            print("x[:-11:2] = ", x[:-11:2])
            print("x[:9:3] = ", x[:9:3])
            print("x[:10:3] = ", x[:10:3])
            print("x[:11:3] = ", x[:11:3])
            print("x[:-9:3] = ", x[:-9:3])
            print("x[:-10:3] = ", x[:-10:3])
            print("x[:-11:3] = ", x[:-11:3])
            print("x[:9:-1] = ", x[:9:-1])
            print("x[:10:-1] = ", x[:10:-1])
            print("x[:11:-1] = ", x[:11:-1])
            print("x[:-9:-1] = ", x[:-9:-1])
            print("x[:-10:-1] = ", x[:-10:-1])
            print("x[:-11:-1] = ", x[:-11:-1])
            print("x[:9:-2] = ", x[:9:-2])
            print("x[:10:-2] = ", x[:10:-2])
            print("x[:11:-2] = ", x[:11:-2])
            print("x[:-9:-2] = ", x[:-9:-2])
            print("x[:-10:-2] = ", x[:-10:-2])
            print("x[:-11:-2] = ", x[:-11:-2])
            print("x[:9:-3] = ", x[:9:-3])
            print("x[:10:-3] = ", x[:10:-3])
            print("x[:11:-3] = ", x[:11:-3])
            print("x[:-9:-3] = ", x[:-9:-3])
            print("x[:-10:-3] = ", x[:-10:-3])
            print("x[:-11:-3] = ", x[:-11:-3])
            #Empty stop tests with stop bounds checks
            print("x[9::1] = ", x[9::1])
            print("x[10::1] = ", x[10::1])
            print("x[11::1] = ", x[11::1])
            print("x[-9::1] = ", x[-9::1])
            print("x[-10::1] = ", x[-10::1])
            print("x[-11::1] = ", x[-11::1])
            print("x[9::2] = ", x[9::2])
            print("x[10::2] = ", x[10::2])
            print("x[11::2] = ", x[11::2])
            print("x[-9::2] = ", x[-9::2])
            print("x[-10::2] = ", x[-10::2])
            print("x[-11::2] = ", x[-11::2])
            print("x[9::3] = ", x[9::3])
            print("x[10::3] = ", x[10::3])
            print("x[11::3] = ", x[11::3])
            print("x[-9::3] = ", x[-9::3])
            print("x[-10::3] = ", x[-10::3])
            print("x[-11::3] = ", x[-11::3])
            print("x[9::-1] = ", x[9::-1])
            print("x[10::-1] = ", x[10::-1])
            print("x[11::-1] = ", x[11::-1])
            print("x[-9::-1] = ", x[-9::-1])
            print("x[-10::-1] = ", x[-10::-1])
            print("x[-11::-1] = ", x[-11::-1])
            print("x[9::-2] = ", x[9::-2])
            print("x[10::-2] = ", x[10::-2])
            print("x[11::-2] = ", x[11::-2])
            print("x[-9::-2] = ", x[-9::-2])
            print("x[-10::-2] = ", x[-10::-2])
            print("x[-11::-2] = ", x[-11::-2])
            print("x[9::-3] = ", x[9::-3])
            print("x[10::-3] = ", x[10::-3])
            print("x[11::-3] = ", x[11::-3])
            print("x[-9::-3] = ", x[-9::-3])
            print("x[-10::-3] = ", x[-10::-3])
            print("x[-11::-3] = ", x[-11::-3])
            #other tests
            print("x[-5:] = ", x[-5:])
            print("x[:-5] = ", x[:-5])
            print("x[-2:-8] = ", x[-2:-8])
            print("x[100::-1] = ", x[100::-1])
            print("x[100:-100:-1] = ", x[100:-100:-1])
            print("x[:-100:-1] = ", x[:-100:-1])
            print("x[::-1] = ", x[::-1])
            print("x[::-2] = ", x[::-2])
            print("x[::-3] = ", x[::-3])
            print("x[:0:-1] = ", x[:0:-1])
            print("x[-5::-2] = ", x[-5::-2])
            print("x[:-5:-2] = ", x[:-5:-2])
            print("x[-2:-8:-2] = ", x[-2:-8:-2])
            print("x[0:9] = ", x[0:9])
            print("x[0:10:1] = ", x[0:10:1] )
            print("x[10:0] = ", x[10:0])
            print("x[10:0:-1] = ", x[10:0:-1])
            print("x[10:-10:-1] = ", x[10:-10:-1])
            print("x[10:-11:-1] = ", x[10:-11:-1])
            """)

    def test_count(self):
        self.assertCodeExecution("""
            print(b'abcabca'.count(97))
            print(b'abcabca'.count(b'abc'))
            print(b'qqq'.count(b'q'))
            print(b'qqq'.count(b'qq'))
            print(b'qqq'.count(b'qqq'))
            print(b'qqq'.count(b'qqqq'))
            print(b'abcdefgh'.count(b'bc',-7, -5))
            print(b'abcdefgh'.count(b'bc',1, -5))
            print(b'abcdefgh'.count(b'bc',0, 3))
            print(b'abcdefgh'.count(b'bc',-7, 500))
            print(b'qqaqqbqqqcqqqdqqqqeqqqqf'.count(b'qq'),1)
            print(b''.count(b'q'),0)
        """)
        self.assertCodeExecution("""
            b'abcabc'.count([]) #Test TypeError invalid byte array
        """, exits_early=True)
        self.assertCodeExecution("""
            b'abcabc'.count(256) #Test ValueError invalid integer range
        """, exits_early=True)
        self.assertCodeExecution("""
            print(b'abcabca'.count(97, [], 3)) #Test Slicing Error on Start
        """, exits_early=True)
        self.assertCodeExecution("""
            print(b'abcabca'.count(97, 3, [])) #Test Slicing Error on End
        """, exits_early=True)

    def test_find(self):
        self.assertCodeExecution("""
            print(b''.find(b'a'))
            print(b'abcd'.find(b''))
            print(b'abcd'.find(b'...'))
            print(b'abcd'.find(b'a'))
            print(b'abcd'.find(b'b'))
            print(b'abcd'.find(b'c'))
            print(b'abcd'.find(b'd'))
            print(b'abcd'.find(b'ab'))
            print(b'abcd'.find(b'bc'))
            print(b'abcd'.find(b'cd'))
            print(b'abcd'.find(b'cd', 2))
            print(b'abcd'.find(b'ab', 3))
            print(b'abcd'.find(b'cd', 2, 3))
            print(b'abcd'.find(b'ab', 3, 4))
        """)

    def test_index(self):
        self.assertCodeExecution("""
            print(b'abcd'.index(b'ab'))
            print(b'abcd'.index(b'bc'))
            print(b'abcd'.index(b'cd'))
            print(b'abcd'.find(b'cd', 2))
            print(b'abcd'.find(b'cd', 2, 3))
        """)
        self.assertCodeExecution("""
            print(b''.index(b'a'))
            print(b'abcd'.index(b''))
            print(b'abcd'.index(b'...'))
            print(b'abcd'.find(b'ab', 3))
            print(b'abcd'.find(b'ab', 3, 4))
        """, exits_early=True)


class UnaryBytesOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
    ]


class BinaryBytesOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_direct_eq_bool',
        'test_direct_eq_bytearray',
        'test_direct_eq_bytes',
        'test_direct_eq_class',
        'test_direct_eq_complex',
        'test_direct_eq_dict',
        'test_direct_eq_float',
        'test_direct_eq_frozenset',
        'test_direct_eq_int',
        'test_direct_eq_list',
        'test_direct_eq_none',
        'test_direct_eq_set',
        'test_direct_eq_str',
        'test_direct_eq_tuple',

        'test_direct_ge_bool',
        'test_direct_ge_bytearray',
        'test_direct_ge_bytes',
        'test_direct_ge_class',
        'test_direct_ge_complex',
        'test_direct_ge_dict',
        'test_direct_ge_float',
        'test_direct_ge_frozenset',
        'test_direct_ge_int',
        'test_direct_ge_list',
        'test_direct_ge_none',
        'test_direct_ge_set',
        'test_direct_ge_str',
        'test_direct_ge_tuple',

        'test_direct_gt_bool',
        'test_direct_gt_bytearray',
        'test_direct_gt_bytes',
        'test_direct_gt_class',
        'test_direct_gt_complex',
        'test_direct_gt_dict',
        'test_direct_gt_float',
        'test_direct_gt_frozenset',
        'test_direct_gt_int',
        'test_direct_gt_list',
        'test_direct_gt_none',
        'test_direct_gt_set',
        'test_direct_gt_str',
        'test_direct_gt_tuple',

        'test_direct_le_bool',
        'test_direct_le_bytearray',
        'test_direct_le_bytes',
        'test_direct_le_class',
        'test_direct_le_complex',
        'test_direct_le_dict',
        'test_direct_le_float',
        'test_direct_le_frozenset',
        'test_direct_le_int',
        'test_direct_le_list',
        'test_direct_le_none',
        'test_direct_le_set',
        'test_direct_le_str',
        'test_direct_le_tuple',

        'test_direct_lt_bool',
        'test_direct_lt_bytearray',
        'test_direct_lt_bytes',
        'test_direct_lt_class',
        'test_direct_lt_complex',
        'test_direct_lt_dict',
        'test_direct_lt_float',
        'test_direct_lt_frozenset',
        'test_direct_lt_int',
        'test_direct_lt_list',
        'test_direct_lt_none',
        'test_direct_lt_set',
        'test_direct_lt_str',
        'test_direct_lt_tuple',

        'test_direct_ne_bool',
        'test_direct_ne_bytearray',
        'test_direct_ne_bytes',
        'test_direct_ne_class',
        'test_direct_ne_complex',
        'test_direct_ne_dict',
        'test_direct_ne_float',
        'test_direct_ne_frozenset',
        'test_direct_ne_int',
        'test_direct_ne_list',
        'test_direct_ne_none',
        'test_direct_ne_set',
        'test_direct_ne_str',
        'test_direct_ne_tuple',

        'test_direct_eq_frozenset',
        'test_direct_ge_frozenset',
        'test_direct_gt_frozenset',
        'test_direct_le_frozenset',
        'test_direct_lt_frozenset',
        'test_direct_ne_frozenset',

        'test_eq_bytearray',
        'test_eq_bytes',
        'test_eq_frozenset',

        'test_ne_frozenset',

        'test_ge_frozenset',

        'test_gt_frozenset',

        'test_le_frozenset',

        'test_lt_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_bool',
        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_slice',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_class',
        'test_multiply_frozenset',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subscr_class',
        'test_subscr_frozenset',

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]


class InplaceBytesOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytes'

    not_implemented = [
        'test_add_class',
        'test_add_frozenset',

        'test_and_class',
        'test_and_frozenset',

        'test_floor_divide_class',
        'test_floor_divide_complex',
        'test_floor_divide_frozenset',

        'test_lshift_class',
        'test_lshift_frozenset',

        'test_modulo_None',
        'test_modulo_NotImplemented',
        'test_modulo_bool',
        'test_modulo_bytearray',
        'test_modulo_bytes',
        'test_modulo_class',
        'test_modulo_complex',
        'test_modulo_dict',
        'test_modulo_float',
        'test_modulo_frozenset',
        'test_modulo_int',
        'test_modulo_list',
        'test_modulo_range',
        'test_modulo_set',
        'test_modulo_slice',
        'test_modulo_str',
        'test_modulo_tuple',

        'test_multiply_class',
        'test_multiply_frozenset',

        'test_or_class',
        'test_or_frozenset',

        'test_power_class',
        'test_power_frozenset',

        'test_rshift_class',
        'test_rshift_frozenset',

        'test_subtract_class',
        'test_subtract_frozenset',

        'test_true_divide_class',
        'test_true_divide_frozenset',

        'test_xor_class',
        'test_xor_frozenset',
    ]
