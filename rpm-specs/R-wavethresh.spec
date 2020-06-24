%define packver  4.6.8
%define packname wavethresh

Summary: R module, Software to perform wavelet statistics and transforms
Name: R-%{packname}
Version: %{packver}
Release: 11%{?dist}
License: GPLv2+
Source0: ftp://cran.r-project.org/pub/R/contrib/main/%{packname}_%{packver}.tar.gz
URL: http://cran.r-project.org/web/packages/wavethresh/
BuildRequires: R-devel >= 3.4.0, tetex-latex, R-MASS

%description
Software to perform 1-d and 2-d wavelet statistics and transforms

%prep
%setup -q -n %{packname}

%build

%install
mkdir -p %{buildroot}%{_libdir}/R/library
cd ..; R CMD INSTALL %{packname} -l %{buildroot}%{_libdir}/R/library
%{__rm} -rf %{buildroot}%{_libdir}/R/library/R.css

%check
cd ..;%{_bindir}/R CMD check %{packname}

%files
%{_libdir}/R/library/%{packname}
%doc DESCRIPTION

%changelog
* Fri Jun  5 2020 Tom Callaway <spot@fedoraproject.org> - 4.6.8-11
- rebuild for R 4

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.8-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 12 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 4.6.8-9
- Remove explicit dependencies provided by automatic dependency generator

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.8-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri May 18 2018 Tom Callaway <spot@fedoraproject.org> - 4.6.8-5
- rebuild for R 3.5.0

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Tom Callaway <spot@fedoraproject.org> - 4.6.8-1
- update to 4.6.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.6.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 José Matos <jamatos@fedoraproject.org> - 4.6.6-1
- update to 4.6.6

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 José Matos <jamatos@fedoraproject.org> - 4.6.5-1
- update to 4.6.5

* Fri May  3 2013 José Matos <jamatos@fedoraproject.org> - 4.6.4-1
- update to 4.6.4

* Thu Apr 11 2013 Tom Callaway <spot@fedoraproject.org> - 4.6.2-1
- update to 4.6.2

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov  9 2011 Tom Callaway <spot@fedoraproject.org> - 4.5-2
- rebuild for R 2.14.0

* Thu Mar 17 2011 José Matos <jamatos@fedoraproject.org> - 4.5-1
- Update to latest stable release
- Update url

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jul 28 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 2.2.11-1
- update to 2.2-11
- use new versioning scheme that includes packrel
- use proper scriptlets

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 14 2008 José Matos <jamatos[AT]fc.up.pt> - 2.2-9
- Rebuild for gcc 4.3

* Mon Jan  7 2008 Alex Lancaster <alexlan[AT]fedoraproject org> - 2.2-8
- BuildRequires: R-devel rather than just R

* Mon Aug 27 2007 José Matos <jamatos[AT]fc.up.pt> - 2.2-7
- License fix, rebuild for devel (F8).

* Thu Apr 26 2007 José Matos <jamatos[AT]fc.up.pt> - 2.2-6
- Rebuild for R 2.5.

* Tue Oct 17 2006 José Matos <jamatos[AT]fc.up.pt> - 2.2-5
- Rebuild for R 2.4.0.

* Thu Sep 14 2006 José Matos <jamatos@fc.up.pt> - 2.2-4
- New upstream version 2.2-9.

* Sun Jun  4 2006 José Matos <jamatos@fc.up.pt> - 2.2-3
- Rebuild for R-2.3.x

* Wed Mar  8 2006 Jose' Matos <jamatos@fc.up.pt> - 2.2-2
- Rename License to simply GPL, added DESCRIPTION to %%doc

* Fri Mar 03 2006 José Matos <jamatos@fc.up.pt> 2.2-1
- Initial package creation
