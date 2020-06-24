%global packname unitizer
%global packver  1.4.10
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          %{packver}
Release:          2%{?dist}
Summary:          Interactive R Unit Tests

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-methods
# Imports:   R-stats, R-utils, R-crayon >= 1.3.2, R-diffobj >= 0.1.5.9000
# Suggests:  R-covr, R-knitr, R-rmarkdown, R-testthat
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-methods
BuildRequires:    R-stats
BuildRequires:    R-utils
BuildRequires:    R-crayon >= 1.3.2
BuildRequires:    R-diffobj >= 0.1.5.9000
BuildRequires:    R-knitr
BuildRequires:    R-rmarkdown
BuildRequires:    R-testthat

%description
Simplifies regression tests by comparing objects produced by test code with
earlier versions of those same objects. If objects are unchanged the tests
pass, otherwise execution stops with error details. If in interactive mode,
tests can be reviewed through the provided interactive environment.


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
# Vignettes use the network.
%{_bindir}/R CMD check %{packname} --no-vignettes


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
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/expkg


%changelog
* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 1.4.10-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.10-1
- Update to latest version

* Mon Mar 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.9-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.8-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.8-1
- Update to latest version

* Sun Mar 17 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.7-1
- Update to latest version

* Wed Feb 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.6-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 22 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.4.5-1
- initial package for Fedora
