%global git_commit bfb667080936ca5c2d23b3282f5893931ec38d3f
%global git_date 20180615

%global git_short_commit %(echo %{git_commit} | cut -c -8)
%global git_suffix %{git_date}git%{git_short_commit}

Name:           airspyone_host
Version:        1.0.9
Release:        8.%{git_suffix}%{?dist}
Summary:        AirSpy host tools and library

License:        GPLv2+
URL:            http://airspy.com/
Source0:        https://github.com/airspy/%{name}/archive/%{git_commit}/%{name}-%{git_suffix}.tar.gz

BuildRequires:  gcc-c++, cmake, libusbx-devel, systemd
Requires:       systemd-udev

%description
Software for AirSpy, a project to produce a low cost, open
source software radio platform.

%package devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
License:        MIT and BSD
Summary:        Development files for %{name}

%description devel
Files needed to develop software against libairspy.

%prep
%setup -q -n %{name}-%{git_commit}

# Remove win stuff
rm -rf libairspy/vc

# Fix udev rule
sed -i -e 's/GROUP="plugdev"/ENV{ID_SOFTWARE_RADIO}="1"/g' airspy-tools/52-airspy.rules

%build
mkdir build
cd build
%cmake ../ -DINSTALL_UDEV_RULES=on

make %{?_smp_mflags}

%install
make -C build install DESTDIR=%{buildroot}

# Remove static object
rm -f %{buildroot}%{_libdir}/libairspy.a

# Move udev rule to correct location
mkdir -p %{buildroot}%{_udevrulesdir}
mv %{buildroot}%{_sysconfdir}/udev/rules.d/52-airspy.rules %{buildroot}%{_udevrulesdir}

%post
%?ldconfig
%udev_rules_update

%postun
%?ldconfig
%udev_rules_update

%files
%license airspy-tools/LICENSE.md
%doc README.md
%{_bindir}/airspy_*
%{_libdir}/libairspy.so.*
%{_udevrulesdir}/52-airspy.rules

%files devel
%{_includedir}/libairspy
%{_libdir}/pkgconfig/libairspy.pc
%{_libdir}/libairspy.so

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-8.20180615gitbfb66708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-7.20180615gitbfb66708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-6.20180615gitbfb66708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.9-5.20180615gitbfb66708
- Fixed FTBFS by adding gcc-c++ requirement
  Resolves: rhbz#1603360

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.9-4.20180615gitbfb66708
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.9-3.20180615gitbfb66708
- Various fixes according to review

* Fri Jun 15 2018 Jaroslav Škarvada <jskarvad@redhat.com> - 1.0.9-2.20180615gitbfb66708
- Update for Fedora

* Mon Dec 19 2016 Dave Burgess <dvd.burgess@gmail.com> - 1.0.9-1
- Initial package
