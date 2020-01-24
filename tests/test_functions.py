import pytest
import numpy as np

from solarsystem.functions import normalize

normal       = np.array([46, 80, 350, 187, 271])
unnorm = np.array([406, 800, -10, 547, 631])
unnorm2 = np.array([406, 700, -10, 547, 632])
NORMALIZE_CASES = (
        (normal, normal, 1.00),
        (normal, unnorm, 1.00)
        )


@pytest.mark.parametrize('case', NORMALIZE_CASES)
def test_normalize(case):
    normal, unnorm, res = case
    use_normalize = np.apply_along_axis(normalize,0,unnorm)
    
    assert np.allclose(normal, use_normalize)
    
    
if __name__ == '__main__':
    pytest.main([__file__])    