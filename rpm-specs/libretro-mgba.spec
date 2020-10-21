%global commit      429d2f2a6ab55716a3465cd709d3d16e3a1b70de
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20191026

%global corename    mgba

Name:           libretro-%{corename}
Version:        0.1.1
Release:        0.3.%{date}git%{shortcommit}%{?dist}
Summary:        mGBA Game Boy Advance Emulator

License:        MPLv2.0
URL:            https://github.com/libretro/mgba
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
Suggests:       gnome-games%{?_isa}
Suggests:       retroarch%{?_isa}

%description
mGBA is an emulator for running Game Boy Advance games. It aims to be faster and
more accurate than many existing Game Boy Advance emulators, as well as adding
features that other emulators lack. It also supports Game Boy and Game Boy Color
games.


%prep
%autosetup -n %{corename}-%{commit} -p1


%build
%set_build_flags
%make_build GIT_VERSION=%{shortcommit}


%install
%make_install prefix=%{_prefix} libdir=%{_libdir}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license LICENSE
%doc README.md PORTING.md CONTRIBUTING.md CHANGES
%{_libdir}/libretro/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.3.20191026git429d2f2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-0.2.20191026git429d2f2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.1-0.1.20191026git429d2f2
- Update to latest git snapshot
- Remove 'libretro-gtk-0_14-0' dependency

* Tue Oct 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.1.1-0.1.20190912git4865aaa
- Initial package
