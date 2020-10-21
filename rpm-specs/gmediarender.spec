%global project gmrender-resurrect
%global repo %{project}

# commit
%global forgeurl https://github.com/hzeller/gmrender-resurrect
#%%global commit 4f221e6b85abf85957b547436e982d7a501a1718
#%%global shortcommit %%(c=%%{commit}; echo ${c:0:7})


Name:    gmediarender
Version: 0.0.8
Release: 5%{?dist}
Summary: Resource efficient UPnP/DLNA renderer
License: GPLv2+
# Following is for Forge-hosted projects packaging automation
# https://fedoraproject.org/wiki/Forge-hosted_projects_packaging_automation

%forgemeta -i

URL:     %{forgeurl}
Source:  %{forgesource}

BuildRequires:  gcc
BuildRequires: systemd
BuildRequires: automake
BuildRequires: libupnp-devel
BuildRequires: gstreamer1-devel

Requires: gstreamer1-plugins-good
Requires(pre): shadow-utils
Requires: firewalld-filesystem
Requires(post): firewalld-filesystem
%{?systemd_requires}
Recommends: gstreamer1-plugins-bad-free

%description
GMediaRender is a resource efficient UPnP/DLNA renderer.

%prep
#%%setup -q -n %%repo-%%{commit}
# Replace above with the following if using forge macro
%forgeautosetup
autoreconf -vfi

%build
%configure
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_bindir}
install -m 0755 src/%{name} %{buildroot}%{_bindir}

install -d %{buildroot}%{_datadir}/%{name}
install -m 0644 data/grender-*.png %{buildroot}%{_datadir}/%{name}

install -d %{buildroot}%{_unitdir}
install -m 0644 dist-scripts/fedora/%{name}.service %{buildroot}%{_unitdir}

install -d %{buildroot}%{_prefix}/lib/firewalld/services
install -m 0644 dist-scripts/fedora/*.xml %{buildroot}%{_prefix}/lib/firewalld/services
# Remove ssdp.xml as firewalld already provides it. RHBZ 1768706
rm %{buildroot}%{_prefix}/lib/firewalld/services/ssdp.xml

%pre
getent group %{name} &>/dev/null || groupadd -r %{name}
getent passwd %{name} &>/dev/null || \
    useradd -r -g %{name} -G audio -M -d %{_datadir}/%{name} -s /sbin/nologin \
    -c "GMediaRender DLNA/UPnP Renderer" %{name}

%post
%systemd_post %{name}.service
%firewalld_reload

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service
if [ $1 -eq 0 ]; then
    getent passwd %{name} &>/dev/null && userdel %{name}
    getent group %{name} &>/dev/null && groupdel %{name}
fi

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/grender-*.png
%{_unitdir}/%{name}.service
%{_prefix}/lib/firewalld/services/%{name}.xml

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - Packaging variables read or set by %forgemeta
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - Packaging variables read or set by %forgemeta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jul 16 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.0.8-3
- libupnp rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - Packaging variables read or set by %%forgemeta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 05 2019 Zamir SUN <sztsian@gmail.com> - 0.0.8-1
- Switch back to origin upstrea and update to 0.0.8
- Fixes 1768706

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitbb7ce8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Zamir SUN <sztsian@gmail.com> - 0-0.10.20190121gitbb7ce8e
- Temporary switch to a compatible upstream for libupnp-1.8.* support

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.git4f221e6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Apr 14 2018 Zamir SUN <sztsian@gmail.com> - 0-0.8.20180414git4f221e6
- Fix versioning
- Update to upstream head 4f221e6
- Use forgemeta macro

* Thu Jan 28 2016 mosquito <sensor.wen@gmail.com> - 0.0.7-1.git4003616
- Build for Fedora23

* Sun Mar 29 2015 <admin@vortexbox.org>
- Updated for systemd snippets, added automatic system user/group add
  and removal upon installation, added FirewallD support

* Mon Sep 16 2013 <admin@vortexbox.org>
- Initial release
