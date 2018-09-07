# [Logstash API](http://logstash-api.hive.pt)

Simple Python API client for [Logstash](https://www.elastic.co/products/logstash).

## Configuration

* `LOSTASH_USERNAME` (`str`) - The secret token to be for authentication on the Logstash API (defaults to `None`)
* `LOSTASH_BUFFER_SIZE` (`int`) - The size of the buffer (in number of entries) until the buffer is flushed (defaults to `128`)
* `LOSTASH_TIMEOUT` (`int`) - The timeout in seconds in seconds until the buffer is flushed (defaults to `30`)

## License

Logstash API is currently licensed under the [Apache License, Version 2.0](http://www.apache.org/licenses/).

## Build Automation

[![Build Status](https://travis-ci.org/hivesolutions/logstash_api.svg?branch=master)](https://travis-ci.org/hivesolutions/logstash_api)
[![Coverage Status](https://coveralls.io/repos/hivesolutions/logstash_api/badge.svg?branch=master)](https://coveralls.io/r/hivesolutions/logstash_api?branch=master)
[![PyPi Status](https://img.shields.io/pypi/v/logstash_api.svg)](https://pypi.python.org/pypi/logstash_api)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/)
