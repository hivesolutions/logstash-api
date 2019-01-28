#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Logstash API
# Copyright (c) 2008-2019 Hive Solutions Lda.
#
# This file is part of Hive Logstash API.
#
# Hive Logstash API is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Logstash API is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Logstash API. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2019 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

from . import base

class LogstashApp(appier.WebApp):

    def __init__(self, *args, **kwargs):
        appier.WebApp.__init__(
            self,
            name = "logstash",
            *args, **kwargs
        )

    @appier.route("/", "GET")
    def index(self):
        return self.log("hello")

    @appier.route("/log/<str:message>", "GET")
    def log(self, message):
        tag = self.field("tag", "default")
        api = self.get_api()
        result = api.log(dict(message = message), tag = tag)
        return result

    @appier.route("/log_bulk", "GET")
    def log_bulk(self):
        messages = self.field("messages", ["hello", "world"], cast = list)
        tag = self.field("tag", "default")
        api = self.get_api()
        messages_l = [dict(message = message) for message in messages]
        result = api.log_bulk(messages_l, tag = tag)
        return result

    def get_api(self):
        return base.get_api()

if __name__ == "__main__":
    app = LogstashApp()
    app.serve()
else:
    __path__ = []
