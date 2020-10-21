%global packname foghorn
%global packver  1.3.1
%global rlibdir  %{_datadir}/R/library

# Tests and vignettes use the network.
%bcond_with network

Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Summarize CRAN Check Results in the Terminal

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-clisymbols >= 1.0.0, R-crayon >= 1.3.2, R-curl >= 2.2, R-httr >= 1.2.1, R-jsonlite >= 1.5, R-rlang >= 0.4.3, R-rvest >= 0.3.2, R-tibble >= 1.2, R-xml2 >= 1.0.0
# Suggests:  R-covr, R-dplyr, R-knitr, R-progress, R-rmarkdown, R-testthat
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-clisymbols >= 1.0.0
BuildRequires:    R-crayon >= 1.3.2
BuildRequires:    R-curl >= 2.2
BuildRequires:    R-httr >= 1.2.1
BuildRequires:    R-jsonlite >= 1.5
BuildRequires:    R-rlang >= 0.4.3
BuildRequires:    R-rvest >= 0.3.2
BuildRequires:    R-tibble >= 1.2
BuildRequires:    R-xml2 >= 1.0.0
BuildRequires:    R-dplyr
BuildRequires:    R-knitr
BuildRequires:    R-progress
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat

%description
The CRAN check results and where your package stands in the CRAN submission
queue in your R terminal.


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
%if %{with network}
%{_bindir}/R CMD check %{packname}
%else
%{_bindir}/R CMD check %{packname} --no-tests --no-vignettes
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%license %{rlibdir}/%{packname}/LICENSE
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.md
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/WORDLIST


%changelog
* Wed Sep 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.3.1-1
- Update to latest version (#1877063)

* Mon Aug 03 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.3-1
- Update to latest version

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.0-5
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- initial package for Fedora
