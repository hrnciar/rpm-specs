%global framework ksmtp 

Name:    kf5-%{framework}
Version: 20.04.2
Release: 1%{?dist}
Summary: KDE SMTP libraries

License: LGPLv2+
URL:     https://cgit.kde.org/%{framework}.git/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

## upstream patches

## upstreamable patches

%global kf5_ver 5.29
BuildRequires: extra-cmake-modules >= %{kf5_ver}
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5KIO)

BuildRequires: cmake(Qt5Network)

BuildRequires: kf5-kmime-devel >= %{version}
BuildRequires: cmake(KF5Mime)

BuildRequires: pkgconfig(libsasl2)

# runtime sasl plugins
Suggests: cyrus-sasl-gssapi%{?_isa}
Recommends: cyrus-sasl-md5%{?_isa}
Requires: cyrus-sasl-plain%{?_isa}

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5CoreAddons)
Requires:       cmake(KF5Mime)
Requires:       kf5-kmime-devel >= %{version}
%description    devel
%{summary}.


%prep
%autosetup -n %{framework}-%{version} -p1


%build
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake_kf5} ..
popd

%make_build -C %{_target_platform}


%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

%find_lang %{name} --all-name --with-html


%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPimSMTP.so.*

%files devel
%{_kf5_libdir}/libKPimSMTP.so
%{_kf5_libdir}/cmake/KPimSMTP/
%{_includedir}/KPim/
%{_kf5_archdatadir}/mkspecs/modules/qt_KSMTP.pri


%changelog
* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Thu Jun 11 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-2
- Recommends: cyrus-sasl-md5 (was Suggests)

* Wed May 27 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0

* Sat Mar 07 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Mon Nov 11 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Fri Oct 18 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Wed Jun 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Fri Dec 14 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Mon Oct 01 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Fri Jul 13 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 18.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Fri Apr 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Thu Dec 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-5
- more upstream fixes

* Fri Dec 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-4
- Fix duplicate authentication (D9476)

* Tue Dec 19 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-3
- pull in upstream fixes

* Mon Dec 18 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-2
- Requires: cyrus-sasl-plain
- Suggests: cyrus-sasl-{gssapi,md5}

* Wed Dec 13 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Fri Nov 24 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.80-2
- fix -devel Requires

* Wed Nov 22 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.11.80-1
- 17.11.80
