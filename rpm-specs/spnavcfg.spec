# Required for suid binary
%global _hardened_build 1

Name:           spnavcfg
Version:        0.3
Release:        12%{?dist}
Summary:        Spacenav daemon interactive configuration program

License:        GPLv3+
URL:            http://spacenav.sourceforge.net/
Source0:        http://downloads.sourceforge.net/spacenav/%{name}-%{version}.tar.gz

Patch0:         spnavcfg-0.3-fix_icon-install.patch


BuildRequires:  gcc
BuildRequires:  libX11
BuildRequires:  gtk2-devel
BuildRequires:  desktop-file-utils

Requires:       spacenavd


%description
Spacenav daemon interactive configuration program.


%prep
%setup -q
%patch0 -p1 -b .icons


%build
export CFLAGS="%{optflags}"
%configure 

# Patch makefile to honor CFLAGS
sed -i 's/CFLAGS =/CFLAGS +=/g' Makefile

# Remove -O3 from build flags
sed -i 's/\-O3//g' Makefile

# Patch makefile to fix missing parameter LDFLAGS
sed -i 's/pkg-config --libs gtk+-2.0/pkg-config --libs gtk+-2.0 x11/g' Makefile


make %{?_smp_mflags}


%install
%make_install

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install                               \
--dir=%{buildroot}%{_datadir}/applications         \
icons/%{name}.desktop

%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%{_datadir}/icons/hicolor/256x256/apps/%{name}.png


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Richard Shaw <hobbes1069@gmail.com> - 0.3-1
- Update to latest upstream release.

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 21 2013 Richard Shaw <hobbes1069@gmail.com> - 0.2.1-5
- Fix compiler flags to meet Fedora guidelines for packages with suid binaries.
  Fixes BZ# 965522.

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 05 2012 Richard Shaw <hobbes1069@gmail.com> - 0.2.1-2
- Rebuild for GCC 4.7.0.

* Tue Aug 16 2011 Richard Shaw <hobbes1069@gmail.com> - 0.2.1-1
- Initial Release
