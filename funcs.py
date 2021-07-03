# -*- coding: utf-8 -*-

from astropy import units as u
from astropy.time import Time
from astroquery.jplhorizons import Horizons
from astropy.table import Table, Column, MaskedColumn

def JPL_Querier(target_id,obs_code,date):
    """
    Function to query JPL Horizons for target information.

    Parameters
    ----------
    target_id : str
        Target ID.

    obs_code : str
        Observatory code of format: '123'.

    date : Time
        Time object of format: Time('yyyy-mm-dd hh:mm:ss'), where time is in UT.

    Returns
    -------
    track_rate_RA : float64
        Tracking rate for RA, in units of ARCSEC*HR.

    track_rate_Dec : float64
        Tracking rate for Dec, in units of ARCSEC*HR.

    """
    epoch_jd = date.jd  # convert Time object to Julian Date
    obj = Horizons(id=target_id,location=obs_code,epochs=epoch_jd)
    eph = obj.ephemerides()
    JPLtableData = eph['datetime_str','RA','DEC','Tmag','RA_rate','DEC_rate','r']
    JPL_colnames = ['datetime_str','RA','DEC','Tmag','RA_rate','DEC_rate','r']
    JPL_astropy_tbl = Table(JPLtableData,names=JPL_colnames)
    track_rate_RA = eph['RA_rate']
    track_rate_Dec = eph['DEC_rate']
    print("Apparent Mag: ",eph['Tmag'][0])
    return JPL_astropy_tbl,track_rate_RA,track_rate_Dec

def rate_convertor(track_rate_RA,track_rate_Dec,input_unit,unit_to_convert_to):
    """
    Function to convert ARCSEC/input_unit to ARCSEC/unit_to_convert_to.

    Parameters
    ----------
    track_rate_RA : float64
        Tracking rate for RA, in units of ARCSEC*HR.

    track_rate_Dec : float64
        Tracking rate for Dec, in units of ARCSEC*HR.

    input_unit : str
        Input unit. Options include 'h','m','s'.

    unit_to_convert_to : str
        Unit to convert to. Options include 'h','m','s'.

    Returns
    -------
    track_rate_RA : float64
        Tracking rate for RA, in units of ARCSEC*HR.

    track_rate_Dec : float64
        Tracking rate for Dec, in units of ARCSEC*HR.

    """
    if unit_to_convert_to == 'h':
        if input_unit == 'm':
            converted_track_rate_RA = track_rate_RA/60
            converted_track_rate_Dec = track_rate_Dec/60
        if input_unit == 's':
            converted_track_rate_RA = track_rate_RA/3600
            converted_track_rate_Dec = track_rate_Dec/3600
    if unit_to_convert_to == 'm':
        if input_unit == 'h':
            converted_track_rate_RA = track_rate_RA*60
            converted_track_rate_Dec = track_rate_Dec*60
        if input_unit == 's':
            converted_track_rate_RA = track_rate_RA/60
            converted_track_rate_Dec = track_rate_Dec/60
    if unit_to_convert_to == 's':
        if input_unit == 'h':
            converted_track_rate_RA = track_rate_RA/3600
            converted_track_rate_Dec = track_rate_Dec/3600
        if input_unit == 'm':
            converted_track_rate_RA = track_rate_RA/60
            converted_track_rate_Dec = track_rate_Dec/60
    converted_track_rate_RA_rounded = round(converted_track_rate_RA[0],4)
    converted_track_rate_Dec_rounded = round(converted_track_rate_Dec[0],4)
    return converted_track_rate_RA_rounded,converted_track_rate_Dec_rounded