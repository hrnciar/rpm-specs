%global realname urdfdom_headers

Name:		urdfdom-headers
Version:	1.0.2
Release:	4%{?dist}
Summary:	The URDF (U-Robot Description Format) headers

License:	BSD
URL:		http://ros.org/wiki/urdf
Source0:	https://github.com/ros/%{realname}/archive/%{version}/%{realname}-%{version}.tar.gz
BuildArch:	noarch

# Install configs to arch independent paths and try to work around cmake's auto-generated architecture check
# https://github.com/ros/urdfdom_headers/issues/27
Patch0:         urdfdom-headers-fedora.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:	cmake

%description
%{summary}

%package devel
Summary: The URDF (U-Robot Description Format) headers
Requires: pkgconfig
BuildArch: noarch
Provides: %{name}-static = %{version}-%{release}

%description devel
The URDF (U-Robot Description Format) headers provides core data structure
headers for URDF.

For now, the details of the URDF specifications reside on
http://ros.org/wiki/urdf

%prep
%setup -qn %{realname}-%{version}
%patch0 -p1 -b .fedora

%build
mkdir build; pushd build
%cmake ..
popd
make -C build %{?_smp_mflags}


%install
make -C build install DESTDIR=%{buildroot}

%files devel
%license LICENSE
%doc README.md
%{_includedir}/urdf_exception
%{_includedir}/urdf_model
%{_includedir}/urdf_model_state
%{_includedir}/urdf_sensor
%{_includedir}/urdf_world
%{_datadir}/pkgconfig/*.pc
%{_datadir}/%{realname}

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 23 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.0.2-1
- Update to 1.0.2

* Fri Nov 23 2018 Till Hofmann <thofmann@fedoraproject.org> - 1.0.1-1
- Update to 1.0.1

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jul 17 2016 Rich Mattes <richmattes@gmail.com> - 0.4.2-1
- Update to release 0.4.2
* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 23 2015 Rich Mattes <richmattes@gmail.com> - 0.3.0-3
- Remove patch that moves include files to /usr/include/urdf

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr 16 2014 Rich Mattes <richmattes@gmail.com> - 0.3.0-1
- Update to release 0.3.0

* Mon Aug 19 2013 Rich Mattes <richmattes@gmail.com> - 0.2.3-1
- Update to release 0.2.3
- Move upstream to github

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Apr 09 2013 Rich Mattes <richmattes@gmail.com> - 0.2.2-2
- Added -static virtual provides to -devel subpackage
- Moved package description to -devel subpackage

* Tue Mar 12 2013 Rich Mattes <richmattes@gmail.com> - 0.2.2-1
- Update to release 0.2.2
- Don't install incorrect LICENSE file

* Tue Oct 16 2012 Rich Mattes <richmattes@gmail.com> - 0.2.1-1
- Update to release 0.2.1

* Wed Sep 26 2012 Rich Mattes <richmattes@gmail.com> - 0.2.0-1
- Initial package
