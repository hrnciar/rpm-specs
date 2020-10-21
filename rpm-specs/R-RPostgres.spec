%global packname RPostgres
%global packver  1.2.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.2.1
Release:          1%{?dist}
Summary:          Rcpp Interface to PostgreSQL

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-bit64, R-blob >= 1.2.0, R-DBI >= 1.1.0, R-hms >= 0.5.0, R-methods, R-Rcpp >= 0.11.4.2, R-withr
# Suggests:  R-DBItest >= 1.7.0, R-testthat
# LinkingTo: R-BH, R-plogr >= 0.2.0, R-Rcpp
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-bit64
BuildRequires:    R-blob >= 1.2.0
BuildRequires:    R-DBI >= 1.1.0
BuildRequires:    R-hms >= 0.5.0
BuildRequires:    R-methods
BuildRequires:    R-Rcpp-devel >= 0.11.4.2
BuildRequires:    R-withr
BuildRequires:    R-BH-devel
BuildRequires:    R-plogr-devel >= 0.2.0
BuildRequires:    R-DBItest >= 1.7.0
BuildRequires:    R-testthat
BuildRequires:    pkgconfig(libpq)

%description
Fully DBI-compliant Rcpp-backed interface to PostgreSQL
<https://www.postgresql.org/>, an open-source relational database.


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
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Wed Sep 30 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-1
- Update to latest version (#1883221)

* Fri Jun 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.0-1
- initial package for Fedora
