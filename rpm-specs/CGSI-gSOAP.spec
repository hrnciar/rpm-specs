Name:		CGSI-gSOAP
Version:	1.3.11
Release:	10%{?dist}
Summary:	GSI plugin for gSOAP

License:	ASL 2.0
URL:		http://glite.web.cern.ch/glite/
#		The source tarfile is created from a repository checkout:
#		git clone https://gitlab.cern.ch/dmc/cgsi-gsoap.git -b master CGSI-gSOAP-1.3.11
#		cd CGSI-gSOAP-1.3.11
#		git checkout v1.3.11
#		cd ..
#		tar --exclude-vcs -z -c -f CGSI-gSOAP-1.3.11.tar.gz CGSI-gSOAP-1.3.11
Source0:	%{name}-%{version}.tar.gz
Patch0:		%{name}-library-linking.patch

BuildRequires:	gcc-c++
BuildRequires:	globus-gss-assist-devel
BuildRequires:	globus-gssapi-gsi-devel
BuildRequires:	gsoap-devel
BuildRequires:	voms-devel
BuildRequires:	doxygen

%description
This is a GSI plugin for gSOAP. It uses the globus GSI libraries to implement
GSI secure authentication and encryption on top of gSOAP.

%package devel
Summary:	GSI plugin for gSOAP - development files
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	gsoap-devel

%description devel
This package provides the header files for programming with the cgsi-gsoap
plugins.

%prep
%setup -q
%patch0 -p1

# Fix bad permissions (which otherwise end up in the debuginfo package)
find . '(' -name '*.h' -o -name '*.c' -o -name '*.cpp' -o -name '*.cc' ')' \
    -exec chmod 644 {} ';'
chmod 644 LICENSE RELEASE-NOTES

# Remove -L/usr/lib and -L/usr/lib64 since they may cause problems
sed -e 's!-L$([A-Z_]*)/lib!!' \
    -e 's!-L$([A-Z_]*)/$(LIBDIR)!!' -i src/Makefile

# Remove gsoap version from library names
sed -e 's!$(GSOAP_VERSION)!!g' -i src/Makefile

%build
. ./VERSION
cd src
make CFLAGS="%optflags -fPIC -I. `pkg-config --cflags gsoap`" \
     SHLIBLDFLAGS="%{?__global_ldflags} -shared" \
     USE_VOMS=yes WITH_EMI=yes WITH_CPP_LIBS=yes \
     LIBDIR=%{_lib} VERSION=$VERSION all doc

%install
. ./VERSION
pushd src
make CFLAGS="%optflags -fPIC -I. `pkg-config --cflags gsoap`" \
     SHLIBLDFLAGS="%{?__global_ldflags} -shared" \
     USE_VOMS=yes WITH_EMI=yes WITH_CPP_LIBS=yes \
     LIBDIR=%{_lib} VERSION=$VERSION install install.man

mkdir -p %{buildroot}%{_pkgdocdir}
mv %{buildroot}%{_datadir}/doc/CGSI/html %{buildroot}%{_pkgdocdir}
popd
install -p -m 644 RELEASE-NOTES %{buildroot}%{_pkgdocdir}
%{!?_licensedir: install -p -m 644 LICENSE %{buildroot}%{_pkgdocdir}}

rm %{buildroot}%{_libdir}/*.a

%ldconfig_scriptlets

%files
%{_libdir}/libcgsi_plugin.so.*
%{_libdir}/libcgsi_plugin_cpp.so.*
%{_libdir}/libcgsi_plugin_voms.so.*
%{_libdir}/libcgsi_plugin_voms_cpp.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/RELEASE-NOTES
%{!?_licensedir: %doc %{_pkgdocdir}/LICENSE}
%{?_licensedir: %license LICENSE}

%files devel
%{_includedir}/cgsi_plugin.h
%{_libdir}/libcgsi_plugin.so
%{_libdir}/libcgsi_plugin_cpp.so
%{_libdir}/libcgsi_plugin_voms.so
%{_libdir}/libcgsi_plugin_voms_cpp.so
%doc %{_pkgdocdir}/html
%doc %{_mandir}/man*/*

%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 22 2020 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3.11-9
- Rebuilt for gsoap 2.8.104 (Fedora 33)

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 17 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3.11-7
- Rebuilt for gsoap 2.8.91 (Fedora 32)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3.11-4
- Rebuild for gsoap 2.8.75 (Fedora 30)

* Mon Jul 16 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3.11-3
- Add BuildRequires on gcc-c++
- Remove workaround for changed default linker flags, the change was reverted

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 30 2018 Oliver Keeble <oliver.keeble@cern.ch> - 1.3.11-1
- New upstream release
- Drop patch 1

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3.10-8
- Rebuild for gsoap 2.8.60 (Fedora 28)
- Add workaround for changed default linker flags

* Mon Nov 06 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3.10-7
- The STACK macro was removed in globus-gsi-credential 7.13. Don't use.
- EPEL 5 End-Of-Life specfile clean-up
  - Remove Group and BuildRoot tags
  - Remove _pkgdocdir macro definition
  - Don't clear the buildroot in the install section
  - Remove the clean section

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jul 13 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3.10-4
- Rebuild for gsoap 2.8.49 (Fedora 27)

* Wed Jun 21 2017 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3.10-3
- Rebuild for gsoap 2.8.48 (Fedora 27)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.3.10-1
- Update for new upstream release

* Mon Sep 19 2016 Mattias Ellert <mattias.ellert@physics.uu.se> - 1.3.8-6
- Rebuild for gsoap 2.8.35 (Fedora 26)

* Fri Aug 26 2016 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.3.8-5
- Rebuilt for new voms

* Tue Apr 19 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.8-4
- Rebuild for gsoap 2.8.30 (Fedora 25)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Feb 02 2016 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.8-2
- Rebuild for gsoap 2.8.28 (Fedora 24)

* Wed Aug 12 2015 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.3.8-1
- Update for new upstream release

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 15 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.7-4
- Rebuild for gsoap 2.8.22 (Fedora 23)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.3.7-3
- Rebuilt for GCC 5 C++11 ABI change

* Wed Jan 21 2015 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.7-2
- Rebuild for gsoap 2.8.21 (Fedora 22)
- Implement new license packaging guidelines

* Thu Nov 06 2014 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.3.7-1
- Update for new upstream release

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jul 15 2014 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.3.6-6
- Dropped multithreading backport. Causes issues to dpm-srm

* Sun Jul 13 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.6-5
- Rebuild for gsoap 2.8.17 (Fedora 22)

* Wed Jul 02 2014 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.3.6-4
- Backported fix for multithreading

* Fri Jun 27 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.6-3
- Fix broken man page

* Fri Jun 27 2014 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.6-2
- Update the source description for the new release

* Fri Jun 27 2014 Alejandro Alvarez Ayllon <aalvarez@cern.ch> - 1.3.6-1
- Update for new upstream release

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 18 2013 Adrien Devresse <adevress at cern.ch> - 1.3.5-7
- Rebuilt for gsoap release

* Thu Aug 08 2013 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.5-6
- Use _pkgdocdir

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.5-2
- Use the right svn tag

* Thu May 24 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.5-1
- Update to version 1.3.5 (EMI 2 release)

* Fri Mar 02 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.4.2-6
- Add missing libraries to linking

* Fri Feb 10 2012 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.4.2-5
- Rebuilt for gsoap 2.8.7 (Fedora 17+)

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 09 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.4.2-3
- Use default LDFLAGS

* Thu Sep 01 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.4.2-2
- Use gsoap cflags from pkg-config

* Mon Jun 20 2011 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.4.2-1
- Update to version 1.3.4.2

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 20 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.4.0-1
- Update to version 1.3.4.0

* Thu Nov 12 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.3.2-2.20090920cvs
- Use cvs checkout date in release tag
- Drop Provides/Obsoletes for the old package name since it was never in Fedora

* Wed Sep 23 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.3.2-1
- Update to version 1.3.3.2
- Drop the patch - all issues fixed upstream
- Change License tag to Apache 2.0

* Fri Aug 14 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.3.1-1
- Update to version 1.3.3.1

* Tue Jun 30 2009 Anders Wäänänen <waananen@nbi.dk> - 1.3.2.2-4
- Fix docdir handling

* Wed Jan 14 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.2.2-3
- Rebuild against distribution Globus

* Wed Nov 19 2008 Anders Wäänänen <waananen@nbi.dk> - 1.3.2.2-2
- Update patch to use $(CPP) instead of ld (2 places)

* Sun Oct 26 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.3.2.2-1
- Update to version 1.3.2.2

* Fri Jan 11 2008 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.2.1.2-1
- Update to version 1.2.1.2

* Tue Jul 24 2007 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.1.17.2-2
- Rebuild against newer globus and voms

* Wed May 09 2007 Mattias Ellert <mattias.ellert@fysast.uu.se> - 1.1.17.2-1
- Initial build
