name: adwaita-blue-gtk-theme
Version: 3.22.21.0
Release: 5%{?dist}
Summary: Adwaita GTK theme variant with blue titlebars and headerbars

License: GPLv3
URL: https://github.com/ryanlerch/adwaita-blue 
Source0: https://github.com/ryanlerch/adwaita-blue/releases/download/v%{version}/adwaita-blue-%{version}.tar.gz

BuildArch: noarch

BuildRequires: sassc 

%description
Adwaita GTK theme variant with blue titlebars and headerbars

%prep
%setup -q -n adwaita-blue-%{version}

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%{_datadir}/themes/Adwaita-blue/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.21.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.21.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.21.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.21.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.22.21.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Oct 09 2017 Ryan Lerch <rlerch@redhat.com> - 3.22.21.0-0
- Initial Release

