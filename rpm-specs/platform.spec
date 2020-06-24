Name:           platform
Version:        2.1.0.1
Release:        9%{?dist}
Summary:        Platform support library used by libCEC and binary add-ons for Kodi

License:        GPLv2+
URL:            https://github.com/Pulse-Eight/platform/
Source0:        https://github.com/Pulse-Eight/%{name}/archive/p8-%{name}-%{version}.tar.gz
# GPLv2 license file
Source1:        http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
%{summary}.


%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake

%description devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.


%prep
%setup -q -n %{name}-p8-%{name}-%{version}

cp -p %{SOURCE1} .


%build
%cmake .
make %{?_smp_mflags}


%install
%make_install


%ldconfig_scriptlets


%files
%doc README.md
%license gpl-2.0.txt
%{_libdir}/*.so.*


%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/p8-%{name}/
%{_libdir}/pkgconfig/*.pc


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Oct 30 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.1.0.1-1
- Update to 2.1.0.1

* Tue Apr 26 2016 Peter Robinson <pbrobinson@fedoraproject.org> 2.0.1-2
- Move to upstream new p8 naming scheme (rhbz 1327853)

* Fri Feb 05 2016 Mohamed El Morabity <melmorabity@fedoraproject.org> - 2.0.1-1
- Update to 2.0.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Aug 21 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.10-4
- Add Requires on cmake for devel subpackage

* Sun Aug 16 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.10-3
- Add license text file

* Tue Jul 28 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.10-2
- Unbundle fstrcmp library

* Sun Jul 19 2015 Mohamed El Morabity <melmorabity@fedoraproject.org> - 1.0.10-1
- Initiam RPM release
