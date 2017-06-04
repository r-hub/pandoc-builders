
FROM ubuntu:14.04

## Install stack

RUN cd /root &&                                   \
    apt-get update &&                             \
    apt-get -y install curl &&                    \
    curl -sSL https://get.haskellstack.org/ | sh

## Download pandoc-citeproc source code from a release.

RUN curl -LO https://hackage.haskell.org/package/pandoc-citeproc-0.10.4/pandoc-citeproc-0.10.4.tar.gz

## Setup stack. This will download and install a GHC compiler
## with the full set of tools needed.

RUN tar xzf pandoc-citeproc-0.10.4.tar.gz

## Need to run a newer plan, to avoid a tls bug that was fixed
## in version 1.3.10.

RUN apt-get -y install sed

RUN cd pandoc-citeproc-0.10.4 && \
    cat stack.yaml | sed 's/^- pandoc-1.19.1/- pandoc-1.19.2.1/' | \
    sed 's/^resolver: lts-7.14/resolver: lts-8.12/' > stack.yaml2 && \
    mv stack.yaml2 stack.yaml

## Extra packages needed for the actual build

## Build the binaries. The result will be in /root/.local/bin,
## two files: pandoc and pandoc-citeproc
## These are shared binaries, but otherwise they are self-contained.

RUN cd pandoc-citeproc-0.10.4 && \
    stack setup && \
    stack install --flag pandoc-citeproc:embed_data_files

## Do the same for pandoc itself

RUN curl -LO https://hackage.haskell.org/package/pandoc-1.19.2.1/pandoc-1.19.2.1.tar.gz && \
    tar xzf pandoc-1.19.2.1.tar.gz && \
    cd pandoc-1.19.2.1 && \
    cat stack.yaml | sed 's/^resolver: lts-[0-9][0-9]*\.[0-9][0-9]*/resolver: lts-8.12/' > stack.yaml2 && \
    mv stack.yaml2 stack.yaml && \
    stack setup && \
    stack install --flag pandoc:embed_data_files

## Now we build a Debian package for this

RUN apt-get -y install debhelper cdbs

RUN cd /root/.local && \
    mkdir pandoc-1.19.2.1 && \
    cp -r bin pandoc-1.19.2.1/ && \
    tar czf /root/pandoc_1.19.2.1.orig.tar.gz pandoc-1.19.2.1 && \
    mkdir pandoc-citeproc-0.10.4 && \
    cp -r bin pandoc-citeproc-0.10.4/ && \
    tar czf /root/pandoc-citeproc_0.10.4.orig.tar.gz pandoc-citeproc-0.10.4

ADD pandoc /root/pandoc
ADD pandoc-citeproc /root/pandoc-citeproc

RUN cd /root/pandoc && \
    tar xzf ../pandoc_1.19.2.1.orig.tar.gz && \
    mv pandoc-1.19.2.1/bin . && \
    dpkg-buildpackage

RUN cd /root/pandoc-citeproc && \
    tar xzf ../pandoc-citeproc_0.10.4.orig.tar.gz && \
    mv pandoc-citeproc-0.10.4/bin . && \
    dpkg-buildpackage

## Create repository

RUN cd /root &&                     \
    mkdir -p ubuntu-14.04/amd64 &&  \
    cp *.deb ubuntu-14.04/amd64 &&  \
    cd ubuntu-14.04 &&              \
    dpkg-scanpackages amd64 |       \
      gzip -9c > amd64/Packages.gz
