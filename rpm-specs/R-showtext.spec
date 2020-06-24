%global packname showtext
%global packver  0.8
%global packrel  1
%global rlibdir  %{_libdir}/R/library

# knitr suggests this package and vice versa.
%global with_doc 1

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          2%{?dist}
Summary:          Using Fonts More Easily in R Graphs

# Main: ASL 2.0
# src/tidy.h, src/utf8.c and src/utf8.h: libpng/zlib
License:          ASL 2.0 and zlib
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}-%{packrel}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-sysfonts >= 0.7.1, R-showtextdb >= 2.0
# Imports:   R-grDevices
# Suggests:  R-knitr, R-rmarkdown, R-prettydoc, R-curl, R-jsonlite
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    pkgconfig(freetype2)
BuildRequires:    pkgconfig(libpng)
BuildRequires:    pkgconfig(zlib)
BuildRequires:    R-sysfonts >= 0.7.1
BuildRequires:    R-showtextdb >= 2.0
BuildRequires:    R-grDevices
BuildRequires:    R-curl
BuildRequires:    R-jsonlite
%if %{with_doc}
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-prettydoc
%endif

%description
Making it easy to use various types of fonts (TrueType, OpenType, Type 1, web
fonts, etc.) in R graphs, and supporting most output formats of R graphics
including PNG, PDF and SVG. Text glyphs will be converted into polygons or
raster images, hence after the plot has been created, it no longer relies on
the font files. No external software such as Ghostscript is needed to use this
package.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_doc}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%doc %{rlibdir}/%{packname}/AUTHORS
%license %{rlibdir}/%{packname}/COPYRIGHTS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.8.1-2
- rebuild for R 4

* Sun May 31 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.1-1
- Update to latest version

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7-1
- Update to latest version

* Wed Feb 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 08 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.1-2
- Rebuild for R 3.5.0
- Fix license tagging
- Fix file line endings

* Thu May 31 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.1-1
- initial package for Fedora
