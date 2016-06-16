'''''''''''''''''''''''''''''''''''''''''''''''''''''
// Authored by Christopher Iliffe Sprague          //
// Christopher.Iliffe.Sprague@gmail.com            //
// +1 703 851 6842                                 //
'''''''''''''''''''''''''''''''''''''''''''''''''''''

import numpy as np
import collections
import copy

grade_dict = (('Fall_2013'  , [[4.00, 3.00],    # Computer Science 1
                               [4.00, 3.33],    # Calc 2
                               [4.00, 3.33],    # Physics I Honours
                               [4.00, 3.67]]),  # Gen Psych
              ('Spring_2014', [[4.00, 4.00],    # IEA
                               [3.00, 2.33],    # Fund Flight
                               [4.00, 3.00],    # Diff Eq
                               [4.00, 3.67]]),  # Philosophy of Religion
              ('Summer_2014', [[4.00, 4.00],    # TF1
                               [4.00, 3.67]]),  # Strengths
              ('Fall_2014'  , [[4.00, 3.67],    # Processes
                               [4.00, 3.33],    # Dynamics
                               [3.00, 2.33],    # Aerostructures
                               [4.00, 3.33],    # Multivar
                               [4.00, 4.00]]),  # Social Psych
              ('Spring_2015', [[4.00, 2.67],    # Spacflight Mechanics
                               [3.00, 3.67],    # Aeroelasticity
                               [2.00, 3.33],    # Aerostructures Lab
                               [4.00, 2.33],    # Numb Comp
                               [4.00, 3.67]]),  # Org Psych
              ('Fall_2015'  , [[4.00, 3.00],    # Mod Con
                               [4.00, 4.00],    # Prop Sys
                               [3.00, 4.00],    # Boundary Layers
                               [3.00, 4.00],    # Space Vehicle Design
                               [5.00, 4.00]]),  # Spacecraft Study
              ('Spring_2016', [[3.00, 4.00],    # PIP
                               [1.00, 4.00],    # PD1
                               [3.00, 4.00],    # MAU
                               [1.00, 4.00],    # PD3
                               [2.00, 3.33],    # FDL
                               [3.00, 4.00],    # Astrodynamics
                               [2.00, 3.67]]),  # PD2
              ('Fall_2016'  , [            ]))

grade_dict         = collections.OrderedDict(grade_dict)
grade_dict_logical = copy.deepcopy(grade_dict)
# grade_dict_logical['Spring_2014'][1][1] = 2.33      # Fund Flight
# grade_dict_logical['Fall_2014'][2][1]   = 2.33      # Aerodynamics
# grade_dict_logical['Spring_2015'][0][1] = 2.67      # Spaceflight Mechanics
# grade_dict_logical['Spring_2015'][3][1] = 2.33      # Numb Comp
grade_dict_logical['Fall_2016'].append([3.00, 4.00])  # Independant Study
semesters = grade_dict.keys()


def Term_GPAs(grade_dict):
    '''Returns list of term GPAs per semester.'''
    term_gpas          = []
    for s in range(len(semesters)):
        data           = np.array(grade_dict[semesters[s]])
        quality_points = np.sum(data[:, 0] * data[:, 1])
        credit_hours   = np.sum(data[:, 0])
        term_gpa       = quality_points / credit_hours
        term_gpas.append(term_gpa)
    return term_gpas


def Cumulative_GPAs(grade_dict):
    '''Returns list of cumulative GPAs per semester.'''
    quality_points_sem = []
    credit_hours_sem   = []
    for s in range(len(semesters)):
        data           = np.array(grade_dict[semesters[s]])
        quality_points = np.sum(data[:, 0] * data[:, 1])
        credit_hours   = np.sum(data[:, 0])
        quality_points_sem.append(quality_points)
        credit_hours_sem.append(credit_hours)
    cumulative_qps     = []
    cumulative_ch      = []
    for s in range(len(semesters)):
        cumulative_qps.append(sum(quality_points_sem[:s + 1]))
        cumulative_ch.append(sum(credit_hours_sem[:s + 1]))
    return np.ndarray.tolist(np.array(cumulative_qps /
                                      np.array(cumulative_ch)))
print Term_GPAs(grade_dict_logical)
print Cumulative_GPAs(grade_dict_logical)
