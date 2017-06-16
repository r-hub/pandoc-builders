
FROM alpine:3.6

## Required packages

RUN apk update
RUN apk add linux-headers zlib-dev libc-dev gcc curl ghc

## stack

RUN curl -sSL https://get.haskellstack.org/ | sh
RUN stack config set system-ghc --global true

## Get the files

RUN curl -LO https://hackage.haskell.org/package/pandoc-1.19.2.1/pandoc-1.19.2.1.tar.gz
RUN curl -LO https://hackage.haskell.org/package/pandoc-citeproc-0.10.4/pandoc-citeproc-0.10.4.tar.gz

## pandoc first

RUN tar xzf pandoc-1.19.2.1.tar.gz && \
    cd pandoc-1.19.2.1 && \
    cat stack.yaml | sed 's/^resolver: lts-[0-9][0-9]*\.[0-9][0-9]*/resolver: lts-8.12/' > stack.yaml2 && \
    mv stack.yaml2 stack.yaml && \
    stack setup && \
    stack install --flag pandoc:embed_data_files --ghc-options='-optl-static -optl-pthread'

## pandoc-citeproc next

RUN tar xzf pandoc-citeproc-0.10.4.tar.gz && \
    cd pandoc-citeproc-0.10.4 && \
    cat stack.yaml | sed 's/^- pandoc-1.19.1/- pandoc-1.19.2.1/' | \
    sed 's/^resolver: lts-7.14/resolver: lts-8.12/' > stack.yaml2 && \
    mv stack.yaml2 stack.yaml && \
    stack setup && \
    stack install --flag pandoc-citeproc:embed_data_files --ghc-options='-optl-static -optl-pthread'

RUN mv ~/.local/bin/pandoc* ~
