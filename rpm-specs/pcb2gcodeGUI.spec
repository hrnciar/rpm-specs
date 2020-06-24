Name:		pcb2gcodeGUI
Version:	1.3.2
Release:	8%{?dist}
Summary:	A GUI for pcb2gcode

License:	GPLv3+
URL:		https://github.com/pcb2gcode/pcb2gcodeGUI/
Source0:	https://github.com/pcb2gcode/%{name}/archive/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:	pkgconfig(Qt5)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Svg)

Requires:       pcb2gcode

%description
A GUI for pcb2gcode, a software for the isolation, routing and drilling
of PCBs.

%prep
%setup -q


%build
%qmake_qt5 PREFIX=%{_prefix}
make %{?_smp_mflags}


%install
make install INSTALL_ROOT=%{buildroot}


%files
%{_bindir}/pcb2gcodeGUI
%doc README.md
%license LICENSE


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Dec  4 2016 Lubomir Rintel <lkundrak@v3.sk> - 1.3.2-1
- Initial packaging
