%global optflags        %{optflags} -flto
%global build_ldflags   %{build_ldflags} -flto

Name:           libcommuni
Version:        3.5.0
Release:        4%{?dist}
Summary:        Cross-platform IRC framework written with Qt

License:        LGPLv2+
URL:            http://communi.github.com
Source0:        https://github.com/communi/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  libicu-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  pkgconfig(Qt5)

%description
A cross-platform IRC framework written with Qt.

Communi provides a set of tools for enabling IRC connectivity in Qt-based C++
and QML applications.


%package        devel
Summary:        Devel files for %{name}

Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Summary:        Devel files for %{name}.


%prep
%autosetup -p1


%build
%qmake_qt5
%make_build


%install
%make_install INSTALL_ROOT=%{buildroot}


%check
LD_LIBRARY_PATH=%{buildroot}%{_libdir} %make_build check


%files
%license LICENSE
%doc AUTHORS README.md CHANGELOG
%{_libdir}/libIrc*.so.*
%{_libdir}/qt5/qml/Communi/

%files devel
%doc doc/*
%{_includedir}/qt5/Communi/
%{_libdir}/libIrc*.so
%{_libdir}/qt5/mkspecs/features/*.prf


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Dec 10 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 3.5.0-3
- Update to 3.5.0
- Switch to Qt5
- Unretire package

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Rex Dieter <rdieter@fedoraproject.org> - 3.4.0-3
- use %%qmake_qt4 macro to ensure proper build flags

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 3.4.0-2
- rebuild for ICU 56.1

* Wed Aug 26 2015 Jan Kaluza <jkaluza@redhat.com> - 3.4.0-1
- update to version 3.4.0

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.0-8
- Rebuilt for GCC 5 C++11 ABI change

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 2.2.0-7
- rebuild for ICU 54.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 2.2.0-6
- rebuild for ICU 53.1

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Feb 14 2014 David Tardon <dtardon@redhat.com> - 2.2.0-3
- rebuild for new ICU

* Wed Sep 11 2013 Jan Kaluza <jkaluza@redhat.com> - 2.2.0-2
- fix obsoletes

* Wed Aug 14 2013 Jan Kaluza <jkaluza@redhat.com> - 2.2.0-1
- update to new upstream version 2.2.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon May 27 2013 Jan Kaluza <jkaluza@redhat.com> - 2.1.1-1
- update to new upstream version 2.1.1
- remove communi subpackage - it is in separate package now

* Fri Feb 01 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 1.2.1-2
- Rebuild for icu 50

* Wed Dec 19 2012 Jan Kaluza <jkaluza@redhat.com> - 1.2.1-1
- update to new upstream version 1.2.1

* Mon Dec 03 2012 Jan Kaluza <jkaluza@redhat.com> - 1.2.0-2
- add upstream fix to parser performance bottleneck caused by encoding settings

* Tue Oct 09 2012 Jan Kaluza <jkaluza@redhat.com> - 1.2.0-1
- update to new upstream version 1.2.0

* Wed Sep 05 2012 Jan Kaluza <jkaluza@redhat.com> - 1.1.2-1
- Initial Fedora packaging
