#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DESCRIPTION: template for doing meta-parameter exploration with sacred using random sampling. You need to have a file
             with a sacred experiment already defined, together with all the parameters needed to run it.

             This script receives as only parameter, the number of runs. For each run, it samples randomly from an
             interval and updates the parameters (previously defined in the script that contains the experiment)
             accordingly, before running it. For this template, we use the base sacred experiment defined in
             'pythonexp.py' which contains only one parameter, namely 'params.misc.foo'. We update it with the string
             'bar#' where # is a randomly sampled number between 128 and 256.

@copyright: Copyright 2018 Deutsches Forschungszentrum fuer Kuenstliche
            Intelligenz GmbH or its licensors, as applicable.

@author: YOU!
"""

import sys
import numpy as np
from pythonexp import exp
from argparse import ArgumentParser


def param_search(runs):
    for run in range(runs):
        # Sample numbers between [128,256]. For learning rates, use 10**np.random.uniform(-3, -5) for example.
        updates = {'params': {
                       'misc': {
                           'foo': 'bar%d' % np.round(2**np.random.uniform(7, 8), decimals=0).astype('int')}}}

        print('### EXP %03d ###' % run)
        print(updates)
        _ = exp.run(config_updates=updates)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--runs', type=int, default=10, help='How many runs to sample parameters for.')
    opts = parser.parse_args(sys.argv[1:])

    param_search(opts.runs)
    print 'All Done!'
