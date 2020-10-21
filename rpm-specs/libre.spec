# No upstream .so name versioning: https://github.com/creytiv/re/issues/249
%global soversion 0

Summary:        Library for real-time communications and SIP stack
Name:           libre
Version:        1.1.0
Release:        2%{?dist}
License:        BSD
URL:            https://github.com/baresip/re
Source0:        https://github.com/baresip/re/archive/v%{version}/re-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  openssl-devel
%else
BuildRequires:  openssl11-devel
%endif
BuildRequires:  zlib-devel
# Cover multiple third party repositories
Obsoletes:      libre0 < 0.6.1-2
Provides:       libre0 = %{version}-%{release}
Provides:       libre0%{?_isa} = %{version}-%{release}
Obsoletes:      re < 0.6.1-2
Provides:       re = %{version}-%{release}
Provides:       re%{?_isa} = %{version}-%{release}

%description
Libre is a portable and generic library for real-time communications with
async IO support and a complete SIP stack with support for SDP, RTP/RTCP,
STUN/TURN/ICE, BFCP and DNS client. 

%package devel
Summary:        Development files for the re library
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig
%if 0%{?fedora} || 0%{?rhel} >= 8
Requires:       openssl-devel
%else
Requires:       openssl11-devel
%endif
Requires:       zlib-devel
# Cover multiple third party repositories
Obsoletes:      libre0-devel < 0.6.1-2
Provides:       libre0-devel = %{version}-%{release}
Provides:       libre0-devel%{?_isa} = %{version}-%{release}
Obsoletes:      re-devel < 0.6.1-2
Provides:       re-devel = %{version}-%{release}
Provides:       re-devel%{?_isa} = %{version}-%{release}

%description devel
The libre-devel package includes header files and libraries necessary for
developing programs which use the re C library.

%prep
%setup -q -n re-%{version}

%build
%if 0%{?rhel} == 7
sed \
  -e 's|\(openssl\)|openssl11/\1|g' \
  -e 's|\(-DUSE_OPENSSL -DUSE_TLS\)|-I%{_includedir}/openssl11 \1|g' \
  -e 's|\(-lssl -lcrypto\)|-L%{_libdir}/openssl11 \1|g' \
  -i mk/re.mk
%endif

%make_build \
  SHELL='sh -x' \
  RELEASE=1 \
  USE_OPENSSL=1 \
  USE_ZLIB=1 \
  EXTRA_CFLAGS="$RPM_OPT_FLAGS" \
  EXTRA_LFLAGS="$RPM_LD_FLAGS" \
  LIB_SUFFIX=.so.%{soversion} \
  SH_LFLAGS="-shared -Wl,-soname,libre.so.%{soversion}"

%install
%make_install \
  LIBDIR=%{_libdir} \
  LIB_SUFFIX=.so.%{soversion}

# Create missing symlink and remove static library
ln -s %{name}.so.%{soversion} $RPM_BUILD_ROOT%{_libdir}/%{name}.so
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}.a

%ldconfig_scriptlets

%files
%license docs/COPYING
%doc docs/ChangeLog
%{_libdir}/%{name}.so.%{soversion}

%files devel
%{_libdir}/%{name}.so
%{_includedir}/re/
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/re/

%changelog
* Mon Oct 12 2020 Robert Scheck <robert@fedoraproject.org> 1.1.0-2
- Removed patch accepting 401 to re-register without stale=true

* Sat Oct 10 2020 Robert Scheck <robert@fedoraproject.org> 1.1.0-1
- Upgrade to 1.1.0 (#1887081)

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 28 2020 Robert Scheck <robert@fedoraproject.org> 0.6.1-2
- Add patch to accept 401 to re-register without stale=true
- Changes to match the Fedora Packaging Guidelines (#1843264 #c1)

* Thu May 28 2020 Robert Scheck <robert@fedoraproject.org> 0.6.1-1
- Upgrade to 0.6.1 (#1843264)
- Initial spec file for Fedora and Red Hat Enterprise Linux
