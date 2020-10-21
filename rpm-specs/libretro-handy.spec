%global commit  5ff55817eafbb1930e222ea2493c22804c872904
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20200317

%global corename handy

Name:           libretro-%{corename}
Version:        0
Release:        0.5.%{date}git%{shortcommit}%{?dist}
Summary:        Atari Lynx emulator Handy for libretro

License:        zlib
URL:            https://github.com/libretro/libretro-handy
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++

Supplements:    gnome-games%{?_isa}
Supplements:    retroarch%{?_isa}

%description
K. Wilkins' Atari Lynx emulator Handy for libretro.


%prep
%autosetup -n libretro-%{corename}-%{commit} -p1


%build
%set_build_flags
%make_build GIT_VERSION=%{shortcommit}


%install
%make_install prefix=%{_prefix} libdir=%{_libdir}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license lynx/license.txt
%doc README.md
%{_libdir}/libretro/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20200317git5ff5581
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.4.20200317git5ff5581
- Update to latest git snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20191129gitfbd7e0d
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.2.20191129gitfbd7e0d
- Update to latest git snapshot
- Remove 'libretro-gtk-0_14-0' dependency

* Tue Oct 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.2.20190801git6b19a4f
- Initial package
