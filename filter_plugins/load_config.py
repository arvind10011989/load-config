#
# (c) 2018 Red Hat, Inc.
#
# Copyright (c) 2017 Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re

from ansible.module_utils.six import string_types
from ansible.errors import AnsibleFilterError


INTERFACE_NAMES = {
    'Et': 'Ethernet',
    'Ma': 'Management',
    'Vl': 'Vlan',
    'Po': 'PortChannel'
}

def to_lines(value):
    if isinstance(value, (list, set, tuple)):
        return value
    elif isinstance(value, string_types):
        return value.split('\n')
    raise AnsibleFilterError('cannot convert value to lines')


def expand_interface_name(name):
    match = re.match('([a-zA-Z]*)', name)
    if match and match.group(1) in INTERFACE_NAMES:
        matched = match.group(1)
        name = name.replace(matched, INTERFACE_NAMES[matched])
    return name


class FilterModule(object):
    """Filters for working with output from network devices"""

    filter_map = {
        'expand_interface_name': expand_interface_name,
        'to_lines': to_lines
    }

    def filters(self):
        return self.filter_map
