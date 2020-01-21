import math      
from .functions import normalize, spherical_ecliptic2equatorial
from .functions import spherical_equatorial2ecliptic


class Moon():
    """Import date and place outputs moons position, phase and rise-set time.
       
       Moon is a class that feeded with date data as well as  geocoordicates  
       outputs moons position around Earth, moon phase and moonrise-moonset/
    
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
        longtitude (float): longitude of place of Moonrise - Moonset in demical 
                            format
        latitude (float): latitude of place of Moonrise-Moonset in demical format
        topographic (bool): Wheather or not moon's position around earth will be calculated regarding earth surface or center

    """    
    
    def __init__(self, year, month, day, hour, minute, UT=0, dst=0, 
                 longtitude=0., latitude=51.48, topographic=False):
        self.year = year
        self.month = month
        self.day = day
        self.UT = UT
        self.dst = dst
        self.longtitude = longtitude
        
        self.latitude = math.radians(latitude)
        self.topographic = topographic
        pr=0.
        if (dst==1) : pr=1/24. 
#        JDN=  (367*(year) - math.floor(7*(year + math.floor((month+9 )/12))/4))
#        + math.floor(275*(month)/9) + (day + 1721013.5 - UT/24. ) # 
        JDN=( (367*(year) - math.floor(7*(year + math.floor((month+9 )/12))/4))
        + math.floor(275*(month)/9) + (day + 1721013.5 - UT/24. ) )
        JD= (JDN + (hour)/24. + minute/1440. - pr)
        j2000= 2451543.5
        d= JD - j2000
        self.d = d
        oblecl=23.4393 - 3.563E-7 * d
        oblecl= math.radians(oblecl)
        self.oblecl = oblecl 
        
        
        w=282.9404 + 4.70935E-5 * d      
        e=(0.016709 - (1.151E-9  * self.d))   
        M=356.047 + 0.9856002585 * self.d   
        M=normalize(M)
        L=w+M   
        L=normalize(L)

        gmsto=L/15 + 12 
        sidtime=(-dst + gmsto - UT + longtitude/15)
        self.sidtime = sidtime
        self.M = M
        self.L = L
        self.e=e
        self.w = w
        
        
    def position(self):
        """Method which returns moon's position around Earth
        
        Returns:
            tuple: Moon's positions around earth in horizontal projection 
            (long, lat and distance in multiple of earth radius)

        """
        
        #moons position
        Ns=125.1228 - 0.0529538083*self.d
        is_=5.1454
        ws=318.0634 + 0.1643573223*self.d
        as_=60.2666 #earth's equatorial radius
        es=0.054900
        Ms=115.3654 + 13.0649929509*self.d
        Ns=normalize(Ns)
        ws=normalize(ws)
        Ms=normalize(Ms)
        
        
        Ms2=math.radians(Ms)
        E0=Ms + (180/math.pi)*es*math.sin(Ms2)*(1+es*math.cos(Ms2))
        E0=normalize(E0) 
        E02=math.radians(E0)
        E1=E0 - (E0 - (180/math.pi)*es*math.sin(E02)-Ms)/(1-es*math.cos(E02))
        E1=normalize(E1) 
        
        E=math.radians(E1)
        xs=as_*(math.cos(E)-es)
        ys=as_*(math.sqrt(1 - es*es))*math.sin(E)
        rs=math.sqrt(xs*xs+ys*ys)
        vs=math.atan2(ys, xs)
        vs=normalize(math.degrees(vs))
        
        xseclip=rs*(math.cos(math.radians(Ns))*math.cos(math.radians(vs+ws)) -
                    math.sin(math.radians(Ns))*math.sin(math.radians(vs+ws))
                    *math.cos(math.radians(is_)))
        yseclip=rs*(math.sin(math.radians(Ns))*math.cos(math.radians(vs+ws)) + 
                    math.cos(math.radians(Ns))*math.sin(math.radians(vs+ws))
                    *math.cos(math.radians(is_)))
        zseclip=rs*math.sin(math.radians(vs+ws))*math.sin(math.radians(is_)) 
        
        long2 = math.atan2( yseclip, xseclip )
        long2=normalize(math.degrees(long2))
        lat2 = math.atan2( zseclip, math.sqrt( xseclip*xseclip + 
                                              yseclip*yseclip ) )
        lat2=math.degrees(lat2)
          
        #Moon's Peturbations
        
        Ls=Ns+ws+Ms #moon' s mean longtitude
        Ls=normalize(Ls)
        
        #moon' s mean anomally
        Ds=Ls-self.L  #moon' s mean elogation
        Ds=normalize(Ds)
        Fs=Ls-Ns #moon' s argument of latitude
        Fs=normalize(Fs)
        
        #Peturbations in Longitude
        D1=-1.274*math.sin(math.radians(Ms- 2*Ds)) #evection
        D2=0.658*math.sin(math.radians(2*Ds)) #variation
        D3=-0.186*math.sin(math.radians(self.M))
        D4=-0.059*math.sin(math.radians(2*Ms- 2*Ds))
        D5=-0.057*math.sin(math.radians(Ms - 2*Ds + self.M))
        D6=0.053*math.sin(math.radians(Ms + 2*Ds))
        D7=0.046*math.sin(math.radians(2*Ds - self.M))
        D8=0.041*math.sin(math.radians(Ms - self.M))
        D9=-0.035*math.sin(math.radians(Ds)) #parallactic equation
        D10=-0.031*math.sin(math.radians(Ms + self.M))
        D11=-0.015*math.sin(math.radians(2*Fs - 2*Ds))
        D12=0.011*math.sin(math.radians(Ms - 4*Ds))
        #Peturbations in Latitude
        D13=-0.173*math.sin(math.radians(Fs - 2*Ds))
        D14=-0.055*math.sin(math.radians(Ms - Fs - 2*Ds))
        D15=-0.046*math.sin(math.radians(Ms + Fs - 2*Ds))
        D16=0.033*math.sin(math.radians(Fs + 2*Ds))
        D17=0.017*math.sin(math.radians(2*Ms + Fs))
        #Peturbations in Distance
        D18=-0.58*math.cos(math.radians(Ms - 2*Ds))
        D19=-0.46*math.cos(math.radians(2*Ds))
        
        longdists=D1+D2+D3+D4+D5+D6+D7+D8+D9+D10+D11+D12
        latdists=D13+D14+D15+D16+D17
        moondist=D18+D19
        #
        long2=long2+longdists
        lat2=lat2+latdists
        r_s=rs+moondist
        
        
        if self.topographic==False:
            return (long2, lat2, r_s)
        
        elif self.topographic==True:
            
            RA_s, Decl_s, r_s = spherical_ecliptic2equatorial(long2, lat2, r_s,
                                                              self.oblecl)
            #
            mpar=math.degrees(math.asin(1/r_s)) 
            #
            gclat=math.degrees(self.latitude) - 0.1924*math.sin(2*self.latitude)
            rho= 0.99833 + 0.00167*math.cos(2*self.latitude)
            HA_s=normalize(self.sidtime*15 - RA_s)
            g = math.degrees(math.atan(math.tan(math.radians(gclat))/
                                       math.cos(math.radians(HA_s)))) 
            topRA_s = (RA_s  - mpar*rho*math.cos(math.radians(gclat))*
                  math.sin(math.radians(HA_s))/math.cos(math.radians(Decl_s)) )
                  
            topDecl_s = ( Decl_s - mpar*rho*math.sin(math.radians(gclat))*
            math.sin(math.radians(g - Decl_s))/math.sin(math.radians(g)) )
             
        
            return spherical_equatorial2ecliptic(topRA_s, topDecl_s, r_s, 
                                                 self.oblecl)
        

        

    def phase(self):
        """Method which returns moon's phase
        
        Returns:
            float: Moon's phase (percent of illumination)
            
        """        
        long2, lat2, r_s = Moon.position(self)
#
        M2=self.M
        E=( M2 + (180/math.pi)*self.e * math.sin(math.radians(self.M))*
        (1+ self.e *math.cos(math.radians(self.M))) )
        E=math.radians(E)
        x=math.cos(E)-self.e 
        y=math.sin(E)*math.sqrt(1-self.e*self.e)
        
#        r=math.sqrt(x*x + y*y) #

        v=math.atan2(y,x)  
        v=math.degrees(v)
        lon=(v+self.w)    
        lon=normalize(lon)
        lon=math.radians(lon)
        
        
        long2_s=math.radians(long2)
        lat2_s=math.radians(lat2)
        x_s_eclip = math.cos(long2_s) * math.cos(lat2_s)
        y_s_eclip = math.sin(long2_s) * math.cos(lat2_s)
        z_s_eclip = math.sin(lat2_s)
        
        x_s_equat = x_s_eclip
        y_s_equat = ( y_s_eclip * math.cos(self.oblecl) - z_s_eclip * 
                     math.sin(self.oblecl) )
        z_s_equat = ( y_s_eclip * math.sin(self.oblecl) + z_s_eclip * 
                     math.cos(self.oblecl) )
        
        RA_s = math.atan2(y_s_equat, x_s_equat)
        RA_s=normalize(math.degrees(RA_s))
        Decl_s = math.atan2(z_s_equat, math.sqrt(x_s_equat*x_s_equat + 
                                                 y_s_equat*y_s_equat))
        Decl_s = math.degrees(Decl_s)
         
        mpar=math.degrees(math.asin(1/r_s)) 
        ###alt_topoc=alt_geoc - mpar*math.cos(alt_geoc)
        gclat=math.degrees(self.latitude) - 0.1924*math.sin(2*self.latitude)
        rho= 0.99833 + 0.00167*math.cos(2*self.latitude)
        HA_s=normalize(self.sidtime*15 - RA_s)
        g = math.degrees(math.atan(math.tan(math.radians(gclat))/
                                   math.cos(math.radians(HA_s)))) 
        topRA_s = ( RA_s  - mpar*rho*math.cos(math.radians(gclat))*
        math.sin(math.radians(HA_s))/math.cos(math.radians(Decl_s)) )
          
        topDecl_s = ( Decl_s - mpar*rho*math.sin(math.radians(gclat))*
        math.sin(math.radians(g - Decl_s))/math.sin(math.radians(g)))
        

        #fasi selinis
        x21=math.cos(math.radians(topRA_s))*math.cos(math.radians(topDecl_s))
        y21=math.sin(math.radians(topRA_s))*math.cos(math.radians(topDecl_s))
        z21=math.sin(math.radians(topDecl_s))
        
        x221=x21
        y221=y21*math.cos(-self.oblecl)-z21*math.sin(-self.oblecl)
        z221=y21*math.sin(-self.oblecl)+z21*math.cos(-self.oblecl)
        
        mlon21=normalize(math.degrees(math.atan2(y221, x221)))
        mlat21=math.degrees(math.atan2(z221, math.sqrt(x221*x221 + y221*y221)))
        mlon21=math.radians(mlon21)
        mlat21=math.radians(mlat21)
        elong_s=math.degrees(math.acos(math.cos(lon - mlon21)* 
                                       math.cos(mlat21)))
#        elong_s2=normalize(360- math.degrees(lon) + math.degrees(mlon21))
        FV21=180 - elong_s
        phase = (1 + math.cos(math.radians(FV21))) / 2 
        
        return phase


    def moonriseset(self):
        """Method which returns moon's rise and set time
        
        Returns:
            tuple: Moon's time of given date where moon rises and sets

        """    
        MoonPos = Moon(year=self.year, month=self.month, day=self.day, hour=12,
               minute=0, UT=self.UT, dst=self.dst, longtitude=self.longtitude, 
               latitude=self.latitude, topographic=True)
        
        long2, lat2, r_s = MoonPos.position()
        topRA_s, topDecl_s, r_s = spherical_ecliptic2equatorial(long2, lat2, 
                                                         r_s, self.oblecl)

        aDecl_s=math.radians(topDecl_s)
        T_s=normalize((topRA_s - self.sidtime*15))/15.04107 
        #mesouranima selinis
        h=math.radians(0) 
        adi_s=( (math.sin(h) -math.sin(self.latitude)*math.sin(aDecl_s))/
        (math.cos(self.latitude)*math.cos(aDecl_s)) )
        Lha_s=math.acos(adi_s)
        Lha_s= (math.degrees(Lha_s))/15.04107
        #ores apo to mesouranima os tin anatoli i os tin disi
        anatoli_s=T_s - Lha_s  
        if (anatoli_s<0) : anatoli_s=anatoli_s+24 
        if (anatoli_s > 24) : anatoli_s=anatoli_s - 24 
        disi_s=T_s + Lha_s
        if (disi_s < 0) : disi_s=disi_s + 24 
        if (disi_s > 24) : disi_s=disi_s - 24 
        
        return(anatoli_s, disi_s)