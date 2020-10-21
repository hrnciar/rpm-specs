%global commit      cb4aa3ee72f98b0891a7bac5c9dac458cdba4d34
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date        20190914

%global corename    prosystem

Name:           libretro-%{corename}
Version:        0
Release:        0.4.%{date}git%{shortcommit}%{?dist}
Summary:        Port of ProSystem to the libretro API

License:        GPLv2
URL:            https://github.com/libretro/prosystem-libretro
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
%license License.txt
%doc README.md
%{_libdir}/libretro/


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.4.20190914gitcb4aa3e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.20190914gitcb4aa3e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Dec 04 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.2.20190914gitcb4aa3e
- Remove 'libretro-gtk-0_14-0' dependency

* Tue Oct 08 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-0.1.20190914gitcb4aa3e
- Initial package
