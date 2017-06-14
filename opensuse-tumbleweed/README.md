
## OpenSUSE Tumbleweed

You can add our RPM repository and then install `pandoc` and
`pandoc-citeproc` via `zypper`.

```sh
zypper addrepo \
  https://files.r-hub.io/pandoc/opensuse-tumbleweed/rhub-pandoc-opensuse-tumbleweed.repo
zypper install pandoc pandoc-citeproc
```
