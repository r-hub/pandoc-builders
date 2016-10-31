
## Fedora 24

You can add our RPM repository and then install `pandoc` and `pandoc-citeproc` via `dnf`.

```sh
curl -o /etc/yum.repos.d/rhub-pandoc-fedora24.repo  \
  https://files.r-hub.io/pandoc/fedora24/rhub-pandoc-fedora24.repo
dnf install pandoc pandoc-citeproc
```
