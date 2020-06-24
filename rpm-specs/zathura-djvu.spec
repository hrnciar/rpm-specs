Name:             zathura-djvu
Version:          0.2.9
Release:          1%{?dist}
Summary:          DjVu support for zathura
License:          zlib
URL:              http://pwmt.org/projects/zathura/plugins/%{name}
Source0:          http://pwmt.org/projects/zathura/plugins/download/%{name}-%{version}.tar.xz
BuildRequires:    binutils
BuildRequires:    cairo-devel
BuildRequires:    coreutils
BuildRequires:    djvulibre-devel
# Needed to validate the desktop file
BuildRequires:    desktop-file-utils
BuildRequires:    girara-devel
BuildRequires:    glib2-devel
# Needed to validate appdata
BuildRequires:    libappstream-glib
BuildRequires:    meson >= 0.43
BuildRequires:    gcc
BuildRequires:    zathura-devel >= 0.3.8
Requires:         zathura >= 0.3.8

%description
The zathura-djvu plugin adds DjVu support to zathura by
using the djvulibre library.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files
%license LICENSE
%doc AUTHORS
%{_libdir}/zathura/libdjvu.so
%{_datadir}/applications/org.pwmt.zathura-djvu.desktop
%{_datadir}/metainfo/org.pwmt.zathura-djvu.metainfo.xml

%changelog
* Wed Apr 15 2020 Petr Šabata <contyk@redhat.com> - 0.2.9-1
- 0.2.9 bump

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Apr 10 2018 Petr Šabata <contyk@redhat.com> - 0.2.8-1
- 0.2.8 bump

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Petr Šabata <contyk@redhat.com> - 0.2.6-1
- 0.2.6 bump

* Fri Feb 26 2016 Petr Šabata <contyk@redhat.com> - 0.2.5-1
- 0.2.5 bump

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jul 02 2015 Petr Šabata <contyk@redhat.com> - 0.2.4-5
- Install the desktop file correctly

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Petr Šabata <contyk@redhat.com> - 0.2.4-3
- Rebuild for new girara

* Tue Jun 09 2015 Petr Šabata <contyk@redhat.com> - 0.2.4-2
- Fix the dep list, install LICENSE with the %%license macro

* Fri Oct 17 2014 Petr Šabata <contyk@redhat.com> - 0.2.4-1
- 0.2.4 bump

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 06 2014 François Cami <fcami@fedoraproject.org> - 0.2.3-5
- Bump for rawhide (again)

* Thu Mar 06 2014 François Cami <fcami@fedoraproject.org> - 0.2.3-4
- Bump for rawhide

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 29 2013 Petr Šabata <contyk@redhat.com> - 0.2.3-2
- Fix a debuginfo regression (#967954)

* Tue May 21 2013 Petr Šabata <contyk@redhat.com> - 0.2.3-1
- 0.2.3 bump
- Dropping the now unneeded patches

* Fri Mar 29 2013 Kevin Fenzi <kevin@scrye.com> 0.2.2-1
- Update to 0.2.2

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jan 12 2013 François Cami <fcami@fedoraproject.org> - 0.2.1-3
- force-require zathura.

* Tue Jan 08 2013 François Cami <fcami@fedoraproject.org> - 0.2.1-2
- Add fix for djvulibre-devel < 3.5.25 - Thanks to M. Schwendt and E. Echeverria

* Tue Jan 01 2013 François Cami <fcami@fedoraproject.org> - 0.2.1-1
- Initial package.
