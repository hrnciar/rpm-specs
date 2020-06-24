%global git e55ca83

%global namedreltag -SNAPSHOT
%global namedversion %{version}%{?namedreltag}

Name: coro-mock
Version: 1.0
Release: 0.17.%{git}git%{?dist}
Summary: A mock library for compiling JVM coroutine-using code on JVMs without coroutines
License: Public Domain
Url: https://github.com/headius/coro-mock
Source0: https://github.com/headius/%{name}/tarball/%{git}/headius-%{name}-%{git}.tar.gz

BuildRequires:  maven-local
BuildRequires:  mvn(junit:junit)

BuildArch: noarch

%description
A small mock library for compiling JVM coroutine-utilizing code on JVMs
without coroutines.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n headius-%{name}-%{git}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.17.e55ca83git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.16.e55ca83git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.15.e55ca83git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.14.e55ca83git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.13.e55ca83git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.e55ca83git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.11.e55ca83git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.10.e55ca83git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Dec 01 2015 Mat Booth <mat.booth@redhat.com> - 1.0-0.9.e55ca83git
- Bring spec up to date to fix FTBFS

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.e55ca83git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 27 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.0-0.7.e55ca83git
- Fix FTBFS due to XMvn changes in F21 (#1106085)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.e55ca83git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.0-0.5.e55ca83git
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.e55ca83git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0-0.3.e55ca83git
- Reverted to old maven packaging standards. *sigh*

* Thu Feb 21 2013 Bohuslav Kabrda <bkabrda@redhat.com> - 1.0-0.2.e55ca83git
- Adapted to new maven packaging standards.

* Tue May 22 2012 Vít Ondruch <vondruch@redhat.com> - 1.0-0.1.e55ca83git
- Adapted from Mageia.

* Sat Feb 25 2012 gil <gil> 1.0-1.mga2
+ Revision: 214942
- imported package coro-mock
