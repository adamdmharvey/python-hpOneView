# -*- coding: utf-8 -*-
###
# (C) Copyright (2012-2016) Hewlett Packard Enterprise Development LP
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
###

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()

__title__ = 'fc-networks'
__version__ = '0.0.1'
__copyright__ = '(C) Copyright (2012-2016) Hewlett Packard Enterprise ' \
                ' Development LP'
__license__ = 'MIT'
__status__ = 'Development'

from hpOneView.common import get_members
from hpOneView.activity import activity
from hpOneView.exceptions import HPOneViewUnknownType


class ResourceClient(object):
    """
    This class implements common functions for HpOneView API rest
    """

    def __init__(self, con, uri):
        self._connection = con
        self._uri = uri
        self._activity = activity(con)

    def get_members(self, uri):
        # TODO: common is deprecated, refactor get_members implementation
        return get_members(self._connection.get(uri))

    def get_all(self, start=0, count=9999999, filter='', query='', sort='', view=''):
        """
        the use of optional parameters are described here:
        http://h17007.www1.hpe.com/docs/enterprise/servers/oneview2.0/cic-api/en/api-docs/current/index.html

        Returns: a dictionary with requested data

        """
        if filter:
            filter = "&filter=" + filter

        if query:
            query = "&query=" + query

        if sort:
            sort = "&sort=" + sort

        if view:
            view = "&view=" + view

        uri = "{0}?start={1}&count={2}{3}{4}{5}{6}".format(self._uri, start, count, filter, query, sort, view)
        return self.get_members(uri)

    def delete(self, obj, force=False, blocking=True, verbose=False, timeout=60):
        if isinstance(obj, dict):
            if 'uri' in obj and obj['uri']:
                uri = obj['uri']
            else:
                raise HPOneViewUnknownType('Unknown object type')
        else:
            uri = self._uri + "/" + obj

        if force:
            uri += '?force=True'

        task, body = self._connection.delete(uri)
        if blocking:
            task = self._activity.wait4task(task, tout=timeout, verbose=verbose)

        return task

    def get_schema(self):
        return self._connection.get(self._uri + '/schema')

    def get(self, id):
        return self._connection.get(self._uri + '/' + id)

    def update(self, id, dict, blocking=True, verbose=False, timeout=60):
        # TODO: Create uri suffix
        # TODO: Verify extract uri from dict
        task, body = self._connection.put(self._uri + '/' + id, dict)
        if blocking:
            task = self._activity.wait4task(task, tout=timeout, verbose=verbose)
        return task

    def create(self, options, blocking=True, verbose=False):
        self._connection.post(self._uri, options)
        task, entity = self._activity.make_task_entity_tuple(self._connection)

        if blocking:
            self._activity.wait4task(task, verbose=verbose)

        return entity