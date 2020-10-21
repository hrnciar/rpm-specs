%undefine __cmake_in_source_build

Name:    qca-qt4
Summary: Qt4 Cryptographic Architecture
Version: 2.2.1
Release: 12%{?dist}

License: LGPLv2+
URL:     https://userbase.kde.org/QCA
Source0: http://download.kde.org/stable/qca/%{version}/qca-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libgcrypt-devel
BuildRequires: pkgconfig(botan-2)
BuildRequires: pkgconfig(libcrypto) pkgconfig(libssl)
BuildRequires: pkgconfig(nss)
BuildRequires: pkgconfig(libpkcs11-helper-1)
BuildRequires: pkgconfig(libsasl2)
BuildRequires: pkgconfig(QtCore)

# qca2 renamed qca
Obsoletes: qca2 < 2.1.0
Provides:  qca2 = %{version}-%{release}
Provides:  qca2%{?_isa} = %{version}-%{release}

# most runtime consumers seem to assume the ossl plugin be present
Recommends: %{name}-ossl%{?_isa}

%description
Taking a hint from the similarly-named Java Cryptography Architecture,
QCA aims to provide a straightforward and cross-platform crypto API,
using Qt4 datatypes and conventions. QCA separates the API from the
implementation, using plugins known as Providers. The advantage of this
model is to allow applications to avoid linking to or explicitly depending
on any particular cryptographic library. This allows one to easily change
or upgrade crypto implementations without even needing to recompile the
application!

%package -n qca
Summary: %{summary}
# qca2 renamed qca
Obsoletes: qca2 < 2.1.0
Provides:  qca2 = %{version}-%{release}
Provides:  qca2%{?_isa} = %{version}-%{release}
Recommends: qca-ossl%{?_isa}
%description -n qca
%description.

%package -n qca-devel
Summary: Qt4 Cryptographic Architecture development files
# qca2 renamed qca
Obsoletes: qca2-devel < 2.1.0
Provides:  qca2-devel = %{version}-%{release}
Provides:  qca2-devel%{?_isa} = %{version}-%{release}
Requires:  qca%{?_isa} = %{version}-%{release}
%description -n qca-devel
This packages contains the development files for QCA.

%package -n qca-botan
Summary: Botan plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-botan
%{summary}.

%package -n qca-cyrus-sasl
Summary: Cyrus-SASL plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-cyrus-sasl
%{summary}.

%package -n qca-gcrypt
Summary: Gcrypt plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-gcrypt
%{summary}.

%package -n qca-gnupg
Summary: Gnupg plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-gnupg
%{summary}.

%package -n qca-logger
Summary: Logger plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-logger
%{summary}.

%package -n qca-nss
Summary: Nss plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-nss
%{summary}.

%package -n qca-ossl
Summary: Openssl plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-ossl
%{summary}.

%package -n qca-pkcs11
Summary: Pkcs11 plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-pkcs11
%{summary}.

%package -n qca-softstore
Summary: Softstore plugin for the Qt4 Cryptographic Architecture
Requires: qca%{?_isa} = %{version}-%{release}
%description -n qca-softstore
%{summary}.


%prep
%autosetup -n qca-%{version}


%build
%cmake \
  -DQCA_DOC_INSTALL_DIR:PATH=%{_docdir}/qca \
  -DQCA_BINARY_INSTALL_DIR:STRING=%{_bindir} \
  -DQCA_FEATURE_INSTALL_DIR:PATH=%{_qt4_prefix}/mkspecs/features \
  -DQCA_INCLUDE_INSTALL_DIR:PATH=%{_qt4_headerdir} \
  -DQCA_LIBRARY_INSTALL_DIR:PATH=%{_qt4_libdir} \
  -DQCA_PLUGINS_INSTALL_DIR:PATH=%{_qt4_plugindir} \
  -DQCA_PRIVATE_INCLUDE_INSTALL_DIR:PATH=%{_qt4_headerdir} \
  -DQT4_BUILD:BOOL=ON

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets -n qca

%files -n qca
%doc README TODO
%license COPYING
%{_qt4_libdir}/libqca.so.2*
%{_bindir}/mozcerts
%{_bindir}/qcatool
%{_mandir}/man1/qcatool.1*
%dir %{_qt4_plugindir}/crypto/
## HACK alert, quirk of recycling default %%_docdir below in -doc subpkg -- rex
%exclude %{_docdir}/qca/html/

%files -n qca-devel
%{_qt4_headerdir}/QtCrypto/
%{_qt4_libdir}/libqca.so
%{_libdir}/pkgconfig/qca2.pc
%{_libdir}/cmake/Qca/
%{_qt4_prefix}/mkspecs/features/crypto.prf

%files -n qca-botan
%doc plugins/qca-botan/README
%{_qt4_plugindir}/crypto/libqca-botan.so

%files -n qca-cyrus-sasl
%doc plugins/qca-gcrypt/README
%{_qt4_plugindir}/crypto/libqca-cyrus-sasl.so

%files -n qca-gcrypt
%{_qt4_plugindir}/crypto/libqca-gcrypt.so

%files -n qca-gnupg
%doc plugins/qca-cyrus-sasl/README
%{_qt4_plugindir}/crypto/libqca-gnupg.so

%files -n qca-logger
%doc plugins/qca-logger/README
%{_qt4_plugindir}/crypto/libqca-logger.so

%files -n qca-nss
%doc plugins/qca-nss/README
%{_qt4_plugindir}/crypto/libqca-nss.so

%files -n qca-ossl
%doc plugins/qca-ossl/README
%{_qt4_plugindir}/crypto/libqca-ossl.so

%files -n qca-pkcs11
%doc plugins/qca-pkcs11/README
%{_qt4_plugindir}/crypto/libqca-pkcs11.so

%files -n qca-softstore
%doc plugins/qca-softstore/README
%{_qt4_plugindir}/crypto/libqca-softstore.so


%changelog
* Fri Sep 04 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-12
- rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jun 24 2020 Rex Dieter <rdieter@fedoraproject.org> - 2.2.1-10
- first try qca-qt4 compat pkg, keep "qca" basename to keep ugprade path
  as simple as possible.

