import pytest
import numpy as np

import solarsystem


#######################################################################
GT       = {
     'Mercury': (263.83033031837124, -4.057599521202387, 0.4659797616165433),
     'Venus': (5.228267566604346, -3.2222136733454767, 0.7262291936644325),
     'Earth': (79.47107541416335, 0.0, 0.9833180862528659),
     'Mars': (214.38221616457562, 0.4891253753974966, 1.5891803735433014),
     'Jupyter': (276.10498313633025, 0.10374961050190847, 5.228112674603031),
     'Saturn': (292.512767008796, 0.05134540100060894, 10.05212207219113),
     'Uranus': (35.35030250536327, 359.5159538071305, 19.809355998647174),
     'Neptune': (348.0172656026235, -1.039905299592724, 29.914939199387618),
     'Pluto': (292.7499413549187, 359.3290225249272, 33.87680754878506),
     'Ceres': (290.86531789432115, -5.404211011344595, 2.9204640444111933),
     'Chiron': (4.327136751763591, 2.943432379699923, 18.810534112295773),
     'Eris': (23.548094614031402, -11.74427433497789, 95.99830322945104)
     }

year   = 2020
month  = 1
day    = 1
hour   = 12
minute = 0
UT     = 0
dst = 0


view='horizontal'
H = solarsystem.Heliocentric(year=year, month=month, day=day, hour=hour, minute=minute, 
                         UT=UT, dst=dst, view=view )
planets=H.planets()

TEST_CASES = [
        (GT, planets, 1.00)
        ]

@pytest.mark.parametrize('case', TEST_CASES)
def test_sun(case):
    gt, planets, res = case

    assert gt==planets
    

   
#######################################################################
GT       = {
 'Sun': (313.54001918188993, 0.0, 0.9855042635175355),
 'Mercury': (329.13639549978916, -0.9055401650824109, 1.149140028843593),
 'Venus': (354.21675167976207, -0.7714897903911068, 1.0768905648872003),
 'Mars': (260.72848328563896, -0.015470334562496468, 1.9328376932087392),
 'Jupyter': (284.10537293037635, 0.03719146078027563, 6.052080896659592),
 'Saturn': (295.25829451079835, 0.008086815219857312, 10.979745586425643),
 'Uranus': (32.90430217695869, -0.4764705301925598, 19.96330699955339),
 'Neptune': (347.16872981177715, -1.0170602744356352, 30.729666206325366),
 'Pluto': (293.4840259504863, -0.7016152779476431, 34.82210554947094),
 'Ceres': (301.14975032080696, -4.792088583166722, 3.8875646031188316),
 'Chiron': (2.3716952337165336, 2.81482872049956, 19.44855116149367),
 'Eris': (23.00482341256768, -11.68562271124933, 96.32545965457294)
 }   
year   = 2020
month  = 2
day    = 2
hour   = 22
minute = 22
UT     = 0
dst = 0

Geq = solarsystem.Geocentric(year=year, month=month, day=day, hour=hour, 
                             minute=minute, UT=UT, dst=dst, plane='ecliptic')
Geqp=Geq.position()


TEST_CASES = [
        (GT, Geqp, 1.00)
        ]

@pytest.mark.parametrize('case', TEST_CASES)
def test_geo(case):
    gt, planets, res = case

    assert gt==planets
    
    
#######################################################################
GT       = [(336.161920584785, -4.437234727099948, 63.108778217035876),
            0.06377092588914574, (7.3145566040862855, 17.881704537217004)]
year   = 2020
month  = 1
day    = 27
hour   = 12
minute = 0
UT     = 0
dst = 0

longtitude = 23.72
latitude   = 37.98

moon = solarsystem.Moon(year=year, month=month, day=day, hour=hour, 
                        minute=minute, UT=UT, dst=dst, longtitude=longtitude,
                        latitude=latitude, topographic=False)
moon_position = moon.position()
moon_phase = moon.phase()
moon_moonriseset = moon.moonriseset()

#TEST_CASES = [
#        (GT[0], moon_position, 1.00),
#        (GT[1], moon_phase, 1.00),
#        (GT[2], moon_moonriseset, 1.00)
#        ]
GT1       = (336.161920584785, -4.437234727099948, 63.108778217035876)
GT2       = 0.06377092588914574
GT3       = (7.3145566040862855, 17.881704537217004)

TEST_CASES = [
        (GT1, moon_position, 1.00),
        (GT2, moon_phase, 1.00),
        (GT3, moon_moonriseset, 1.00)
        ]

@pytest.mark.parametrize('case', TEST_CASES)
def test_moon(case):
    gt, planets, res = case

    assert np.allclose(gt, planets)  