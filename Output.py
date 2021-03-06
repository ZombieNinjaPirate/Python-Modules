"""
Copyright (c) 2014, Are Hansen - Honeypot Development.

All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted
provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions
and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions
and the following disclaimer in the documentation and/or other materials provided with the
distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND AN EXPRESS OR
IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER
IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF
THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""


__author__ = 'Are Hansen'
__date__ = '2014, July 25'
__version__ = '0.0.1'


import operator


def source(items, nol):
    """Formats and prints the results showing source IP stats. """
    banner = '   {0}   {1}'.format('Hits', 'IP address')
    header = '-' * 33
    stdout_list = []
    
    for key, value in sorted(items.iteritems(), key=operator.itemgetter(1), reverse=True):
        stdout_list.append('{0:>7}   {1}'.format(value, key))

    print '{0}\n{1}'.format(banner, header)

    for std in stdout_list[:nol]:
        print std
    print ''


def origin(items, nol):
    """Formats and prints the results showing country of origin. """
    banner = '   {0}   {1}'.format('Hits', 'Country of origin')
    header = '-' * 33
    stdout_list = []

    for key, value in sorted(items.iteritems(), key=operator.itemgetter(1), reverse=True):
        stdout_list.append('{0:>7}   {1}'.format(value, key))

    print '{0}\n{1}'.format(banner, header)

    for std in stdout_list[:nol]:
        print std
    print ''


def passwd(items, nol):
    """Formats and prints the results showing password frequency. """
    banner = '  {0}   {1}'.format('Tries', 'Password')
    header = '-' * 33
    stdout_list = []

    for key, value in sorted(items.iteritems(), key=operator.itemgetter(1), reverse=True):
        stdout_list.append('{0:>7}   {1}'.format(value, key))

    print '{0}\n{1}'.format(banner, header)

    for std in stdout_list[:nol]:
        print std
    print ''


def usrnames(items, nol):
    """Formats and prints the results showing username frequency. """
    banner = '  {0}   {1}'.format('Tries', 'Username')
    header = '-' * 33
    stdout_list = []

    for key, value in sorted(items.iteritems(), key=operator.itemgetter(1), reverse=True):
        stdout_list.append('{0:>7}   {1}'.format(value, key))

    print '{0}\n{1}'.format(banner, header)

    for std in stdout_list[:nol]:
        print std
    print ''


def combinations(items, nol):
    """Formats and prints the results showing user/password combination frequency. """
    banner = '  {0}   {1}'.format('Tries', 'Combinations')
    header = '-' * 33
    stdout_list = []

    for key, value in sorted(items.iteritems(), key=operator.itemgetter(1), reverse=True):
        stdout_list.append('{0:>7}   {1}'.format(value, key))

    print '{0}\n{1}'.format(banner, header)

    for std in stdout_list[:nol]:
        print std
    print ''
