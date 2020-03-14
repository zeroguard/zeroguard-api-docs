#!/usr/bin/env python
"""Watch Sphinx documentation source code, rebuild and re-host on change.

WARNING: This is a development only server. By no means it should be used in
production. As of 2020-03-14 documentation is planned to be hosted on
ReadTheDocs. Check Makefile for relevant targets.
"""
import logging
import os
import re
import sys

from livereload import Server, shell

MAKEFILE_PATH = './Makefile'

DOCKER_PORT_RE = re.compile(r'.+-p\s\d+:(\d+).*')
SPHINX_SOURCE_DIR_RE = re.compile(r'^SPHINX_SOURCE_DIR\s:?=\s(.+)')
SPHINX_BUILD_DIR_RE = re.compile(
    r'^SPHINX_BUILD_DIR\s:?=\s\$\(SPHINX_SOURCE_DIR\)/(.+)'
)


# pylama: ignore=I901:
def parse_out_config(file_path, logger):
    """Parse out a port number on which to listen."""
    config = {
        'port': None,
        'sphinx_source_dir': None,
        'sphinx_build_dir': None
    }

    with open(file_path) as mkfile:
        for line_number, line in enumerate(mkfile):
            if all(config.values()):
                break

            if not config['port']:
                port = DOCKER_PORT_RE.match(line)

                if not port:
                    continue

                try:
                    port = int(port[1])
                    config['port'] = port

                except ValueError as err:
                    logger.warning((
                        'Failed to convert a port number parsed out from '
                        'Makefile to an integer: port_number="%s", '
                        'file_path="%s", line_number="%s", error="%s"'
                    ), port, file_path, line_number, err)

            if not config['sphinx_source_dir']:
                sphinx_source_dir = SPHINX_SOURCE_DIR_RE.match(line)

                if sphinx_source_dir:
                    config['sphinx_source_dir'] = sphinx_source_dir[1]

            if not config['sphinx_build_dir']:
                sphinx_build_dir = SPHINX_BUILD_DIR_RE.match(line)

                if sphinx_build_dir:
                    config['sphinx_build_dir'] = sphinx_build_dir[1]

    config['sphinx_build_dir'] = os.path.join(
        config['sphinx_source_dir'],
        config['sphinx_build_dir']
    )

    return config


def main():
    """Run a development server that will watch Sphinx source code."""
    # Initialize a logger
    logger = logging.getLogger(os.path.basename(sys.argv[0]))

    # Get run configuration from a Makefile
    config = parse_out_config(MAKEFILE_PATH, logger)
    port, sphinx_source_dir, sphinx_build_dir = (
        config['port'],
        config['sphinx_source_dir'],
        config['sphinx_build_dir']
    )

    if not all(config.values()):
        logger.error((
            'Parsed out configuration from Makefile: port="%s", '
            'sphinx_source_dir="%s", sphinx_build_dir="%s"'
        ), port, sphinx_source_dir, sphinx_build_dir)

        sys.exit(1)

    logger.info((
        'Parsed out configuration from Makefile: port="%s", '
        'sphinx_source_dir="%s", sphinx_build_dir="%s"'
    ), port, sphinx_source_dir, sphinx_build_dir)

    # Initialize livereload server and watch Sphinx documentation changes
    server = Server()

    server.watch(
        os.path.join(sphinx_source_dir, '*.rst'),
        shell('make docs')
    )

    server.serve(
        host='0.0.0.0',
        port=port,
        root=sphinx_build_dir
    )


if __name__ == '__main__':
    main()
