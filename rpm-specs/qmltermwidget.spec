Name:       qmltermwidget
Summary:    A port of QTermWidget to QML
Version:    0.2.0
Release:    5%{?dist}
License:    GPLv2+
URL:        https://github.com/Swordfish90/%{name}
Source0:    %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

Patch0:     qtw-0.2.0--fix-missing-includes.patch

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Quick)

%description
This project is a QML port of QTermWidget. It is written
to be as close as possible to the upstream project in order
to make cooperation possible.

%prep
%setup -q
%patch0 -p1


%build
%qmake_qt5
%make_build


%install
make install INSTALL_ROOT=%{buildroot}


%files
%license LICENSE
%doc README.md AUTHORS
%{_qt5_qmldir}/QMLTermWidget/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Artur Iwicki <fedora@svgames.pl> - 0.2.0-5
- Fix build errors due to missing #includes

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Dec 19 2018 Artur Iwicki <fedora@svgames.pl> - 0.2.0-1
- Update to latest upstream version

* Sat Jul 21 2018 Artur Iwicki <fedora@svgames.pl> - 0.1.0-6.20171027git08958f7
- Use "%%{_qt5_qmldir}" instead of "%%{_qt5_prefix}/qml"

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-5.20171027git08958f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4.20171027git08958f7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Nov 10 2017 Artur Iwicki <fedora@svgames.pl> 0.1.0-3.20171027git08958f7
- Fix typo in Source0
- Fix typo in License: tag
- Remove the 'pkgconfig(Qt5Declarative)' build-requirement

* Fri Nov 10 2017 Artur Iwicki <fedora@svgames.pl> 0.1.0-2.20171027.git.08958f7
- Update to newest upstream snapshot (contains some bugfixes)

* Wed Jul 13 2016 Neal Gompa <ngompa13@gmail.com> 0.1.0-1
- Initial packaging
