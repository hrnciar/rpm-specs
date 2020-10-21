%global packname haven
%global packver  2.3.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.3.1
Release:          2%{?dist}
Summary:          Import and Export 'SPSS', 'Stata' and 'SAS' Files

License:          MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-forcats >= 0.2.0, R-hms, R-methods, R-Rcpp >= 0.11.4, R-readr >= 0.1.0, R-rlang >= 0.4.0, R-tibble, R-tidyselect, R-vctrs >= 0.3.0
# Suggests:  R-covr, R-fs, R-knitr, R-rmarkdown, R-testthat, R-pillar >= 1.4.0, R-cli, R-crayon
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-forcats >= 0.2.0
BuildRequires:    R-hms
BuildRequires:    R-methods
BuildRequires:    R-Rcpp-devel >= 0.11.4
BuildRequires:    R-readr >= 0.1.0
BuildRequires:    R-rlang >= 0.4.0
BuildRequires:    R-tibble
BuildRequires:    R-tidyselect
BuildRequires:    R-vctrs >= 0.3.0
BuildRequires:    R-fs
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat
BuildRequires:    R-pillar >= 1.4.0
BuildRequires:    R-cli
BuildRequires:    R-crayon

%description
Import foreign statistical formats into R via the embedded 'ReadStat' C
library, <https://github.com/WizardMac/ReadStat>.


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
%{_bindir}/R CMD check %{packname}


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
%{rlibdir}/%{packname}/examples
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 20 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.1-1
- Update to latest version
- Fixes rhbz#1842613

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 2.3.0-2
- rebuild for R 4

* Sun May 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.3.0-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 13 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.1-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.1-1
- Update to latest version

* Fri May 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.0-1
- initial package for Fedora
