
# Pandoc builders

> Build recent Pandoc packages for Linux distributions

## Distribution packages

Dockerized builds for `pandoc` and `pandoc-citeproc`. Please see the README in the directory of your distribution. Currently supported distributions:
* CentOS 7 (`pandoc` 1.19.2.1 and `pandoc-citeproc` 0.10.4)
* CentOS 6 (`pandoc` 1.19.2.1 and `pandoc-citeproc` 0.10.4)
* Fedora 24 (`pandoc` 1.19.2.1 and `pandoc-citeproc` 0.10.4)
* Ubuntu 16.04 (`pandoc` 1.19.2.1 and `pandoc-citeproc` 0.10.4)
* Ubuntu 14.04 (`pandoc` 1.19.2.1 and `pandoc-citeproc` 0.10.4)
* Ubuntu 12.04 (`pandoc` 1.19.2.1 and `pandoc-citeproc` 0.10.4)
* OpenSUSE Tumbleweed (`pandoc` 1.19.2.1 and `pandoc-citeproc` 0.10.4)

All `pandoc` and `pandoc-citeproc` binaries are self-contained, and have minimal dependencies (typically only `libgmp`).

## Static binaries

The `Dockerfile` in the `linux-64-static` directory builds
static `pandoc` and `pandoc-citeproc` binaries. These are
appropriate for any 64 bit Linux installation. You can also
download them from https://files.r-hub.io/pandoc/linux-64

## License

MIT @ R Consortium
