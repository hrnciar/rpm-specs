%global packname backports
%global packver  1.1.10
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1.10
Release:          1%{?dist}
Summary:          Reimplementations of Functions Introduced Since R-3.0.0

License:          GPLv2 or GPLv3
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:   R-utils
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-utils

%description
Functions introduced or changed since R v3.0.0 are re-implemented in this
package. The backports are conditionally exported in order to let R resolve
the function name to either the implemented backport, or the respective
base version, if available. Package developers can make use of new
functions or arguments by selectively importing specific backports to
support older installations.


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
* Wed Sep 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.10-1
- Update to latest version (#1879297)

* Tue Aug 25 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.9-1
- Update to latest version (#1871938)

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.8-1
- Update to latest version

* Wed Jun  3 2020 Tom Callaway <spot@fedoraproject.org> - 1.1.7-2
- rebuild for R 4

* Thu May 21 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.7-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 02 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.5-1
- Update to latest version

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.4-1
- Update to latest version

* Fri Feb 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.3-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 1.1.2-3
- rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Dec 18 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.2-1
- Update to latest version.

* Thu Nov 09 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 1.1.1-1
- initial package for Fedora
