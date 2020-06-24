%global packname jsonlite
%global packver  1.6.1
%global rlibdir  %{_libdir}/R/library

# Several hard-require this package or are not yet available.
%global with_suggests 0

Name:             R-%{packname}
Version:          1.6.1
Release:          2%{?dist}
Summary:          A Robust, High Performance JSON Parser and Generator for R

# Bundled yajl is ISC.
License:          MIT and ISC
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:
# Suggests:  R-httr, R-curl, R-plyr, R-testthat, R-knitr, R-rmarkdown, R-R.rsp, R-sp
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-plyr
BuildRequires:    R-testthat
BuildRequires:    R-sp
%if 0%{with_suggests}
BuildRequires:    R-httr
BuildRequires:    R-curl
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-R.rsp
%endif
# https://github.com/jeroen/jsonlite/issues/201
Provides: bundled(yajl) = 2.1.1

%description
A fast JSON parser and generator optimized for statistical data and the web.
Started out as a fork of 'RJSONIO', but has been completely rewritten in recent
versions. The package offers flexible, robust, high performance tools for
working with JSON in R and is particularly powerful for building pipelines and
interacting with a web API. The implementation is based on the mapping
described in the vignette (Ooms, 2014). In addition to converting JSON data
from/to R objects, 'jsonlite' contains functions to stream, validate, and
prettify JSON data. The unit tests included with the package verify that all
edge cases are encoded and decoded consistently for use with dynamic data in
systems and applications.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with_suggests}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} --ignore-vignettes --no-examples
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 1.6.1-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.6-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 1.5-7
- rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Nov 07 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5-5
- Cleanup optional Requires.

* Tue Sep 12 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5-4
- Make note of bundled yajl.

* Thu Sep 07 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5-3
- Skip testing examples.

* Fri Sep 01 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5-2
- new package built with tito

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.5-1
- initial package for Fedora
