%global packname dbplyr
%global packver  1.4.3
%global rlibdir  %{_datadir}/R/library

%global __suggests_exclude ^R\\((Lahman|RMariaDB|RPostgres)\\)

# Not yet available.
%global with_suggests 0

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Summary:          A 'dplyr' Back End for Databases

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-assertthat >= 0.2.0, R-DBI >= 1.0.0, R-dplyr >= 0.8.0, R-glue >= 1.2.0, R-lifecycle, R-methods, R-purrr >= 0.2.5, R-R6 >= 2.2.2, R-rlang >= 0.2.0, R-tibble >= 1.4.2, R-tidyselect >= 0.2.4, R-utils
# Suggests:  R-bit64, R-covr, R-knitr, R-Lahman, R-nycflights13, R-RMariaDB >= 1.0.2, R-rmarkdown, R-RPostgres >= 1.1.3, R-RSQLite >= 2.1.0, R-testthat >= 2.0.0
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-assertthat >= 0.2.0
BuildRequires:    R-DBI >= 1.0.0
BuildRequires:    R-dplyr >= 0.8.0
BuildRequires:    R-glue >= 1.2.0
BuildRequires:    R-lifecycle
BuildRequires:    R-methods
BuildRequires:    R-purrr >= 0.2.5
BuildRequires:    R-R6 >= 2.2.2
BuildRequires:    R-rlang >= 0.2.0
BuildRequires:    R-tibble >= 1.4.2
BuildRequires:    R-tidyselect >= 0.2.4
BuildRequires:    R-utils
BuildRequires:    R-bit64
BuildRequires:    R-knitr
BuildRequires:    R-nycflights13
BuildRequires:    R-rmarkdown
BuildRequires:    R-RSQLite >= 2.1.0
BuildRequires:    R-testthat >= 2.0.0
%if %{with_suggests}
BuildRequires:    R-Lahman
BuildRequires:    R-RMariaDB >= 1.0.2
BuildRequires:    R-RPostgres >= 1.1.3
%endif

%description
A 'dplyr' back end for databases that allows you to work with remote database
tables as if they are in-memory data frames. Basic features works with any
database that has a 'DBI' back end; more advanced features require 'SQL'
translation to be provided by the package author.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
# Don't need coverage; it's not packaged either.
sed -i 's/covr, //g' DESCRIPTION

# Fix executable bits.
chmod -x README.md
popd


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
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
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


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.3-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.3-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 25 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.2-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 24 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.0-1
- Update to latest version

* Mon Mar 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.0-1
- initial package for Fedora
