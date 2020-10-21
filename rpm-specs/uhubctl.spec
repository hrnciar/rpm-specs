Name:           uhubctl
Version:        2.2.0
Release:        2%{?dist}
Summary:        USB hub per-port power control

License:        GPLv2
URL:            https://github.com/mvp/%{name}
Source0:        https://github.com/mvp/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  libusbx-devel

%description
uhubctl is utility to control USB power per-port on smart USB hubs. Smart hub
is defined as one that implements per-port power switching.


%prep
%autosetup -p1

# Ensure version doesn't have '-dev'
echo %{version} > VERSION


%build
%make_build


%install
%make_install


%files
%license COPYING LICENSE
%doc README.md
%{_sbindir}/%{name}


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Scott K Logan <logans@cottsay.net> - 2.2.0-1
- Initial package (rhbz#1840296)
