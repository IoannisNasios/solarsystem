
# **SOLARSYSTEM** 

[![PyPI version](https://badge.fury.io/py/solarsystem.svg)](https://badge.fury.io/py/solarsystem)
[![Documentation Status](https://readthedocs.org/projects/solarsystem/badge/?version=latest)](https://solarsystem.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.org/IoannisNasios/solarsystem.svg?branch=master)](https://travis-ci.org/IoannisNasios/solarsystem)
[![codecov](https://codecov.io/gh/IoannisNasios/solarsystem/branch/master/graph/badge.svg)](https://codecov.io/gh/IoannisNasios/solarsystem)
[![Downloads](https://pepy.tech/badge/solarsystem/month)](https://pepy.tech/project/solarsystem/month)


**Our Solar System consists of:**

* our Star, the Sun
* 8 Planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune
* Some dwarf Planets: Pluto, Ceres, Eris, (Haumea, Makemake, Quaoar, Sedna, Orcus, 2007 OR10, not yet included here)
* Some Centaurs: Chiron (onlyone included here)
* Many moons orbiting planets. Our Moon (Selene in Greek  or Luna in Latin) is orbiting Earth


**solarsystem** is a python library for finding position of **planets** around **Sun** or around **Earth**.


Also with solarsystem we can find positions around Sun/Earth of **dwarf planets** (only 3 planets so far) and **Chiron Centaur**
and position of **moon** around Earth


Furthermore we compute sunrise/sunset, moonrise/moonset and moon phase for given place (geocoordinates).


Except all computation above with this library a set of usefull functions are included with which we can **convert between coordinate systems**:

* Transform spherical to rectangular projection.
* Transform rectangular to spherical projection.
* Transform ecliptic to equatorial projection.
* Transform equatorial to ecliptic projection.
* Transform eclipitc to spherical projection.
* Transform spherical to eclipitc projection.


&nbsp;   &nbsp;   &nbsp;   


## **Quick start**

```python
import solarsystem
```

Initialize class


```python
H = solarsystem.Heliocentric(year=2020, month=1, day=1, hour=12, minute=0 )
```

Compute position of planets around sun


```python
planets_dict=H.planets()
print('Planet','   \t','Longitude','   \t','Latitude','   \t','Distance in AU')
for planet in planets_dict:
    pos=planets_dict[planet]
    print(planet,'   \t',round(pos[0],2),'   \t',round(pos[1],2),'   \t',round(pos[2],2))
```


```python
# Planet      Longitude    Latitude    Distance in AU
# Mercury     263.83       -4.06        0.47
# Venus       5.23         -3.22        0.73
# Earth       280.53        0.0         0.98
# Mars        214.38        0.49        1.59
# Jupiter     276.1         0.1         5.23
# Saturn      292.51        0.05        10.05
# Uranus      35.35         359.52      19.81
# Neptune     348.02       -1.04        29.91
# Pluto       292.75        359.33      33.88
# Ceres       290.87       -5.4         2.92
# Chiron      4.33          2.94        18.81
# Eris        23.55        -11.74       96.0
```

&nbsp;   &nbsp;   &nbsp;   

## **Examples - Use Cases**

* Solar System Live: https://github.com/IoannisNasios/solarsystem/blob/master/examples/Solar_System_Live.ipynb.
    * Plot planets around Sun, watch where planets are around Sun
    * Get the Geocentric positions of Sun, planets, nano planets, our Moon and 1 Centaur

* RiseSet Calendar : https://github.com/IoannisNasios/solarsystem/blob/master/examples/RiseSet_Calendar.ipynb.
    * Time of sun rise and set within each day
    Time of moon rise and set within each day
    Moon phase - percent of illumination


&nbsp;   &nbsp;   &nbsp;   

## **Documentation**

The full documentation is available at [solarsystem.readthedocs.io](https://solarsystem.readthedocs.io)
&nbsp; &nbsp;

**Alternatively you can build documentation:**

[install sphinx](http://www.sphinx-doc.org/en/master/usage/installation.html)

Go to docs/ directory
```python
cd docs
```
Build html files
```python
make html
```
Open _build/html/index.html in browser.


&nbsp;   &nbsp;   &nbsp;   

## **Installation** 

install from Pypi:
```python
pip install solarsystem
```

Latest version from source:
```python
pip install git+https://github.com/IoannisNasios/solarsystem
```

&nbsp;   &nbsp;   &nbsp;   

## **Requirements**

No requirements, no additional libraries needs to be installed.

Exception: example notebook [Solar System Live](https://github.com/IoannisNasios/solarsystem/blob/master/examples/Solar_System_Live.ipynb), matplotlib is needed in order to view the plot


&nbsp;   &nbsp;   &nbsp;   

## **Python versions**
* solarsystem is tested and runs normal for python versions 3.4+ and 2.7
* running solarsystem on previous python versions should also run but use with caution.

&nbsp;   &nbsp;   &nbsp;   

## **Citing**

If you find this library useful, please consider citing:


```
@misc{Nasios:2020,
  Author = {Ioannis Nasios},
  Title = {solarsystem},
  Year = {2020},
  Publisher = {GitHub},
  Journal = {GitHub repository},
  Howpublished = {\url{https://github.com/IoannisNasios/solarsystem}}
}
```

&nbsp;   &nbsp;   &nbsp;  

## **License**
solarsystem is MIT-licensed.
Read [License](https://github.com/IoannisNasios/solarsystem/blob/master/LICENSE)

&nbsp; 
