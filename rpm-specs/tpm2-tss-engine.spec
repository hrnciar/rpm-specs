Name:           tpm2-tss-engine
Version:        1.0.1
Release:        2%{?dist}
Summary:      OpenSSL Engine for TPM2 devices using the tpm2-tss software stack

License:     BSD
URL:            https://github.com/tpm2-software/tpm2-tss-engine
Source0:        https://github.com/tpm2-software/tpm2-tss-engine/releases/download/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  gcc
BuildRequires:  gcc-c++ 
BuildRequires:  pkgconfig
BuildRequires:  pandoc
BuildRequires:  tpm2-tss-devel 
BuildRequires:  openssl-devel

Requires:       openssl 
Requires:       tpm2-tss

%description
tpm2-tss-engine is an engine implementation for OpenSSL that uses tpm2-tss 
software stack. It uses the Enhanced System API (ESAPI) interface of the
TSS 2.0 for downwards communication. It supports RSA decryption and signatures
as well as ECDSA signatures.

%prep
%autosetup -n %{name}-%{version}


%build
%configure 
%make_build


%install
%make_install
find %{buildroot}%{_libdir}/engines-1.1 -type f -name \*.la  -exec rm {} +
find %{buildroot}%{_libdir}/engines-1.1 -type f -name \*.a  -exec rm {} +



%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_libdir}/engines-1.1/libtpm2tss.so
%{_libdir}/engines-1.1/tpm2tss.so


%package devel
Summary:  Headers and libraries for building applications against tpm2-tss-engine
Requires: %{name}%{_isa} = %{version}-%{release}

%description devel
This package contains headers and libraries for building apps applications
against tpm2-tss-engine

%files devel
%{_includedir}/tpm2-tss-engine.h
%{_mandir}/man3/tpm2tss_*.3.*



%package utilities
Summary:  Utility binary for openssl using tpm2-tss software stack
Requires: %{name}%{_isa} = %{version}-%{release}

%description utilities
This package contains the binary of the engine implementation for openssl that
uses the tpm2-tss software stack

%files utilities
%{_bindir}/tpm2tss-genkey
%{_datadir}/bash-completion/completions/tpm2tss-genkey
%{_mandir}/man1/tpm2tss-*.1.*




%changelog
* Sun Mar 1 2020 Mathias Zavala <zvl.mathias@gmail.com> - 1.0.1-2
- Move tpm2-tss.so from -devel to main package to fix missing engine error 

* Mon Nov 18 2019 Mathias Zavala <zvl.mathias@gmail.com> - 1.0.1-1
- initial version of the package
