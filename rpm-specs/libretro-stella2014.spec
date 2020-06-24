%global commit      722744c11b36c1614740b6060d0bdb187660ffac
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20191129

%global corename    stella2014

Name:           libretro-%{corename}
Version:        0
Release:        0.2.%{date}git%{shortcommit}%{?dist}
Summary:        Port of Stella to libretro

License:        GPLv2
URL:            https://github.com/libretro/stella2014-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

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
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license stella/license.txt
%doc README.md
%{_libdir}/libretro/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20191129git722744c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20191129git722744c
- Update to latest git snapshot
- Remove 'libretro-gtk-0_14-0' dependency

* Mon Oct 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20190921git6d74ad9
- Initial package
