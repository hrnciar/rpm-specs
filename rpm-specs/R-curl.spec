%bcond_with check

%global packname  curl
%global rlibdir  %{_libdir}/R/library

# Dependency loops and/or not yet packaged.
%global with_doc 1
# These all require the network at the moment + dependency loop.
%global with_test 0

Name:             R-%{packname}
Version:          4.3
Release:          3%{?dist}
Summary:          A Modern and Flexible Web Client for R

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-spelling, R-testthat >= 1.0.0, R-knitr, R-jsonlite, R-rmarkdown, R-magrittr, R-httpuv >= 1.4.4, R-webutils
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    pkgconfig(libcurl)
%if %{with check}
BuildRequires:    R-spelling
BuildRequires:    R-testthat >= 1.0.0
BuildRequires:    R-jsonlite
BuildRequires:    R-httpuv >= 1.4.4
%if %{with_doc}
BuildRequires:    R-knitr
BuildRequires:    glyphicons-halflings-fonts
BuildRequires:    R-rmarkdown
BuildRequires:    R-magrittr
%endif
%if %{with_test}
BuildRequires:    R-webutils
%endif
%endif

%description
The curl() and curl_download() functions provide highly configurable drop-in
replacements for base url() and download.file() with better performance,
support for encryption (https, ftps), gzip compression, authentication, and
other 'libcurl' goodies. The core of the package implements a framework for
performing fully customized requests where data can be processed either in
memory, on disk, or streaming via the callback or connection interfaces. Some
knowledge of 'libcurl' is recommended; for a more-user-friendly web client see
the 'httr' package which builds on this package with http specific tools and
logic.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if %{with check}
ARGS=
%if ! %{with_test}
export _R_CHECK_FORCE_SUGGESTS_=0
ARGS="$ARGS --no-tests --no-examples"
%endif
%if ! %{with_doc}
export _R_CHECK_FORCE_SUGGESTS_=0
ARGS="$ARGS --ignore-vignettes"
%endif
%{_bindir}/R CMD check %{packname} $ARGS
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 4.3-3
- conditionalize check to break loop with httpuv
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Dec 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.3-1
- Update to latest version

* Fri Sep 27 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.2-1
- Update to latest version

* Wed Sep 18 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.1-1
- Update to latest version

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.3-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.3-1
- Update to latest version
- Enable documentation

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 3.2-2
- rebuild for R 3.5.0

* Wed Apr 25 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 3.2-1
- New upstream release.

* Fri Mar 09 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 3.1-1
- New upstream release.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 3.0-1
- New upstream release.

* Fri Aug 25 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.8.1-1
- initial package for Fedora
