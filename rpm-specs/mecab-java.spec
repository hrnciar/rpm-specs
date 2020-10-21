%define		mainver		0.996
#%%define		betaver		pre3
%define		relnumber	3

Name:		mecab-java
Version:	%{mainver}
Release:	%{?betaver:0.}%{relnumber}%{?betaver:.%betaver}%{?dist}
Summary:	Java binding for MeCab

License:	BSD or LGPLv2+ or GPL+
URL:		http://mecab.sourceforge.net/
Source0:	http://mecab.googlecode.com/files/%{name}-%{mainver}%{?betaver}.tar.gz

# This is not release number specific
BuildRequires:	gcc-c++
BuildRequires:	mecab-devel = %{version}
BuildRequires:	java-devel
# java related macros
BuildRequires:	javapackages-tools
# %%check
BuildRequires:	mecab-jumandic
BuildRequires:	glibc-langpack-ja

Requires:	mecab = %{version}
Requires:	java-headless

%description
%{summary}.

%prep
%setup -q -n %{name}-%{mainver}%{?betaver}
%{__sed} -i.opt -e 's|-O3||' Makefile

# ??? What are the following lines for?
# Disabling for now
: %{__sed} -i.test \
	-e '/test\.java/s|\$|-$|' Makefile

%build
# Failed with -j4 on Matt's mass build
%{__make} -j1 \
	CXX="g++ $RPM_OPT_FLAGS -fno-strict-aliasing" \
	JAVAC="%{javac} -encoding UTF8" \
	JAR=%{jar} \
	INCLUDE=/usr/lib/jvm/java/include

%install
#%%{__mkdir_p} $RPM_BUILD_ROOT%%{_libdir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_libdir}/%{name}
%{__mkdir_p} $RPM_BUILD_ROOT%{_jnidir}

%{__install} -cm 644 MeCab.jar $RPM_BUILD_ROOT%{_jnidir}/
#%%{__install} -cm 755 libMeCab.so $RPM_BUILD_ROOT%%{_libdir}
%{__install} -cm 755 libMeCab.so $RPM_BUILD_ROOT%{_libdir}/%{name}/

%check
export JAVA=%{java}
LANG=ja_JP.utf8
%{__make} test || :

%files
%doc bindings.html
%doc AUTHORS COPYING BSD GPL LGPL

#%%{_libdir}/libMeCab.so
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libMeCab.so
%{_jnidir}/MeCab.jar

%changelog
* Fri Aug 07 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.996-3
- F-33: mass rebuild
- Remove unused python macro

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-2.15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 11 2020 Jiri Vanek <jvanek@redhat.com> - 0.996-2.14
- Rebuilt for JDK-11, see https://fedoraproject.org/wiki/Changes/Java11

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-2.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-2.12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-2.11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.996-2.10
- Add BR:glibc-langpack-ja
  See https://fedoraproject.org/wiki/Changes/Remove_glibc-langpacks-all_from_buildroot

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-2.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-2.8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-2.7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-2.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-2.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.996-2.4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.996-2.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 0.996-2.2
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.996-2.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Jun 19 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.996-2
- Switch to openjdk for F-21

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.996-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.996-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.996-1
- 0.996

* Sun Feb 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.995-2
- Add BR: java for %%check

* Sun Feb 10 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.995-1
- 0.995

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.994-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul  2 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.994-1
- 0.994

* Thu Mar 29 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.993-1
- 0.993

* Sun Jan 15 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.991-1
- 0.991

* Mon Jan  9 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.99-1
- 0.99

* Thu Jan  5 2012 Mamoru Tasaka <mtasaka@fedoraproject.org> - 0.98-3
- F-17: rebuild against gcc47

* Mon Feb 14 2011 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.98-2
- F-15 mass rebuild

* Tue Sep 29 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.98-1
- 0.98

* Sat Jul 25 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.98-0.3.pre3
- F-12: Mass rebuild

* Thu Jun  4 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.98-0.2.pre3
- 0.98pre3

* Mon Mar  9 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.98-0.1.pre1
- Update to 0.98pre1

* Tue Feb 24 2009 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.97-3
- %%global-lize "nested" macro

* Fri Aug 29 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.97-2
- Use -j1 (-j4 failed)

* Sun Feb  3 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.97-1
- 0.97

* Fri Oct 26 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.96-3
- License fix

* Wed Aug 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.96-2.dist.3
- Mass rebuild (buildID or binutils issue)

* Fri Aug  3 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.96-2.dist.1
- License update

* Sun Jun 17 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.96-2
- Nuke test for now

* Fri Jun 15 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.96-1
- 0.96

* Thu Mar 22 2007 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 0.95-1
- Initial packaging.
