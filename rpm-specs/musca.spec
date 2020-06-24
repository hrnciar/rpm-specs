Name:           musca
Version:        0.9.24
Release:        19%{?dist}
Summary:        A simple dynamic window manager fox X

License:        GPLv3
URL:            http://aerosuidae.net/musca.html
Source0:        http://aerosuidae.net/%{name}-%{version}.tgz
Patch0:         dmenu_run.patch

BuildRequires:  gcc
BuildRequires:  coreutils, sed, libX11-devel
Requires:       dmenu, xterm

%description
musca is a simple dynamic window manager for X, with features nicked
from ratpoison and dwm. Musca operates as a tiling window manager by default. 
It uses manual tiling, which means the user determines how the screen is 
divided into non-overlapping frames, with no restrictions on layout.

%prep
%setup -q

%patch0 -p0

%build
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -p -m 0755 musca $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m 0644 musca.1 $RPM_BUILD_ROOT%{_mandir}/man1

# Create desktop file
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xsessions/
cat << EOF > $RPM_BUILD_ROOT/%{_datadir}/xsessions/musca.desktop
[Desktop Entry]
Name=Musca
Comment=A tiling manager for X
Exec=musca
TryExec=musca
Type=XSession
EOF


%files
%doc gpl.txt
%{_bindir}/musca
%{_datadir}/xsessions/musca.desktop
%{_mandir}/man1/musca.1.gz


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.24-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.24-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.24-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.24-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.24-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 25 2012 Damien Durand <splinux25@gmail.com> - 0.9.24-4
- Release bumped for F17.

* Wed Apr 25 2012 Damien Durand <splinux25@gmail.com> - 0.9.24-3
- dmenu_run in config file instead of dmenu.

* Sun Feb 19 2012 Damien Durand <splinux25@gmail.com> - 0.9.24-2
- Add a proper description.
- We preserve timestamp with the install command.
- Add coreutils and sed in BuildRequires.

* Thu Jan 18 2012 Damien Durand <splinux25@gmail.com> - 0.9.24-1
- Initial release.
