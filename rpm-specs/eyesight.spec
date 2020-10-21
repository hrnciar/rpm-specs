Name:           eyesight
Summary:        Hawaii desktop image viewer
Version:        0.1.4
Release:        13%{?dist}
License:        GPLv2+
URL:            http://hawaiios.org/projects/eyesight
Source0:        https://github.com/hawaii-desktop/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  cmake
BuildRequires:  bzip2-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  desktop-file-utils

%description
Image viewer for the Hawaii desktop.


%prep
%setup -q -n %{name}-%{version}


%build
%cmake .
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}

desktop-file-install --delete-original                          \
        --dir %{buildroot}%{_datadir}/applications           \
        %{buildroot}%{_datadir}/applications/*.desktop

%find_lang %{name} --all-name --with-qt


%files -f %{name}.lang
%{_bindir}/eyesight
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/eyesight.desktop
%dir %{_datadir}/eyesight
%dir %{_datadir}/eyesight/translations
# These short-named translations probably need renaming upstream, since they
# are not picked up by find_lang
%{_datadir}/eyesight/translations/??.qm
%doc COPYING
%doc README.md


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-13
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Jan 23 2016 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.1.4-2
- Rebuild

* Sun Aug 23 2015 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.1.4-1
- Update to latest version

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.1.2-5
- Rebuilt for GCC 5 C++11 ABI change

* Thu Mar 26 2015 Richard Hughes <rhughes@redhat.com> - 0.1.2-4
- Add an AppData file for the software center

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov 10 2013 Pier Luigi Fiorini <pierluigi.fiorini@gmail.com> - 0.1.2-1
- Update to latest version

* Thu Oct 24 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.1-3
- Bulk sad and useless attempt at consistent SPEC file formatting

* Tue Oct 15 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.1-2
- Use %%find_lang properly
- Clarify licence
- Remove old RPM relics

* Mon Sep 16 2013 Lubomir Rintel <lkundrak@v3.sk> - 0.1.1-1
- Initial packaging
