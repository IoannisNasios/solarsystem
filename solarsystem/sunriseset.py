import math
from .functions import normalize

class Sunriseset():
    """Import date outputs Sunrise and Sunset time.
    
    Args:
        year (int): Year (4 digits) ex. 2020.
        month (int): Month (1-12).
        day (int): Day (1-31).
        UT: Time Zone (deviation from UT, -12:+14), ex. for Greece (GMT + 2) 
            enter UT = 2.
        dst (int): daylight saving time (0 or 1). Wheather dst is applied at 
                   given time and place.
        longtitude (float): longitude of place of Sunrise - Sunset in demical format.
        latitude (float): latitude of place of Sunrise - Sunset in demical format.

    """
    
    def __init__(self, year, month, day, UT=0, dst=0, longtitude=0., 
                 latitude=51.48):
        self.UT =  UT
        self.dst = dst
        self.longtitude = longtitude
        self.latitude = latitude
        pr=0.
        if (dst==1) : pr=1/24. 
        JDN= ((367*(year) - math.floor(7*(year + math.floor((month+9 )/12))/4))
        + math.floor(275*(month)/9) + (day + 1721013.5 - UT/24. ) )   
        JD= (JDN + (12)/24. + 0/1440. - pr)
        j2000= 2451543.5
        d= JD - j2000
        self.d = d
        oblecl=23.4393 - 3.563E-7 * d
        oblecl= math.radians(oblecl)
        self.oblecl = oblecl 
        

    def riseset(self):
        """Get the time of sun rise and set within given date.
        
        Returns:
            tuple: Sunrise - Sunset time of given date
            
        """
        
        #Sun's trajectory elements
        w=282.9404 + 4.70935E-5 * self.d      
        e=(0.016709 - (1.151E-9  * self.d))   
        M=356.047 + 0.9856002585 * self.d   
        M=normalize(M)
        L=w+M   
        L=normalize(L)

        M2=M
        M=math.radians(M)
        E=M2 + (180/math.pi)*e*math.sin(M)*(1+e*math.cos(M))
        E=math.radians(E)
        x=math.cos(E)-e
        y=math.sin(E)*math.sqrt(1-e*e)
        
        r=math.sqrt(x*x + y*y) 
        v=math.atan2(y,x)  
        v=math.degrees(v)
        lon=(v+w)   
        lon=normalize((lon))
        lon=math.radians(lon) 
        x2=r * math.cos(lon) 
        y2=r * math.sin(lon)
        z2=0
        
        xequat = x2   
        yequat = (y2*math.cos(self.oblecl) - z2 * math.sin(self.oblecl))
        zequat = (y2*math.sin(self.oblecl) + z2 * math.cos(self.oblecl))

    
        RA=math.atan2(yequat, xequat)
        RA=math.degrees(RA)
        RA=normalize(RA)
        Decl=math.atan2(zequat, math.sqrt(xequat*xequat +yequat*yequat))
        Decl=math.degrees(Decl)
        #RA2=RA/15
        
        gmsto=L/15 + 12 
        
        sidtime=(-self.dst + gmsto - self.UT + self.longtitude/15)
        
        HA=(sidtime*15 - RA) #gonia oras
        HA=math.radians(HA)
        Decl=math.radians(Decl)
        
        x3=math.cos(HA)*math.cos(Decl)
        y3=math.sin(HA)*math.cos(Decl)
        z3=math.sin(Decl)
        
        
        latitude=math.radians(self.latitude)
        xhor=(x3*math.sin(latitude) - z3*math.cos(latitude))
        yhor=y3
        zhor=(x3*math.cos(latitude) + z3*math.sin(latitude))
        azim=math.atan2(yhor, xhor) 
        azim=math.degrees(azim)
#        azimuth=azim + 180 
        altitude=math.asin(zhor)
        altitude=math.degrees(altitude)
        
        T_sun=normalize((RA - sidtime*15))/15 
        h=math.radians(-0.833)
        adi=(math.sin(h) -math.sin(latitude)*math.sin(Decl))/(math.cos(latitude)*math.cos(Decl))
        Lha=math.acos(adi)
        Lha= (math.degrees(Lha))/15
        anatoli=T_sun - Lha  
        disi=T_sun + Lha
        
        return (anatoli, disi)