Summary: GUI client for Fwknop
Name: fwknop-gui
Version: 1.3.1
Release: 11%{?dist}
License: GPLv3+
URL: https://incomsystems.biz/fwknop-gui/
Source: %{url}/downloads/%{name}-%{version}.tar.gz
BuildRequires: gcc-c++ make cmake
BuildRequires: fwknop-devel
BuildRequires: wxGTK3-devel
BuildRequires: libcurl-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gpgme-devel
BuildRequires: pkgconfig(libqrencode)
BuildRequires: asciidoc

%description
Fwknop-gui is a cross platform gui that can save
and send knocks to a server running fwknopd.

%prep
%autosetup -n %{name}

%build
%cmake . -DwxWidgets_CONFIG_EXECUTABLE=%{_bindir}/wx-config-3.0
%make_build

%install
%make_install
install -p -m0644 -D %{name}.appdata.xml %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/fwknop-gui.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%files
%license LICENSE
%dir %{_datadir}/%{name}
%doc %{_datadir}/%{name}/help.html
%doc %{_mandir}/man8/%{name}.8*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Björn Esser <besser82@fedoraproject.org> - 1.3.1-9
- Rebuilt (libqrencode.so.4)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.3.1-2
- Rebuild for gpgme 1.18

* Mon Sep 05 2016 Jakub Jelen <jjelen@redhat.com> - 1.3.1-1
- New upstream release (fixing a bug in the QR code prompt)

* Wed Aug 10 2016 Jakub Jelen <jjelen@redhat.com> - 1.3-2
- Packaging tweaks

* Fri Aug 05 2016 Jakub Jelen <jjelen@redhat.com> - 1.3-1
- Initial release
