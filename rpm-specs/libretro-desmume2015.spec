%global commit      c27bb71aa28250f6da1576e069b4b8cc61986beb
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20190817

%global corename    desmume2015

Name:           libretro-%{corename}
Version:        0
Release:        0.3.%{date}git%{shortcommit}%{?dist}
Summary:        Port of Desmume to libretro
ExclusiveArch:  i686 x86_64

License:        GPLv2
URL:            https://github.com/libretro/desmume2015
Source0:        %{url}/archive/%{commit}/%{name}-%{version}.%{date}git%{shortcommit}.tar.gz
Source1:        https://raw.githubusercontent.com/flathub/org.gnome.Games/master/libretro-cores/%{corename}.libretro

BuildRequires:  gcc-c++
Suggests:       gnome-games%{?_isa}
Suggests:       retroarch%{?_isa}

%description
Port of Desmume to libretro based on Desmume SVN circa 2015.


%prep
%autosetup -n %{corename}-%{commit} -p1


%build
%set_build_flags
cd desmume
%make_build GIT_VERSION=%{shortcommit}


%install
cd desmume
%make_install prefix=%{_prefix} libdir=%{_libdir}
install -Dp -m 0644 %{SOURCE1} %{buildroot}%{_libdir}/libretro/%{corename}.libretro


%files
%license desmume/COPYING
%doc desmume/dsm.txt
%{_libdir}/libretro/


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20190817gitc27bb71
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.2.20190817gitc27bb71
- Remove 'libretro-gtk-0_14-0' dependency

* Mon Oct 07 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20170817gitc27bb71
- Initial package
