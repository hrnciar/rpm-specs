%global commit      ce63911ecbd794f24d737669e5add4f4e98d14e6
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20191113

%global corename    beetle-pce-fast

Name:           libretro-%{corename}
Version:        0
Release:        0.3.%{date}git%{shortcommit}%{?dist}
Summary:        Standalone port of Mednafen PCE Fast to libretro

License:        GPLv2
URL:            https://github.com/libretro/beetle-pce-fast-libretro
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/mednafen_pce_fast.libretro

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
install -m 0644 -Dp %{SOURCE1} %{buildroot}%{_libdir}/libretro/mednafen_pce_fast.libretro


%files
%license COPYING
%doc README.md
%{_libdir}/libretro/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20191113gitce63911
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.2.20191113gitce63911
- Update to latest git snapshot
- Remove 'libretro-gtk-0_14-0' dependency

* Tue Oct 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.2.20190911git7bbbdf1
- Initial package
