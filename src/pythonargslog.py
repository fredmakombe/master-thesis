#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
DESCRIPTION: Python template with an argument parser and logger. Put all the "main" logic into the method called "main".
             Only use the true "__main__" section to add script arguments. The logger writes to a hidden folder './log/'
             and uses the name of this file, followed by the date (by default). The argument parser comes with a default
             option --quiet to keep the stdout clean.

@copyright: Copyright 2018 Deutsches Forschungszentrum fuer Kuenstliche
            Intelligenz GmbH or its licensors, as applicable.

@author: YOU!
"""

import os
import sys
import time
import logging
import argparse
import traceback


def main(opts):
    """Main loop"""
    pass


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser_general_group = parser.add_argument_group('GENERAL', 'General Options')
    parser_specific_group = parser.add_argument_group('SPECIFIC', 'Specific Options')
    parser_general_group.add_argument('--quiet',
                                      action='store_true',
                                      help='Do not print to stdout (log only).')
    parser_specific_group.add_argument('-i',
                                       '--input',
                                       metavar='FILE',
                                       dest='infile',
                                       required=True,
                                       help='Input File')

    opts = parser.parse_args(sys.argv[1:])

    # Setup logging
    basename = os.path.basename(sys.argv[0]).split('.')[0]
    log_folder = '.log/%s' % time.strftime('%y-%m-%d')
    logfile = time.strftime('%Hh%Mm%Ss') + '-' + basename + '.log'
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    logging.basicConfig(format='%(asctime)s - %(filename)s:%(funcName)s %(levelname)s: %(message)s',
                        filename=os.path.join(log_folder, logfile),
                        level=logging.INFO)
    # # Manage the LOG and where to pipe it (log file only or log file + STDOUT)
    if not opts.quiet:
        fmtr = logging.Formatter(fmt='%(funcName)s %(levelname)s: %(message)s')
        stderr_handler = logging.StreamHandler()
        stderr_handler.formatter = fmtr
        logging.getLogger().addHandler(stderr_handler)
        logging.info('Printing activity to the console')
    logging.info('Running parameters: \n%s' % str(opts.__dict__))

    try:
        main(opts)
    except Exception as exp:
        if opts.quiet:
            print('Unhandled error: %s' % repr(exp))
        logging.error('Unhandled error: %s' % repr(exp))
        logging.error(traceback.format_exc())
        sys.exit(-1)
    finally:
        print('All Done (logged to %s).' % os.path.join(log_folder, logfile))
