%global packname  httr
%global rlibdir  %{_datadir}/R/library

# Not yet available.
%global with_suggests 0
# Tests check many external URLs.
%global with_network 0

Name:             R-%{packname}
Version:          1.4.1
Release:          3%{?dist}
Summary:          Tools for Working with URLs and HTTP

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-curl >= 3.0.0, R-jsonlite, R-mime, R-openssl >= 0.8, R-R6
# Suggests:  R-covr, R-httpuv, R-jpeg, R-knitr, R-png, R-readr, R-rmarkdown, R-testthat >= 0.8.0, R-xml2
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-curl >= 3.0.0
BuildRequires:    R-jsonlite
BuildRequires:    R-mime
BuildRequires:    R-openssl >= 0.8
BuildRequires:    R-R6
BuildRequires:    R-httpuv
BuildRequires:    R-jpeg
BuildRequires:    R-knitr
BuildRequires:    R-png
%if %{with_suggests}
BuildRequires:    R-readr
%endif
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat >= 0.8.0
BuildRequires:    R-xml2

%description
Useful tools for working with HTTP organised by HTTP verbs (GET(), POST(),
etc). Configuration functions make it easy to control additional request
components (authenticate(), add_headers() and so on).


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if !%{with_network}
ARGS="--no-examples --no-tests --no-vignettes"
%endif
%if %{with_suggests}
%{_bindir}/R CMD check %{packname} $ARGS
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname} $ARGS
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/demo


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.1-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.1-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- initial package for Fedora
