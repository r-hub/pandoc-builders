
## Ubuntu 16.04

Add our repository to `apt`, and install as usual:

```sh
echo "deb https://files.r-hub.io/pandoc/ubuntu-16.04/ amd64/" > \
  /etc/apt/sources.list.d/rhub-pandoc-ubuntu-16.04.list
apt-get update
apt-get install pandoc pandoc-citeproc
```

Note that these packages are not signed currently, so `apt-get` will issue warnings.
