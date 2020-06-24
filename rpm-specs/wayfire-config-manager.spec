# LTO
%global optflags        %{optflags} -flto
%global build_ldflags   %{build_ldflags} -flto

Name:           wayfire-config-manager
Version:        0.4.0
Release:        2%{?dist}
Summary:        Wayfire Config Manager

License:        MIT
URL:            https://github.com/WayfireWM/wcm
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(wayfire)
BuildRequires:  pkgconfig(wf-config) >= 0.4.0

Requires:       hicolor-icon-theme

%description
%{summary}.


%prep
%autosetup -n wcm-%{version} -p1


%build
%meson
%meson_build


%install
%meson_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop


%files
%license LICENSE
%{_bindir}/wcm
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/wayfire/


%changelog
* Sun Mar 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-2
- Enable LTO

* Sun Mar 22 2020 Artem Polishchuk <ego.cordatus@gmail.com> - 0.4.0-1
- Update to 0.4.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-4.20190920git2f3e075
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Sep 26 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0-3.20190920git2f3e075
- Tiny fixes

* Thu Sep 26 2019 gasinvein <gasinvein@gmail.com>
- Initial package
