Name:      compat-libicu63
Version:   63.2
Release:   2%{?dist}
Summary:   Compat package with icu libraries

License:   MIT and UCD and Public Domain
URL:       http://site.icu-project.org/
Source0:   https://github.com/unicode-org/icu/releases/download/release-63-2/icu4c-63_2-src.tgz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: doxygen, autoconf, python2

# https://bugzilla.redhat.com/show_bug.cgi?id=1708935 temporarily roll back to 63.1
Patch0: roll-back-63.2-to-63.1-patched.patch
Patch4: gennorm2-man.patch
Patch5: icuinfo-man.patch
Patch100: armv7hl-disable-tests.patch

# Explicitly conflict with older icu packages that ship libraries
# with the same soname as this compat package
Conflicts: libicu < 64

%description
Compatibility package with icu libraries ABI version 63.


%prep
%setup -q -n icu
%patch0 -p2 -b .roll-back-63.2-to-63.1-patched.patch
%patch4 -p1 -b .gennorm2-man.patch
%patch5 -p1 -b .icuinfo-man.patch
%ifarch armv7hl
%patch100 -p1 -b .armv7hl-disable-tests.patch
%endif


%build
pushd source
autoconf
CFLAGS='%optflags -fno-strict-aliasing'
CXXFLAGS='%optflags -fno-strict-aliasing'
# Endian: BE=0 LE=1
%if ! 0%{?endian}
CPPFLAGS='-DU_IS_BIG_ENDIAN=1'
%endif

#rhbz856594 do not use --disable-renaming or cope with the mess
OPTIONS='--with-data-packaging=library --disable-samples'
%if 0%{?debugtrace}
OPTIONS=$OPTIONS' --enable-debug --enable-tracing'
%endif
%configure $OPTIONS

#rhbz#225896
sed -i 's|-nodefaultlibs -nostdlib||' config/mh-linux
#rhbz#813484
sed -i 's| \$(docfilesdir)/installdox||' Makefile
# There is no source/doc/html/search/ directory
sed -i '/^\s\+\$(INSTALL_DATA) \$(docsrchfiles) \$(DESTDIR)\$(docdir)\/\$(docsubsrchdir)\s*$/d' Makefile
# rhbz#856594 The configure --disable-renaming and possibly other options
# result in icu/source/uconfig.h.prepend being created, include that content in
# icu/source/common/unicode/uconfig.h to propagate to consumer packages.
test -f uconfig.h.prepend && sed -e '/^#define __UCONFIG_H__/ r uconfig.h.prepend' -i common/unicode/uconfig.h

# more verbosity for build.log
sed -i -r 's|(PKGDATA_OPTS = )|\1-v |' data/Makefile

make %{?_smp_mflags} VERBOSE=1


%install
make %{?_smp_mflags} -C source install DESTDIR=$RPM_BUILD_ROOT
chmod +x $RPM_BUILD_ROOT%{_libdir}/*.so.*

# Remove files that aren't needed for the compat package
rm -rf $RPM_BUILD_ROOT%{_bindir}
rm -rf $RPM_BUILD_ROOT%{_includedir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.so
rm -rf $RPM_BUILD_ROOT%{_libdir}/icu/
rm -rf $RPM_BUILD_ROOT%{_libdir}/pkgconfig/
rm -rf $RPM_BUILD_ROOT%{_sbindir}
rm -rf $RPM_BUILD_ROOT%{_datadir}/icu/
rm -rf $RPM_BUILD_ROOT%{_mandir}


%files
%license LICENSE
%{_libdir}/*.so.*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 63.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 01 2019 Pete Walter <pwalter@fedoraproject.org> - 63.2-1
- Initial packaging
