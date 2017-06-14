
## CentOS 7

You can add our RPM repository and then install `pandoc` and `pandoc-citeproc` via `yum`.

```sh
curl -o /etc/yum.repos.d/rhub-pandoc-centos7.repo  \
  https://files.r-hub.io/pandoc/centos7/rhub-pandoc-centos7.repo
yum install pandoc pandoc-citeproc
```
