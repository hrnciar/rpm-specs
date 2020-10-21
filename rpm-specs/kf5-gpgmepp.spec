%undefine __cmake_in_source_build
%global framework gpgmepp

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Name:    kf5-%{framework}
Version: 16.08.3
Release: 14%{?dist}
Summary: C++ wrapper and Qt integration for GpgMe library

License: LGPLv2+
URL:     https://cgit.kde.org/%{framework}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/applications/%{version}/src/%{framework}-%{version}.tar.xz

BuildRequires:  boost-devel
BuildRequires:  extra-cmake-modules
BuildRequires:  gpgme-devel libgpg-error-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel

# enforce minimal gpgme runtime
%global gpgme_version %(gpgme-config --version 2> /dev/null || echo 0)
%if "%{?gpgme_version}" != "0"
Requires: gpgme%{?_isa} >= %{gpgme_version}
%endif

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel
Requires:       gpgme-devel libgpg-error-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
%{cmake_kf5} \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF}
%cmake_build


%install
%cmake_install


%check
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
make test ARGS="--output-on-failure --timeout 30" -C %{_target_platform} ||:
%endif


%ldconfig_scriptlets

%files
%license COPYING.LIB
%{_kf5_libdir}/libKF5Gpgmepp.so.*
%{_kf5_libdir}/libKF5Gpgmepp-pthread.so.*
%{_kf5_libdir}/libKF5QGpgme.so.*

%files devel
%{_kf5_includedir}/gpgmepp_version.h
%{_kf5_includedir}/gpgme++/
%{_kf5_includedir}/qgpgme/
%{_kf5_libdir}/libKF5Gpgmepp.so
%{_kf5_libdir}/libKF5Gpgmepp-pthread.so
%{_kf5_libdir}/libKF5QGpgme.so
%{_kf5_libdir}/cmake/KF5Gpgmepp/
%{_kf5_archdatadir}/mkspecs/modules/qt_QGpgme.pri


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.08.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 16.08.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.08.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 16.08.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.08.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 16.08.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.08.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.08.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Jonathan Wakely <jwakely@redhat.com> - 16.08.3-6
- Rebuilt for Boost 1.64

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-5
- update URL, enforce minimal gpgme runtime dep

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 16.08.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 16 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-3
- rebuild

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 16.08.3-2
- Rebuild for gpgme 1.18

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Thu Sep 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Sat Sep 03 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0

* Sun Jul 10 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-4
- Fix typo in Summary, -devel: Requires: boost-devel

* Thu May 26 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-3
- -devel: Requires: gpgme-devel

* Thu May 19 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-2
- -devel: Requires: libgpg-error-devel, minimize %%check deps

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- 16.04.1

* Sun May 01 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-1
- 16.04.0, update URL, support bootstrap, add %%check

* Tue Mar 15 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.3-1
- 15.12.3

* Sun Feb 14 2016 Rex Dieter <rdieter@fedoraproject.org> - 15.12.2-1
- 15.12.2

* Sat Feb 06 2016 Rex Dieter <rdieter@fedoraproject.org> 15.12.1-1
- 15.12.1

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 15.12.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 15 2015 Jan Grulich <jgrulich@redhat.com> - 15.12.0-2
- Remove obsoletes/conflicts with kdepimlibs

* Tue Dec 15 2015 Jan Grulich <jgrulich@redhat.com> - 15.12-0-1
- Update to 15.12.0

* Mon Dec 07 2015 Jan Grulich <jgrulich@redhat.com> - 15.11.90-1
- Update to 15.11.90

* Thu Dec 03 2015 Jan Grulich <jgrulich@redhat.com> - 15.11.80-1
- Update to 15.11.80

* Mon Aug 24 2015 Daniel Vrátil <dvratil@redhat.com> - 15.08.0-1
- Initial version
