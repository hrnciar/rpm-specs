%global packname RMariaDB
%global packver  1.0.10
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.0.10
Release:          1%{?dist}
Summary:          Database Interface and 'MariaDB' Driver

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-bit64, R-DBI >= 1.1.0, R-hms >= 0.5.0, R-methods, R-Rcpp >= 0.12.4
# Suggests:  R-DBItest >= 1.7.0, R-rprojroot, R-testthat
# LinkingTo: R-BH, R-plogr, R-Rcpp
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-bit64
BuildRequires:    R-DBI >= 1.1.0
BuildRequires:    R-hms >= 0.5.0
BuildRequires:    R-methods
BuildRequires:    R-Rcpp-devel >= 0.12.4
BuildRequires:    R-BH-devel
BuildRequires:    R-plogr-devel
BuildRequires:    R-DBItest >= 1.7.0
BuildRequires:    R-rprojroot
BuildRequires:    R-testthat
BuildRequires:    mariadb-connector-c-devel

%description
Implements a 'DBI'-compliant interface to 'MariaDB'
(<https://mariadb.org/>) and 'MySQL' (<https://www.mysql.com/>) databases.


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
* Fri Aug 28 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.10-1
- Update to latest version

* Fri Aug 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.9-2
- Rebuild to fix dist tag

* Sun Aug 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.9-1
- initial package for Fedora
