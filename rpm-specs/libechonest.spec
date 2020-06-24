
%define qt5 1
#define tests 1

Name:		libechonest
Version: 	2.3.0
Release:	12%{?dist}
Summary:	C++ wrapper for the Echo Nest API

License:	GPLv2+
URL:		https://projects.kde.org/projects/playground/libs/libechonest
Source0:	http://files.lfranchi.com/libechonest-%{version}.tar.bz2

BuildRequires:	cmake
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(QtNetwork)
%if 0%{?qt5}
BuildRequires:  pkgconfig(Qt5Network)
%endif


%description
libechonest is a collection of Qt4 classes designed to make a developer's
life easy when trying to use the APIs provided by The Echo Nest.

%package	devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description	devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%if 0%{?qt5}
%package -n libechonest-qt5
Summary: libechonest Qt5 bindings
%description -n libechonest-qt5
libechonest is a collection of Qt5 classes designed to make a developer's
life easy when trying to use the APIs provided by The Echo Nest.

%package -n libechonest-qt5-devel
Summary: Development files for libechonest-qt5
Requires: libechonest-qt5%{?_isa} = %{version}-%{release}
%description -n libechonest-qt5-devel
%{summary}.
%endif


%prep
%setup -q


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} .. \
  -DBUILD_WITH_QT4:BOOL=ON \
  -DECHONEST_BUILD_TESTS:BOOL=%{?tests:ON}%{!?tests:OFF}

make %{?_smp_mflags}
popd

%if 0%{?qt5}
mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%{cmake} .. \
  -DBUILD_WITH_QT4:BOOL=OFF \
  -DECHONEST_BUILD_TESTS:BOOL=%{?tests:ON}%{!?tests:OFF} 

make %{?_smp_mflags}
popd
%endif


%install
%if 0%{?qt5}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5
%endif
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}


%check
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
test "$(pkg-config --modversion libechonest)" = "%{version}" 
%if 0%{?qt5}
test "$(pkg-config --modversion libechonest5)" = "%{version}"
%endif
## The tests need active internet connection, which is not available in koji builds
%if 0%{?tests}
time make test -C %{_target_platform} ARGS="--timeout 300 --output-on-failure" ||:
%endif


%ldconfig_scriptlets

%files
%doc AUTHORS COPYING README TODO
%{_libdir}/libechonest.so.2.3*

%files devel
%{_includedir}/echonest/
%{_libdir}/libechonest.so
%{_libdir}/pkgconfig/libechonest.pc

%if 0%{?qt5}
%ldconfig_scriptlets -n libechonest-qt5

%files -n libechonest-qt5
%doc AUTHORS COPYING README TODO
%{_libdir}/libechonest5.so.2.3*

%files -n libechonest-qt5-devel
%{_includedir}/echonest/
%{_libdir}/libechonest5.so
%{_libdir}/pkgconfig/libechonest5.pc
%endif


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.3.0-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Nov 05 2014 Rex Dieter <rdieter@fedoraproject.org> 2.3.0-1
- 2.3.0, add -qt5 support

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-1
- 2.1.0

* Sun Mar 24 2013 Rex Dieter <rdieter@fedoraproject.org> 2.0.3-1
- 2.0.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jan 09 2013 Rex Dieter <rdieter@fedoraproject.org> 2.0.2-1
- 2.0.2

* Tue Nov 27 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-3
- rebuild (qjson)

* Fri Nov 23 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-2
- rebuild (qjson)

* Thu Jul 26 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-1
- Update to 2.0.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 23 2011 Rex Dieter <rdieter@fedoraproject.org> 1.2.1-1
- Update to 1.2.1
- BR: pkgconfig(QtNetwork)

* Sat Oct 08 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.2.0-1
- Update to 1.2.0

* Fri Aug 19 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.1.9-1
- Update to 1.1.9

* Wed Jun 01 2011 Rex Dieter <rdieter@fedoraproject.org> 1.1.8-1
- 1.1.8
- track soname
- %%check: verify pkgconfig sanity

* Tue May 10 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.1.5-1
- Update to 1.1.5

* Sun Mar 27 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.1.4-1
- Update to 1.1.4

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 30 2011 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.1.1-1
- Update to 1.1.1

* Mon Dec 20 2010 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 1.1.0-1
- Initial Fedora package
