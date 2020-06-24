# https://github.com/kypeli/kQOAuth/commit/7c31a120f86f3351a9eb0bafd321f2a977b3e0a5
%global commit0 7c31a120f86f3351a9eb0bafd321f2a977b3e0a5
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global commitdate 20140122
%global sname kqoauth

Name:           %{sname}-qt5
Version:        0.98
Release:        0.6.%{commitdate}git%{shortcommit0}%{?dist}
Summary:        Qt OAuth support library
License:        LGPLv2+
Url:            https://github.com/kypeli/kQOAuth
Source0:        https://github.com/kypeli/kQOAuth/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  gcc-c++ 
BuildRequires:  compat-openssl10-devel

%description
kQOAuth is a OAuth 1.0 library written for Qt in C++. The goals for the
library have been to provide easy integration to existing Qt5 applications
utilizing Qt5 signals describing the OAuth process, and to provide a
convenient approach to OAuth authentication.

kQOAuth has support for retrieving the user authorization from the service
provider's website. kQOAuth will open the user's web browser to the
authorization page, give a local URL as the callback URL and setup a HTTP
server on this address to listen for the reply from the service and then
process it.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -qn kQOAuth-%{commit0}
sed -i -e 's|\/usr\/lib|"%{_libdir}"|' kqoauth.prf
find ./ -name "*.pro" -print0| xargs -r0 sed -i -e 's|\/lib|/"%{_lib}"|' --

# Fix pkgconfig file
sed -i 's|QtCore QtNetwork|Qt5Core Qt5Network|g' src/pcfile.sh

%build
%{qmake_qt5} KQOAUTH_LIBDIR=%{_libdir} \
  QMAKE_LFLAGS="${RPM_LD_FLAGS} -Wl,--as-needed"
%make_build

%install
%make_install INSTALL_ROOT=%{buildroot}

%check
export LD_LIBRARY_PATH=%{buildroot}%{_libdir}
make check

%ldconfig_scriptlets

%files
%doc CHANGELOG README
%license COPYING
%{_libdir}/lib%{sname}.so.*

%files devel
%{_includedir}/QtKOAuth/
%{_libdir}/lib%{sname}.so
%{_libdir}/pkgconfig/%{sname}.pc
%exclude %{_libdir}/lib%{sname}.prl
%exclude %{_libdir}/qt5/mkspecs/features/%{sname}.prf

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.6.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.5.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.4.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.3.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.98-0.2.20140122git7c31a12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Nov 25 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.98-0.1.20140122git7c31a12
- inital build
