Name:           GAPDoc
Version:        1.6.3
Release:        3%{?dist}
Summary:        GAP documentation tool

# The package is all GPLv2+ except for some of the mathml files
License:        GPLv2+ and MPLv1.1 and W3C
URL:            http://www.math.rwth-aachen.de/~Frank.Luebeck/%{name}/
Source0:        http://www.math.rwth-aachen.de/~Frank.Luebeck/%{name}/%{name}-%{version}.tar.bz2
BuildArch:      noarch

BuildRequires:  gap-devel
BuildRequires:  ghostscript
BuildRequires:  tex(color.sty)
BuildRequires:  tex(english.ldf)
BuildRequires:  tex(enumitem.sty)
BuildRequires:  tex(fancyvrb.sty)
BuildRequires:  tex(geometry.sty)
BuildRequires:  tex(pslatex.sty)
BuildRequires:  tex(psnfss.map)
BuildRequires:  tex(tex)
BuildRequires:  tex-cm-super
BuildRequires:  tex-ec
BuildRequires:  tex-helvetic
BuildRequires:  tex-latex-bin
BuildRequires:  tex-rsfs
BuildRequires:  tex-symbol
BuildRequires:  tex-times

Requires:       gap-core

Provides:       gap-pkg-gapdoc = %{version}-%{release}

%description
This package describes a document format for writing GAP documentation.

The idea is to define a sufficiently abstract markup language for GAP
documentation which can be (relatively easily) converted into different
output formats.  We used XML to define such a language.

This package provides:
- Utilities to use the documentation which is written in GAPDoc format
  with the GAP help system.  If you don't want to write your own
  (package) documentation you can skip to the last point of this list.
- The description of a markup language for GAP documentation (which is
  defined using the XML standard).
- Three example documents using this language: The GAPDoc documentation
  itself, a short example which demonstrates all constructs defined in
  the GAPDoc language, and a very short example explained in the
  introduction of the main documentation.
- A mechanism for distributing documentation among several files,
  including source code files.
- GAP programs (written by the first named author) which produce from
  documentation written in the GAPDoc language several document formats:
  * text format with color markup for onscreen browsing.
  * LaTeX format and from this PDF- (and DVI)-versions with hyperlinks.
  * HTML (XHTML 1.0 strict) format for reading with a Web-browser (and
    many hooks for CSS layout).
- Utility GAP programs which are used for the above but can be of
  independent interest as well:
  * Unicode strings with translations to and from other encodings
  * further utilities for manipulating strings
  * tools for dealing with BibTeX data
  * another data format BibXMLext for bibliographical data including
    tools to manipulate/translate them
  * a tool ComposedDocument for composing documents which are
    distributed in many files

%package latex
Summary:        All LaTeX dependencies for GAPDoc
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help
Requires:       ghostscript
Requires:       tex(color.sty)
Requires:       tex(english.ldf)
Requires:       tex(enumitem.sty)
Requires:       tex(fancyvrb.sty)
Requires:       tex(geometry.sty)
Requires:       tex(pslatex.sty)
Requires:       tex(psnfss.map)
Requires:       tex(tex)
Requires:       tex-cm-super
Requires:       tex-ec
Requires:       tex-helvetic
Requires:       tex-latex-bin
Requires:       tex-rsfs
Requires:       tex-symbol
Requires:       tex-times

# Needed to fetch BibTeX entries from MathSciNet
Suggests:       gap-pkg-io

%description latex
This package contains all of the LaTeX dependencies for GAPDoc.  GAP
proper requires that the GAP portions of GAPDoc be installed; it
refuses to start otherwise.  However, if GAPDoc is not actively used,
then dragging in all of the LaTeX dependencies is wasteful.  Install
this package to pull in all of the necessary LaTeX dependencies for
building GAP package documentation.

%package doc
Summary:        GAPDoc documentation
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for GAPDoc.

%prep
%autosetup

# Fix character encoding
iconv -f ISO8859-1 -t UTF-8 3k+1/3k+1.bib > 3k+1/3k+1.bib.utf8
touch -r 3k+1/3k+1.bib 3k+1/3k+1.bib.utf8
mv -f 3k+1/3k+1.bib.utf8 3k+1/3k+1.bib

%build
# Link to main GAP documentation
ln -s %{_gap_dir}/doc ../../doc
mkdir ../pkg
ln -s ../GAPDoc-%{version} ../pkg
gap -l "$PWD/..;%{_gap_dir}" < makedocrel.g
rm -fr ../../doc ../pkg

# Remove build paths
sed -i "s|$PWD/..|%{_gap_dir}|g" doc/*.html example/*.html

%install
mkdir -p %{buildroot}%{_gap_dir}/pkg
cp -a ../%{name}-%{version} %{buildroot}%{_gap_dir}/pkg/%{name}
rm -f %{buildroot}%{_gap_dir}/pkg/%{name}/{3k+1,doc,example}/clean
rm -f %{buildroot}%{_gap_dir}/pkg/%{name}/{3k+1,doc,example}/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr,tex}
rm -f %{buildroot}%{_gap_dir}/pkg/%{name}/{CHANGES,GPL,README.md}

%files
%doc CHANGES README.md
%license GPL
%{_gap_dir}/pkg/%{name}/
%exclude %{_gap_dir}/pkg/%{name}/3k+1/
%exclude %{_gap_dir}/pkg/%{name}/doc/
%exclude %{_gap_dir}/pkg/%{name}/example/

%files latex
# This is a metapackage to pull in dependencies only

%files doc
%docdir %{_gap_dir}/pkg/%{name}/3k+1/
%docdir %{_gap_dir}/pkg/%{name}/doc/
%docdir %{_gap_dir}/pkg/%{name}/example/
%{_gap_dir}/pkg/%{name}/3k+1/
%{_gap_dir}/pkg/%{name}/doc/
%{_gap_dir}/pkg/%{name}/example/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Jerry James <loganjerry@gmail.com> - 1.6.3-1
- New upstream version

* Fri Feb  1 2019 Jerry James <loganjerry@gmail.com> - 1.6.2-3
- Rebuild for GAP 4.10.0
- Change BRs and Rs due to recent TeXLive packaging changes
- Create -doc subpackage

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 1.6.2-1
- New upstream version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 1.6.1-4
- Require tex(pdftex.map) also so PostScript fonts can be generated

* Sat Mar 10 2018 Jerry James <loganjerry@gmail.com> - 1.6.1-3
- Require metafont as well to generate fonts as needed

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan  6 2018 Jerry James <loganjerry@gmail.com> - 1.6.1-1
- New upstream version

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Jerry James <loganjerry@gmail.com> - 1.6-1
- New upstream version

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Oct 18 2016 Jerry James <loganjerry@gmail.com> - 1.5.1-11
- Adjust dependencies for the latest texlive

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 1.5.1-10
- Rebuild for gap 4.8.3
- Split out LaTeX dependencies into a -latex subpackage

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 1.5.1-8
- Minimize LaTeX dependencies
- Drop scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 23 2015 Jerry James <loganjerry@gmail.com> - 1.5.1-6
- Fix scriptlets so they don't complain when uninstalling
- Use license macro

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Sep 25 2012 Jerry James <loganjerry@gmail.com> - 1.5.1-2
- Rebuild to fix _gap_dir expansion issue

* Thu Sep 13 2012 Jerry James <loganjerry@gmail.com> - 1.5.1-1
- New upstream version

* Mon Aug 20 2012 Jerry James <loganjerry@gmail.com> - 1.3-2
- Fix line endings in some mathml files

* Tue Jan 31 2012 Jerry James <loganjerry@gmail.com> - 1.3-1
- Initial RPM
