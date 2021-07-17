# -*- coding: utf-8 -*-

from funcs import *

target_id = 'C/2019 F1'
obs_code = '474'
date = Time('2021-07-04 15:00:00') #Time needs to be in UT


JPL_astropy_tbl,my_track_rate_RA,my_track_rate_Dec = JPL_Querier(target_id,obs_code,date)
converted_track_rate_RA,converted_track_rate_Dec = rate_convertor(my_track_rate_RA,my_track_rate_Dec,'h','s')

print("TraRA: ",converted_track_rate_RA)
print("TraDec: ",converted_track_rate_Dec)