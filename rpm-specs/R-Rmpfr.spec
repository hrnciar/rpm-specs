# When we are bootstrapping, we drop some dependencies, and/or build time tests.
%{?_with_bootstrap: %global bootstrap 1}

%global packname Rmpfr
%global packver  0.8-1
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.8.1
Release:          4%{?dist}
Summary:          R MPFR - Multiple Precision Floating-Point Reliable

License:          GPLv2+
URL:              https://CRAN.R-project.org/package=%{packname}
Source0:          https://cran.r-project.org/src/contrib/%{packname}_%{packver}.tar.gz

# Here's the R view of the dependencies world:
# Depends:   R-gmp >= 0.5-8
# Imports:   R-stats, R-utils, R-methods
# Suggests:  R-MASS, R-Bessel, R-polynom, R-sfsmisc >= 1.0-20, R-Matrix
# LinkingTo:
# Enhances:

BuildRequires:    R-devel
BuildRequires:    tex(latex)
BuildRequires:    tex(hanging.sty)
BuildRequires:    R-gmp >= 0.5.8
BuildRequires:    gmp-devel >= 4.2.3
BuildRequires:    mpfr-devel >= 3.0.0
BuildRequires:    R-stats
BuildRequires:    R-utils
BuildRequires:    R-methods
BuildRequires:    R-MASS
%if ! 0%{?bootstrap}
# Hard-dependency on this.
BuildRequires:    R-Bessel
%endif
BuildRequires:    R-polynom
BuildRequires:    R-sfsmisc >= 1.0.20
BuildRequires:    R-Matrix

%description
Arithmetic (via S4 classes and methods) for arbitrary precision floating
point numbers, including transcendental ("special") functions.  To this
end, the package interfaces to the 'LGPL' licensed 'MPFR' (Multiple
Precision Floating-Point Reliable) Library which itself is based on the
'GMP' (GNU Multiple Precision) Library.


%prep
%setup -q -c -n %{packname}


%build


%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css


%check
%if ! 0%{?bootstrap}
%{_bindir}/R CMD check %{packname}
%else
_R_CHECK_FORCE_SUGGESTS_=0 %{_bindir}/R CMD check %{packname}
%endif


%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS.Rd
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%dir %{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/libs/%{packname}.so
%{rlibdir}/%{packname}/check-tools.R
%{rlibdir}/%{packname}/demo


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun  7 2020 Tom Callaway <spot@fedoraproject.org> - 0.8.1-3
- bootstrap off

* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 0.8.1-2
- bootstrap build for R 4

* Mon Feb 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.8.1-1
- Update to latest version

* Sat Feb 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-6
- Backport fix for -fno-common change

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct  9 2019 Jerry James <loganjerry@gmail.com> - 0.7.2-4
- Rebuild for mpfr 4

* Sun Aug 11 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-3
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.2-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.1-1
- Update to latest version

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Tom Callaway <spot@fedoraproject.org> - 0.7.0-2
- rebuild for R 3.5.0

* Wed Mar 28 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.7.0-1
- initial package for Fedora
