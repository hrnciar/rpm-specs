Name:           exif
Version:        0.6.21
Release:        17%{?dist}
Summary:        Utility to show EXIF information hidden in JPEG files
Summary(fr):    Outil pour afficher les informations EXIF masquées dans les fichiers JPEG

License:        LGPLv2+
URL:            http://libexif.sourceforge.net/
Source0:        http://downloads.sourceforge.net/libexif/%{name}-%{version}.tar.bz2

BuildRequires:  gcc
BuildRequires:  libexif-devel
BuildRequires:  popt-devel


%description
Small command-line utility to show EXIF information hidden
in JPEG files.

%description -l fr
Petit utilitaire en ligne de commande pour afficher les informations
EXIF masquées dans les fichiers JPEG.


%prep
%setup -q
# Convert to UTF8 AUTHORS doc file :
iconv -f iso-8859-1 -t utf8 AUTHORS >AUTHORS.tmp
touch -r AUTHORS AUTHORS.tmp
mv AUTHORS.tmp AUTHORS


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
%find_lang %{name}


%check
make check


%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS COPYING NEWS README ChangeLog
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.21-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.21-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.21-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.21-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.21-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.21-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 0.6.21-3
- Add French translation in spec file

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 17 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 0.6.21-1
- Update to 0.6.21
  - Fix CVE-2012-2845 (RHBZ #840002,#840003)
- Update scriplet in %%prep section of spec file

* Fri Apr 13 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 0.6.20-3
- fix license in spec file (again)

* Wed Feb 24 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 0.6.20-2
- fix license in spec file
- remove %%{_datadir}/locale/* lines in %%files section
- fix man file extension in %%files section
- add %%check section

* Mon Feb 13 2012 Matthieu Saulnier <fantom@fedoraproject.org> - 0.6.20-1
- Initial Release
