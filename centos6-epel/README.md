
## CentOS 6

You can add our RPM repository and then install `pandoc` and `pandoc-citeproc` via `yum`.

```sh
curl -o /etc/yum.repos.d/rhub-pandoc-centos6.repo  \
  https://files.r-hub.io/pandoc/centos6/rhub-pandoc-centos6.repo
yum install pandoc pandoc-citeproc
```
