def utm_to_lat_lon(zone, easting, northing, northernHemisphere= True):
    if easting == None or northing == None:
        latitude = 0.0
        longitude = 0.0
    else:
        zone = int(zone)
        easting = float(easting)
        northing = float(northing)

        if not northernHemisphere:
            northing = 10000000 - northing

        a = 6378137
        e = 0.081819191
        e1sq = 0.006739497
        k0 = 0.9996

        arc = northing / k0
        mu = arc / (a * (1 - np.power(e, 2) / 4.0 - 3 * np.power(e, 4) / 64.0 - 5 * np.power(e, 6) / 256.0))

        ei = (1 - np.power((1 - e * e), (1 / 2.0))) / (1 + np.power((1 - e * e), (1 / 2.0)))

        ca = 3 * ei / 2 - 27 * np.power(ei, 3) / 32.0

        cb = 21 * np.power(ei, 2) / 16 - 55 * np.power(ei, 4) / 32
        cc = 151 * np.power(ei, 3) / 96
        cd = 1097 * np.power(ei, 4) / 512
        phi1 = mu + ca * np.sin(2 * mu) + cb * np.sin(4 * mu) + cc * np.sin(6 * mu) + cd * np.sin(8 * mu)

        n0 = a / np.power((1 - np.power((e * np.sin(phi1)), 2)), (1 / 2.0))

        r0 = a * (1 - e * e) / np.power((1 - np.power((e * np.sin(phi1)), 2)), (3 / 2.0))
        fact1 = n0 * np.tan(phi1) / r0

        _a1 = 500000 - easting
        dd0 = _a1 / (n0 * k0)
        fact2 = dd0 * dd0 / 2

        t0 = np.power(np.tan(phi1), 2)
        Q0 = e1sq * np.power(np.cos(phi1), 2)
        fact3 = (5 + 3 * t0 + 10 * Q0 - 4 * Q0 * Q0 - 9 * e1sq) * np.power(dd0, 4) / 24

        fact4 = (61 + 90 * t0 + 298 * Q0 + 45 * t0 * t0 - 252 * e1sq - 3 * Q0 * Q0) * np.power(dd0, 6) / 720

        lof1 = _a1 / (n0 * k0)
        lof2 = (1 + 2 * t0 + Q0) * np.power(dd0, 3) / 6.0
        lof3 = (5 - 2 * Q0 + 28 * t0 - 3 * np.power(Q0, 2) + 8 * e1sq + 24 * np.power(t0, 2)) * np.power(dd0, 5) / 120
        _a2 = (lof1 - lof2 + lof3) / np.cos(phi1)
        _a3 = _a2 * 180 / np.pi

        latitude = str(180 * (phi1 - fact1 * (fact2 + fact3 + fact4)) / np.pi)

        if not northernHemisphere:
            latitude = -latitude

        longitude = str(((zone > 0) and (6 * zone - 183.0) or 3.0) - _a3)

    return latitude, longitude
