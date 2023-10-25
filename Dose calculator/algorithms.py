from math import floor

def frieds_dose_pattern(child_age_in_months: int, dose_for_adults: int):

    result = (child_age_in_months * dose_for_adults) / 150
    return floor(result)

def cowlings_dose_pattern(child_age_in_years: int, dose_for_adult: int):
    result = (child_age_in_years * dose_for_adult) / 24
    return floor(result)

def youngs_dose_pattern(child_age_in_years: int, dose_for_adult: int):
    result = (child_age_in_years * dose_for_adult) / (child_age_in_years + 12)
    return floor(result)

def clarks_dose_pattern(child_mass_of_body: int, dose_for_adult: int):
    result = (child_mass_of_body * dose_for_adult) / 70
    return floor(result)

def skin_surface_dose_pattern(child_skin_surface: int, dose_for_adult: int):
    result = (child_skin_surface * dose_for_adult) / 1.8
    return floor(result)