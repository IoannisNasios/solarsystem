import pytest
import numpy as np

from solarsystem.functions import normalize
from solarsystem.functions import demical2clock, demical2hms, demical2arcs
from solarsystem.functions import spherical2rectangular, rectangular2spherical



#######################################################################
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
    
    
#######################################################################
GT = np.array([    [  0.35369445,  -0.14446606,  -0.04433056],
                   [  0.53722196,   0.48367157,  -0.02451152],
                   [  0.5503132 ,   0.81614222,   0.        ],
                   [ -1.09281674,  -1.11642282,   0.0036069 ],
                   [  0.72664596,  -5.1689156 ,   0.00553491],
                   [  3.96071058,  -9.23633983,   0.00371127],
                   [ 16.10318172,  11.53045737,  -0.16640123],
                   [ 29.27281629,  -6.13822889,  -0.54472103],
                   [ 13.16840355, -31.22630711,  -0.41779994],
                   [  1.2426797 ,  -2.63795734,  -0.31074705],
                   [ 18.73041376,   1.48902159,   0.95822955],
                   [ 86.15221006,  37.57063938, -19.51859302]])
    
PRETRANS = np.array([  [337.78250105,  -6.61844677,   0.38462372],
                       [ 41.9973343 ,  -1.94206805,   0.72328862],
                       [ 56.00876684,   0.        ,   0.98434381],
                       [225.61219113,   0.13228268,   1.56226161],
                       [278.00219836,   0.0607553 ,   5.21974458],
                       [293.21053423,   0.02115878,  10.04973708],
                       [ 35.60402603, 359.51862918,  19.80635247],
                       [348.15721084,  -1.04337454,  29.91441707],
                       [292.86557318, 359.2936734 ,  33.891941  ],
                       [295.2240226 ,  -6.08283114,   2.93251352],
                       [  4.54531366,   2.91944783,  18.8139254 ],
                       [ 23.56182623, -11.73191245,  95.99339412] ])   

#TEST_CASES=[]
#for i in range(len(GT)):
#    TEST_CASES.append((GT[i,:], PRETRANS[i,:], 1.0))
TEST_CASES = [
        (GT, PRETRANS, 1)
        ]   
@pytest.mark.parametrize('case', TEST_CASES)
def test_s2r(case):
    normal, unnorm, res = case
    after = []
    for i in range(len(unnorm)):
        after.append(spherical2rectangular(unnorm[i,0],unnorm[i,1],unnorm[i,2]))
    after = np.array(after)    
    assert np.allclose(normal, after)
    
    
#######################################################################
GT = np.array([  [337.78250105,  -6.61844677,   0.38462372],
                       [ 41.9973343 ,  -1.94206805,   0.72328862],
                       [ 56.00876684,   0.        ,   0.98434381],
                       [225.61219113,   0.13228268,   1.56226161],
                       [278.00219836,   0.0607553 ,   5.21974458],
                       [293.21053423,   0.02115878,  10.04973708],
                       #[ 35.60402603, 359.51862918,  19.80635247],
                       [348.15721084,  -1.04337454,  29.91441707],
                       #[292.86557318, 359.2936734 ,  33.891941  ],
                       [295.2240226 ,  -6.08283114,   2.93251352],
                       [  4.54531366,   2.91944783,  18.8139254 ],
                       [ 23.56182623, -11.73191245,  95.99339412] ])  
    
PRETRANS =   np.array([    [  0.35369445,  -0.14446606,  -0.04433056],
                   [  0.53722196,   0.48367157,  -0.02451152],
                   [  0.5503132 ,   0.81614222,   0.        ],
                   [ -1.09281674,  -1.11642282,   0.0036069 ],
                   [  0.72664596,  -5.1689156 ,   0.00553491],
                   [  3.96071058,  -9.23633983,   0.00371127],
                   #[ 16.10318172,  11.53045737,  -0.16640123],
                   [ 29.27281629,  -6.13822889,  -0.54472103],
                   #[ 13.16840355, -31.22630711,  -0.41779994],
                   [  1.2426797 ,  -2.63795734,  -0.31074705],
                   [ 18.73041376,   1.48902159,   0.95822955],
                   [ 86.15221006,  37.57063938, -19.51859302]])

#TEST_CASES=[]
#for i in range(len(GT)):
#    TEST_CASES.append((GT[i,:], PRETRANS[i,:], 1.0))    
TEST_CASES = [
        (GT, PRETRANS, 1)
        ]   
@pytest.mark.parametrize('case', TEST_CASES)
def test_r2s(case):
    normal, unnorm, res = case
    after = []
    for i in range(len(unnorm)):
        ans=rectangular2spherical(unnorm[i,0],unnorm[i,1],unnorm[i,2])
        
        after.append(((ans[0]),(ans[1]),ans[2]))
    after = np.array(after)    
    assert np.allclose(normal, after)



#######################################################################
GT = np.array(['00:28:47', '08:58:12', '07:55:11', '23:06:00', '15:09:00'])
times = np.array([0.48, 8.97, 7.92, 23.1, 15.15])
TEST_CASES = [
        (GT, times, 1.00)
        ]

@pytest.mark.parametrize('case', TEST_CASES)
def test_d2c(case):
    gt, times, res = case
    use_demical2clock=[]
    for i in range(len(times)):
        use_demical2clock.append(demical2clock(times[i]))
    use_demical2clock = np.array(use_demical2clock)
    
    assert (gt==use_demical2clock).all()


#######################################################################
GT = np.array(['5h 18m 43s', '0h 21m 11s', '11h 19m 38s', '18h 18m 27s',
       '22h 36m 0s'])
degrees = np.array([79.68, 5.3, 169.91, 274.614, 339])
TEST_CASES = [
        (GT, degrees, 1.00)
        ]

@pytest.mark.parametrize('case', TEST_CASES)
def test_d2hms(case):
    gt, degrees, res = case
#    use_demical2hms = np.apply_along_axis(demical2hms,0,degrees)
    use_demical2hms=[]
    for i in range(len(degrees)):
        use_demical2hms.append(demical2hms(degrees[i]))
    use_demical2hms = np.array(use_demical2hms)
    
    assert (gt==use_demical2hms).all()



#######################################################################
GT = np.array(["1° 54.6'", "89° 38.82'", "316° 24.0'", "257° 37.8'", 
               "172° 0.0'"])
degrees = np.array([1.91, 89.647, 316.4, 257.63, 172.0])
TEST_CASES = [
        (GT, degrees, 1.00)
        ]

@pytest.mark.parametrize('case', TEST_CASES)
def test_d2arcs(case):
    gt, degrees, res = case
#    use_demical2arcs = np.apply_along_axis(demical2arcs,0,degrees)
    use_demical2arcs=[]
    for i in range(len(degrees)):
        use_demical2arcs.append(demical2arcs(degrees[i]))
    use_demical2arcs = np.array(use_demical2arcs)
    
    assert (gt==use_demical2arcs).all()





    
if __name__ == '__main__':
    pytest.main([__file__])    