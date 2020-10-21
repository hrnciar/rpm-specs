%global extuuid		refresh-wifi@kgshank.net
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		gse-refresh-wifi
%global giturl		https://github.com/kgshank/%{gitname}


Name:		gnome-shell-extension-refresh-wifi
Version:	6.0
Release:	7%{?dist}
Summary:	GNOME Shell Extension Refresh Wifi Connections by kgshank

License:	GPLv3+
URL:		https://extensions.gnome.org/extension/905/refresh-wifi-connections/
Source0:	%{giturl}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Update to untagged version 8.
Patch0:		%{giturl}/compare/6.0...master.patch#/%{name}-6.0_update_to_v8.patch

BuildArch:	noarch

Requires:	gnome-shell-extension-common

%description
Introduce a manual scan button for new wifi network scan.


%prep
%autosetup -n %{gitname}-%{version} -p 1


%build
# Place license file on toplevel.
%{__mv} %{extuuid}/license COPYING

# Set proper permissions on files.
%{_bindir}/find . -type f -print | %{_bindir}/xargs %{__chmod} -c -x


%install
%{__mkdir} -p %{buildroot}%{extdir}
%{__cp} -pr %{extuuid}/* %{buildroot}%{extdir}


%files
%license COPYING
%doc README.md
%{extdir}


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Björn Esser <besser82@fedoraproject.org> - 6.0-1
- Initial import (rhbz#1520151)

* Sun Dec 03 2017 Björn Esser <besser82@fedoraproject.org> - 6.0-0.1
- Initial rpm release (rhbz#1520151)
