
%if 0%{?fedora}
%global qt4 1
%endif
%global qt5 1

%if 0%{?fedora} > 26 || 0%{?rhel} > 7
%global botan 1
%endif

#global snap 20181017

Name:    qca
Summary: Qt Cryptographic Architecture
Version: 2.2.1
Release: 3%{?dist}

License: LGPLv2+
URL:     https://userbase.kde.org/QCA
%if 0%{?snap}
Source0: qca-%{version}-%{snap}git.tar.xz
Source10: qca.sh
%else
Source0: http://download.kde.org/stable/qca/%{version}/qca-%{version}.tar.xz
%endif

## upstream patches

## upstreamable patches

BuildRequires: cmake >= 2.8.12
BuildRequires: gcc-c++
BuildRequires: libgcrypt-devel
%if 0%{?botan}
BuildRequires: pkgconfig(botan-2)
%else
Obsoletes: qca-botan < %{version}-%{release}
%endif
BuildRequires: pkgconfig(libcrypto) pkgconfig(libssl)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(libpkcs11-helper-1)
BuildRequires: pkgconfig(libsasl2)
%if 0%{?qt4}
BuildRequires: pkgconfig(QtCore)
%endif
# apidocs
# may need to add some tex-related ones too -- rex
BuildRequires: doxygen-latex
BuildRequires: graphviz

# qca2 renamed qca
Obsoletes: qca2 < 2.1.0
Provides:  qca2 = %{version}-%{release}
Provides:  qca2%{?_isa} = %{version}-%{release}

# most runtime consumers seem to assume the ossl plugin be present
Recommends: %{name}-ossl%{?_isa}

%description
Taking a hint from the similarly-named Java Cryptography Architecture,
QCA aims to provide a straightforward and cross-platform crypto API,
using Qt datatypes and conventions. QCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
application!

%package devel
Summary: Qt Cryptographic Architecture development files
# qca2 renamed qca
Obsoletes: qca2-devel < 2.1.0
Provides:  qca2-devel = %{version}-%{release}
Provides:  qca2-devel%{?_isa} = %{version}-%{release}
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description devel
This packages contains the development files for QCA.

%package doc
Summary: QCA API documentation
BuildArch: noarch
%description doc
This package includes QCA API documentation in HTML

%package botan
Summary: Botan plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description botan
%{summary}.

%package cyrus-sasl
Summary: Cyrus-SASL plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description cyrus-sasl
%{summary}.

%package gcrypt
Summary: Gcrypt plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gcrypt
%{summary}.

%package gnupg
Summary: Gnupg plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: gnupg
%description gnupg
%{summary}.

%package logger
Summary: Logger plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description logger
%{summary}.

%package nss
Summary: Nss plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description nss
%{summary}.

%package ossl
Summary: Openssl plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description ossl
%{summary}.

%package pkcs11
Summary: Pkcs11 plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description pkcs11
%{summary}.

%package softstore
Summary: Pkcs11 plugin for the Qt Cryptographic Architecture
Requires: %{name}%{?_isa} = %{version}-%{release}
%description softstore
%{summary}.

%if 0%{?qt5}
%package qt5
Summary: Qt5 Cryptographic Architecture
BuildRequires: pkgconfig(Qt5Core)
%if ! 0%{?botan}
Obsoletes: qca-qt5-botan < %{version}-%{release}
%endif
# most runtime consumers seem to assume the ossl plugin be present
Recommends: %{name}-qt5-ossl%{?_isa}
%description qt5
Taking a hint from the similarly-named Java Cryptography Architecture,
QCA aims to provide a straightforward and cross-platform crypto API,
using Qt datatypes and conventions. QCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
application!

%package qt5-devel
Summary: Qt5 Cryptographic Architecture development files
Requires:  %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-devel
%{summary}.

%package qt5-botan
Summary: Botan plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-botan
%{summary}.

%package qt5-cyrus-sasl
Summary: Cyrus-SASL plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-cyrus-sasl
%{summary}.

%package qt5-gcrypt
Summary: Gcrypt plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-gcrypt
%{summary}.

%package qt5-gnupg
Summary: Gnupg plugin for the Qt Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
Requires: gnupg
%description qt5-gnupg
%{summary}.

%package qt5-logger
Summary: Logger plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-logger
%{summary}.

%package qt5-nss
Summary: Nss plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-nss
%{summary}.

%package qt5-ossl
Summary: Openssl plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-ossl
%{summary}.

%package qt5-pkcs11
Summary: Pkcs11 plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-pkcs11
%{summary}.

%package qt5-softstore
Summary: Pkcs11 plugin for the Qt5 Cryptographic Architecture
Requires: %{name}-qt5%{?_isa} = %{version}-%{release}
%description qt5-softstore
%{summary}.
%endif


%prep
%autosetup -p1


%build
%if 0%{?qt5}
mkdir %{_target_platform}-qt5
pushd %{_target_platform}-qt5
%{cmake} .. \
  -DQCA_BINARY_INSTALL_DIR:STRING=%{_bindir} \
  -DQCA_FEATURE_INSTALL_DIR:PATH=%{_qt5_archdatadir}/mkspecs/features \
  -DQCA_INCLUDE_INSTALL_DIR:PATH=%{_qt5_headerdir} \
  -DQCA_LIBRARY_INSTALL_DIR:PATH=%{_qt5_libdir} \
  -DQCA_PLUGINS_INSTALL_DIR:PATH=%{_qt5_plugindir} \
  -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{_qt5_headerdir} \
  -DQT4_BUILD:BOOL=OFF
popd

%make_build -C %{_target_platform}-qt5
%endif

%if 0%{?qt4}
mkdir %{_target_platform}
pushd %{_target_platform}
%{cmake} .. \
  -DQCA_DOC_INSTALL_DIR:PATH=%{_docdir}/qca \
  -DQCA_BINARY_INSTALL_DIR:STRING=%{_bindir} \
  -DQCA_FEATURE_INSTALL_DIR:PATH=%{_qt4_prefix}/mkspecs/features \
  -DQCA_INCLUDE_INSTALL_DIR:PATH=%{_qt4_headerdir} \
  -DQCA_LIBRARY_INSTALL_DIR:PATH=%{_qt4_libdir} \
  -DQCA_PLUGINS_INSTALL_DIR:PATH=%{_qt4_plugindir} \
  -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{_qt4_headerdir} \
  -DQT4_BUILD:BOOL=ON
popd

%make_build -C %{_target_platform}

%make_build doc -C %{_target_platform}
%endif


%install
%if 0%{?qt5}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}-qt5
%endif
%if 0%{?qt4}
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# no make install target for docs yet
mkdir -p %{buildroot}%{_docdir}/qca
cp -a %{_target_platform}/apidocs/html/ \
      %{buildroot}%{_docdir}/qca/
%endif


%check
export CTEST_OUTPUT_ON_FAILURE=1
export PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig
# skip slow archs
%ifnarch %{arm} ppc64 s390x
%if 0%{?qt4}
test "$(pkg-config --modversion qca2)" = "%{version}"
make test ARGS="--timeout 180 --output-on-failure" -C %{_target_platform} ||:
%endif
%if 0%{?qt5}
test "$(pkg-config --modversion qca2-qt5)" = "%{version}"
make test ARGS="--timeout 180 --output-on-failure" -C %{_target_platform}-qt5
%endif
%endif


%if 0%{?qt4}
%ldconfig_scriptlets

%files
%doc README TODO
%license COPYING
%{_qt4_libdir}/libqca.so.2*
%{_bindir}/mozcerts
%{_bindir}/qcatool
%{_mandir}/man1/qcatool.1*
%dir %{_qt4_plugindir}/crypto/
## HACK alert, quirk of recycling default %%_docdir below in -doc subpkg -- rex
%exclude %{_docdir}/qca/html/

%files doc
%{_docdir}/qca/html/

%files devel
%{_qt4_headerdir}/QtCrypto
%{_qt4_libdir}/libqca.so
%{_libdir}/pkgconfig/qca2.pc
%{_libdir}/cmake/Qca/
%{_qt4_prefix}/mkspecs/features/crypto.prf

%if 0%{?botan}
%files botan
%doc plugins/qca-botan/README
%{_qt4_plugindir}/crypto/libqca-botan.so
%endif

%files cyrus-sasl
%doc plugins/qca-gcrypt/README
%{_qt4_plugindir}/crypto/libqca-cyrus-sasl.so

%files gcrypt
%{_qt4_plugindir}/crypto/libqca-gcrypt.so

%files gnupg
%doc plugins/qca-cyrus-sasl/README
%{_qt4_plugindir}/crypto/libqca-gnupg.so

%files logger
%doc plugins/qca-logger/README
%{_qt4_plugindir}/crypto/libqca-logger.so

%files nss
%doc plugins/qca-nss/README
%{_qt4_plugindir}/crypto/libqca-nss.so

%files ossl
%doc plugins/qca-ossl/README
%{_qt4_plugindir}/crypto/libqca-ossl.so

%files pkcs11
%doc plugins/qca-pkcs11/README
%{_qt4_plugindir}/crypto/libqca-pkcs11.so

%files softstore
%doc plugins/qca-softstore/README
%{_qt4_plugindir}/crypto/libqca-softstore.so
%endif

%if 0%{?qt5}
%ldconfig_scriptlets qt5

%files qt5
%doc README TODO
%license COPYING
%{_bindir}/mozcerts-qt5
%{_bindir}/qcatool-qt5
%{_mandir}/man1/qcatool-qt5.1*
%{_qt5_libdir}/libqca-qt5.so.2*
%dir %{_qt5_plugindir}/crypto/

%files qt5-devel
%{_qt5_headerdir}/QtCrypto
%{_qt5_libdir}/libqca-qt5.so
%{_libdir}/pkgconfig/qca2-qt5.pc
%{_libdir}/cmake/Qca-qt5/
%{_qt5_archdatadir}/mkspecs/features/crypto.prf

%if 0%{?botan}
%files qt5-botan
%doc plugins/qca-botan/README
%{_qt5_plugindir}/crypto/libqca-botan.so
%endif

%files qt5-cyrus-sasl
%doc plugins/qca-gcrypt/README
%{_qt5_plugindir}/crypto/libqca-cyrus-sasl.so

%files qt5-gcrypt
%{_qt5_plugindir}/crypto/libqca-gcrypt.so

%files qt5-gnupg
%doc plugins/qca-cyrus-sasl/README
%{_qt5_plugindir}/crypto/libqca-gnupg.so

%files qt5-logger
%doc plugins/qca-logger/README
%{_qt5_plugindir}/crypto/libqca-logger.so

%files qt5-nss
%doc plugins/qca-nss/README
%{_qt5_plugindir}/crypto/libqca-nss.so

%files qt5-ossl
%doc plugins/qca-ossl/README
%{_qt5_plugindir}/crypto/libqca-ossl.so

%files qt5-pkcs11
%doc plugins/qca-pkcs11/README
%{_qt5_plugindir}/crypto/libqca-pkcs11.so

%files qt5-softstore
%doc plugins/qca-softstore/README
%{_qt5_plugindir}/crypto/libqca-softstore.so
%endif


%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 25 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-1
- 2.2.1

* Mon Apr 22 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.2.0-1
- 2.2.0 formal release

* Tue Feb 12 2019 Rex Dieter <rdieter@fedoraproject.org> - 2.2.0-0.10.20181017
- make qt4 tests non-fatal

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-0.9.20181017
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.2.0-0.8.20181017
- 2.2.0-20181017 snapshot

* Wed Oct 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.2.0-0.7.20180619
- (re)enable botan support for real

* Mon Sep 10 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.2.0-0.6.20180619
- Recommends: qca(-qt5)-ossl

* Tue Jul 24 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.2.0-0.5.20180619
- 2.2.0-20180619 snapshot
- (re)enable botan support
- use %%_qt5_archdatadir/mkspecs

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-0.4.20180105
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sun Mar 04 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.2.0-0.2.20180105
- use %%make_build %%ldconfig_scriptlets
- BR: gcc-c++

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-0.2.20180105
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Rex Dieter <rdieter@fedoraproject.org> - 2.2.0-0.1.20180105
- 2.2.0-20180105 snapshot
- support openssl-1.1 (f27+)
- disable botan backend (f27+, until supports openssl-1.1 too, see #1531569)

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1.3-6
- re-enable pkcs11 support (#1423077)

* Mon Apr 24 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1.3-5
- Obsoletes: qca-pkcs11 (when pkcs11 support is disabled)

* Mon Apr 24 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1.3-4
- disable pkcs11 support on f26+ (#1423077)

* Fri Feb 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1.3-3
- update URL (#1423876)

* Fri Feb 17 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1.3-2
- use upstream tarball

* Mon Feb 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1.3-1
- qca-2.1.3 (#1419662)

* Mon Feb 06 2017 Rex Dieter <rdieter@fedoraproject.org> - 2.1.1-9
- pull in upstream fixes (#1419662), update URL

* Thu Jul 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.1.1-8
- pull in some upstream fixes

* Sat Apr 30 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.1.1-7
- own plugindir/crypto

* Wed Apr 20 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.1.1-6
- rebuild (qt)

* Mon Apr 18 2016 Rex Dieter <rdieter@fedoraproject.org> - 2.1.1-5
- update URL

* Mon Feb 08 2016 Rex Dieter <rdieter@fedoraproject.org> 2.1.1-4
- rebuild (botan), %%check: make qt5 tests non-fatal (FIXME: BigInteger test fails on rawhide)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Rex Dieter <rdieter@fedoraproject.org> 2.1.1-2
- pull in latest upstream fixes, fix build (related to install paths)

* Sat Oct 17 2015 Rex Dieter <rdieter@fedoraproject.org> 2.1.1-1
- 2.1.1

* Mon Aug 03 2015 Helio Chissini de Castro <helio@kde.org> - 2.1.0-14
- Add missing header. Breaks compilation for upcoming okular on Qt5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 01 2015 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-12
- exclude -doc content from main pkg

* Thu Apr 23 2015 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-11
- rebuild (gcc5)

* Thu Feb 19 2015 Rex Dieter <rdieter@fedoraproject.org> - 2.1.0-10
- rebuild (gcc5)

* Wed Jan 14 2015 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-9
- drop no_ansi workaround

* Wed Jan 14 2015 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-8
- workaround -gcrypt ftbfs (#1182200)
- BR: graphviz (docs use 'dot' apparently)

* Tue Jan 13 2015 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-7
- more upstream fixes (qt5 branch too)

* Tue Dec 02 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-6
- pull in upstream patches (primarily for qt5 parallel-installability)

* Mon Dec 01 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-5
- %%check: fix unittests

* Mon Dec 01 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-4
- initial qt5 support

* Fri Nov 14 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-3
- -doc: use %%_docdir instead, %%check: skip filewatch unittest

* Fri Nov 14 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-2
- -botan, -doc subpkgs, add READMEs to plugin subpkgs

* Fri Nov 14 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.0-1
- 2.1.0

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Mar 08 2014 Kevin Kofler <Kevin@tigcc.ticalc.org> - 2.0.3-7
- Rebuild against fixed qt to fix -debuginfo (#1074041)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 07 2012 Sven Lankes <sven@lank.es> - 2.0.3-3
- Fix build with gcc 4.7.0

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Nov 29 2010 Sven Lankes <sven@lank.es> - 2.0.3-1
- new upstream release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue May 05 2009 Sven Lankes <sven@lank.es> - 2.0.2-1
- new upstream release - qt 4.5-compat-fixes

* Wed Apr 08 2009 Sven Lankes <sven@lank.es> - 2.0.1-1
- new upstream release
- removed 64bit patch - now upstream

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri May 30 2008 Dennis Gilmore <dennis@ausil.us> - 2.0.0-3
- crypto.prf is in libdir not datadir

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.0-2
- Autorebuild for GCC 4.3

* Sun Oct 21 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.0.0-1
- version 2.0.0 final

* Sun Oct 21 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.0.0-0.4.beta7
- fix build on x86_64

* Sun Oct 21 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.0.0-0.3.beta7
- missing BR: openssl

* Thu Sep 13 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.0.0-0.2.beta7
- review from bug 289681 (thanks Rex)

* Sun Sep 09 2007 Aurelien Bompard <abompard@fedoraproject.org> 2.0.0-0.1.beta7
- initial package
