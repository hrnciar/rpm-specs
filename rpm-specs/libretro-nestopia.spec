%global commit      3aab0a3db12eab4653874928a1926703cc0ee845
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20191128

%global corename    nestopia

Name:           libretro-%{corename}
Version:        0
Release:        0.2.%{date}git%{shortcommit}%{?dist}
Summary:        Nestopia emulator with libretro interface

License:        GPLv2
URL:            https://github.com/libretro/nestopia
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
Suggests:       gnome-games%{?_isa}
Suggests:       retroarch%{?_isa}

%description
%{summary}.


%prep
%autosetup -n %{corename}-%{commit} -p1


%build
%set_build_flags
%make_build -C libretro GIT_VERSION=%{shortcommit}


%install
%make_install -C libretro prefix=%{_prefix} libdir=%{_libdir}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license COPYING
%{_libdir}/libretro/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20191128git3aab0a3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20191128git3aab0a3
- Update to latest git snapshot
- Remove 'libretro-gtk-0_14-0' dependency

* Tue Oct 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20190921git7f48c21
- Initial package
