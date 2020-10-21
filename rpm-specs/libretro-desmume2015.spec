%global commit  93d5789d60f82436e20ccad05ce9cb43c6e3656e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date    20200228

%global corename desmume2015

Name:           libretro-%{corename}
Version:        0
Release:        0.5.%{date}git%{shortcommit}%{?dist}
Summary:        Port of Desmume to libretro
ExclusiveArch:  i686 x86_64

License:        GPLv2
URL:            https://github.com/libretro/desmume2015
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++

Supplements:    gnome-games%{?_isa}
Supplements:    retroarch%{?_isa}

%description
Port of Desmume to libretro based on Desmume SVN circa 2015.


%prep
%autosetup -n %{corename}-%{commit} -p1


%build
%set_build_flags
%make_build \
    -C desmume \
    GIT_VERSION=%{shortcommit}


%install
%make_install \
    -C desmume \
    prefix=%{_prefix} \
    libdir=%{_libdir}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license desmume/COPYING
%doc desmume/dsm.txt
%{_libdir}/libretro/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.5.20200228git93d5789
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.4.20200228git93d5789
- Update to latest git snapshot

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20190817gitc27bb71
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.2.20190817gitc27bb71
- Remove 'libretro-gtk-0_14-0' dependency

* Mon Oct 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20170817gitc27bb71
- Initial package
