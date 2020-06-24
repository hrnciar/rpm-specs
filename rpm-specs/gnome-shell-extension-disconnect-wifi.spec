%global extuuid		disconnect-wifi@kgshank.net
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		gse-disconnect-wifi
%global giturl		https://github.com/kgshank/%{gitname}


Name:		gnome-shell-extension-disconnect-wifi
Version:	17
Release:	6%{?dist}
Summary:	GNOME Shell Extension Disconnect Wifi by kgshank

License:	GPLv3+
URL:		https://extensions.gnome.org/extension/904/disconnect-wifi/
Source0:	%{giturl}/archive/V%{version}.tar.gz#/%{name}-%{version}.tar.gz

# Update to untagged version 8.
Patch0:		%{giturl}/compare/V17...master.patch#/%{name}-17_update_to_V18.patch

BuildArch:	noarch

Requires:	gnome-shell-extension-common

%description
Adds a Disconnect option for Wifi in status menu, when a network is
connected.  Shows a Reconnect option, after network is disconnected.


%prep
%autosetup -n %{gitname}-%{version} -p 1


%build
# Place license file on toplevel.
%{__mv} %{extuuid}/license COPYING

# Remove useless files.
%{_bindir}/find . -name '*.po' -print -delete
%{_bindir}/find . -name '*.pot' -print -delete

# Set proper permissions on files.
%{_bindir}/find . -type f -print | %{_bindir}/xargs %{__chmod} -c -x


%install
%{__mkdir} -p %{buildroot}%{extdir}
%{__cp} -pr %{extuuid}/* %{buildroot}%{extdir}
%{__cp} -pr %{extuuid}/locale %{buildroot}%{_datadir}

# Remove unneded files.
%{__rm} -fr %{buildroot}%{extdir}/{LICENSE,README*,locale,schemas}

# Create manifest for i18n.
%find_lang %{name} --all-name


%files -f %{name}.lang
%license COPYING
%doc README.md
%{extdir}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 17-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 17-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 03 2017 Björn Esser <besser82@fedoraproject.org> - 17-1
- Initial import (rhbz#1520150)

* Sun Dec 03 2017 Björn Esser <besser82@fedoraproject.org> - 17-0.1
- Initial rpm release (rhbz#1520150)
