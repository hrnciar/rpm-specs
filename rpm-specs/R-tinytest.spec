%global packname tinytest
%global packver  1.2.1
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          1.2.1
Release:          2%{?dist}
Summary:          Lightweight and Feature Complete Unit Testing Framework

License:          GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-parallel, R-utils
# Suggests:
# LinkingTo:
# Enhances:

BuildArch:        noarch
BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    tex(sectsty.sty)
BuildRequires:    R-parallel
BuildRequires:    R-utils

%description
Provides a lightweight (zero-dependency) and easy to use unit testing
framework. Main features: install tests with the package. Test results are
treated as data that can be stored and manipulated. Test files are R scripts
interspersed with test commands, that can be programmed over. Fully automated
build-install-test sequence for packages. Skip tests when not run locally (e.g.
on CRAN). Flexible and configurable output printing. Compare computed output
with output stored with the package. Run tests in parallel.  Extensible by
other packages. Report side effects.


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
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/tinytest
%{rlibdir}/%{packname}/CITATION


%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.2.1-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.2.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest version

* Mon Aug 26 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.4-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.9.4-1
- initial package for Fedora
