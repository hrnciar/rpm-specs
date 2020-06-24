%global major	17
%filter_provides_in %{python3_sitearch}/.*\.so$

Summary:	Library and tool to control NAT in UPnP-enabled routers
Name:		miniupnpc
Version:	2.1
Release:	6%{?dist}
License:	BSD
URL:		http://miniupnp.free.fr/
Source:		http://miniupnp.free.fr/files/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:	cmake
Source1:	USAGE

%description
miniupnpc is an implementation of a UPnP client library, enabling
applications to access the services provided by an UPnP "Internet
Gateway Device" present on the network. In UPnP terminology, it is
a UPnP Control Point.

This package includes upnpc, a UPnP client application for configuring 
port forwarding in UPnP enabled routers.

%package	devel
Summary:	Development files for miniupnpc 
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	devel
This package contains the header files and development documentation
for %{name}.

%package	-n python3-%{name}
Summary:	Python3 interface to %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools

%description	-n python3-%{name}
This package contains python3 interfaces to %{name}.

%prep
%autosetup -p1
cp %{SOURCE1} .

%build
%py3_build

%make_build

%install
%py3_install

%set_build_flags
%make_install INSTALLPREFIX=%{_prefix} LIBDIR=%{_lib}

chmod +x $RPM_BUILD_ROOT%{_libdir}/libminiupnpc.so.%{major}

rm $RPM_BUILD_ROOT%{_libdir}/*.a

%check
make CFLAGS="%{optflags} -DMINIUPNPC_SET_SOCKET_TIMEOUT" check

%ldconfig_scriptlets

%files
%doc Changelog.txt
%doc LICENSE
%doc README
%{_libdir}/libminiupnpc.so.%{major}
%{_bindir}/external-ip
%{_bindir}/upnpc
%doc USAGE

%files		devel
%{_includedir}/miniupnpc
%{_libdir}/libminiupnpc.so
%{_libdir}/pkgconfig/miniupnpc.pc
%{_mandir}/man3/miniupnpc.3*

%files		-n python3-%{name}
%{python3_sitearch}/miniupnpc-%{version}-py3.*.egg-info/
%{python3_sitearch}/miniupnpc*.so

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.1-6
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 15 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-4
- Subpackage python2-miniupnpc has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.1-3
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 06 2019 Kalev Lember <klember@redhat.com> - 2.1-1
- Update to 2.1

* Wed Feb 06 2019 Kalev Lember <klember@redhat.com> - 2.0-13
- Fix FTBFS (#1604853)

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0-10
- Rebuilt for Python 3.7

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.0-9
- Rebuilt for Python 3.7

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 2.0-7
- Python 2 binary package renamed to python2-miniupnpc
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jun 08 2016 François Kooman <fkooman@tuxed.net> - 2.0-1
- update to 2.0

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Sat Oct 31 2015 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.9-6
- Correct buffer overflow in XML parsing (#1270842, #1270182)

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Wed Apr 16 2014 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.9-1
- Update to latest upstream release (#1062206)
- Correct possible DoS crash vector (patch already in tarball) (#1085618)

* Tue Aug 13 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.8-1
- Update to latest upstream release (#996357)
- Build extra python3 module

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 05 2013 Domingo Becker <domingobecker@gmail.com> - 1.6-9
- Added upnpc, a client side tool, to the main package.
- Added USAGE file with instructions on how to use upnpc.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 30 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-6
- Add Changelog.txt to documentation.
- Correct package version in setup.py.
- Correct rpmlint warning on source rpm.
- Filter provides of private python shared object (817311#c19).

* Sat May 26 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-5
- Build python module (817311#c14).

* Mon May 21 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-4
- Use %%name for source and patch names.
- Enable %%check.

* Mon May 7 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-3
- Prefer %%global over %%define.
- Add proper documentation to main package.
- Ensure library is built before making simple test programs.

* Wed May 2 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-2
- Rename package to miniupnpc to match source tarball.
- Add patch to enable build of tests.
- Include manual page to devel package.
- Change License to match LICENSE file.

* Sat Apr 28 2012 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 1.6-1
- Initial libminiupnpc spec.
