%global with_lua 1
%global with_luajit 0
%global with_sysfs 1
%global with_opcua 1

Name:     4diac-forte
Version:  1.11.0
Release:  2%{?dist}
Summary:  IEC 61499 runtime environment
License:  EPL
URL:      http://eclipse.org/4diac
Source0:  https://git.eclipse.org/c/4diac/org.eclipse.4diac.forte.git/snapshot/org.eclipse.4diac.forte-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: make
BuildRequires: gcc-c++
BuildRequires: systemd
%{?systemd_requires}

%if 0%{?with_opcua}
BuildRequires: open62541-devel >= 1.0
%endif

%if 0%{?with_lua}
BuildRequires: lua-devel >= 5.1
%endif

%if 0%{?with_luajit}
BuildRequires: luajit-devel >= 2.1.0
%endif

%description
The 4DIAC runtime environment (4DIAC-RTE, FORTE) is a small portable
implementation of an IEC 61499 runtime environment targeting small
embedded control devices (16/32 Bit), implemented in C++. It supports
online-reconfiguration of its applications and the real-time capable
execution of all function block types provided by the IEC 61499 standard.

%prep
%setup -q -n org.eclipse.4diac.forte-%{version}

%build
mkdir -p bin/posix
cd bin/posix
%cmake -DFORTE_ARCHITECTURE=Posix \
       -DFORTE_COM_ETH=ON \
       -DFORTE_COM_FBDK=ON \
       -DFORTE_COM_LOCAL=ON \
%if 0%{?with_opcua}
       -DFORTE_COM_OPC_UA=ON -DFORTE_COM_OPC_UA_INCLUDE_DIR=%{_includedir} -DFORTE_COM_OPC_UA_LIB_DIR=%{_libdir} -DFORTE_COM_OPC_UA_LIB=libopen62541.so -DFORTE_COM_OPC_UA_MASTER_BRANCH=ON \
%endif
       -DFORTE_MODULE_CONVERT=ON \
       -DFORTE_MODULE_IEC61131=ON \
%if 0%{?with_sysfs}
       -DFORTE_MODULE_SysFs=ON \
%endif
       -DFORTE_MODULE_UTILS=ON \
%if 0%{?with_lua}
       -DFORTE_USE_LUATYPES=Lua \
%endif
%if 0%{?with_luajit}
       -DFORTE_USE_LUATYPES=LuaJIT \
%endif
       -DFORTE_TESTS=OFF \
       ../..

%make_build

%install
mkdir -p %{buildroot}%{_unitdir}
install -p systemd/4diac-forte.service %{buildroot}%{_unitdir}

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -p systemd/4diac-forte-sysconfig %{buildroot}%{_sysconfdir}/sysconfig/4diac-forte

cd bin/posix
%make_install

%post
%systemd_post 4diac-forte.service

%preun
%systemd_preun 4diac-forte.service

%postun
%systemd_postun_with_restart 4diac-forte.service

%files
%license epl-2.0.html
%{_bindir}/forte
%{_unitdir}/4diac-forte.service
%config(noreplace) %{_sysconfdir}/sysconfig/4diac-forte

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.11.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Oct 07 2019 Jens Reimann <jreimann@redhat.com> - 1.11.0-1
- Update to release 1.11.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Peter Robinson <pbrobinson@fedoraproject.org> 1.9.0-4
- Build fixes and cleanup

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.0-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Apr 19 2018 Jens Reimann <jreimann@redhat.com> - 1.9.0-1.1
- Update to the final release 1.9.0
- Enable Lua integration
- Enable OPC UA integration

* Mon Feb 05 2018 Jens Reimann <jreimann@redhat.com> - 1.9.0.M3-0.1
- Initial version of the package
