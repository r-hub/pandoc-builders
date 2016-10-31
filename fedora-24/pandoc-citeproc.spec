%global debug_package %{nil}

%define prefix %{_bindir}

Summary: Citeproc support for pandoc
Name: pandoc-citeproc
Version: 0.10.2.2
Release: 1
License: BSD
Group: Text/Processing
URL: https://hackage.haskell.org/package/pandoc-citeproc
Source0: source.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: gmp

%description
The pandoc-citeproc library exports functions for using the citeproc system
with pandoc. It relies on citeproc-hs, a library for rendering bibliographic
reference citations into a variety of styles using a macro language called
Citation Style Language (CSL). More details on CSL can be found here:
<http://citationstyles.org/>.

Currently this package includes a heavily revised copy of the citeproc-hs code.
When citeproc-hs is updated to be compatible, this package will simply depend
on citeproc-hs.

This package also contains an executable: pandoc-citeproc, which works as a
pandoc filter, and also has a mode for converting bibliographic databases a
YAML format suitable for inclusion in pandoc YAML metadata.

%prep
%setup -q -n bin

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}%{prefix}
cp ${RPM_BUILD_DIR}/bin/pandoc-citeproc %{buildroot}%{prefix}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root) %{prefix}/pandoc-citeproc

%changelog
* Sun Oct 31 2016 Gábor Csárdi <csardi.gabor@gmail.com> - 0.10.2.2
- Initial build.
