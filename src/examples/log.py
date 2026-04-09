#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Logstash API
# Copyright (c) 2008-2024 Hive Solutions Lda.
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

__copyright__ = "Copyright (c) 2008-2024 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import logstash


def main():
    api = logstash.API()

    api.logger.trace("This is a trace message")
    api.logger.debug("This is a debug message")
    api.logger.info("This is an info message")
    api.logger.warning("This is a warning message")
    api.logger.error("This is an error message")

    api.logger.info("Logger name: %s", api.logger.name)
    api.logger.info("Logger level: %s", api.logger.level)
    api.logger.info("Logger handlers: %s", api.logger.handlers)

    api.log({})


if __name__ == "__main__":
    main()
else:
    __path__ = []
