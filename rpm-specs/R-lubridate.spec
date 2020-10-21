%global packname lubridate
%global packver  1.7.9
%global rlibdir  %{_libdir}/R/library

# knitr is not yet available.
%global with_doc  1

Name:             R-%{packname}
Version:          1.7.9
Release:          3%{?dist}
Summary:          Make dealing with dates a little easier

License:          GPLv2+ and ASL 2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-generics, R-Rcpp >= 0.12.13
# Suggests:  R-covr, R-knitr, R-testthat >= 2.1.0, R-vctrs >= 0.3.0
# LinkingTo:
# Enhances:

BuildRequires:    cctz-devel
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-generics
BuildRequires:    R-Rcpp-devel >= 0.12.13
BuildRequires:    R-testthat >= 2.1.0
BuildRequires:    R-vctrs >= 0.3.0
%if %{with_doc}
BuildRequires:    R-knitr
%endif

%description
Functions to work with date-times and time-spans: fast and user friendly
parsing of date-time data, extraction and updating of components of a date-time
(years, months, days, hours, minutes, and seconds), algebraic manipulation on
date-time and time-span objects. The 'lubridate' package has a consistent and
memorable syntax that makes working with dates easy and fun. Parts of the
'CCTZ' source code, released under the Apache 2.0 License, are included in this
package. See <https://github.com/google/cctz> for more details.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION

# Delete bundled cctz.
rm -r %{packname}/src/cctz
cat > %{packname}/src/Makevars << EOF
CXX_STD = CXX11
PKG_CPPFLAGS= -I. -I/usr/include/cctz
PKG_LIBS= -lcctz
EOF
sed -i '/time_zone_if/d' %{packname}/src/update.cpp


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# Used to update sources; don't need to package it.
rm %{buildroot}%{rlibdir}/%{packname}/cctz.sh


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
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/data
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/pkgdown


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.9-1
- Update to latest version

* Sat Jun  6 2020 Tom Callaway <spot@fedoraproject.org>  - 1.7.8-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.8-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.4-6
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.7.4-2
- rebuild for R 3.5.0

* Thu Apr 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.4-1
- Update to latest release

* Sun Mar 18 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.3-4
- Add missing Rcpp Requires.
- Make library name explicit.

* Sat Mar 17 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.3-3
- Unbundle cctz.

* Mon Mar 05 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.3-2
- Enable doc build.

* Sun Mar 04 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.3-1
- initial package for Fedora
