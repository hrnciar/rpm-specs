Name:           tikzit
URL:            https://tikzit.github.io/
Version:        2.1.5
Release:        1%{?dist}
License:        GPLv3+
Summary:        Diagram editor for pgf/TikZ
Source:         https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

Requires:       hicolor-icon-theme
BuildRequires:  gcc-c++
BuildRequires:  flex
BuildRequires:  bison
BuildRequires:  qt5-qtbase-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  desktop-file-utils

%description
TikZiT is a graphical tool for rapidly creating an editing node-and-edge
style graphs. It was originally created to aid in the typesetting of
"dot" diagrams of interacting quantum observables, but can be used as a
general graph editing program.

%prep
%autosetup -n %{name}-%{version}

%build
export OBJCFLAGS="%{optflags}"
%qmake_qt5 PREFIX=%{_prefix}
%make_build V=1
sed -i "s|\r||g" README.md

%install
%make_install INSTALL_ROOT="%{buildroot}"

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

%files
%{_bindir}/tikzit
%license COPYING
%doc README.md
%{_datadir}/mime/packages/user-tikz-document.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/tikzit.1.gz

%changelog
* Fri May 08 2020 W. Michael Petullo <mike@flyn.org> 2.1.5-1
- New upstream version

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 2.1.4-3
- Rebuild for poppler-0.84.0

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 17 2019 W. Michael Petullo <mike@flyn.org> 2.1.4-1
- New upstream version
- BuildRequire poppler-qt5-devel
- Install man page

* Thu Dec 06 2018 W. Michael Petullo <mike@flyn.org> 2.0-1
- New upstream version

* Tue Nov 04 2014 Eric Smith <brouhaha@fedorapeople.org> 1.0-1
- Initial version
