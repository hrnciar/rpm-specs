Name:       lifeograph
Version:    1.5.1.1
Release:    3%{?dist}
Summary:    A diary program

License:    GPLv3+
URL:        http://%{name}.wikidot.com/start
Source0:    https://launchpad.net/%{name}/trunk/1.5.1/+download/%{name}-%{version}.tar.bz2

# Correct desktop file to add semi colons to a few fields
Patch0:     %{name}-0.11.1-desktop-file.patch

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  enchant2-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtkmm30-devel
BuildRequires:  intltool
BuildRequires:  libgcrypt-devel
Requires:       hicolor-icon-theme

%description
Lifeograph is a diary program to take personal notes on life. It has all
essential functionality expected in a diary program and strives to have
a clean and streamlined user interface.


%prep
%autosetup -c %{name}-%{version} -S patch
sed -i 's|<build_time.h>|"build_time.h"|' src/lifeograph.cpp

%build
./create_time_build_time_header.sh %{name} ./src/ ./src/
find . -name "build_time.h" -print

%cmake -DCMAKE_BUILD_TYPE=Release .
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}/%{_datadir}/applications/
cp -p build/%{name}.desktop %{buildroot}/%{_datadir}/applications

mkdir -p %{buildroot}/%{_mandir}/man1/
cp -p %{name}.1 %{buildroot}/%{_mandir}/man1/

mkdir -p %{buildroot}/%{_datadir}/mime/packages/
cp -p %{name}.xml %{buildroot}/%{_datadir}/mime/packages/

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}-symbolic.svg

%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/net.sourceforge.%{name}.appdata.xml
%{_mandir}/man1/%{name}*
%{_datadir}/mime/packages/%{name}*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Apr 16 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.1.1-1
- Update to 1.5.1

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 12 2019 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.5.0-1
- Update to latest release
- use autosetup
- Fix FTBFS

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.4.2-5
- Remove obsolete scriptlets

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon May 15 2017 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_27_Mass_Rebuild

* Mon May 01 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.2-1
- Update to 1.4.2

* Mon Feb 13 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.1-1
- Update to lastest upstream release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 14 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.0-2
- Fix build

* Mon Nov 14 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.0-1
- Update to stable release
- Use license macro

* Mon Oct 17 2016 Ankur SInha <ankursinha AT fedoraproject DOT org> - 1.4.0-0.4.rc2
- Fix setup macro

* Mon Oct 17 2016 Ankur SInha <ankursinha AT fedoraproject DOT org> - 1.4.0-0.3.rc2
- correct changelog

* Mon Oct 17 2016 Ankur SInha <ankursinha AT fedoraproject DOT org> - 1.4.0-0.2.rc2
- Update to new rc

* Sun Aug 28 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.4.0-0.1.rc1
- Update to latest upstream release - 1.4.0.rc1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.3.0-1
- Update to latest upstream release

* Fri Jan 15 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.2.1-1
- Update to latest upstream release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.0-4
- Rebuilt for GCC 5 C++11 ABI change

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 1.1.0-3
- update mime scriptlet

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Aug 17 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.1.0-1
- Update to latest upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-3.r1642
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Apr 11 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.0.1-2.r1642
- Update to revision 1642 to fix gnome 3.12 crash

* Mon Feb 24 2014 Ankur Sinha <ankursinha AT fedoraproject DOT org> 1.0.1-1
- Update to latest upstream release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Jun 15 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.11.1-2
- Replace sed with patch
- Update desktop database
- Bug# 973868

* Thu Jun 13 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.11.1-1
- Initial rpmbuild
