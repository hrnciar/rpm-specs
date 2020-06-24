%global packname  Rcompression
%global packver   0.93
%global packrel   2

Name:             R-%{packname}
Version:          %{packver}.%{packrel}
Release:          28%{?dist}
Summary:          R Package for in-memory compression
License:          zlib
URL:              http://www.omegahat.net/Rcompression/
Source0:          http://www.omegahat.net/Rcompression/%{packname}_%{packver}-%{packrel}.tar.gz
Patch0:           R-Rcompression-stdlib.patch
Patch1:           R-Rcompression-DESCRIPTION-Blank-line-fix.patch
Requires:         texlive-latex
BuildRequires:    R-devel >= 3.4.0, zlib-devel, bzip2-devel, autoconf
BuildRequires:    automake, libtool
Provides:         bundled(minizip)

%description
This package is a basic R interface to the zlib and bzip2 facilities for 
compressing and uncompressing data that are in memory rather than in files.

%prep
%setup -c -q -n %{packname}
%patch0 -p1 -b .stdlib
%patch1 -p1 -b .blfix
cd %{packname}
autoreconf -if

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
%{_bindir}/R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library 
# Clean up in advance of check
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -rf %{buildroot}%{_libdir}/R/library/R.css

# Delete pointless sampleData directory full of test files
rm -rf %{buildroot}%{_libdir}/R/library/%{packname}/sampleData/

%check
# Recursive loop with RCurl
# Also, the tests seem to be broken.
# %{_bindir}/R CMD check %{packname}

%files
%dir %{_libdir}/R/library/%{packname}
%doc %{_libdir}/R/library/%{packname}/LICENSE
%doc %{_libdir}/R/library/%{packname}/html
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/libs/

%changelog
* Mon Jun  8 2020 Tom Callaway <spot@fedoraproject.org> - 0.93.2-28
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.2-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.93.2-26
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.2-25
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Oct  5 2018 Tom Callaway <spot@fedoraproject.org> - 0.93.2-23
- use bundled minizip

* Tue Sep 04 2018 Pavel Raiskup <praiskup@redhat.com> - 0.93.2-22
- rebuild against minizip-compat-devel, rhbz#1609830, rhbz#1615381

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 0.93.2-20
- rebuild for R 3.5.0

* Fri Mar 23 2018 Tom Callaway <spot@fedoraproject.org> - 0.93.2-19
- rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.2-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu May 18 2017 Tom Callaway <spot@fedoraproject.org> - 0.93.2-15
- rebuild for R 3.4.0, update urls

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.93.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 0.93.2-8
- rebuild for R3

* Fri Feb 22 2013 Tom Callaway <spot@fedoraproject.org> - 0.93.2-7
- fix FTBFS caused by blank line in DESCRIPTION (bz 913864)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Tom Callaway <spot@fedoraproject.org> 0.93.2-3
- delete sampleData/ because it is full of useless junk
- add missing BR

* Fri Nov 11 2011 Tom Callaway <spot@fedoraproject.org> 0.93.2-2
- unbundle minizip and use system copy

* Thu Nov 10 2011 Tom "spot" Callaway <tcallawa@redhat.com> 0.93.2-1
- initial package for Fedora
