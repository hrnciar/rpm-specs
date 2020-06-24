Name:           nudoku
Version:        2.0.0
Release:        2%{?dist}
Summary:        Ncurses based Sudoku game
License:        GPLv3
Url:            https://github.com/jubalh/%{name}
Source0:        https://github.com/jubalh/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  cairo-devel
BuildRequires:  gettext-devel
BuildRequires:  ncurses-devel

%description
nudoku is a ncurses based Sudoku game.

%prep
%autosetup -n %{name}-%{version} 

%build
export CFLAGS="%{build_cflags} -I%{_datadir}/gettext"
%configure --enable-cairo
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/nudoku
%{_mandir}/man6/nudoku.6.*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Aug 18 2019 Robin Lee <cheeselee@fedoraproject.org> - 2.0.0-1
- Release 2.0.0 (RHBZ#1742392)

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Sep  1 2018 Robin Lee <cheeselee@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0 (BZ#1569510)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 08 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.2.5-1
- Update to version 0.2.5

* Tue Mar 29 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.2.4-2
- Fix license
- Fix description
- Fix Summary
- Fix group

* Mon Mar 07 2016 Fabio Alessandro Locati <fale@fedoraproject.org> - 0.2.4-1
- First Fedora Release
