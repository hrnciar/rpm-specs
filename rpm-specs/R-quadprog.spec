%global packname  quadprog
%global packvers  1.5-8
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.5.8
Release:          6%{?dist}
Summary:          Functions to Solve Quadratic Programming Problems

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packvers}.tar.gz
Patch0001:        Fix-FSF-address.patch

# Here's the R view of the dependencies world:
# Depends:
# Imports:
# Suggests:
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)

%description
This package contains routines and documentation for solving quadratic
programming problems.


%prep
%setup -q -c -n %{packname}

pushd %{packname}
%patch0001 -p1
popd


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
%license %{packname}/GPL-?
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{packname}/ChangeLog
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so


%changelog
* Mon Aug 10 2020 Tom Callaway <spot@fedoraproject.org> - 1.5.8-6
- rebuild for FlexiBLAS R

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 1.5.8-3
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.8-1
- Update to latest version

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon May 06 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.7-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.5-2
- Rebuild for R 3.5.0

* Sun May 06 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.5.5-1
- initial package for Fedora
