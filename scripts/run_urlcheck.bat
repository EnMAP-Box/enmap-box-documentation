:: see https://github.com/urlstechie/urlchecker-python
:: install with pip install urlchecker

urlchecker check --no-print --file-types .md,.py,.rst --exclude-patterns https://enmap-box.readthedocs.io/en/latest/general/glossary.html,https://tiles.wmflabs.org,https://fbinter.stadt-berlin.de/fb/wfs --exclude-files /scripts/create_external_link_file.py,/source/dev_section/external_links.rst --retry-count 3 --timeout 5