%global debug_package %{nil}

%define prefix %{_bindir}

Summary: Conversion between markup formats
Name: pandoc
Version: 1.19.2.1
Release: 1
License: GPLv2+
Group: Text/Processing
URL: https://hackage.haskell.org/package/pandoc
Source0: source.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: gmp

%description
Pandoc is a Haskell library for converting from one markup format to another,
and a command-line tool that uses this library. It can read markdown and
(subsets of) HTML, reStructuredText, LaTeX, DocBook, MediaWiki markup, TWiki
markup, Haddock markup, OPML, Emacs Org-Mode, txt2tags and Textile, and it can
write markdown, reStructuredText, XHTML, HTML 5, LaTeX, ConTeXt, DocBook, OPML,
OpenDocument, ODT, Word docx, RTF, MediaWiki, DokuWiki, Textile, groff man
pages, plain text, Emacs Org-Mode, AsciiDoc, Haddock markup, EPUB (v2 and v3),
FictionBook2, InDesign ICML, and several kinds of HTML/javascript slide shows
(S5, Slidy, Slideous, DZSlides, reveal.js).

In contrast to most existing tools for converting Markdown to HTML, pandoc has
a modular design: it consists of a set of readers, which parse text in a given
format and produce a native representation of the document, and a set of
writers, which convert this native representation into a target format.
Thus, adding an input or output format requires only adding a reader or writer.

%prep
%setup -q -n bin

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}%{prefix}
cp ${RPM_BUILD_DIR}/bin/pandoc %{buildroot}%{prefix}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(-,root,root) %{prefix}/pandoc

%changelog
* Fri Jun  2 2017 Gábor Csárdi <csardi.gabor@gmail.com> - 1.19.2.1
- Upgrade version.
* Sun Oct 31 2016 Gábor Csárdi <csardi.gabor@gmail.com> - 1.18
- Initial build.
