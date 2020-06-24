%global commit      f7d0de1f6a69e24d2dd962a308e7f3206c8d2fc8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20191113

%global corename    beetle-wswan

Name:           libretro-%{corename}
Version:        0
Release:        0.2.%{date}git%{shortcommit}%{?dist}
Summary:        Standalone port of Mednafen WonderSwan to libretro, itself a fork of Cygne

License:        GPLv2
URL:            https://github.com/libretro/beetle-wswan-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_wswan.libretro

BuildRequires:  gcc-c++
Suggests:       gnome-games%{?_isa}
Suggests:       retroarch%{?_isa}

%description
%{summary}.


%prep
%autosetup -n %{corename}-libretro-%{commit} -p1


%build
%set_build_flags
%make_build GIT_VERSION=%{shortcommit}


%install
%make_install prefix=%{_prefix} libdir=%{_libdir}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/mednafen_wswan.libretro


%files
%license COPYING
%{_libdir}/libretro


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20191113gitf7d0de1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20191113gitf7d0de1
- Update to latest git snapshot
- Remove 'libretro-gtk-0_14-0' dependency

* Tue Oct 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20190914git925cb8c
- Initial package
