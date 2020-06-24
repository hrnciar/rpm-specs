%global packname  units
%global packvers  0.6-6
%global rlibdir   %{_libdir}/R/library

%global __suggests_exclude ^R\\((ggforce)\\)

Name:             R-%{packname}
Version:          0.6.6
Release:          2%{?dist}
Summary:          Measurement Units for R Vectors

License:          GPLv2
URL:              https://cran.r-project.org/package=%{packname}
Source0:          %{url}&version=%{packvers}#/%{packname}_%{packvers}.tar.gz

BuildRequires:    R-devel >= 3.0.0
BuildRequires:    R-Rcpp-devel udunits2-devel R-testthat
# BuildRequires:  R-udunits2 R-NISTunits R-measurements
# BuildRequires:  R-tibble R-pillar R-ggforce R-magrittr
# BuildRequires:  R-knitr R-rmarkdown
Recommends:       R-xml2
Obsoletes:        R-units-devel < 0.6.3

%description
Support for measurement units in R vectors, matrices and arrays: automatic
propagation, conversion, derivation and simplification of units; raising
errors in case of unit incompatibility. Compatible with the POSIXct, Date
and difftime classes. Uses the UNIDATA udunits library and unit database
for unit compatibility checking and conversion.
Documentation about 'units' is provided in the paper by Pebesma, Mailund
& Hiebert (2016, <doi:10.32614/RJ-2016-061>), included in this package as
a vignette; see 'citation("units")' for details.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
export LANG=C.UTF-8
export _R_CHECK_FORCE_SUGGESTS_=0
%{_bindir}/R CMD check --ignore-vignettes %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/share

%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.6.6-2
- rebuild for R 4

* Fri Mar 20 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.6-1
- Update to 0.6-6

* Thu Feb 06 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.5-3
- Resubmitted due to s390x failure in Mass Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 07 2020 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.5-1
- Update to 0.6-5

* Thu Aug 22 2019 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.4-1
- Update to 0.6-4

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.6.3-3
- Remove explicit dependencies provided by automatic dependency generator

* Sun Aug 04 2019 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.3-2
- Add dropped -devel subpackage to Obsoletes

* Wed Jul 31 2019 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.3-1
- Update to 0.6-3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 05 2018 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.2-1
- Update to 0.6-2

* Sat Sep 22 2018 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.1-1
- Update to 0.6-1
- Remove patch for 0.6-0 (included in 0.6-1)

* Wed Aug 15 2018 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.0-3
- Bump version to trigger rebuild due to target misconfiguration in f29
- Fix SPEC indentations

* Tue Aug 14 2018 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.0-2
- Remove R-core and udunits2 from Requires, not needed

* Mon Aug 13 2018 Iñaki Úcar <iucar@fedoraproject.org> - 0.6.0-1
- initial package for Fedora
