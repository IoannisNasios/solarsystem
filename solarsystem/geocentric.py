from .functions import sun2planet, spherical2rectangular, ecliptic2equatorial
from .functions import rectangular2spherical  
from .heliocentric import Heliocentric

class Geocentric():
    """Import date data outputs planets positions around Earth.
    
    Args:
        year (int): Year (4 digits) ex. 2020
        month (int): Month (1-12)
        day (int): Day (1-31)
        hour (int): Hour (0-23)
        minute (int): Minute (0-60)
        UT: Time Zone (deviation from UT, -12:+14), ex. for Greece (GMT + 2) 
            enter UT = 2
        dst (int): daylight saving time (0 or 1). Wheather dst is applied at 
                   given time and place
        plane: desired output format. Should be one of: ecliptic, equatorial.
               Default: ecliptic
            
    """
    
    def __init__(self, year, month, day, hour, minute, UT=0, dst=0, 
                 plane='ecliptic'):
        self.plane=plane
        self.planetoncenter = 'Earth'
        h = Heliocentric(year=year, month=month, day=day, hour=hour, 
                         minute=minute, UT=UT, dst=dst, view='rectangular' )
        hplanets = h.planets()
        planets=[]
        for key in hplanets:
            planets.append(hplanets[key])
        self.objectlist = [ "Mercury","Venus","Earth","Mars","Jupyter","Saturn"
                           ,"Uranus","Neptune","Pluto","Ceres","Chiron","Eris"]
        self.planets = planets
        self.oblecl = h.oblecl

        
    def position(self):
        """Main method which returns a dictionary of geocentric positions.
        
        Returns:
            dictionary: Planet positions around earth: Each row represents a 
                        planet and each column the position of that planet.
                        
        """        
        c = self.planets[2]
        RA, Decl, r = rectangular2spherical(c[0],c[1],c[2])
        planetccentric_pos={'Sun':(RA, Decl, r)}

        for i in range(len(self.planets)):
            if i != 2:
                planetccentric_pos[self.objectlist[i]] = sun2planet(self.planets[i][0],
                                  self.planets[i][1], self.planets[i][2],
                               self.planets[2][0], self.planets[2][1], 
                               self.planets[2][2])
                
        if self.plane=='equatorial':
            v1,v2,v3=planetccentric_pos['Sun']
            vv1,vv2,vv3 = spherical2rectangular(v1,v2,v3)
            vvv1,vvv2,vvv3 = ecliptic2equatorial(vv1,vv2,vv3, self.oblecl)
            vvvv1,vvvv2,vvvv3 = rectangular2spherical(vvv1,vvv2,vvv3)
            planetccentric_pos['Sun'] = (vvvv1,vvvv2,vvvv3)
            
            for i in range(len(self.objectlist)):
                if i != 2:
                    v1,v2,v3=planetccentric_pos[self.objectlist[i]]
                    vv1,vv2,vv3 = spherical2rectangular(v1,v2,v3)
                    vvv1,vvv2,vvv3 = ecliptic2equatorial(vv1,vv2,vv3, 
                                                         self.oblecl)
                    vvvv1,vvvv2,vvvv3 = rectangular2spherical(vvv1,vvv2,vvv3)
                    planetccentric_pos[self.objectlist[i]] =(vvvv1,vvvv2,vvvv3)
                
        return planetccentric_pos
     
    def objectnames(self):
        """Names of solar system objects used. 
        
        Returns:
            list: A list of solar system objects
            
        """               
        orderedobjects= ["Sun", "Mercury","Venus","Mars","Jupyter","Saturn","Uranus",
                "Neptune","Pluto","Ceres","Chiron","Eris"]
        return( orderedobjects )    