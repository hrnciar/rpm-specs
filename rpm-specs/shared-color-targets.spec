Summary: Shared color targets for creating color profiles
Name: shared-color-targets
Version: 0.1.7
Release: 8%{?dist}
URL: http://github.com/hughsie/shared-color-targets
Source0: http://people.freedesktop.org/~hughsient/releases/%{name}-%{version}.tar.xz
License: GPLv2+ and Public Domain and CC-BY-SA
BuildArch: noarch

BuildRequires: gcc

Requires: color-filesystem

%description 
The shared-color-targets package contains various targets which are
useful for programs that create ICC profiles.
This package only contains the free targets that can be safely
distributed with Fedora.

%prep
%setup -q

%build
%configure

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING
%dir %{_datadir}/color/targets
%{_datadir}/color/targets/*.it8
%dir %{_datadir}/shared-color-targets

# Wolf Faust
%dir %{_datadir}/shared-color-targets/wolf_faust
%{_datadir}/shared-color-targets/wolf_faust/*
%dir %{_datadir}/color/targets/wolf_faust
%dir %{_datadir}/color/targets/wolf_faust/reflective
%{_datadir}/color/targets/wolf_faust/reflective/*.it8
%dir %{_datadir}/color/targets/wolf_faust/transmissive
%{_datadir}/color/targets/wolf_faust/transmissive/*.it8

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Aug 19 2016 Richard Hughes <richard@hughsie.com> 0.1.7-1
- New upstream release with several new targets from Wolf Faust.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Oct 27 2015 Richard Hughes <richard@hughsie.com> 0.1.6-1
- New upstream release with several new targets from Wolf Faust.

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Dec 20 2014 Richard Hughes <richard@hughsie.com> 0.1.5-1
- New upstream release with several new targets from Wolf Faust.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 04 2014 Richard Hughes <richard@hughsie.com> 0.1.4-1
- New upstream release with several new targets from Wolf Faust.

* Mon Dec 02 2013 Richard Hughes <richard@hughsie.com> 0.1.3-1
- New upstream release with several new targets from Wolf Faust.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Nov 28 2012 Richard Hughes <richard@hughsie.com> 0.1.2-1
- New upstream release with several new targets from Wolf Faust.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Feb 23 2012 Richard Hughes <richard@hughsie.com> 0.1.1-1
- New upstream release with several new targets from Wolf Faust.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Sep 08 2011 Richard Hughes <richard@hughsie.com> 0.1.0-3
- New upstream release with several new targets from Wolf Faust.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.1-0.9.20091218git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 18 2009 Richard Hughes <richard@hughsie.com> 0.0.1-0.8.20091218git
- Update from git
