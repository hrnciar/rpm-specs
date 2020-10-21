%global packname DBItest
%global packver  1.7.0
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.7.0
Release:          2%{?dist}
Summary:          Testing DBI Backends

License:          LGPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-blob >= 1.2.0, R-callr, R-DBI >= 1.1.0, R-desc, R-hms >= 0.5.0, R-lubridate, R-methods, R-R6, R-rlang >= 0.2.0, R-testthat >= 2.0.0, R-withr
# Suggests:  R-debugme, R-devtools, R-knitr, R-lintr, R-rmarkdown, R-RSQLite
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-blob >= 1.2.0
BuildRequires:    R-callr
BuildRequires:    R-DBI >= 1.1.0
BuildRequires:    R-desc
BuildRequires:    R-hms >= 0.5.0
BuildRequires:    R-lubridate
BuildRequires:    R-methods
BuildRequires:    R-R6
BuildRequires:    R-rlang >= 0.2.0
BuildRequires:    R-testthat >= 2.0.0
BuildRequires:    R-withr
BuildRequires:    R-debugme
BuildRequires:    R-devtools
BuildRequires:    R-knitr
BuildRequires:    R-lintr
BuildRequires:    R-rmarkdown
BuildRequires:    R-RSQLite

%description
A helper that tests 'DBI' back ends for conformity to the interface.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 07 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.0-2
- Rebuild for R 4

* Sun May 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.7.0-1
- initial package for Fedora
