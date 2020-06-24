Name:           nsnake
Version:        3.0.1
Release:        10%{?dist}
Summary:        The classic snake game with textual interface
# the old homepage is down
#URL:            http://nsnake.alexdantas.net/
URL:            https://github.com/alexdantas/nSnake
Source0:        https://github.com/alexdantas/nSnake/archive/v%{version}.tar.gz#/nSnake-%{version}.tar.gz
License:        GPLv3+
BuildRequires:  gcc-c++
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  ncurses-devel

%description
nSnake is a implementation of the classic snake game with textual interface.
It is playable at command-line and uses the nCurses C library for graphics.

%prep
%setup -qn nSnake-%{version}
sed -i -r 's/^VERSION =.*/VERSION = %{version}/' Makefile

%build
make CFLAGS_PLATFORM="%{optflags}" LDFLAGS_PLATFORM="%{?__global_ldflags}" V=1 %{?_smp_mflags}
make doc

%install
%make_install

%files
%doc AUTHORS BUGS ChangeLog README.md TODO doc/html
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man6/nsnake.6*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/games/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}.xpm

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 10 2018 Robin Lee <cheeselee@fedoraproject.org> - 3.0.1-6
- BR gcc-c++ for http://fedoraproject.org/wiki/Changes/Remove_GCC_from_BuildRoot

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Aug 23 2016 Robin Lee <cheeselee@fedoraproject.org> - 3.0.1-1
- Update to 3.0.1 (BZ#1120131)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.5-3
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Christopher Meng <rpm@cicku.me> - 2.0.5-1
- Update to 2.0.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 08 2014 Christopher Meng <rpm@cicku.me> - 2.0.0-1
- Update to 2.0.0

* Tue Jul 30 2013 Christopher Meng <rpm@cicku.me> - 1.7-3
- Move to unversioned docdir.

* Wed May 15 2013 Christopher Meng <rpm@cicku.me> - 1.7-2
- Fix upstream messup.

* Wed May 15 2013 Christopher Meng <rpm@cicku.me> - 1.7-1
- New verson with manpages fix.

* Tue May 14 2013 Christopher Meng <rpm@cicku.me> - 1.5-3
- Fix debuginfo.

* Sun May 12 2013 Christopher Meng <rpm@cicku.me> - 1.5-2
- Some fixes.

* Sat Apr 20 2013 Christopher Meng <rpm@cicku.me> - 1.5-1
- Initial Package.
