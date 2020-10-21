Name:		spi-tools
Version:	0.8.5
Release:	1%{?dist}
Summary:	Simple command line tools to help using Linux spidev devices

License:	GPLv2
URL:		https://github.com/cpb-/spi-tools/
Source0:	https://github.com/cpb-/spi-tools/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Don-t-override-the-compiler-flags-with-nonsense-ones.patch

BuildRequires:	gcc
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	help2man

%description
This package contains spi-config and spi-pipe, simple command line tools to
help using Linux spidev devices.


%prep
%setup -q
%patch0 -p1


%build
autoreconf -fi
%configure
%make_build


%install
%make_install


%files
%{_bindir}/spi-config
%{_bindir}/spi-pipe
%{_mandir}/man1/spi-config.1*
%{_mandir}/man1/spi-pipe.1*
%doc README.md
%license LICENSE


%changelog
* Sat Oct 10 16:02:10 BST 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 0.8.5-1
- Update to 0.8.5

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Jan 19 2020 Lubomir Rintel <lkundrak@v3.sk> - 0.8.4-1
- Update to 0.8.4

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 18 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.8.3-1
- Update to 0.8.3
- Drop Group tag
- Fix Source

* Sat Mar 24 2018 Lubomir Rintel <lkundrak@v3.sk> - 0.8.1-1
- Initial packaging
