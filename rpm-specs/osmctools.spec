%global commit f341f5f237737594c1b024338f0a2fc04fabdff3

Name:           osmctools
Version:        0.9
Release:        6%{?dist}
Summary:        Tools to manipulate OpenStreetMap files

# Debian man pages are GPLv2+
License:        AGPLv3 and GPLv2+
URL:            https://gitlab.com/osm-c-tools/osmctools
Source0:        https://gitlab.com/osm-c-tools/osmctools/repository/archive.tar.gz?ref=%{version}#/%{name}-%{version}.tar.gz
# Man pages from Debian
Source1:        osmconvert.1
Source2:        osmfilter.1
Source3:        osmupdate.1

BuildRequires:  gcc
BuildRequires:  zlib-devel
BuildRequires:  autoconf
BuildRequires:  automake
Requires:       wget


%description
Small collection of basic OpenStreetMap tools, include converter, filter and
updater files.

Programs include:
* osmconvert - Converter of OSM files
* osmfilter - The experimental OSM filters data
* osmupdate - Update OSM files.


%prep
%autosetup -n %{name}-%{version}-%{commit}


%build
autoreconf -fvi
%configure
%make_build


%install
%make_install

# Install man pages
install -d %{buildroot}%{_mandir}/man1/
for i in %{SOURCE1} %{SOURCE2} %{SOURCE3}; do
  install -p -m 0644 ${i} %{buildroot}%{_mandir}/man1/
done


%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/osmconvert
%{_bindir}/osmfilter
%{_bindir}/osmupdate
%{_mandir}/man1/osmconvert.1*
%{_mandir}/man1/osmfilter.1*
%{_mandir}/man1/osmupdate.1*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 02 2018 Andrea Musuruane <musuruan@gmail.com> - 0.9-1
- Updated to new upstream release
- Updated man pages from Debian

* Wed Feb 21 2018 Andrea Musuruane <musuruan@gmail.com> - 0.8-3
- Added gcc dependency

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 25 2017 Andrea Musuruane <musuruan@gmail.com> - 0.8-1
- Updated to new upstream release
- Updated man pages from Debian

* Fri Aug 25 2017 Andrea Musuruane <musuruan@gmail.com> - 0.7-2
- Fixed License tag

* Sun Jun 25 2017 Andrea Musuruane <musuruan@gmail.com> - 0.7-1
- First release

