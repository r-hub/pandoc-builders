
FROM fedora:24

RUN cd /root &&	                                  \
    curl -sSL https://get.haskellstack.org/ | sh

## Download pandoc-citeproc source code from a release.
## This will build both pandoc-citeproc and pandoc

RUN cd /root && \
    curl -LO https://hackage.haskell.org/package/pandoc-citeproc-0.10.2.2/pandoc-citeproc-0.10.2.2.tar.gz

## Setup stack. This will download and install a GHC compiler
## with the full set of tools needed.

RUN cd /root && \
    tar xzf pandoc-citeproc-0.10.2.2.tar.gz && \
    cd /root/pandoc-citeproc-0.10.2.2 && \
    stack setup

## Extra packages needed for the actual build

## Build the binaries. The result will be in /root/.local/bin,
## two files: pandoc and pandoc-citeproc
## These are shared binaries, but otherwise they are self-contained.

RUN dnf install -y git zlib-devel

RUN cd /root/pandoc-citeproc-0.10.2.2 && \
    stack install --flag pandoc:embed_data_files --flag pandoc-citeproc:embed_data_files

## Now we build RPM packages for both

RUN dnf install -y rpm-build &&                             \
    cd /root &&                                             \
    mkdir -p rpmbuild/{BUILD,RPMS,SPECS,SRPMS,SOURCES} &&   \
    cd .local &&                                            \
    tar czf /root/rpmbuild/SOURCES/source.tar.gz bin

ADD pandoc.spec /root/rpmbuild/SPECS/pandoc.spec
ADD pandoc-citeproc.spec /root/rpmbuild/SPECS/pandoc-citeproc.spec

RUN cd /root && rpmbuild --define "_topdir `pwd`/rpmbuild" -bb rpmbuild/SPECS/pandoc.spec
RUN cd /root && rpmbuild --define "_topdir `pwd`/rpmbuild" -bb rpmbuild/SPECS/pandoc-citeproc.spec

## Create a repository

RUN dnf install -y createrepo &&                 \
    cd /root &&                                  \
    mkdir fedora24 &&                            \
    cp rpmbuild/RPMS/x86_64/pandoc-* fedora24 && \
    createrepo fedora24

ADD rhub-pandoc-fedora24.repo /root/fedora24/rhub-pandoc-fedora24.repo
