Name:           astyle
Version:        3.1
Release:        9%{?dist}
Summary:        Source code formatter for C-like programming languages

%global majorversion    3
%global soversion       3.1.0

License:        LGPLv3+
URL:            http://astyle.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}_%{version}_linux.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  java-devel >= 1:1.8.0


# Make the astyle-lib usable for arduino
Patch0:         astyle-arduino.patch
# Fix (hardcoded) path to html-help
Patch1:         astyle-html-help.patch
# Fix abort with gcc8 -Wp,-D_GLIBCXX_ASSERTION
# https://bugzilla.redhat.com/show_bug.cgi?id=1573092
# Patch proposed: https://sourceforge.net/p/astyle/bugs/503/
Patch2:         astyle-r655-gcc8-vector-at-end.patch

%description
Artistic Style is a source code indenter, source code formatter, and
source code beautifier for the C, C++, C# and Java programming
languages.

%package devel
Summary:        Source code formatter for C-like programming languages
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Artistic Style is a source code indenter, source code formatter, and
source code beautifier for the C, C++, C# and Java programming
languages.

This package contains the shared library.


%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
chmod a-x src/*
chmod a-x doc/*

pushd src
    # it's much easier to compile it here than trying to fix the Makefile
    g++ %{optflags} -DASTYLE_LIB -DASTYLE_JNI -fPIC -I/usr/lib/jvm/java/include -I/usr/lib/jvm/java/include/linux -c ASBeautifier.cpp ASEnhancer.cpp ASFormatter.cpp ASResource.cpp astyle_main.cpp
    g++ -shared -o libastyle.so.%{soversion} *.o -Wl,-soname,libastyle.so.%{majorversion}
    ln -s libastyle.so.%{soversion} libastyle.so
    g++ %{optflags} -c ASLocalizer.cpp astyle_main.cpp
    g++ %{optflags} -o astyle ASLocalizer.o astyle_main.o -L. -lastyle
popd

%install
pushd src
    mkdir -p %{buildroot}{%{_bindir},%{_libdir},%{_includedir}}

    install -p -m 755 astyle %{buildroot}%{_bindir}
    install -p -m 755 libastyle.so.%{soversion} %{buildroot}%{_libdir}
    cp -P libastyle.so %{buildroot}%{_libdir}
    install -p -m 644 astyle.h %{buildroot}%{_includedir}
popd

%ldconfig_scriptlets

%files
%doc doc/*.html
%{_bindir}/astyle
%{_libdir}/libastyle.so.%{majorversion}
%{_libdir}/libastyle.so.%{soversion}

%files devel
%{_libdir}/libastyle.so
%{_includedir}/astyle.h

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon May 14 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1-5
- Fix abort with gcc8 -Wp,-D_GLIBCXX_ASSERTION (bug 1573092)

* Mon Feb 19 2018 Jens Lody <fedora@jenslody.de> - 3.1-4
- Add BuildRequires for gcc-c++.

* Tue Feb 13 2018 Jens Lody <fedora@jenslody.de> - 3.1-3
- Build fix
- Consistently use macros instead of variables in spec-file

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 13 2018 Jens Lody <fedora@jenslody.de> - 3.1-1
- Update to 3.1 (#1533678)
- Fix project url (no https !)

* Sun Sep 24 2017 Jens Lody <fedora@jenslody.de> - 3.0.1-4
- Fix #1493473 (astyle --html does not find documentation).

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 31 2017 Jens Lody <fedora@jenslody.de> - 3.0.1-1
- Update to 3.0.1

* Sat Apr 29 2017 Jens Lody <fedora@jenslody.de> - 3.0-2
- Make the astyle-lib usable for arduino.

* Mon Apr 10 2017 Jens Lody <fedora@jenslody.de> - 3.0-1
- Update to 3.0

* Sun Feb 12 2017 Jens Lody <fedora@jenslody.de> - 2.06-1
- update to 2.06 (#1411164)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.05.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.05.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.05.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.05.1-2
- Rebuilt for GCC 5 C++11 ABI change

* Wed Dec 17 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.05.1-1
- update to 2.05.1 (#1175136), but stay at same soversion for library

* Thu Nov 20 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.05-1
- update to 2.05 (#1166336)

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.04-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Mar 20 2014 Dan Horák <dan[at]danny.cz> - 2.04-3
- compile directly in %%build so the astyle binary links against our library
- include public header file in devel subpackage
- use full version info in soname as there is no API/ABI compatibility guaranteed

* Fri Jan 17 2014 Thomas Spura <tomspur@fedoraproject.org> - 2.04-2
- build shared library without SONAME (opened bug upstream to provide a SONAME in the next release, #1054422)
- remove defattr
- remove clean section

* Tue Nov  5 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.04-1
- update to new version (fixes #1025982, #996008)

* Tue Jul 30 2013 Thomas Spura <tomspur@fedoraproject.org> - 2.03-1
- update to new version (fixes #990162)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.02.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Dec  4 2011 Thomas Spura <tomspur@fedoraproject.org> - 2.02.1-1
- update to new version

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.01-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  1 2010 Thomas Spura <tomspur@fedoraproject.org> - 2.01-1
- update to new version

* Sat Jan 30 2010 Thomas Spura <tomspur@fedoraproject.org> - 1.24-1
- update to new version
- change license to LGPLv3+ (changed since 1.23, but missed there)

* Tue Oct 13 2009 Thomas Spura <tomspur@fedoraproject.org> - 1.23-1
- Update to new version
- patch from Sep 24 2008 not needed anymore for gcc-4.4

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Sep 24 2008 Debarshi Ray <rishi@fedoraproject.org> - 1.21-9
- Fixed build failure with gcc-4.3. Closes Red Hat Bugzilla bug #433971.

* Wed May 21 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.21-8
- fix license tag

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.21-7
- Autorebuild for GCC 4.3

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.21-6
- Rebuild for selinux ppc32 issue.

* Mon Jul 2 2007 Adam M. Dutko <gnome at dux-linux org> 1.21-5
- Fixed sourceforge Source0 link.
- Updated to 1.21.

* Tue Jun 19 2007 Adam M. Dutko <gnome at dux-linux org> 1.20.2-4
- Removed macros from changelog
- Formatted changelog from 1.20.2-2

* Tue Jun 19 2007 Adam M. Dutko <gnome at dux-linux org> 1.20.2-3
- Changed licensing to LGPL from GPL
- Removed execute bit from src/*
- Used bindir/install instead of /usr/bin/install

* Thu Jun 14 2007 Mary Ellen Foster <mefoster gmail com> 1.20.2-2
- Modifications from Ralf Corsepius (thanks!):
- Eliminated use of build/Makefile; just compile and install directly
- Use bindir rather than /usr/bin

* Sat May 12 2007 Adam Monsen <haircut@gmail.com> 1.20.2-1
- removed Makefile patch

* Thu Sep 21 2006 Mary Ellen Foster <mefoster gmail com> 1.19-1
- Initial package
