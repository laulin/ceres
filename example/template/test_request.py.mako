import unittest
from ${name}_request import ${variables["action"]}_${name}

<%def name="test(test_name, test_vector)">
    def test_${test_name}(self):
        result = ${variables["action"]}_${name}(\
%for k, v in tests[test_name].items():
${k}=${v}${')' if loop.last else ', '}\
%endfor

        expected = ${variables[test_name]}
        self.assertEquals(result, expected)
</%def>

class Test${name}(unittest.TestCase):
% for test_name, test_vector in tests.items():
${test(test_name, test_vector)}
%endfor


if __name__ == "__main__":
    unittest.main()