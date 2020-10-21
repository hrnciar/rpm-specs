%undefine __cmake_in_source_build

%global  framework kross-interpreters
%global  kross_ruby 1
%global  kross_java 0
%if 0%{?fedora} < 31
%global  kross_python2 1
%endif

Name:    kf5-kross-interpreters
Summary: Kross interpreters for KDE Frameworks 5
Version: 20.08.1
Release: 1%{?dist}

License: LGPLv2+
URL:     https://cgit.kde.org/%{framework}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

%if 0%{?kross_ruby}
BuildRequires: ruby-devel ruby
%endif

%if 0%{?kross_java}
BuildRequires: java-devel
%endif

%if 0%{?kross_python2}
BuildRequires:  python2-devel
%endif

BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kdelibs4support-devel
BuildRequires:  kf5-kross-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  qt5-qtbase-devel

%description
%{summary}.

# named to match as an addon to kf5-kross
%package -n kf5-kross-python2
Summary:  KF5 Kross plugin for python2
Obsoletes: kf5-kross-python < 16.04
Provides:  kf5-kross-python = %{version}-%{release}
Provides: kf5kross(python2) = %{version}-%{release}
%description -n kf5-kross-python2
Python plugin for the Kross archtecture in KDE Frameworks 5.

# named to match as an addon to kf5-kross
%package -n kf5-kross-java
Summary:  KF5 Kross plugin for java
Provides: kf5kross(java) = %{version}-%{release}
%description -n kf5-kross-java
Java plugin for the Kross archtecture in KDE Frameworks 5.

# named to match as an addon to kf5-kross
%package -n kf5-kross-ruby
Summary:  KF5 Kross plugin for ruby
Provides: kf5kross(ruby) = %{version}-%{release}
%description -n kf5-kross-ruby
Ruby plugin for the Kross archtecture in KDE Frameworks 5.

%prep
%autosetup -n %{framework}-%{version}


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install


%if 0%{?kross_python2}
%files -n kf5-kross-python2
%license COPYING
%{_kf5_qtplugindir}/krosspython.so
%endif

%if 0%{?kross_java}
%files -n kf5-kross-java
%license COPYING
%{_kf5_qtplugindir}/kross/kross.jar
%{_kf5_qtplugindir}/krossjava.so
%endif

%if 0%{?kross_ruby}
%files -n kf5-kross-ruby
%license COPYING
%{_kf5_qtplugindir}/krossruby.so
%endif

%changelog
* Tue Sep 15 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.1-1
- 20.08.1

* Tue Aug 18 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.08.0-1
- 20.08.0

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jul 10 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.3-1
- 20.04.3

* Fri Jun 12 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.2-1
- 20.04.2

* Tue May 26 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.1-1
- 20.04.1

* Fri Apr 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 20.04.0-1
- 20.04.0

* Fri Mar 06 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.3-1
- 19.12.3

* Tue Feb 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.2-1
- 19.12.2

* Fri Jan 31 2020 Rex Dieter <rdieter@fedoraproject.org> - 19.12.1-1
- 19.12.1

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 19.08.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 19.08.3-2
- F-32: rebuild against ruby27

* Tue Nov 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.3-1
- 19.08.3

* Thu Oct 17 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.2-1
- 19.08.2

* Sun Sep 29 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.1-1
- 19.08.1

* Mon Aug 19 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.08.0-1
- 19.08.0

* Thu Aug 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-3
- drop python2 support f31+ (#1738034)
- use %%make_build

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 19.04.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.3-1
- 19.04.3

* Tue Jun 04 2019 Rex Dieter <rdieter@fedoraproject.org> - 19.04.2-1
- 19.04.2

* Fri Mar 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.3-1
- 18.12.3

* Tue Feb 05 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.2-1
- 18.12.2

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 18.12.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Vít Ondruch <vondruch@redhat.com> - 18.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.6

* Tue Jan 08 2019 Rex Dieter <rdieter@fedoraproject.org> - 18.12.1-1
- 18.12.1

* Sat Dec 15 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.12.0-1
- 18.12.0

* Tue Nov 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.3-1
- 18.08.3

* Wed Oct 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.2-1
- 18.08.2

* Sun Sep 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.08.1-1
- 18.08.1

* Thu Jul 12 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.3-1
- 18.04.3

* Wed Jun 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.2-1
- 18.04.2

* Wed May 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.1-1
- 18.04.1

* Thu Apr 19 2018 Rex Dieter <rdieter@fedoraproject.org> - 18.04.0-1
- 18.04.0

* Tue Mar 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.3-1
- 17.12.3

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 17.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Feb 06 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.2-1
- 17.12.2

* Thu Jan 11 2018 Rex Dieter <rdieter@fedoraproject.org> - 17.12.1-1
- 17.12.1

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 17.12.0-2
- F-28: rebuild for ruby25

* Thu Dec 28 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.12.0-1
- 17.12.0

* Wed Nov 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.3-1
- 17.08.3

* Tue Sep 05 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.08.1-1
- 17.08.1

* Thu Aug 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.3-1
- 17.04.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 17.04.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 15 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.2-1
- 17.04.2

* Sat Jun 03 2017 Rex Dieter <rdieter@fedoraproject.org> - 17.04.1-1
- 17.04.1

* Thu Mar 09 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.3-1
- 16.12.3

* Wed Feb 08 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.2-1
- 16.12.2

* Thu Jan 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 16.12.1-2
- F-26: rebuild for ruby24

* Wed Jan 11 2017 Rex Dieter <rdieter@fedoraproject.org> - 16.12.1-1
- 16.12.1

* Mon Dec 05 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.3-1
- 16.08.3

* Thu Oct 13 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.2-1
- 16.08.2

* Mon Sep 26 2016 Than Ngo <than@redhat.com> - 16.08.1-1
- add ruby plugin

* Wed Sep 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.1-1
- 16.08.1

* Fri Aug 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.08.0-1
- 16.08.0

* Sat Aug 06 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.90-1
- 16.07.90

* Fri Jul 29 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.07.80-1
- 16.07.80

* Sat Jul 09 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.3-1
- 16.04.3

* Sun Jun 12 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.2-1
- 16.04.2

* Sun May 08 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.1-1
- 16.04.1

* Sat Apr 23 2016 Rex Dieter <rdieter@fedoraproject.org> - 16.04.0-1
- 16.04.0, -BR: cmake, update URL
- drop empty main pkg
- rename kf5-kross-python => kf5-kross-python2

* Tue Dec 01 2015 Rex Dieter <rdieter@fedoraproject.org> 15.08.3-1
- kf5-kross-interpreters (parallel-installable with kde4 kross-interpreters)

