%global commit  357e1463a01fe2ca0dd91941aacaaa9944f95e4d
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20200510

%global corename nestopia

Name:           libretro-%{corename}
Version:        0
Release:        0.3.%{date}git%{shortcommit}%{?dist}
Summary:        Nestopia emulator with libretro interface

License:        GPLv2
URL:            https://github.com/libretro/nestopia
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++

Supplements:    gnome-games%{?_isa}
Supplements:    retroarch%{?_isa}

%description
%{summary}.


%prep
%autosetup -n %{corename}-%{commit} -p1


%build
%set_build_flags
%make_build -C libretro GIT_VERSION=%{shortcommit}


%install
%make_install \
    -C libretro \
    libdir=%{_libdir} \
    prefix=%{_prefix}
install -Dp -m0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license COPYING
%{_libdir}/libretro/


%changelog
* Sun Aug 09 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.3.20200510git357e146
- Update to latest git snapshot

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20191128git3aab0a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20191128git3aab0a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20191128git3aab0a3
- Update to latest git snapshot
- Remove 'libretro-gtk-0_14-0' dependency

* Tue Oct 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20190921git7f48c21
- Initial package
