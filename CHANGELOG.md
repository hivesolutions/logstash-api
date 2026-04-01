# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

*

### Changed

*

### Fixed

*

## [0.2.4] - 2026-04-01

### Changed

* Use appier's built-in logger (`self.logger`) instead of module-level `logging` in `log_bulk` and `_flush_buffer`
* Removed unused module-level `logger` variable and `logging` import from `base.py`

## [0.2.3] - 2026-04-01

### Fixed

* Using pytest on CI deploy job

## [0.2.2] - 2026-04-01

### Fixed

* Issue with deploy CI

## [0.2.1] - 2026-04-01

### Changed

* New build process added to GitHub Actions for automated testing and deployment

## [0.2.0] - 2026-04-01

### Added

* Warning-level logging for failed `log_bulk` and `_flush_buffer` operations with message count and error details

## [0.1.1] - 2024-04-23

### Changed

* Code structure to be compliant with `black`
* Added `raise_e` param in the bulk dump of data
