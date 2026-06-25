import pytest
import numpy as np
from datetime import datetime
import solarsystem


#######################################################################
GT       = {
     'Mercury': (263.83033031837124, -4.057599521202387, 0.4659797616165433),
     'Venus': (5.228267566604346, -3.2222136733454767, 0.7262291936644325),
     'Earth': (100.5289245858366, 0.0, 0.9833180862528658),
     'Mars': (214.38221616457562, 0.4891253753974966, 1.5891803735433014),
     'Jupiter': (276.10498313633025, 0.10374961050190847, 5.228112674603031),
     'Saturn': (292.512767008796, 0.05134540100060894, 10.05212207219113),
     'Uranus': (35.35030250536327, -0.48404619286953715, 19.809355998647174),
     'Neptune': (348.0172656026235, -1.039905299592724, 29.914939199387618),
     'Pluto': (292.7499413549187, -0.6709774750727665, 33.87680754878506),
     'Ceres': (290.86531789432115, -5.404211011344595, 2.9204640444111933),
     'Chiron': (4.327136751763591, 2.943432379699923, 18.810534112295773),
     'Eris': (23.548094614031402, -11.74427433497789, 95.99830322945104)
     }
GT2       = {
 'Mercury': (-0.049954746687863795, -0.4621195543652435, -0.03297239743832171),
 'Venus': (0.7220644052172724, 0.06607221451735312, -0.04082032480874338),
 'Earth': (-0.17968356066528413, 0.9667617476807011, 0),
 'Mars': (-1.3114849994179518, -0.8973947336694352, 0.013566426916695826),
 'Jupiter': (0.5560117501416899, -5.198453948006299, 0.009466916443751654),
 'Saturn': (3.8488483131935203, -9.286088717491223, 0.009008170828773239),
 'Uranus': (16.156527438922527, 11.460767849633234, -0.16735140661318196),
 'Neptune': (29.25827921158193, -6.209824739715596, -0.5429194988087228),
 'Pluto': (13.09960254295737, -31.239096028464672, -0.3967143031550649),
 'Ceres': (1.0355652247801526, -2.716810703397821, -0.2750536344563635),
 'Chiron': (18.732169225956646, 1.4174013926682936, 0.9659207897275007),
 'Eris': (86.16175536857236, 37.550227779065736, -19.539870226800428)
 }
GT3       = {
 'Mercury': (22.12039266339318, -3.132591766656097, 0.3323343096130607),
 'Venus': (57.06840450167902, -1.150720440796739, 0.7220179596826576),
 'Earth': (133.54001918188996, 0.0, 0.9855042635175355),
 'Mars': (230.30948635742487, -0.019283814606376803, 1.5506084548362438),
 'Jupiter': (278.77809888574956, 0.04315029133833213, 5.2163201637078),
 'Saturn': (293.4953519041396, 0.008836050038306491, 10.048740488192404),
 'Uranus': (35.70758126278654, -0.4802762003449428, 19.805123014589874),
 'Neptune': (348.2143161325276, -1.0447883955838808, 29.9142042499695),
 'Pluto': (292.91272745154566, -0.7207406987369872, 33.89812043286358),
 'Ceres': (296.9956063882021, -6.348419264773433, 2.9371044625138607),
 'Chiron': (4.634314557503773, 2.909651356888129, 18.815260866820807),
 'Eris': (23.567429379498012, -11.726867709299205, 95.9913888974132)
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
                         UT=UT, dst=dst, view=view, precession=False )
planets=H.planets()

view='rectangular'
H = solarsystem.Heliocentric(year=year, month=month, day=day, hour=hour, minute=minute, 
                         UT=UT, dst=dst, view=view, precession=False )
planets2=H.planets()


year   = 2020
month  = 2
day    = 2
hour   = 22
minute = 22
UT     = 0
dst = 0
view='horizontal'
H = solarsystem.Heliocentric(year=year, month=month, day=day, hour=hour, minute=minute, 
                         UT=UT, dst=dst, view=view, precession=False )
planets3=H.planets()


GT4 = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus',
       'Neptune', 'Pluto', 'Ceres', 'Chiron', 'Eris']
planetnames = H.planetnames()

TEST_CASES = [
        (GT, planets, 1.00),
        (GT2, planets2, 1.00),
        (GT3, planets3, 1.00),
        (GT4, planetnames, 1.00)
        ]

@pytest.mark.parametrize('case', TEST_CASES)
def test_sun(case):
    gt, planets, res = case

    assert gt==planets
    

   
########################################################################
GT       = {
 'Sun': (313.54001918188993, 0.0, 0.9855042635175355),
 'Mercury': (329.13639549978916, -0.9055401650824109, 1.149140028843593),
 'Venus': (354.21675167976207, -0.7714897903911068, 1.0768905648872003),
 'Mars': (260.72848328563896, -0.015470334562496468, 1.9328376932087392),
 'Jupiter': (284.10537293037635, 0.03719146078027563, 6.052080896659592),
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
                             minute=minute, UT=UT, dst=dst, plane='ecliptic', precession=False)
Geqp=Geq.position()

GT2        = {
 'Sun': (292.83347822938697, -21.77935583163034, 0.983452824414035),
 'Mercury': (277.3605919017942, -19.947148929399585, 0.7173580272492874),
 'Venus': (292.8672951986823, -22.595037149099902, 1.7111215807917122),
 'Mars': (140.25113399199614, 19.855893626311836, 0.6932268585329089),
 'Jupiter': (331.0291634937027, -12.848058212698385, 5.746902856264739),
 'Saturn': (185.18200480151202, 0.30605183120176804, 9.161284469474062),
 'Uranus': (354.2364709298132, -3.2994616636943292, 20.524444428857382),
 'Neptune': (327.3421977631819, -13.611388178718649, 30.818037712573652),
 'Pluto': (273.8525959675548, -18.29513894503039, 32.660999322592076),
 'Ceres': (247.5305196731464, -18.003612359941492, 3.3553694975311865),
 'Chiron': (323.98721277147393, -8.041398632289553, 16.960814330290393),
 'Eris': (24.304746541378183, -4.57825597789273, 96.68387041763495)
 }

year   = 2010
month  = 1
day    = 11
hour   = 11
minute = 11
UT     = 0
dst = 0
Geq = solarsystem.Geocentric(year=year, month=month, day=day, hour=hour, minute=minute, 
                         UT=UT, dst=dst, plane='equatorial', precession=False)
Geqp2=Geq.position()


GT3 = ['Sun', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus',
       'Neptune', 'Pluto', 'Ceres', 'Chiron', 'Eris']
objectnames = Geq.objectnames()

TEST_CASES = [
        (GT, Geqp, 1.00),
        (GT2, Geqp2, 1.00),
        (GT3, objectnames, 1.00)
        ]

@pytest.mark.parametrize('case', TEST_CASES)
def test_geo(case):
    gt, planets, res = case

    assert gt==planets
    

########################################################################
GT       = {
 'Mercury': (85.48447781077277, 4.249622141286909, 0.3080313908134294),
 'Venus': (138.89768144324836, 3.007889909743782, 0.7184797601869075),
 'Earth': (238.3717084498826, 0.0, 1.011738915568791),
 'Mars': (10.297625980333176, -1.1665624736283975, 1.4019357059812947),
 'Jupiter': (120.32822710175401, 0.44510467760678746, 5.260530714488254),
 'Saturn': (6.2192714330329775, -2.372647758963991, 9.498446014763244),
 'Uranus': (61.140525582484614, -0.16914258530381987, 19.447448007580306),
 'Neptune': (1.831471384728164, -1.3567408673135444, 29.866824811084072),
 'Pluto': (303.59524650999856, -4.056301843157102, 35.47028900432166),
 'Ceres': (54.70685575300535, -4.550747671511338, 2.779835747898551),
 'Chiron': (26.081292519359124, 0.3304639643684204, 18.30084284575825),
 'Eris': (24.38443397283854, -10.483655525835333, 95.46473499699579)
 }
 
GT2        = {
 'Sun': (220.55786637995158, -15.745652318204225, 0.9913949566141237),
 'Mercury': (204.41005165893708, -8.04713036354636, 0.8588572318658695),
 'Venus': (220.5471102647177, -14.892358650380178, 1.7144959936172632),
 'Mars': (213.69045510124275, -13.143773035605108, 2.5736991107579468),
 'Jupiter': (340.47695748050035, -9.697775641426752, 4.467967187830642),
 'Saturn': (110.75242297224868, 21.603896657180485, 8.586420447787356),
 'Uranus': (207.52483035820683, -10.771358124715318, 19.41514396087036),
 'Neptune': (247.24184958286696, -20.251262452694917, 31.1818548238278),
 'Pluto': (194.18783067766907, 11.651024320874818, 31.626203796695137),
 'Ceres': (339.00673300516155, -22.460842756233717, 2.501308590028498),
 'Chiron': (19.81055386576869, 9.27314267675375, 17.58190129776312),
 'Eris': (20.339990391083674, -13.451748531929889, 96.84628278511121)}
 
year   = 2026
month  = 5
day    = 19
hour   = 18
minute = 0
UT     = 0
dst = 1

view='horizontal'
H = solarsystem.Heliocentric(year=year, month=month, day=day, hour=hour, minute=minute, 
                         UT=UT, dst=dst, view=view, precession=True )
planets=H.planets()



year   = 1974
month  = 11
day    = 5
hour   = 11
minute = 11
UT     = 0
dst = 0
Geq = solarsystem.Geocentric(year=year, month=month, day=day, hour=hour, minute=minute, 
                         UT=UT, dst=dst, plane='equatorial', precession=True)
Geqp2=Geq.position()


TEST_CASES = [
        (GT,  planets, 1.00),
        (GT2, Geqp2, 1.00)
        ]

@pytest.mark.parametrize('case', TEST_CASES)
def test_precession(case):
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
moon_moonriseset = tuple([x.timestamp() for x in moon_moonriseset])

#TEST_CASES = [
#        (GT[0], moon_position, 1.00),
#        (GT[1], moon_phase, 1.00),
#        (GT[2], moon_moonriseset, 1.00)
#        ]
GT1       = (336.161920584785, -4.437234727099948, 63.108778217035876)
GT2       = 0.06377092588914574
GT3       = (1580102134.0, 1580141375.0)

TEST_CASES = [
        (GT1, moon_position, 1.00),
        (GT2, moon_phase, 1.00),
        (GT3, moon_moonriseset, 1.00)
        ]

@pytest.mark.parametrize('case', TEST_CASES)
def test_moon(case):
    gt, planets, res = case

    assert np.allclose(gt, planets)  
    
    
#######################################################################
GT       = (1577850065.0, 1577884548.0)
year   = 2020
month  = 1
day    = 1
hour   = 12
minute = 0
UT     = 0
dst = 0

longtitude = 23.72
latitude   = 37.98

s = solarsystem.Sunriseset(year=year, month=month, day=day, 
                         UT=UT, dst=dst, longtitude=longtitude, latitude=latitude)

compute = s.riseset()
compute = tuple([x.timestamp() for x in compute])

TEST_CASES = [
        (GT, compute, 1.00)
        ]

@pytest.mark.parametrize('case', TEST_CASES)
def test_sunriseset(case):
    gt, times, res = case

    assert np.allclose(gt, times)  
    
if __name__ == '__main__':
    pytest.main([__file__])        
