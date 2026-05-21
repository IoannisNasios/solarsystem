
# **SOLARSYSTEM** 

[![PyPI version](https://badge.fury.io/py/solarsystem.svg)](https://badge.fury.io/py/solarsystem)
[![Documentation Status](https://readthedocs.org/projects/solarsystem/badge/?version=latest)](https://solarsystem.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/IoannisNasios/solarsystem/graph/badge.svg?token=w2cNJJSQ65)](https://codecov.io/gh/IoannisNasios/solarsystem)
[![GPL](https://img.shields.io/badge/license-MIT-green.svg?style=flat)](https://github.com/IoannisNasios/solarsystem/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/solarsystem/month)](https://pepy.tech/project/solarsystem)


**Our Solar System consists of:**

* our Star, the Sun
* 8 Planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus and Neptune
* Some dwarf Planets: Pluto, Ceres, Eris, (Haumea, Makemake, Quaoar, Sedna, Orcus, 2007 OR10, not yet included here)
* Some Centaurs: Chiron (onlyone included here)
* Many moons orbiting planets. Our Moon (Selene in Greek  or Luna in Latin) is included here.


**solarsystem** is a python library for calculating the position (approximately) of **planets** around **Sun** or around **Earth**.


Also with solarsystem we can find the locations around Sun/Earth of the **dwarf planets** (Pluto, Ceres and Eris here), the **Chiron Centaur** and the location of **moon** around Earth.


Furthermore we compute the sunrise/sunset, moonrise/moonset datetimes as well as the moon phase for any given place on Earth (geocoordinates).


In addition, a set of useful functions are included for **converting between coordinate systems**:

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
H = solarsystem.Heliocentric(year=2020, month=1, day=1, hour=12, minute=0, precession=True)
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
# Planet      Longitude   Latitude    Distance in AU
# Mercury     263.55       -4.06       0.47
# Venus         4.95       -3.22       0.73
# Earth       100.25        0.0        0.98
# Mars        214.1         0.49       1.59
# Jupiter     275.83        0.1        5.23
# Saturn      292.23        0.05      10.05
# Uranus       35.07      359.52      19.81
# Neptune     347.74       -1.04      29.91
# Pluto       292.47      359.33      33.88
# Ceres       290.44       -5.4        2.92
# Chiron        3.86        2.94      18.81
# Eris         23.08      -11.74      96.0
```

&nbsp;   &nbsp;   &nbsp;   
* In version 0.1.6 'precession' (of the equinoxes) was added in calculations with True been the default value.  

## **Examples - Use Cases**

* Solar System Live: https://github.com/IoannisNasios/solarsystem/blob/master/examples/Solar_System_Live.ipynb.
    * Plot planets around Sun, watch where planets are around Sun
    * Get the Geocentric positions of Sun, planets, nano planets, our Moon and 1 Centaur

* RiseSet Calendar : https://github.com/IoannisNasios/solarsystem/blob/master/examples/RiseSet_Calendar.ipynb.
    * Time of sun rise and set within each day  
    * Time of moon rise and set within each day  
    * Moon phase - percent of illumination  


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

Exceptions:  
* For the example notebook [Solar System Live](https://github.com/IoannisNasios/solarsystem/blob/master/examples/Solar_System_Live.ipynb), the matplotlib library is needed in order to view the plot  
* For the [python code tests](https://github.com/IoannisNasios/solarsystem/tree/master/tests), libraries pytest and numpy are required  


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
