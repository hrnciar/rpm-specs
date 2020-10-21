# Define libsuffix.
%global libsuffix yui
%global libname lib%{libsuffix}

# Do we build with Mono?
%ifarch %{mono_arches}
%global with_mono 1
%endif # arch %%{mono_arches}

# release commit because SUSE didn't tag it :(
%global relcommit 59dfa64f05adb40c7da88325255d758f4588ab42

# CMake-builds go out-of-tree.
%undefine __cmake_in_source_build


Name:		%{libname}-bindings
Version:	2.0.2
Release:	1%{?dist}
Summary:	Language bindings for %{libname}

License:	LGPLv2 or LGPLv3
URL:		https://github.com/%{libname}/%{name}
# No tag :(
#Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	%{url}/archive/%{relcommit}/%{name}-%{version}.tar.gz

# Patches for upstream to fix bindings
Patch0500:      libyui-bindings-2.0.2-fix-building-ruby-bindings.patch

# Patches from Mageia to enable libyui-mga bindings
Patch1000:	libyui-bindings-2.0.2-menubar.patch

BuildRequires:  gcc-c++
BuildRequires:	boost-devel
BuildRequires:	cmake
BuildRequires:	%{libname}-devel >= 3.10.0
BuildRequires:	%{libname}-mga-devel >= 1.1.0
BuildRequires:	swig

%description
This package provides Mono / CSharp, Perl, Python and Ruby language
bindings to access functions of %{libname}.
An User Interface engine that provides abstraction from graphical user
interfaces (Qt, Gtk) and text based user interfaces (ncurses).


%if 0%{?with_mono}
%package -n mono-%{libsuffix}
Summary:	Mono / CSharp bindings for %{libname}

BuildRequires:	mono-devel		>= 4.0.0

%description -n mono-%{libsuffix}
This package provides Mono / CSharp language bindings to access
functions of %{libname}.
An User Interface engine that provides the abstraction from
graphical user interfaces (Qt, Gtk) and text based user
interfaces (ncurses).
%endif # 0%%{?with_mono}


%package -n perl-%{libsuffix}
Summary:	Perl bindings for %{libname}

BuildRequires:	perl-devel
BuildRequires:	perl-generators

Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description -n perl-%{libsuffix}
This package provides Perl language bindings to access
functions of %{libname}.
An User Interface engine that provides the abstraction from
graphical user interfaces (Qt, Gtk) and text based user
interfaces (ncurses).


%package -n python3-%{libsuffix}
Summary:	Python3 bindings for %{libname}

BuildRequires:	python3-devel

%{?python_provide:%python_provide python3-%{libsuffix}}

%description -n python3-%{libsuffix}
This package provides Python3 language bindings to access
functions of %{libname}.
An User Interface engine that provides the abstraction from
graphical user interfaces (Qt, Gtk) and text based user
interfaces (ncurses).


%package -n ruby-%{libsuffix}
Summary:	Ruby bindings for %{libname}

BuildRequires:	ruby-devel

Requires:	ruby(release)

%description -n ruby-%{libsuffix}
This package provides Ruby language bindings to access
functions of %{libname}.
An User Interface engine that provides the abstraction from
graphical user interfaces (Qt, Gtk) and text based user
interfaces (ncurses).


%prep
%autosetup -n %{name}-%{relcommit} -p1


%build
%cmake							\
	-DLIB=%{_libdir}				\
	-DMONO_LIBRARIES=%{_libdir}			\
	-DPython_ADDITIONAL_VERSIONS=%{python3_version}	\
	-DPYTHON_EXECUTABLE=%{__python3}		\
	-DPYTHON_SITEDIR=%{python3_sitearch}		\
	-DCMAKE_BUILD_TYPE=RELEASE			\
	-DBUILD_RUBY_GEM=NO				\
	-DWITH_MONO=%{?with_mono:ON}%{!?with_mono:OFF}	\
	-DWITH_PERL=ON					\
	-DWITH_PYTHON=ON				\
	-DWITH_RUBY=ON					\
	-DWITH_MGA=YES

%cmake_build


%install
%cmake_install


%if 0%{?with_mono}
%files -n mono-%{libsuffix}
%doc package/%{name}.changes README.md
%license COPYING*
%{_libdir}/%{libsuffix}/%{libsuffix}.dll
%{_libdir}/%{libsuffix}/%{libsuffix}.so
%endif


%files -n perl-%{libsuffix}
%doc package/%{name}.changes README.md swig/perl/examples
%license COPYING*
%{perl_vendorarch}/%{libsuffix}.so
%{perl_vendorlib}/%{libsuffix}.pm


%files -n python3-%{libsuffix}
%doc package/%{name}.changes README.md swig/python/examples
%license COPYING*
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/*%{libsuffix}.*


%files -n ruby-%{libsuffix}
%doc package/%{name}.changes README.md swig/ruby/examples
%license COPYING*
%{ruby_vendorarchdir}/_%{libsuffix}.*
%{ruby_vendorlibdir}/%{libsuffix}.rb
%{ruby_vendorlibdir}/%{libsuffix}/


%changelog
* Sat Aug 01 2020 Neal Gompa <ngompa13@gmail.com> - 2.0.2-1
- Rebase to 2.0.2 (#1815689)

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-25
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jun 22 2020 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.2-23
- Perl 5.32 rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-22
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jan 18 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.2-20
- F-32: rebuild against ruby27

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-19
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-18
- Rebuilt for Python 3.8

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu May 30 2019 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.2-16
- Perl 5.30 rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.2-14
- F-30: rebuild against ruby26

* Wed Jan 09 2019 Miro Hrončok <mhroncok@redhat.com>
- Drop the Python 2 bindings (#1627388)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 1.1.2-11
- Perl 5.28 rebuild

* Wed Jun 27 2018 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.2-10
- Perl 5.28 rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.1.2-9
- Rebuilt for Python 3.7

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.2-7
- F-28: rebuild for ruby25

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1.2-4
- Rebuilt for Boost 1.64

* Sun Jun 04 2017 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.2-3
- Perl 5.26 rebuild

* Sat Apr 29 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.2-2
- Rebuilt for bootstrapping new arch: s390x

* Fri Apr 14 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.2-1
- New upstream version
- Updated Patches for libyui-mga
- Drop unused patches
- Spec-file cosmetics

* Thu Apr 13 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-13
- Rebuilt for libyui.so.8

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-11
- Rebuilt for Boost 1.63

* Thu Feb 02 2017 Björn Esser <besser82@fedoraproject.org> - 1.1.1-10
- Add MGA-patches to support libyui-mga and dnfdragora

* Fri Jan 27 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1.1-9
- Rebuilt for Boost 1.63

* Thu Jan 12 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.1.1-8
- F-26: rebuild for ruby24

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.1-7
- Rebuild for Python 3.6

* Tue Oct 25 2016 Philippe Makowski <makowski@fedoraproject.org> - 1.1.1-6
- fixed python 2 and 3 bindings
- fixed python3 YWidget and YItem pointer comparison
- added patch to use FindPerlLibs.cmake instead of FindPerl.cmake

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.1-4
- Perl 5.24 rebuild

* Wed Mar 30 2016 Björn Esser <fedora@besser82.io> - 1.1.1-3
- bump to avoid self-obsoletion

* Wed Mar 30 2016 Björn Esser <fedora@besser82.io> - 1.1.1-2
- replace `python-yui` with `python2-yui` using proper Provides and Obsoletes

* Tue Mar 29 2016 Björn Esser <fedora@besser82.io> - 1.1.1-1
- new upstream release
- drop Patch0, applied in upstream tarball
- handle %%license and %%doc properly

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Jonathan Wakely <jwakely@redhat.com> - 1.1.0-17
- Rebuilt for Boost 1.60

* Tue Jan 12 2016 Vít Ondruch <vondruch@redhat.com> - 1.1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.3

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Aug 27 2015 Jonathan Wakely <jwakely@redhat.com> - 1.1.0-14
- Rebuilt for Boost 1.59

* Thu Aug 27 2015 Björn Esser <bjoern.esser@gmail.com> - 1.1.0-13
- rebuilt for so-name-bump in libyui-3.2.1

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-12
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.1.0-11
- rebuild for Boost 1.58

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 1.1.0-9
- Perl 5.22 rebuild

* Tue May 19 2015 Björn Esser <bjoern.esser@gmail.com> - 1.1.0-8
- rebuilt for mono-4.0.1, again

* Mon May 18 2015 Björn Esser <bjoern.esser@gmail.com> - 1.1.0-7
- rebuilt for mono-4.0.1

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.0-6
- Rebuilt for GCC 5 C++11 ABI change

* Mon Feb 02 2015 Björn Esser <bjoern.esser@gmail.com> - 1.1.0-5
- rebuilt for libyui-3.1.5, again

* Mon Feb 02 2015 Björn Esser <bjoern.esser@gmail.com> - 1.1.0-4
- Rebuild for boost 1.57.0

* Thu Jan 22 2015 Björn Esser <bjoern.esser@gmail.com> - 1.1.0-3
- add Patch0: use upstream-patch for older CMake instead of sed-cludge

* Thu Jan 22 2015 Dan Horák <dan[at]danny.cz> - 1.1.0-2
- fix build without Mono

* Tue Jan 20 2015 Björn Esser <bjoern.esser@gmail.com> - 1.1.0-1
- new upstream release
- rebuilt for libyui-3.1.5
- keep doc-files in unfied %%{_pkgdocdir}
- small improvements to spec-file
- drop Patch0, now in upstream sources

* Sun Jan 18 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.0-6
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_2.2
- Remove deprecated Config: usage

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 1.0.4-4
- Perl 5.20 rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 Björn Esser <bjoern.esser@gmail.com> - 1.0.4-1
- new upstream version
- build a Python3 version
- minor improvents on spec

* Thu Apr 24 2014 Vít Ondruch <vondruch@redhat.com> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Changes/Ruby_2.1

* Tue Mar 18 2014 Björn Esser <bjoern.esser@gmail.com> - 1.0.2-10
- rebuilt for libyui-3.0.13

* Wed Oct 02 2013 Björn Esser <bjoern.esser@gmail.com> - 1.0.2-9
- added "Versioned MODULE_COMPAT_ Requires"

* Wed Oct 02 2013 Björn Esser <bjoern.esser@gmail.com> - 1.0.2-8
- adaptions for new Python-guidelines
- use %%{ruby_vendorarchdir} instead of hardcoded path

* Fri Aug 30 2013 Björn Esser <bjoern.esser@gmail.com> - 1.0.2-7
- libyui 3.0.10 rebuilt

* Sat Aug 03 2013 Petr Pisar <ppisar@redhat.com> - 1.0.2-6
- Perl 5.18 rebuild

* Sat Jul 27 2013 Björn Esser <bjoern.esser@gmail.com> - 1.0.2-5
- include examples in own subdir
- removed hardening flags

* Sat Jul 27 2013 Björn Esser <bjoern.esser@gmail.com> - 1.0.2-4
- fix build, removed trailing backslash

* Sat Jul 27 2013 Björn Esser <bjoern.esser@gmail.com> - 1.0.2-3
- libyui-3.0.9 rebuilt on all branches
- removed Group-tag

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 1.0.2-2
- Perl 5.18 rebuild on F20 / rawhide

* Thu Jun 20 2013 Björn Esser <bjoern.esser@gmail.com> - 1.0.2-1
- new upstream-version
- copyright changed GPLv2 -> LGPLv2 or LGPLv3 matching libyui* now.
- removed `/usr/bin/env` from hashbang of examples
- adapted Source0 obsoleting %%commit

* Sat May 18 2013 Björn Esser <bjoern.esser@gmail.com> - 1.0.1-2
- improved readability: tag ordering

* Wed May 15 2013 Björn Esser <bjoern.esser@gmail.com> - 1.0.1-1
- Initial RPM release.
