%?mingw_package_header

# For the curious:
# 0.9.5a soversion = 0
# 0.9.6  soversion = 1
# 0.9.6a soversion = 2
# 0.9.6c soversion = 3
# 0.9.7a soversion = 4
# 0.9.7ef soversion = 5
# 0.9.8ab soversion = 6
# 0.9.8g soversion = 7
# 0.9.8jk + EAP-FAST soversion = 8
# 1.0.0 soversion = 10
# 1.1.0 soversion = 1_1 (same as upstream although presence of some symbols
#                        depends on build configuration options)
%global soversion 1_1

# Enable the tests.
# These only work some of the time, but fail randomly at other times
# (although I have had them complete a few times, so I don't think
# there is any actual problem with the binaries).
%global run_tests 0

Name:           mingw-openssl
Version:        1.1.1c
Release:        6%{?dist}
Summary:        MinGW port of the OpenSSL toolkit

License:        OpenSSL
URL:            http://www.openssl.org/

# We have to remove certain patented algorithms from the openssl source
# tarball with the hobble-openssl script which is included below.
# The original openssl upstream tarball cannot be shipped in the .src.rpm.
Source:         openssl-%{version}-hobbled.tar.xz

Source1:        hobble-openssl
Source2:        Makefile.certificate
Source6:        make-dummy-cert
Source7:        renew-dummy-cert
Source9:        opensslconf-new.h
Source10:       opensslconf-new-warning.h
Source11:       README.FIPS
Source12:       ec_curve.c
Source13:       ectest.c

# Build changes
Patch1: openssl-1.1.1-build.patch
Patch2: openssl-1.1.1-defaults.patch
Patch3: openssl-1.1.0-no-html.patch
Patch4: openssl-1.1.1-man-rename.patch
# Bug fixes
Patch21: openssl-1.1.0-issuer-hash.patch
# Functionality changes
Patch31: openssl-1.1.1-conf-paths.patch
Patch32: openssl-1.1.1-version-add-engines.patch
Patch33: openssl-1.1.1-apps-dgst.patch
Patch36: openssl-1.1.1-no-brainpool.patch
Patch37: openssl-1.1.1-ec-curves.patch
Patch38: openssl-1.1.1-no-weak-verify.patch
Patch40: openssl-1.1.1-disable-ssl3.patch
Patch41: openssl-1.1.1-system-cipherlist.patch
Patch42: openssl-1.1.1-fips.patch
Patch43: openssl-1.1.1-ignore-bound.patch
Patch44: openssl-1.1.1-version-override.patch
Patch45: openssl-1.1.1-weak-ciphers.patch
Patch46: openssl-1.1.1-seclevel.patch
Patch47: openssl-1.1.1-ts-sha256-default.patch
Patch48: openssl-1.1.1-fips-post-rand.patch
Patch49: openssl-1.1.1-evp-kdf.patch
Patch50: openssl-1.1.1-ssh-kdf.patch
# Backported fixes including security fixes
Patch51: openssl-1.1.1-upstream-sync.patch
Patch52: openssl-1.1.1-s390x-update.patch
Patch53: openssl-1.1.1-fips-crng-test.patch
Patch54: openssl-1.1.1-regression-fixes.patch

# MinGW-specific patches.
# The function secure_getenv is a GNU extension which isn't available on Windows
# This reverts part of openssl-1.1.0-no-weak-verify.patch
Patch101:       openssl-mingw64-dont-use-secure-getenv.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-zlib

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-zlib

BuildRequires:  perl-interpreter
BuildRequires:  perl-FindBin
BuildRequires:  perl-lib
BuildRequires:  perl-File-Compare
BuildRequires:  perl-File-Copy
BuildRequires:  sed
BuildRequires:  /usr/bin/cmp
BuildRequires:  lksctp-tools-devel
BuildRequires:  /usr/bin/rename
BuildRequires:  /usr/bin/pod2man

%if %{run_tests}
# Required both to build, and to run the tests.
# XXX This needs to be fixed - cross-compilation should not
# require running executables.
BuildRequires:  wine

# Required to run the tests.
BuildRequires:  xorg-x11-server-Xvfb
%endif


%description
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains Windows (MinGW) libraries and development tools.


# Win32
%package -n mingw32-openssl
Summary:        MinGW port of the OpenSSL toolkit
#Requires:       ca-certificates >= 2008-5
Requires:       pkgconfig

%description -n mingw32-openssl
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains Windows (MinGW) libraries and development tools.

%package -n mingw32-openssl-static
Summary:        Static version of the MinGW port of the OpenSSL toolkit
Requires:       mingw32-openssl = %{version}-%{release}

%description -n mingw32-openssl-static
Static version of the MinGW port of the OpenSSL toolkit.

# Win64
%package -n mingw64-openssl
Summary:        MinGW port of the OpenSSL toolkit
#Requires:       ca-certificates >= 2008-5
Requires:       pkgconfig

%description -n mingw64-openssl
The OpenSSL toolkit provides support for secure communications between
machines. OpenSSL includes a certificate management tool and shared
libraries which provide various cryptographic algorithms and
protocols.

This package contains Windows (MinGW) libraries and development tools.

%package -n mingw64-openssl-static
Summary:        Static version of the MinGW port of the OpenSSL toolkit
Requires:       mingw64-openssl = %{version}-%{release}

%description -n mingw64-openssl-static
Static version of the MinGW port of the OpenSSL toolkit.


%?mingw_debug_package


%prep
%setup -q -n openssl-%{version}

# The hobble_openssl is called here redundantly, just to be sure.
# The tarball has already the sources removed.
%{SOURCE1} > /dev/null

cp %{SOURCE12} crypto/ec/
cp %{SOURCE13} test/

%patch1 -p1 -b .build   %{?_rawbuild}
%patch2 -p1 -b .defaults
%patch3 -p1 -b .no-html  %{?_rawbuild}
%patch4 -p1 -b .man-rename

%patch21 -p1 -b .issuer-hash

%patch31 -p1 -b .conf-paths
%patch32 -p1 -b .version-add-engines
%patch33 -p1 -b .dgst
%patch36 -p1 -b .no-brainpool
%patch37 -p1 -b .curves
%patch38 -p1 -b .no-weak-verify
%patch40 -p1 -b .disable-ssl3
%patch41 -p1 -b .system-cipherlist
#%patch42 -p1 -b .fips
%patch43 -p1 -b .ignore-bound
%patch44 -p1 -b .version-override
%patch45 -p1 -b .weak-ciphers
%patch46 -p1 -b .seclevel
%patch47 -p1 -b .ts-sha256-default
#%patch48 -p1 -b .fips-post-rand
#%patch49 -p1 -b .evp-kdf
#%patch50 -p1 -b .ssh-kdf
%patch51 -p1 -b .upstream-sync
%patch52 -p1 -b .s390x-update
%patch53 -p1 -b .crng-test
%patch54 -p1 -b .regression

# MinGW specific patches
%patch101 -p1 -b .secure_getenv_mingw

# Create two copies of the source folder as OpenSSL doesn't support out of source builds
mkdir ../build_win32
mv * ../build_win32
mv ../build_win32 .
mkdir build_win64
cp -Rp build_win32/* build_win64


%build
###############################################################################
# Win32
###############################################################################
pushd build_win32

PERL=%{__perl} \
CFLAGS="%{mingw32_cflags}" \
LDFLAGS="%{mingw32_ldflags}" \
./Configure \
  --prefix=%{mingw32_prefix} \
  --openssldir=%{mingw32_sysconfdir}/pki/tls \
  zlib enable-camellia enable-seed enable-rfc3779 \
  enable-cms enable-md2 enable-rc5 enable-ssl3 enable-ssl3-method \
  enable-weak-ssl-ciphers \
  no-mdc2 no-ec2m \
  --cross-compile-prefix=%{mingw32_target}- \
  shared mingw

# Do not run this in a production package the FIPS symbols must be patched-in
#util/mkdef.pl crypto update

make all

# Overwrite FIPS README
cp -f %{SOURCE11} .

popd

###############################################################################
# Win64
###############################################################################
pushd build_win64

PERL=%{__perl} \
CFLAGS="%{mingw64_cflags}" \
LDFLAGS="%{mingw64_ldflags}" \
./Configure \
  --prefix=%{mingw64_prefix} \
  --openssldir=%{mingw64_sysconfdir}/pki/tls \
  zlib enable-camellia enable-seed enable-rfc3779 \
  enable-cms enable-md2 enable-rc5 enable-ssl3 enable-ssl3-method \
  enable-weak-ssl-ciphers enable-ec_nistp_64_gcc_128 \
  no-mdc2 no-ec2m no-hw \
  --cross-compile-prefix=%{mingw64_target}- \
  shared mingw64

# Do not run this in a production package the FIPS symbols must be patched-in
#util/mkdef.pl crypto update

make all

# Overwrite FIPS README
cp -f %{SOURCE11} .

popd

# Clean up the .pc files
for i in build_win{32,64}/libcrypto.pc build_win{32,64}/libssl.pc build_win{32,64}/openssl.pc ; do
  sed -i '/^Libs.private:/{s/-L[^ ]* //;s/-Wl[^ ]* //}' $i
done


%if %{run_tests}
%check
#----------------------------------------------------------------------
# Run some tests.

# We must revert patch31 before tests otherwise they will fail
patch -p1 -R < %{PATCH31}

# This is a bit of a hack, but the test scripts look for 'openssl'
# by name.
pushd build_win32/apps
ln -s openssl.exe openssl
popd

# This is useful for diagnosing Wine problems.
WINEDEBUG=+loaddll
export WINEDEBUG

# Make sure we can find the installed DLLs.
WINEDLLPATH=%{mingw32_bindir}
export WINEDLLPATH

# The tests run Wine and require an X server (but don't really use
# it).  Therefore we create a virtual framebuffer for the duration of
# the tests.
# XXX There is no good way to choose a random, unused display.
# XXX Setting depth to 24 bits avoids bug 458219.
unset DISPLAY
display=:21
Xvfb $display -screen 0 1024x768x24 -ac -noreset & xpid=$!
trap "kill -TERM $xpid ||:" EXIT
sleep 3
DISPLAY=$display
export DISPLAY

make test

#----------------------------------------------------------------------
%endif

# Add generation of HMAC checksum of the final stripped library
##define __spec_install_post \
#    #{?__debug_package:#{__debug_install_post}} \
#    #{__arch_install_post} \
#    #{__os_install_post} \
#    fips/fips_standalone_sha1 $RPM_BUILD_ROOT/#{_lib}/libcrypto.so.#{version} >$RPM_BUILD_ROOT/#{_lib}/.libcrypto.so.#{version}.hmac \
#    ln -sf .libcrypto.so.#{version}.hmac $RPM_BUILD_ROOT/#{_lib}/.libcrypto.so.#{soversion}.hmac \
##{nil}


%install
mkdir -p $RPM_BUILD_ROOT%{mingw32_libdir}/openssl
mkdir -p $RPM_BUILD_ROOT%{mingw32_bindir}
mkdir -p $RPM_BUILD_ROOT%{mingw32_includedir}
mkdir -p $RPM_BUILD_ROOT%{mingw32_mandir}

mkdir -p $RPM_BUILD_ROOT%{mingw64_libdir}/openssl
mkdir -p $RPM_BUILD_ROOT%{mingw64_bindir}
mkdir -p $RPM_BUILD_ROOT%{mingw64_includedir}
mkdir -p $RPM_BUILD_ROOT%{mingw64_mandir}

%mingw_make_install DESTDIR=$RPM_BUILD_ROOT install

# Install the file applink.c (#499934)
install -m644 build_win32/ms/applink.c $RPM_BUILD_ROOT%{mingw32_includedir}/openssl/applink.c
install -m644 build_win64/ms/applink.c $RPM_BUILD_ROOT%{mingw64_includedir}/openssl/applink.c

# Remove the man pages
rm -rf $RPM_BUILD_ROOT%{mingw32_mandir}
rm -rf $RPM_BUILD_ROOT%{mingw64_mandir}

# Set permissions on lib*.dll.a so that strip works.
chmod 0755 $RPM_BUILD_ROOT%{mingw32_libdir}/libcrypto.dll.a
chmod 0755 $RPM_BUILD_ROOT%{mingw32_libdir}/libssl.dll.a
chmod 0755 $RPM_BUILD_ROOT%{mingw64_libdir}/libcrypto.dll.a
chmod 0755 $RPM_BUILD_ROOT%{mingw64_libdir}/libssl.dll.a

# Install a makefile for generating keys and self-signed certs, and a script
# for generating them on the fly.
mkdir -p $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pki/tls/certs
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pki/tls/certs/Makefile
install -m755 %{SOURCE6} $RPM_BUILD_ROOT%{mingw32_bindir}/make-dummy-cert
install -m755 %{SOURCE7} $RPM_BUILD_ROOT%{mingw32_bindir}/renew-dummy-cert

mkdir -p $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pki/tls/certs
install -m644 %{SOURCE2} $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pki/tls/certs/Makefile
install -m755 %{SOURCE6} $RPM_BUILD_ROOT%{mingw64_bindir}/make-dummy-cert
install -m755 %{SOURCE7} $RPM_BUILD_ROOT%{mingw64_bindir}/renew-dummy-cert

mkdir -m700 $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pki/CA
mkdir -m700 $RPM_BUILD_ROOT%{mingw32_sysconfdir}/pki/CA/private

mkdir -m700 $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pki/CA
mkdir -m700 $RPM_BUILD_ROOT%{mingw64_sysconfdir}/pki/CA/private

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-openssl.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-openssl.debugfiles



# Win32
%files -n mingw32-openssl -f mingw32-openssl.debugfiles
%doc build_win32/LICENSE
%{mingw32_bindir}/openssl.exe
%{mingw32_bindir}/c_rehash
%{mingw32_bindir}/libcrypto-%{soversion}.dll
%{mingw32_bindir}/libssl-%{soversion}.dll
%{mingw32_bindir}/make-dummy-cert
%{mingw32_bindir}/renew-dummy-cert
%{mingw32_libdir}/libcrypto.dll.a
%{mingw32_libdir}/libssl.dll.a
%{mingw32_libdir}/engines-%{soversion}
%{mingw32_libdir}/pkgconfig/*.pc
%{mingw32_includedir}/openssl
%config(noreplace) %{mingw32_sysconfdir}/pki

%files -n mingw32-openssl-static
%{mingw32_libdir}/libcrypto.a
%{mingw32_libdir}/libssl.a

# Win64
%files -n mingw64-openssl -f mingw64-openssl.debugfiles
%doc build_win64/LICENSE
%{mingw64_bindir}/openssl.exe
%{mingw64_bindir}/c_rehash
%{mingw64_bindir}/libcrypto-%{soversion}-x64.dll
%{mingw64_bindir}/libssl-%{soversion}-x64.dll
%{mingw64_bindir}/make-dummy-cert
%{mingw64_bindir}/renew-dummy-cert
%{mingw64_libdir}/libcrypto.dll.a
%{mingw64_libdir}/libssl.dll.a
%{mingw64_libdir}/engines-%{soversion}
%{mingw64_libdir}/pkgconfig/*.pc
%{mingw64_includedir}/openssl
%config(noreplace) %{mingw64_sysconfdir}/pki

%files -n mingw64-openssl-static
%{mingw64_libdir}/libcrypto.a
%{mingw64_libdir}/libssl.a


%changelog
* Tue Aug 04 2020 Sandro Mani <manisandro@gmail.com> - 1.1.1c-6
- Ensure mingw CFLAGS and LDFLAGS are used
- Add BR: perl-File-Copy

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1c-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Richard W.M. Jones <rjones@redhat.com> - 1.1.1c-4
- +BR perl-FindBin and perl-lib, no longer pulled in implicitly.
- +BR perl-File-Compare.

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1c-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Fabiano Fidêncio <fidencio@redhat.com> - 1.1.1c-1
- Update the sources accordingly to its native counter part, rhbz#1740772

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0h-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0h-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Aug 24 2018 Christophe Fergeau <cfergeau@redhat.com> - 1.1.0h-1
- Sync with f28 openssl 1.1.0h

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2h-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Richard W.M. Jones <rjones@redhat.com> - 1.0.2h-6
- Remove mktemp build dependency, part of coreutils.

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2h-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Sandro Mani <manisandro@gmail.com> - 1.0.2h-4
- Exclude *.debug files from non-debug packages

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2h-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2h-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat May  7 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.2h-1
- Synced with native openssl-1.0.2h-1
- Fixes RHBZ #1332591 #1332589 #1330104 #1312861 #1312857 #1307773 #1302768

* Sat Feb  6 2016 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.2f-1
- Synced with native openssl-1.0.2f-2
- Fixes RHBZ #1239685 #1290334 #1302768

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2a-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 24 2015 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.2a-1
- Synced with native openssl-1.0.2a-1.fc23
- Fixes various CVE's (RHBZ #1203855 #1203856)

* Mon Dec 22 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1j-1
- Synced with native openssl-1.0.1j-3.fc22
- Add support for RFC 5649
- Prevent compiler warning "Please include winsock2.h before windows.h"
  when using the OpenSSL headers
- Fixes various CVE's (RHBZ #1127889 #1127709 #1152851)

* Thu Aug 21 2014 Marc-André Lureau <marcandre.lureau@redhat.com> - 1.0.1i-1
- Synced with native openssl-1.0.1i-3.fc21
- Fixes various flaws (RHBZ#1096234 and RHBZ#1127705)
  CVE-2014-3505 CVE-2014-3506 CVE-2014-3507 CVE-2014-3511
  CVE-2014-3510 CVE-2014-3508 CVE-2014-3509 CVE-2014-0221
  CVE-2014-0198 CVE-2014-0224 CVE-2014-0195 CVE-2010-5298
  CVE-2014-3470

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1e-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Apr  9 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1e-6
- Synced patches with native openssl-1.0.1e-44.fc21
- Fixes CVE-2014-0160 (RHBZ #1085066)

* Sat Jan 25 2014 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1e-5
- Synced patches with native openssl-1.0.1e-38.fc21
- Enable ECC support (RHBZ #1037919)
- Fixes CVE-2013-6450 (RHBZ #1047844)
- Fixes CVE-2013-4353 (RHBZ #1049062)
- Fixes CVE-2013-6449 (RHBZ #1045444)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1e-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 10 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1e-3
- Rebuild to resolve InterlockedCompareExchange regression in mingw32 libraries

* Fri May 10 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1e-2
- Fix build of manual pages with current pod2man (#959439)

* Sun Mar 24 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1e-1
- Update to 1.0.1e (RHBZ #920868)
- Synced patches with native openssl-1.0.1e-4.fc19

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1c-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jan 11 2013 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1c-2
- Fix FTBFS against latest pod2man

* Fri Nov  9 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.1c-1
- Update to 1.0.1c
- Synced patches with native openssl-1.0.1c-7.fc19

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0d-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Mar 10 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.0d-6
- Added win64 support

* Wed Mar 07 2012 Kalev Lember <kalevlember@gmail.com> - 1.0.0d-5
- Pass the path to perl interpreter to Configure

* Tue Mar 06 2012 Kalev Lember <kalevlember@gmail.com> - 1.0.0d-4
- Renamed the source package to mingw-openssl (#800443)
- Modernize the spec file
- Use mingw macros without leading underscore

* Mon Feb 27 2012 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.0d-3
- Rebuild against the mingw-w64 toolchain

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0d-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sat Apr 23 2011 Kalev Lember <kalev@smartlink.ee> - 1.0.0d-1
- Update to 1.0.0d
- Synced patches with Fedora native openssl-1.0.0d-2

* Fri Mar 04 2011 Kai Tietz <ktietz@redhat.com>
- Fixes for CVE-2011-0014 openssl: OCSP stapling vulnerability

* Thu Mar  3 2011 Kai Tietz <ktietz@redhat.com> - 1.0.0a-3
- Bump and rebuild.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jun 19 2010 Kalev Lember <kalev@smartlink.ee> - 1.0.0a-1
- Updated to openssl 1.0.0a
- Synced patches with Fedora native openssl-1.0.0a-1
- Use sed to fix up cflags instead of unmaintainable patch
- Rebased mingw32 specific patches
- Disabled capieng to fix build
- Properly regenerate def files with mkdef.pl and drop linker-fix.patch

* Thu Nov 26 2009 Kalev Lember <kalev@smartlink.ee> - 1.0.0-0.6.beta4
- Merged patches from native Fedora openssl (up to 1.0.0-0.16.beta4)
- Dropped the patch to fix non-fips mingw build,
  as it's now merged into fips patch from native openssl

* Sun Nov 22 2009 Kalev Lember <kalev@smartlink.ee> - 1.0.0-0.5.beta4
- Updated to version 1.0.0 beta 4
- Merged patches from native Fedora openssl (up to 1.0.0-0.15.beta4)
- Added patch to fix build with fips disabled

* Fri Sep 18 2009 Kalev Lember <kalev@smartlink.ee> - 1.0.0-0.4.beta3
- Rebuilt to fix debuginfo

* Sun Aug 30 2009 Kalev Lember <kalev@smartlink.ee> - 1.0.0-0.3.beta3
- Simplified the lib renaming patch

* Sun Aug 30 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.0-0.2.beta3
- Fixed invalid RPM Provides

* Fri Aug 28 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 1.0.0-0.1.beta3
- Update to version 1.0.0 beta 3
- Use %%global instead of %%define
- Automatically generate debuginfo subpackage
- Merged various changes from the native Fedora package (up to 1.0.0-0.5.beta3)
- Don't use the %%{_mingw32_make} macro anymore as it's ugly and causes side-effects
- Added missing BuildRequires mingw32-dlfcn (Kalev Lember)
- Reworked patches to rename *eay32.dll to lib*.dll (Kalev Lember)
- Patch Configure script to use %%{_mingw32_cflags} (Kalev Lember)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8j-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat May  9 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.8j-6
- Add the file include/openssl/applink.c to the package (BZ #499934)

* Tue Apr 14 2009 Erik van Pienbroek <epienbro@fedoraproject.org> - 0.9.8j-5
- Fixed %%defattr line
- Added -static subpackage

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8j-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 20 2009 Richard W.M. Jones <rjones@redhat.com> - 0.9.8j-3
- Rebuild for mingw32-gcc 4.4

* Mon Feb  2 2009 Levente Farkas <lfarkas@lfarkas.org> - 0.9.8j-2
- Various build fixes.

* Wed Jan 28 2009 Levente Farkas <lfarkas@lfarkas.org> - 0.9.8j-1
- update to new upstream version.

* Mon Dec 29 2008 Levente Farkas <lfarkas@lfarkas.org> - 0.9.8g-2
- minor cleanup.

* Tue Sep 30 2008 Richard W.M. Jones <rjones@redhat.com> - 0.9.8g-1
- Initial RPM release.
