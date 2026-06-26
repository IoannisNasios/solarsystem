
# 🌌 solarsystem

[![PyPI version](https://badge.fury.io/py/solarsystem.svg)](https://badge.fury.io/py/solarsystem)
[![Documentation Status](https://readthedocs.org/projects/solarsystem/badge/?version=latest)](https://solarsystem.readthedocs.io/en/latest/?badge=latest)
[![codecov](https://codecov.io/gh/IoannisNasios/solarsystem/graph/badge.svg?token=w2cNJJSQ65)](https://codecov.io/gh/IoannisNasios/solarsystem)
[![GPL](https://img.shields.io/badge/license-MIT-green.svg?style=flat)](https://github.com/IoannisNasios/solarsystem/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/solarsystem/month)](https://pepy.tech/project/solarsystem)




**solarsystem** is a lightweight, dependency-free Python library for computing Solar System positions, Solar-Lunar events, and coordinate transformations.

It is designed for **education, visualization, and lightweight astronomical computation**, without requiring external ephemeris datasets or heavy scientific dependencies.

---

## Supported Celestial Bodies  

- The Sun (our central star)  
- All 8 major planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune  
- Dwarf planets: Pluto, Ceres, Eris *(with additional bodies planned to be included in future releases)*  
- Minor bodies: Chiron (Centaur class)  
- Natural satellites: Earth's Moon (Luna / Selene)

---

## Features   

The library provides tools for:  

### Planetary Positioning  
- Approximate heliocentric positions of planets
- Geocentric positions for Earth-based observations
- Support for dwarf planets and selected minor bodies

### Solar/Lunar Events (for any location on Earth)  
- Sunrise and sunset times 
- Moonrise and moonset calculations
- Lunar illumination percentage

### Coordinate Transformations  
- Spherical ↔ Cartesian  
- Ecliptic ↔ Equatorial  
- Ecliptic ↔ Spherical projections  

---

## ⚡ Installation  

Install directly from PyPI:

```bash
pip install solarsystem
```

Or install from GitHub:
```bash
pip install git+https://github.com/IoannisNasios/solarsystem
```


---

## Quick start  

```python
import solarsystem
```

Initialize Heliocentric class


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
# Uranus       35.07       -0.48      19.81
# Neptune     347.74       -1.04      29.91
# Pluto       292.47       -0.67      33.88
# Ceres       290.44       -5.4        2.92
# Chiron        3.86        2.94      18.81
# Eris         23.08      -11.74      96.0
```


---

## Example Applications

The repository includes Jupyter notebooks:

- **Solar System Live**  
  Real-time planetary visualization and animation  
  https://github.com/IoannisNasios/solarsystem/blob/master/examples/Solar_System_Live.ipynb  

- **RiseSet Calendar**  
https://github.com/IoannisNasios/solarsystem/blob/master/examples/RiseSet_Calendar.ipynb  
  Yearly calendar of:
  - sunrise / sunset  
  - moonrise / moonset  
  - lunar illumination  

---

## 🌀 Precession Support (v0.1.6+)

Starting from **version 0.1.6**, the library includes an optional **precession of the equinoxes correction**.

- Default: `precession=True`
- Can be disabled: `precession=False`

### Why this matters:

- Improves long-term coordinate consistency
- Reduces systematic longitude drift across epochs
- Allows both:
  - *modern ephemeris-style calculations*
  - *fixed-frame educational mode*


---


## 📊 Accuracy and Validation

To evaluate numerical performance, the library was compared against **JPL DE440 ephemerides**.

### Summary of results:

- Mean longitude error: *<< 1° (mean absolute error ~0.007°)*  
- Mean latitude error: *~0.002°*  
- Mean distance error: *~0.05 AU*  
- Lunar illumination error: *~0.2%*  
- Moonrise / Moonset timing difference: *~2-3 minutes*  

Full results and figures are included in the accompanying research paper.  
Validation Notebooks used can be found in https://github.com/IoannisNasios/solarsystem/blob/master/performance/

These results indicate that `solarsystem` achieves **adequate calculations for various use cases**, while maintaining a lightweight computational design.


---


## 📚 Documentation

Full documentation is available at:  
https://solarsystem.readthedocs.io

### Build documentation locally

```bash
pip install sphinx
cd docs
make html
```
Open _build/html/index.html in browser.  


---

## Requirements  
Core package:  
No external dependencies 

Optional:  
matplotlib → for visualization notebooks  
pytest, numpy → for running tests  
matplotlib, skyfield, numpy → for performance evaluation notebooks  


---

## Python Support  

Tested on:  

Python 3.4+  
Python 2.7 (legacy support)  

Newer Python versions are recommended for best performance and compatibility. 

---

## 📖 Citing  

Preprint can be found on [Arxiv](https://arxiv.org/pdf/2606.27055)  
If you use this library in your work, please cite:  


```
@misc{nasios2026solarsystemvalidatedlightweightpython,
      title={Solarsystem: A Validated Lightweight Python Package for Planetary Positions and Solar-Lunar Event Calculations}, 
      author={Ioannis Nasios},
      year={2026},
      eprint={2606.27055},
      archivePrefix={arXiv},
      primaryClass={astro-ph.EP},
      url={https://arxiv.org/abs/2606.27055}, 
}
```



---

## License  

MIT License ©

