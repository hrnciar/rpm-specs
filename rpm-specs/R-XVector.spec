%global packname  XVector
%global rlibdir %{_libdir}/R/library

%global __suggests_exclude ^R\\((drosophila2probe)\\)

Name:             R-%{packname}
Version:          0.28.0
Release:          1%{dist}
Summary:          Representation and manipulation of external sequences
License:          Artistic 2.0
URL:              http://www.bioconductor.org/packages/release/bioc/html/XVector.html
Source0:          http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRequires:    R-devel >= 3.4.0 tex(latex) R-methods R-IRanges-devel >= 2.21.6
BuildRequires:    R-BiocGenerics >= 0.19.2 R-S4Vectors-devel >= 0.25.14 R-utils

%description
Memory efficient S4 classes for storing sequences "externally" (behind an R
external pointer, or on disk).

%package devel
Summary:          Development files for R-XVector
Requires:         %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for R-XVector.

%prep
%setup -q -c -n %{packname}

sed -i '/importFrom(zlibbioc)/d' XVector/NAMESPACE
sed -i '/import(zlibbioc)/d' XVector/NAMESPACE
sed -i -e 's/zlibbioc, //' XVector/DESCRIPTION

%build

%install
mkdir -p %{buildroot}%{rlibdir}
R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
# Testing tests optional deps we don't package
# _R_CHECK_FORCE_SUGGESTS_=false %%{_bindir}/R CMD check %%{packname}

%files
%dir %{rlibdir}/%{packname}/
%doc %{rlibdir}/%{packname}/html/
%{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta/
%{rlibdir}/%{packname}/R/
%{rlibdir}/%{packname}/help/
%{rlibdir}/%{packname}/unitTests/
%{rlibdir}/%{packname}/libs/

%files devel
%{rlibdir}/%{packname}/include/

%changelog
* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 0.28.0-1
- rebuild for R 4
- update to 0.28.0

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.26.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Nov 21 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.26.0-2
- Exclude Suggests for unavailable packages

* Wed Nov  6 2019 Tom Callaway <spot@fedoraproject.org> - 0.26.0-1
- update to 0.26.0

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.24.0-2
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 31 2019 Tom Callaway <spot@fedoraproject.org> - 0.24.0-1
- update to 0.24.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 16 2018 Tom Callaway <spot@fedoraproject.org> - 0.20.0-1
- update to 0.20.0, rebuild for R 3.5.0

* Fri Mar 23 2018 Tom Callaway <spot@fedoraproject.org> - 0.18.0-1
- update to 0.18.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.16.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 24 2017 Tom Callaway <spot@fedoraproject.org> 0.16.0-1
- update to 0.16.0

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec  7 2015 Tom Callaway <spot@fedoraproject.org> - 0.10.0-1
- update to 0.10.0

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 29 2015 Tom Callaway <spot@fedoraproject.org> - 0.8.0-1
- update to 0.8.0
- fix DESCRIPTION to not be doc

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun  9 2014 Tom Callaway <spot@fedoraproject.org> - 0.4.0-1
- update to 0.4.0

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 24 2014 Tom Callaway <spot@fedoraproject.org> - 0.2.0-1
- initial package
