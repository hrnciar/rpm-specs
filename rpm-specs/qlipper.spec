Name:		qlipper
Version:	5.1.2
Release:	5%{?dist}
License:	GPLv3+
Summary:	Lightweight clipboard history
URL:		https://github.com/pvanek/qlipper
Source0:	https://github.com/pvanek/%{name}/archive/%{version}.tar.gz/%{name}-%{version}.tar.gz
BuildRequires:	gcc-c++
BuildRequires:	cmake
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	qt5-qttools-devel
BuildRequires:	qt5-qtbase-private-devel
# Contains a modified copy of qxt, we cannot use the Fedora one (segfaults)
Provides:       bundled(libqxt) = 0.7.0

%description
Lightweight clipboard history applet.


%prep
%setup -q


%build
%cmake -DCMAKE_BUILD_TYPE=release -DUSE_SYSTEM_QXT=OFF -DUSE_SYSTEM_QTSA=ON
%cmake_build


%install
%cmake_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
%find_lang %{name} --with-qt --without-mo

%files -f %{name}.lang
%license COPYING
%doc README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/qlipper.png


%changelog
* Fri Aug 07 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-5
- Spec fixes against F33
- Source URL fixed

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 21 2019 TI_Eugene <ti.eugene@gmail.com> - 5.1.2-1
- Version bump

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jan 24 2018 TI_Eugene <ti.eugene@gmail.com> - 5.1.1-1
- Version bump

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 17 2017 derschc <lupinix@mailbox.org> - 5.0.0-2
- Fixed RHBZ#1402994 by using the modified, bundled qxt

* Mon Nov 21 2016 TI_Eugene <ti.eugene@gmail.com> - 5.0.0-1
- Version bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 TI_Eugene <ti.eugene@gmail.com> - 2.0.2-1
- Version bump.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 TI_Eugene <ti.eugene@gmail.com> 2.0.1-2
- License upgraded to GPLv3+
- INSTALL_PREFIX removed from %%cmake flags
- "cross-platform" removed from %%description

* Sat Apr 06 2013 TI_Eugene <ti.eugene@gmail.com> 2.0.1-1
- initial packaging for Fedora
