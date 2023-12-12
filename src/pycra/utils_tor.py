#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re

def to_Hz(unit_str):
    """
    conversion: string indication about unit (e.g. MHz) --> float (e.g. 1e6)
    """

    assert isinstance(unit_str, str)

    scaling = float('nan')
    if unit_str == 'MHz':
        scaling = 1e6
    elif unit_str == 'GHz':
        scaling = 1e9
    else:
        print('Unit conversion is not implemented for given string: %s' % unit_str)
        raise

    return scaling

def read_frequencies(dict_graspobj, prefix='single_'):
    """
    Read frequency values as given in .tor file
    """
    
    freqstr = dict_graspobj[prefix+'frequencies']['frequency_list']
    freqsformat = 'sequence\((.*)\)'
    mm = re.search(freqsformat, freqstr)
    if not mm:
        print('Failed to read frequencies! Not in following regex format: %s' % freqsformat)
        raise
    else: 
        floatchars = '(\-?[0-9\.]+)\s([a-zA-Z]+)'
        freqs_units = re.findall(floatchars, mm.groups()[0])
        freqs = [float(freq) for freq,_ in freqs_units]
        units = [unit for _,unit in freqs_units]

        try:
            freqs = [freq*to_Hz(unit) for freq,unit in zip(freqs, units)]
            units = ['Hz']*len(units)
        except Exception as ee:
            print('Failed frequency conversion to Herz!')

    return freqs, units

def read_tor(filepath):
    """
    Read objects from .tor file into a dictionary for further processing.

    Idea (terms: GRASP manual description of the 'objects window'):
        dict_graspobj = {object_name: {'object_class': categorizing_name, attribute1: values, ...}, ...}

    Example:
        dict_grasoobj = {'single_frequencies': {'object_class': 'frequency', 'frequency_list': 'sequence(11.0 GHz,12.0 GHz)'}, ...}

    """

    # non-empty lines between arenthesis start with indent line: '  frequency_list   : '
    attribute_chars = ' '*2 + '([^\s]*)\s+:\s(.*)'
    
    # read the file
    with open(filepath) as f:
        lines = f.readlines()
    
    # drop tailing spaces and return characters. Identify related rows.
    lines = [line.rstrip() for line in lines]
    lines = [line for line in lines if line] # drop empty lines (needed?)
    sidx = [ii for ii,line in enumerate(lines) if line=='(']
    eidx = [ii for ii,line in enumerate(lines) if line==')']
    assert len(sidx) == len(eidx) # or some more advanced testing...

    # dynamically create dictionary of dictionaries
    dict_graspobj = {}
    for ii,jj in zip(sidx, eidx):
        # initialize dictionary for each object and store categorizing name
        objname, objclass = lines[ii-1].split()
        dict_graspobj[objname] = {'object_class': objclass}
        for idx in range(ii+1,jj):
            # search and store attributes and corresponding values
            mm = re.search(attribute_chars, lines[idx])
            add_to_previous = False
            if not mm:
                add_to_previous = True
            elif len(mm.groups()) != 2:
                add_to_previous = True
            else:
                attr = mm.groups()[0]
                specs = mm.groups()[1]
                dict_graspobj[objname][attr] = specs
            if add_to_previous:
                try:
                    dict_graspobj[objname][attr] += lines[idx]
                except Exception as ee:
                    print(repr('Problem in line %s: %s' % (idx, lines[idx])))

    return dict_graspobj