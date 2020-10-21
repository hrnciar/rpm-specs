%global packname yaml
%global packver  2.2.1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2.2.1
Release:          4%{?dist}
Summary:          Methods to Convert R Data to YAML and Back

# R library is BSD; bundled libyaml is MIT.
License:          BSD and MIT
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:  R-RUnit
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    R-RUnit
# Slightly patched, so can't unbundle yet.
Provides:         bundled(libyaml) = 0.1.7

%description
Implements the 'libyaml' 'YAML' 1.1 parser and emitter
(<http://pyyaml.org/wiki/LibYAML>) for R.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css
rm %{buildroot}%{rlibdir}/%{packname}/implicit.re


%check
%{_bindir}/R CMD check %{packname}


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CHANGELOG
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%license %{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/THANKS
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/tests


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun  4 2020 Tom Callaway <spot@fedoraproject.org> - 2.2.1-2
- rebuild for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.1-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.0-4
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.2.0-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 2.1.19-2
- rebuild for R 3.5.0

* Wed May 02 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 2.1.19-1
- Update to latest version.

* Mon Mar 12 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.1.18-1
- Update to latest version.

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.1.16-1
- Update to latest version.

* Tue Nov 07 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.1.14-4
- Make note of bundled libyaml.

* Tue Nov 07 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.1.14-3
- Remove extra Requires.

* Thu Aug 24 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.1.14-2
- Fix license field.

* Fri Feb 17 2017 Elliott Sales de Andrade <quantum.analyst@gmail.com> 2.1.14-1
- initial package for Fedora
