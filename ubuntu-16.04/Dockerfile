
FROM ubuntu:16.04

## Install stack

RUN cd /root &&                                   \
    apt-get update &&                             \
    apt-get -y install curl &&                    \
    curl -sSL https://get.haskellstack.org/ | sh

## Download pandoc-citeproc source code from a release.
## This will build both pandoc-citeproc and pandoc

RUN curl -LO https://hackage.haskell.org/package/pandoc-citeproc-0.10.4.1/pandoc-citeproc-0.10.4.1.tar.gz

## Setup stack. This will download and install a GHC compiler
## with the full set of tools needed.

RUN tar xzf pandoc-citeproc-0.10.4.1.tar.gz && \
        cd pandoc-citeproc-0.10.4.1 && \
	                stack setup

## Extra packages needed for the actual build

## Build the binaries. The result will be in /root/.local/bin,
## two files: pandoc and pandoc-citeproc
## These are shared binaries, but otherwise they are self-contained.

RUN cd pandoc-citeproc-0.10.4.1 && \
        stack install --flag pandoc:embed_data_files --flag pandoc-citeproc:embed_data_files

## Now we build a Debian package for this

RUN apt-get -y install debhelper cdbs

RUN cd /root/.local && \
    mkdir pandoc-1.19.2.1 && \
    cp -r bin pandoc-1.19.2.1/ && \
    tar czf /root/pandoc_1.19.2.1.orig.tar.gz pandoc-1.19.2.1 && \
    mkdir pandoc-citeproc-0.10.4.1 && \
    cp -r bin pandoc-citeproc-0.10.4.1/ && \
    tar czf /root/pandoc-citeproc_0.10.4.1.orig.tar.gz pandoc-citeproc-0.10.4.1

ADD pandoc /root/pandoc
ADD pandoc-citeproc /root/pandoc-citeproc

RUN cd /root/pandoc && \
    tar xzf ../pandoc_1.19.2.1.orig.tar.gz && \
    mv pandoc-1.19.2.1/bin . && \
    dpkg-buildpackage

RUN cd /root/pandoc-citeproc && \
    tar xzf ../pandoc-citeproc_0.10.4.1.orig.tar.gz && \
    mv pandoc-citeproc-0.10.4.1/bin . && \
    dpkg-buildpackage

## Create repository

RUN cd /root &&                     \
    mkdir -p ubuntu-16.04/amd64 &&  \
    cp *.deb ubuntu-16.04/amd64 &&  \
    cd ubuntu-16.04 &&              \
    dpkg-scanpackages amd64 |       \
      gzip -9c > amd64/Packages.gz
