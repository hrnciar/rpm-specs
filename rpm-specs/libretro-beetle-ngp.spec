%global commit  3d31f4ad9f8d8367ccf492f04640c8ca172ef81d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20200518

%global corename beetle-ngp

Name:           libretro-%{corename}
Version:        0
Release:        0.2.%{date}git%{shortcommit}%{?dist}
Summary:        Standalone port of Mednafen NGP to the libretro API, itself a fork of Neopop

License:        GPLv2
URL:            https://github.com/libretro/beetle-ngp-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_ngp.libretro

BuildRequires:  gcc-c++

Supplements:    gnome-games%{?_isa}
Supplements:    retroarch%{?_isa}

%description
%{summary}.


%prep
%autosetup -n %{corename}-libretro-%{commit} -p1


%build
%set_build_flags
%make_build GIT_VERSION=%{shortcommit}


%install
%make_install prefix=%{_prefix} libdir=%{_libdir}
install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_libdir}/libretro/mednafen_ngp.libretro


%files
%license COPYING
%doc readme.md
%{_libdir}/libretro/


%changelog
* Thu May 21 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.2.20200518git3d31f4a
- Update to latest git snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20191121gitd839c35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20191121gitd839c35
- Update to latest git snapshot
- Remove 'libretro-gtk-0_14-0' dependencie

* Tue Oct 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20190911git6130e40
- Initial package
