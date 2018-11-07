#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DESCRIPTION: template for a Sacred Experiment. Any parameters that need to be passed to the experiment itself, can be
             specified as an attribute of the 'config()' method. We suggest to use a single dictionary where each key
             corresponds to the name of the parameters and the value, well, the value of that parameter. You can nest
             all you want in case you need a richer hierarchy of arguments and they will be accessible from the outside
             if you need to call the script with different parameters along the road. Check the documentation of sacred
             in https://sacred.readthedocs.io.

             Make sure the EXP_FOLDER points to a valid folder (right now it points to ./exp/ but if this script goes
             into a subfolder (like ./src/models/) you need to adjust the path accordingly.

             The main point of entry is the 'run()' method in this case. Put your main logic there. Notice that it
             receives only one argument, namely 'params' which coincides with the name of the attribute defined in the
             'config()' method.

             HACK: for very special cases, you may need to access the ID of the experiment that it is currently running.
             Sacred doesn't officially expose this and instead, it recommends using 'artifacts' to copy files that have
             been created to the log folder. If you absolutely need this, you can get it via 'exp.current_run._id'.

@copyright: Copyright 2018 Deutsches Forschungszentrum fuer Kuenstliche
            Intelligenz GmbH or its licensors, as applicable.

@author: YOU!
"""

import os
import sys

from sacred import Experiment
from sacred.observers import file_storage

exp = Experiment('Main Experiment')
# Add a FileObserver if one hasn't been attached already
EXP_FOLDER = '../exp/'
log_location = os.path.join(EXP_FOLDER, os.path.basename(sys.argv[0])[:-3])
if len(exp.observers) == 0:
    print('Adding a file observer in %s' % log_location)
    exp.observers.append(file_storage.FileStorageObserver.create(log_location))


@exp.config
def config():
    """
    Put all your experiment's meta parameters here. Try to use python primitives, hashable functions and dictionaries
    as much as possible. This way, you can setup those parameters from the command line more easily.
    :return: None
    """
    # Define all the parameters as dictionaries inside the main 'params' dictionary. This way, the interface of the
    # main method, doesn't need to change every-time you add a new group.
    params = {}
    # Add as many groups as you need and name them whatever makes more sense to you.
    params['misc'] = {'foo': 'bar'}


@exp.automain
def run(params):
    """
    Experiment's entry point. All dictionaries in the config() method are accesible by name.
    :param params: Members defined inside the config() method.
    :return: None or int or just up to you.
    """
    misc = params['misc']
    print(misc['foo'])  # gets the string 'bar' as defined in 'config()'
