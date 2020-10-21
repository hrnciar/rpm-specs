Name:           low-memory-monitor
Version:        2.0
Release:        5%{?dist}
Summary:        Monitors low-memory conditions

License:        GPLv3+
URL:            https://gitlab.freedesktop.org/hadess/low-memory-monitor
Source0:        https://gitlab.freedesktop.org/hadess/low-memory-monitor/uploads/18351c4a6587ba7121594f9dfec05d71/low-memory-monitor-2.0.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  gtk-doc
BuildRequires:  systemd

%description
The Low Memory Monitor is an early boot daemon that will monitor memory
pressure information coming from the kernel, and, first, send a signal
to user-space applications when memory is running low, and then activate
the kernel's OOM killer when memory is running really low.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description doc

This package contains the documentation for %{name}.

%prep
%autosetup


%build
%meson -Dgtk_doc=true -Dtrigger_kernel_oom=false
%meson_build


%install
%meson_install


%post
%systemd_post low-memory-monitor.service

%preun
%systemd_preun low-memory-monitor.service

%postun
%systemd_postun_with_restart low-memory-monitor.service


%files
%license COPYING
%doc NEWS README.md
%{_unitdir}/low-memory-monitor.service
%{_libexecdir}/low-memory-monitor
%{_datadir}/dbus-1/system.d/org.freedesktop.LowMemoryMonitor.conf

%files doc
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/%{name}/

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 19 2019 Bastien Nocera <bnocera@redhat.com> - 2.0-3
+ low-memory-monitor-2.0-3
- Disable OOM killer by default for now
- Import into Fedora (#1769843)

* Mon Nov 18 2019 Bastien Nocera <bnocera@redhat.com> - 2.0-2
+ low-memory-monitor-2.0-2
- Rename -docs subpackage to -doc

* Thu Nov 14 2019 Bastien Nocera <bnocera@redhat.com> - 2.0-1
+ low-memory-monitor-2.0-1
- Update to 2.0

* Thu Nov 07 2019 Bastien Nocera <bnocera@redhat.com> - 1.1-2
+ low-memory-monitor-1.1-2
- Add missing requires for the main package in the docs one
- Add config tag for low-memory-monitor.conf

* Thu Nov 07 2019 Bastien Nocera <bnocera@redhat.com> - 1.1-1
+ low-memory-monitor-1.1-1
- Initial Fedora packaging
