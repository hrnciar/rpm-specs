Name:           cxxtools
Version:        2.2.1
Release:        20%{?dist}
Summary:        A collection of general-purpose C++ classes
Epoch:          1

License:        LGPLv2+ 
URL:            http://www.tntnet.org/cxxtools.html
Source0:        http://www.tntnet.org/download/cxxtools-%{version}.tar.gz
Patch0:         cxxtools-2.2-arm.patch
# https://github.com/maekitalo/cxxtools/commit/86d4bb1881172752a80b706f9cc5fb0ebfa1b04e
Patch1:         cxxtools-float.patch
BuildRequires:  gcc
BuildRequires:  gcc-c++
Provides:       bundled(md5-polstra)

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{epoch}:%{version}-%{release}

%description    devel
Development files for %{name}


%prep
%setup -q
%patch0 -p0 -b .arm
%patch1 -p1 -b .float

# fix spurious executable perm
find -name "*.cpp" -exec chmod -x {} \;
find -name "*.h" -exec chmod -x {} \;

%build
%configure --disable-static \
%ifarch s390 s390x aarch64
    --with-atomictype=pthread \
%endif
    %{nil}
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# Find and remove all la files
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%check
    test/alltests

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libcxxtools*.so.*

%files devel
%{_bindir}/cxxtools-config
%{_libdir}/libcxxtools*.so
%{_libdir}/pkgconfig/%{name}-*.pc
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/cxxtools/

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 21 2018 Martin Gansser <martinkg@fedoraproject.org> - 1:2.2.1-17
- Fix FTBFS due missing BR gcc gcc-c++ (RHBZ#1603733)

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 29 2016 Than Ngo <than@redhat.com> - 2:2.2.1-11
- backport upstream patch to fix the rounding errors on ppc
- cleanup specfile

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:2.2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Oct 09 2015 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-9
- Rebuilt

* Thu Sep 24 2015 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-8
- Rebuilt
- added epoch to allow upgrade to older release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.2.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 baude <baude@us.ibm.com> - 2.2.1-3
- Moving removal of .las from check to install section 

* Mon Feb 17 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-2
- fix build on aarch64 where atomicity detection fails

* Mon Jan 20 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-1
- new release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 3 2013 Martin Gansser <martinkg@fedoraproject.org> - 2.2-1
- new release
- spec file cleanup

* Fri Sep 21 2012 Jon Ciesla <limburgher@gmail.com> - 2.1.1-5
- Fix FTBFS on ARM.

* Thu Jul 26 2012 Dan Horák <dan[at]danny.cz> - 2.1.1-4
- fix build on s390(x) where atomicity detection fails

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Martin Gansser <linux4martin@gmx.de> - 2.1.1-2
- added Provides: bundled(md5-polstra)

* Sat May 26 2012 Martin Gansser <linux4martin@gmx.de> - 2.1.1-1
- rebuild for new release
- fixed url
- removed empty files from doc
- fixed Requires for devel package
- added group tag for main package
- added unit test

* Sun Apr 29 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-1
- new release
- removed license comment

* Mon Sep 19 2011 Sebastian Vahl <fedora@deadbabylon.de> - 2.0-2
- split into -devel subpkg

* Sun Sep 18 2011 Sebastian Vahl <fedora@deadbabylon.de> - 2.0-1
- initial release

