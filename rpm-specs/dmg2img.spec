Summary:        Uncompress the Apple compressed disk image files
Name:           dmg2img
Version:        1.6.7
Release:        9%{?dist}
# dmg2img is GPL without specific version
# vfdecrypt is MIT licensed
License:        GPL+ and MIT
Source0:        http://vu1tur.eu.org/tools/%{name}-%{version}.tar.gz
Patch0:         dmg2img-1.6.2-nostrip.patch
URL:            http://vu1tur.eu.org/tools/
BuildRequires:  gcc
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(openssl) < 1.1.0
BuildRequires:  pkgconfig(zlib)


%description
This package contains dmg2img utility that is able to uncompress compressed dmg
files into plain disk or filesystem images.


%prep
%setup -q
%patch0 -p1


%build
make CC="%{__cc}" CFLAGS="%{optflags}" %{_smp_mflags}


%install
install -D -p -m 0755 dmg2img %{buildroot}%{_bindir}/dmg2img
install -D -p -m 0755 vfdecrypt %{buildroot}%{_bindir}/vfdecrypt
install -D -p -m 0644 vfdecrypt.1 %{buildroot}%{_mandir}/man1/vfdecrypt.1


%files
%license COPYING
%doc README
%{_bindir}/dmg2img
%{_bindir}/vfdecrypt
%{_mandir}/man1/vfdecrypt.1*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 30 2017 Peter Lemenkov <lemenkov@gmail.com> - 1.6.7-1
- Ver. 1.6.7

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Nov 16 2014 Peter Lemenkov <lemenkov@gmail.com> - 1.6.5-1
- Ver. 1.6.5

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jan 09 2012 Lubomir Rintel <lkundrak@v3.sk> - 1.6.2-2
- Add a missing BR (Richard Shaw, #749752)
- Cosmetic fixes (Scott Tsai, #749752)

* Fri Oct 29 2011 Lubomir Rintel <lkundrak@v3.sk> - 1.6.2-1
- Initial packaging
