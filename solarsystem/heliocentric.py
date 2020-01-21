import math
from .functions import normalize, Planet_Sun

class Heliocentric:
    """Import date data outputs planets positions around Sun.
    
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
        view: desired output format. Should be one of: horizontal (long in 
              degrees, lat in degrees, distance in AU) or 
              rectangular (x, y, z, all in AU).
              Default: horizontal.
 
    """
    
    def __init__(self, year, month, day, hour, minute, UT=0, dst=0, 
                 view='horizontal'): 

        self.view = view
        pr=0.
        if (dst==1) : pr=1/24. 
        JDN=( (367*(year) - math.floor(7*(year + math.floor((month+9 )/12))/4))
        + math.floor(275*(month)/9) + (day + 1721013.5 - UT/24. ) )
        JD= (JDN + (hour)/24. + minute/1440. - pr)
        j2000= 2451543.5
        d= JD - j2000
        self.d = d
        
        # sun' s trajectory elements
        w=282.9404 + 4.70935E-5 * d      
#        a=1
        e=(0.016709 - (1.151E-9  * d))   
        M=356.047 + 0.9856002585 * d   
        M=normalize(M)
        L=w+M   
        L=normalize(L)
        oblecl=23.4393 - 3.563E-7 * d
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
        lon=normalize(lon)
        lon=math.radians(lon) 
        x2=r * math.cos(lon) 
        y2=r * math.sin(lon)
        z2=0
        
        
        xequat = x2   
        oblecl= math.radians(oblecl)
        self.oblecl = oblecl
        yequat = (y2*math.cos(oblecl) + z2 * math.sin(oblecl))
        zequat = (y2*math.sin(oblecl) + z2 * math.cos(oblecl))
       
        
        RA=math.atan2(yequat, xequat)
        RA=math.degrees(RA)
        RA=normalize(RA)
        Decl=math.atan2(zequat, math.sqrt(xequat*xequat +yequat*yequat))
        Decl=math.degrees(Decl)

        self.x=normalize(math.degrees(x))
        self.y=normalize(math.degrees(y))
        self.r=r
        self.x2=x2
        self.y2=y2
        self.z2=z2
        self.lon = normalize(-math.degrees(lon))
        lat = math.atan2( z2, math.sqrt( x2**2 + y2**2 ) )
        lat=normalize(math.degrees(lat))
        self.lat=lat
        
        

    def planetnames(self):
        """Names of solar system objects used. 
        
        Returns:
            list: A list of solar system objects.
            
        """  
        return( ["Mercury","Venus","Earth","Mars","Jupyter","Saturn","Uranus",
                "Neptune","Pluto","Ceres","Chiron","Eris"])

    

    def planets(self):
        """Main method which returns a dictionary of Heliocentric positions.
        
        Returns:
            dictionary: Planet positions around sun: Dictionary of tuples. Each
            row represents a planet and each column the position of that planet.
            
        """
        
        # Planets trajectory elements
        #Ermis
        N_er=48.3313 + 3.24587E-5 *self.d
        i_er=7.0047 +5.00E-8 *self.d
        w_er=29.1241 + 1.01444E-5 *self.d
        a_er=0.387098
        e_er=0.205635 + 5.59E-10 *self.d
        M_er=168.6562 + 4.0923344368 *self.d
        
        M_er=normalize(M_er)
        
        #Afroditi
        N_af=76.6799 + 2.46590E-5 *self.d
        i_af=3.3946 +2.75E-8 *self.d
        w_af=54.8910 + 1.38374E-5 *self.d
        a_af=0.723330
        e_af=0.006773 - 1.30E-9 *self.d
        M_af=48.0052 + 1.6021302244 *self.d
        
        M_af=normalize(M_af)
        
        #Aris
        N_ar=49.5574 + 2.11081E-5 *self.d
        i_ar=1.8497 - 1.78E-8 *self.d
        w_ar=286.5016 + 2.92961E-5 *self.d
        a_ar=1.523688
        e_ar=0.093405 + 2.51E-9 *self.d
        M_ar=18.6021 + 0.5240207766 *self.d
        
        M_ar=normalize(M_ar)
        
        #Dias
        N_di=100.4542 + 2.76854E-5 *self.d
        i_di=1.3030 - 1.557E-7 *self.d
        w_di=273.8777 + 1.6450E-5 *self.d
        a_di=5.20256
        e_di=0.048498 + 4.469E-9 *self.d
        M_di=19.8950 + 0.0830853001 *self.d
        
        M_di=normalize(M_di)
        
        #Kronos
        N_kr=113.6634 + 2.38980E-5 *self.d
        i_kr=2.4886 - 1.081E-7 *self.d
        w_kr=339.3939 + 2.97661E-5 *self.d
        a_kr=9.55475
        e_kr=0.055546 - 9.499E-9 *self.d
        M_kr=316.9670 + 0.0334442282 *self.d
        
        M_kr=normalize(M_kr)
        
        #Ouranos
        N_ou=74.0005 + 1.3978E-5 *self.d
        i_ou=0.7733 + 1.9E-8 *self.d
        w_ou=96.6612 + 3.0565E-5 *self.d
        a_ou=19.18171 - 1.55E-8 *self.d
        e_ou=0.047318 + 7.45E-9 *self.d
        M_ou=142.5905 + 0.011725806 *self.d
        
        M_ou=normalize(M_ou)
        
        #Poseidonas
        N_po=131.7806 + 3.0173E-5 *self.d
        i_po=1.7700 - 2.55E-7 *self.d
        w_po=272.8461 - 6.027E-6 *self.d
        a_po=30.05826 + 3.313E-8 *self.d
        e_po=0.008606 + 2.15E-9 *self.d
        M_po=260.2471 + 0.005995147 *self.d
        
        M_po=normalize(M_po)
          
        
        #D CERES epoch 2455400.5 2010-jul-23.0   j2000= 2451543.5
        ddd = self.d + 2451543.5 - 2455400.5
        
        N_ce=80.39319901972638  + 1.1593E-5 *ddd
        i_ce=10.58682160714853 - 2.2048E-6*ddd
        w_ce=72.58981198193074  + 1.84E-5*ddd
        a_ce=2.765348506018043 
        e_ce=0.07913825487621974 + 1.8987E-8*ddd
        M_ce=113.4104433863731   + 0.21408169952325  * ddd 
        
        M_ce=normalize(M_ce)
        
        #A CHIRON epoch  2456400.5 2013-apr-18.0   j2000= 2451543.5
        dddd = self.d + 2451543.5 - 2456400.5
        
        N_ch=209.3557401732507 	 
        i_ch=6.929449422368333 	
        w_ch=339.3298742575888 	
        a_ch=13.6532230321495 
        e_ch=0.3803659797957286  
        M_ch=122.8444574834622  +  0.01953670401251872 * dddd   
        
        M_ch=normalize(M_ch)
        
        #A ERIS epoch  2456400.5 2013-apr-18.0   j2000= 2451543.5
        ddddd= self.d + 2451543.5 - 2456400.5
        
        N_pe=36.0308972598494  
        i_pe=43.88534676566927 
        w_pe=150.8002573158863 
        a_pe=67.95784302407351 
        e_pe=0.4370835020505101 
        M_pe=203.2157808586589 +  0.001759319413340421 * ddddd   
        
        M_pe=normalize(M_pe)
        

        #Ermis
        xereclip,yereclip,zereclip, long2_er, lat2_er, r_er = Planet_Sun(M_er, 
                                            e_er, a_er, N_er, w_er, i_er)
        
        #Afroditi
        xafeclip,yafeclip,zafeclip, long2_af, lat2_af, r_af = Planet_Sun(M_af, 
                                            e_af, a_af, N_af, w_af, i_af)
        
        #Aris
        xareclip,yareclip,zareclip, long2_ar, lat2_ar, r_ar = Planet_Sun(M_ar, 
                                            e_ar, a_ar, N_ar, w_ar, i_ar)
        
        
        #Dias
        xdieclip,ydieclip,zdieclip, long2_di, lat2_di, r_di = Planet_Sun(M_di, 
                                            e_di, a_di, N_di, w_di, i_di)
        
        #Kronos
        xkreclip,ykreclip,zkreclip, long2_kr, lat2_kr, r_kr = Planet_Sun(M_kr, 
                                            e_kr, a_kr, N_kr, w_kr, i_kr)
        
        #Ouranos
        xoueclip,youeclip,zoueclip, long2_ou, lat2_ou, r_ou = Planet_Sun(M_ou, 
                                            e_ou, a_ou, N_ou, w_ou, i_ou)
        
        #Poseidonas
        xpoeclip,ypoeclip,zpoeclip, long2_po, lat2_po, r_po = Planet_Sun(M_po, 
                                            e_po, a_po, N_po, w_po, i_po)
        
        
        #Ceres
        xceeclip,yceeclip,zceeclip, long2_ce, lat2_ce, r_ce = Planet_Sun(M_ce, 
                                            e_ce, a_ce, N_ce, w_ce, i_ce)
        
        #Chiron
        xcheclip,ycheclip,zcheclip, long2_ch, lat2_ch, r_ch = Planet_Sun(M_ch, 
                                            e_ch, a_ch, N_ch, w_ch, i_ch)
        
        #Eris
        xpeeclip,ypeeclip,zpeeclip, long2_pe, lat2_pe, r_pe = Planet_Sun(M_pe, 
                                            e_pe, a_pe, N_pe, w_pe, i_pe)
        
        #ploutonas
        S_pl  = math.radians(  50.03  +  0.033459652 *  self.d)
        P_pl  = math.radians( 238.95  +  0.003968789 *  self.d)
        
        long2_pl = (238.9508  +  0.00400703 * self.d - 19.799 * math.sin(P_pl)
                     + 19.848 * math.cos(P_pl) + 0.897 * math.sin(2*P_pl)
               - 4.956 * math.cos(2*P_pl) + 0.610 * math.sin(3*P_pl)
               + 1.211 * math.cos(3*P_pl) - 0.341 * math.sin(4*P_pl)
               - 0.190 * math.cos(4*P_pl) + 0.128 * math.sin(5*P_pl)
               - 0.034 * math.cos(5*P_pl) - 0.038 * math.sin(6*P_pl)
               + 0.031 * math.cos(6*P_pl) + 0.020 * math.sin(S_pl - P_pl) 
               - 0.010 * math.cos(S_pl - P_pl) )
        lat2_pl = ( -3.9082 - 5.453 * math.sin(P_pl) - 14.975 * math.cos(P_pl)
                      + 3.527 * math.sin(2*P_pl) + 1.673 * math.cos(2*P_pl)
                      - 1.051 * math.sin(3*P_pl) + 0.328 * math.cos(3*P_pl)
                      + 0.179 * math.sin(4*P_pl) - 0.292 * math.cos(4*P_pl)
                      + 0.019 * math.sin(5*P_pl) + 0.100 * math.cos(5*P_pl)
                      - 0.031 * math.sin(6*P_pl) - 0.026 * math.cos(6*P_pl)
                      + 0.011 * math.cos(S_pl - P_pl) )
        r_pl = ( 40.72 + 6.68 * math.sin(P_pl) + 6.90 * math.cos(P_pl)
                      - 1.18 * math.sin(2*P_pl) - 0.03 * math.cos(2*P_pl)
                      + 0.15 * math.sin(3*P_pl) - 0.14 * math.cos(3*P_pl))
        
        long2_pl=math.radians(long2_pl)
        lat2_pl=math.radians(lat2_pl)
        x_pl = r_pl * math.cos(long2_pl) * math.cos(lat2_pl) #eclip
        y_pl = r_pl * math.sin(long2_pl) * math.cos(lat2_pl)
        z_pl = r_pl * math.sin(lat2_pl)
        
 
    
        #Perturbations 
        M_di=normalize(M_di)
        M_kr=normalize(M_kr)
        M_ou=normalize(M_ou)
        
        #add to Jupiter long
        di_diat1=-0.332*math.sin(math.radians(2*M_di - 5 * M_kr - 67.6))
        di_diat2=-0.056*math.sin(math.radians(2*M_di - 2 * M_kr +21))
        di_diat3=0.042*math.sin(math.radians(3*M_di - 5 * M_kr +21))
        di_diat4=-0.036*math.sin(math.radians(M_di - 2 * M_kr))
        di_diat5=0.022*math.cos(math.radians(M_di - M_kr))
        di_diat6=0.023*math.sin(math.radians(2*M_di - 3 * M_kr + 52))
        di_diat7=-0.016*math.sin(math.radians(M_di - 5 * M_kr - 69))
        
        #add to Saturn long
        kr_diat1=0.812*math.sin(math.radians(2*M_di - 5 * M_kr - 67.6))
        kr_diat2=-0.229*math.cos(math.radians(2*M_di - 4 * M_kr -2))
        kr_diat3=0.119*math.sin(math.radians(M_di - 2 * M_kr - 3))
        kr_diat4=0.046*math.sin(math.radians(2*M_di - 6 * M_kr - 69))
        kr_diat5=0.014*math.sin(math.radians(M_di - 3* M_kr + 32))
        #add to Saturn lat
        kr_diat6=-0.02*math.cos(math.radians(2*M_di - 4 * M_kr - 2))
        kr_diat7=0.018*math.sin(math.radians(2*M_di - 6 * M_kr - 49))
       
        #add to Uranus long
        ou_diat1=0.04*math.sin(math.radians(M_kr - 2 * M_ou + 6))
        ou_diat2=0.035*math.sin(math.radians(M_kr - 3 * M_ou + 33))
        ou_diat3=-0.015*math.sin(math.radians(M_di - M_ou +20))
        
        diataraxes_long_di=(di_diat1 + di_diat2 + di_diat3 + di_diat4 + 
                            di_diat5 + di_diat6 + di_diat7)
        diataraxes_long_kr=(kr_diat1 + kr_diat2 + kr_diat3 + kr_diat4 
                            + kr_diat5)
        diataraxes_lat_kr=(kr_diat6 + kr_diat7)
        diataraxes_long_ou=(ou_diat1 + ou_diat2 + ou_diat3)
        
        #Corrected coordinates for the three planets
        long2_di=long2_di + diataraxes_long_di
        long2_kr=long2_kr + diataraxes_long_kr
        lat2_kr=lat2_kr + diataraxes_lat_kr
        long2_ou=long2_ou + diataraxes_long_ou
        
        long2_di=(math.radians(long2_di))
        lat2_di=(math.radians(lat2_di))
        long2_kr=(math.radians(long2_kr))
        lat2_kr=(math.radians(lat2_kr))
        long2_ou=(math.radians(long2_ou)) 
        lat2_ou=(math.radians(lat2_ou)) 
        
        #Recompute positions of three planets
        xdieclip = r_di * math.cos(long2_di) * math.cos(lat2_di)
        ydieclip = r_di * math.sin(long2_di) * math.cos(lat2_di) 
        zdieclip = r_di * math.sin(lat2_di)
        xkreclip = r_kr * math.cos(long2_kr) * math.cos(lat2_kr)
        ykreclip = r_kr * math.sin(long2_kr) * math.cos(lat2_kr) 
        zkreclip = r_kr * math.sin(lat2_kr)
        xoueclip = r_ou * math.cos(long2_ou) * math.cos(lat2_ou)
        youeclip = r_ou * math.sin(long2_ou) * math.cos(lat2_ou) 
        zoueclip = r_ou * math.sin(lat2_ou)  
        
        
        long2_di=normalize(math.degrees(long2_di))
        lat2_di=normalize(math.degrees(lat2_di))
        long2_kr=normalize(math.degrees(long2_kr))
        lat2_kr=normalize(math.degrees(lat2_kr))
        long2_ou=normalize(math.degrees(long2_ou)) 
        lat2_ou=normalize(math.degrees(lat2_ou)) 
        
        long2_pl=normalize(math.degrees(long2_pl))
        lat2_pl=normalize(math.degrees(lat2_pl))
        
 
        if self.view == 'horizontal':
            return {
                    'Mercury':(long2_er, lat2_er, r_er),
                    'Venus'  :(long2_af, lat2_af, r_af),
                    'Earth'  :(self.lon, self.lat, self.r),
                    'Mars'   :(long2_ar, lat2_ar, r_ar),
                    'Jupyter':(long2_di, lat2_di, r_di),
                    'Saturn' :(long2_kr, lat2_kr, r_kr),
                    'Uranus' :(long2_ou, lat2_ou, r_ou),
                    'Neptune':(long2_po, lat2_po, r_po),
                    'Pluto'  :(long2_pl, lat2_pl, r_pl),
                    'Ceres'  :(long2_ce, lat2_ce, r_ce),
                    'Chiron' :(long2_ch, lat2_ch, r_ch),
                    'Eris'   :(long2_pe, lat2_pe, r_pe)
                    }
            
        elif self.view == 'rectangular':     
            return {
                    'Mercury':(xereclip,yereclip,zereclip),
                    'Venus'  :(xafeclip,yafeclip,zafeclip),
                    'Earth'  :(self.x2, self.y2, self.z2),
                    'Mars'   :(xareclip,yareclip,zareclip),
                    'Jupyter':(xdieclip,ydieclip,zdieclip),
                    'Saturn' :(xkreclip,ykreclip,zkreclip),
                    'Uranus' :(xoueclip,youeclip,zoueclip),
                    'Neptune':(xpoeclip,ypoeclip,zpoeclip),
                    'Pluto'  :(x_pl,y_pl,z_pl),
                    'Ceres'  :(xceeclip,yceeclip,zceeclip),
                    'Chiron' :(xcheclip,ycheclip,zcheclip),
                    'Eris'   :(xpeeclip,ypeeclip,zpeeclip)
                    }