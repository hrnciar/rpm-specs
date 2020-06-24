%global packname  readr
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.3.1
Release:          5%{?dist}
Summary:          Read Rectangular Text Data

# Mainly GPLv2+; only src/grisu3.? are ASL 2.0
License:          GPLv2+ and ASL 2.0
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-Rcpp >= 0.12.0.5, R-tibble, R-hms >= 0.4.1, R-R6, R-clipr, R-crayon, R-methods
# Suggests:  R-curl, R-testthat, R-knitr, R-rmarkdown, R-stringi, R-covr, R-spelling
# LinkingTo: R-Rcpp, R-BH
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-Rcpp-devel >= 0.12.0.5
BuildRequires:    R-tibble
BuildRequires:    R-hms >= 0.4.1
BuildRequires:    R-R6
BuildRequires:    R-BH-devel
BuildRequires:    R-clipr
BuildRequires:    R-crayon
BuildRequires:    R-methods
BuildRequires:    R-curl
BuildRequires:    R-testthat
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-stringi
BuildRequires:    R-spelling

%description
The goal of 'readr' is to provide a fast and friendly way to read
rectangular data (like 'csv', 'tsv', and 'fwf'). It is designed to
flexibly parse many types of data found in the wild, while still cleanly
failing when data unexpectedly changes.


%prep
%setup -q -c -n %{packname}

# Don't need coverage; it's not packaged either.
sed -i 's/, covr//g' %{packname}/DESCRIPTION


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
export LANG=C.UTF-8
%{_bindir}/R CMD check %{packname}


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
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%dir %{rlibdir}/%{packname}/rcon
%{rlibdir}/%{packname}/rcon/librcon.so
%{rlibdir}/%{packname}/WORDLIST
%{rlibdir}/%{packname}/extdata


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.3.1-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Feb 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Aug 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-2
- Fix license tag

* Tue Aug 14 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.1-1
- initial package for Fedora
