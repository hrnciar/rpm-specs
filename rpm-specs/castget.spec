Name:           castget
Version:        2.0.1
Release:        3%{?dist}
Summary:        A command-line podcast downloader

License:        LGPLv2+
URL:            https://castget.johndal.com/
Source0:        https://download-mirror.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  id3lib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libxml2-devel

%description
castget is a simple, command-line based RSS enclosure downloader. It is
primarily intended for automatic, unattended downloading of podcasts.


%prep
%autosetup


%build
%configure
%make_build


%install
%make_install


%files
%license COPYING.LIB COPYING
%doc AUTHORS CHANGES.md ChangeLog.old INSTALL castgetrc.example
%{_bindir}/%{name}
%{_mandir}/man?/*


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Oct 26 2019 Ed Marshall <esm@logic.net> - 2.0.1-1
- Update to 2.0.1.

* Fri Oct 11 2019 Ed Marshall <esm@logic.net> - 2.0.0-1
- Update to 2.0.0.

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Ed Marshall <esm@logic.net> - 1.2.4-1
- Initial package.
