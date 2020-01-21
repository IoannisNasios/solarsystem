import math

    

def normalize(degrees):  
    """
    set degrees always between 0 - 360
    
    Args:
        degrees (float): degrees to be adjusted
        
    Returns:
        float: degrees between 0-360
        
    """
    return degrees % 360

    

def spherical2rectangular(RA, Decl, r):
    """Transform spherical to rectangular projection.
    
    From spherical (RA,Decl) coordinates system to rectangular(x,y,z) or 
    by replacing RA with longitude and Decl with latitude we can tranform 
    ecliptic coordinates to horizontal (azimuth,altitude).
    
    Args:
        RA: Right Ascension.
        Decl: Declination.
        r: Distance in astronomical units.
   
    Returns:
        tuple: x, y, z rectangular coordinate system. 
        
    """
    
    RA = math.radians(RA)
    Decl = math.radians(Decl)
    x = r * math.cos(RA) * math.cos(Decl)
    y = r * math.sin(RA) * math.cos(Decl)
    z = r * math.sin(Decl)
    
    return (x, y, z)


def rectangular2spherical(x, y, z):
    """Transform rectangular to spherical projection.
    
    From rectangular(x,y,z) coordinates system to spherical (RA,Decl, r) or 
    by replacing x with azimuth and y with altitude we can tranform 
    horizontal coordinates to ecliptic (longitude, latitude).
    
    Args:
        x: value on x axis of a rectangular projection.
        y: value on y axis of a rectangular projection.
        z: value on z axis of a rectangular projection.
   
    Returns:
        tuple: RA, Decl, r spherical coordinate system. 
        
    """
    
    r    = math.sqrt( x*x + y*y + z*z )
    RA   = math.atan2( y, x )
#    Decl = math.asin( z / r ) 
    Decl = math.atan2( z, math.sqrt( x*x + y*y ) )
    
    RA = normalize(math.degrees(RA))
    Decl = (math.degrees(Decl))
    return (RA, Decl, r)
    


def ecliptic2equatorial(xeclip, yeclip, zeclip, oblecl):
    """Transform ecliptic to equatorial projection.
    
    Args:
        xeclip: value on x axis of ecliptic plane.
        yeclip: value on y axis of ecliptic plane.
        zeclip: value on z axis of ecliptic plane.
        oblecl: obliquity of the ecliptic, approximately 23.4 degrees for earth
   
    Returns:
        tuple: x, y, z equatorial projection 
        
    """
#    oblecl = math.radians(oblecl)
    
    xequat = xeclip
    yequat = yeclip * math.cos(oblecl) - zeclip * math.sin(oblecl)
    zequat = yeclip * math.sin(oblecl) + zeclip * math.cos(oblecl)
    
    return (xequat, yequat, zequat)



def equatorial2ecliptic(xequat, yequat, zequat, oblecl):
    """Transform equatorial to ecliptic projection.
    
    Args:
        xequat: value on x axis of equatorial plane
        yequat: value on y axis of equatorial plane
        zequat: value on z axis of equatorial plane
        oblecl: obliquity of the ecliptic, approximately 23.4 degrees for earth
   
    Returns:
        tuple: x, y, z ecliptic projection 
        
    """
    
#    oblecl = math.radians(oblecl)
    xeclip = xequat
    yeclip = yequat * math.cos(-oblecl) - zequat * math.sin(-oblecl)
    zeclip = yequat * math.sin(-oblecl) + zequat * math.cos(-oblecl)
    return (xeclip, yeclip, zeclip)
    


def spherical_ecliptic2equatorial(long, lat, distance, oblecl):
    """Transform eclipitc to spherical projection for given obliquity.
    
    From spherical (RA, Decl, distance) coordinates system to 
    eclipitc(long, lat, distance).
    
    Args:
        long: Longitude.
        last: Latitude.
        distance: Distance in astronomical units.
        oblecl: obliquity (axial tilt).
            
    Returns:
        tuple: RA, Decl, distance spherical coordinate system. 
        
    """
    
    b = spherical2rectangular(long,lat,distance)
    c = ecliptic2equatorial(b[0],b[1],b[2], oblecl)
    return rectangular2spherical(c[0],c[1],c[2])


def spherical_equatorial2ecliptic(RA, Decl, distance, oblecl):
    """Transform spherical to eclipitc projection for given obliquity.
    
    From spherical (RA, Decl, distance) coordinates system to 
    eclipitc(long, lat, distance).
    
    Args:
        RA: Right Ascension.
        Decl: Declination.
        distance: Distance in astronomical units.
        oblecl: obliquity (axial tilt).
            
    Returns:
        tuple: long, lat, distance eclipitc coordinate system. 
        
    """
    
    b = spherical2rectangular(RA, Decl,distance)
    c = equatorial2ecliptic(b[0],b[1],b[2], oblecl)
    return rectangular2spherical(c[0],c[1],c[2])


def demical2clock(demicaltime):
    """
    Convert demical time view to Hours, Minutes and Seconds.
    
    Args:
        demicaltime (float): time to be converted.
        
    Returns:
        str: one string representation in hours, minutes format.
        
    """ 
    h = int(demicaltime)
    m = int((demicaltime - h) * 60)
    s = int(((demicaltime-h)*60 - m ) * 60)
    h=str(h)
    m=str(m)
    s=str(s)
    if len(h)==1: h = '0' + h
    if len(m)==1: m = '0' + m
    if len(s)==1: s = '0' + s
    res = h + ':'+ m + ':'+ s
    return res


def demical2arcs(num):
    """
    Convert Demical view to Degrees and minutes.
    
    Args:
        num (float): degrees to be converted.
        
    Returns:
        str: one string representation in degrees and minutes format.
        
    """       
    return(str(int(num))+u"\u00b0 "+str(round(abs(num - int(num))*60,2))+"'")

#def degrees2hours(degrees):
#    """
#    Convert degrees to string representation of hours, minutes and seconds.
#    
#    Args:
#        degrees (float): degrees to be converted.
#        
#    Returns:
#        str: one string representation in hours, minutes and seconds format.
#        
#    """    
#    h=degrees//15
#    r=(degrees%15)*4
#    m=int(r)
#    s=int((r-m)*60)
#    return (str(h)+'h '+str(m)+'m '+str(s)+'s')

def demical2hms(degrees):
    """
    Convert degrees to string representation of hours, minutes and seconds.
    
    Args:
        degrees (float): degrees to be converted.
        
    Returns:
        str: one string representation in hours, minutes and seconds format.
        
    """   
    
    h = int(degrees/15)
    m = int((degrees/15 - h) * 60)
    s = int(((degrees/15-h)*60 - m ) * 60)
    h=str(h)
    m=str(m)
    s=str(s)
    if len(h)==1: h =  h
    if len(m)==1: m =  m
    if len(s)==1: s =  s
    res = h + 'h '+ m + 'm '+ s +'s'
    return res


def Planet_Sun(M, e, a, N, w, i):
    """
    Helper Function. From planet's trajectory elements to position around sun
        
    Returns:
        tuple: position elements
        
    """
    M2=math.radians(M)
    E0=M + (180/math.pi)*e*math.sin(M2)*(1+e*math.cos(M2))
    E0=normalize(E0) 
    E02=math.radians(E0)
    E1=E0 - (E0 - (180/math.pi)*e*math.sin(E02)-M)/(1-e*math.cos(E02))
    E1=normalize(E1) 
    E=math.radians(E1)
    x=a*(math.cos(E)-e)
    y=a*(math.sqrt(1 - e*e))*math.sin(E)

    r=math.sqrt(x*x+y*y)
    v=math.atan2(y, x)
    v=normalize(math.degrees(v))

    xeclip=r*(math.cos(math.radians(N))*math.cos(math.radians(v+w)) - math.sin(math.radians(N))*math.sin(math.radians(v+w))*math.cos(math.radians(i)))
    yeclip=r*(math.sin(math.radians(N))*math.cos(math.radians(v+w)) + math.cos(math.radians(N))*math.sin(math.radians(v+w))*math.cos(math.radians(i)))
    zeclip=r*math.sin(math.radians(v+w))*math.sin(math.radians(i)) 
    long2 = math.atan2( yeclip, xeclip )
    long2=normalize(math.degrees(long2))
    lat2 = math.atan2( zeclip, math.sqrt( xeclip*xeclip +yeclip*yeclip ) )
    lat2=math.degrees(lat2)
    return (xeclip,yeclip,zeclip, long2, lat2, r)


def sun2planet(xeclip, yeclip, zeclip, x, y, z):
    """
    Helper Function. From Hliocentric to Geocentric position
        
    Returns:
        tuple: geocentric view of object.
        
    """
    x_geoc=(x+xeclip)
    y_geoc=(y+yeclip)
    z_geoc=(z+zeclip)

    return rectangular2spherical(x_geoc, y_geoc, z_geoc)
#    t = ecliptic2equatorial(x_geoc, y_geoc, z_geoc, 23.4)
#    return rectangular2spherical(t[0],t[1],t[2])