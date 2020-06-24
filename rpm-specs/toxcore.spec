%global sover   2

Name:           toxcore
Version:        0.2.12
Release:        1%{?dist}
Summary:        Peer to peer instant messenger

# GPLv3+: main library
# BSD: toxencryptsave/crypto_pwhash_scryptsalsa208sha256
# ISC: toxcore/crypto_core_mem.c
License:        GPLv3+ and BSD and ISC
URL:            https://github.com/TokTok/c-toxcore
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/TokTok/c-toxcore/issues/1144
Patch0:         toxcore-0.2.12-install_libmisc.patch

BuildRequires:  gcc-c++
BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  pkgconfig(libsodium)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(vpx)

%description
Tox is a peer to peer (serverless) instant messenger aimed at making
security and privacy easy to obtain for regular users. It uses NaCl
for its encryption and authentication.

%package devel
Summary:        Development files for Toxcore
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Tox is a peer to peer (serverless) instant messenger aimed at making
security and privacy easy to obtain for regular users. It uses NaCl
for its encryption and authentication.

This package contains Toxcore development files.

%prep
%autosetup -p1 -n c-%{name}-%{version}

%build
mkdir _build
cd _build
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%cmake -DSTRICT_ABI=ON ..
%make_build

%install
cd _build
%make_install
rm -f %{buildroot}/%{_libdir}/*.{a,la}

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/DHT_bootstrap
%{_libdir}/libtoxcore.so.%{sover}*
%{_libdir}/libmisc_tools.so

%files devel
%{_includedir}/tox/
%{_libdir}/libtoxcore.so
%{_libdir}/pkgconfig/toxcore.pc

%changelog
* Thu Jun 18 12:54:43 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.12-1
- Release 0.2.12 (#1815942)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Sep 22 19:37:15 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.10-1
- Release 0.2.10

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Feb 18 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.9-1
- Update to 0.2.9

* Tue Feb 05 2019 Björn Esser <besser82@fedoraproject.org> - 0.2.8-3
- rebuilt (libvpx)

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Oct 07 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.8-1
- Upstream release 0.2.8

* Fri Aug 31 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.7-2
- Add patch to install libmisc_tools needed by DHT_bootstrap

* Fri Aug 31 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.7-1
- Upstream release 0.2.7

* Sat Aug 04 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.4-1
- Upstream release 0.2.4

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 26 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.3-1
- Upstream release 0.2.3

* Thu Apr 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.2-2
- Build using cmake

* Thu Apr 19 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.2-1
- Upstream release 0.2.2

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.11-3
- actually rebuild for new libvpx

* Fri Jan 26 2018 Tom Callaway <spot@fedoraproject.org> - 0.1.11-2
- rebuild for new libvpx

* Wed Jan 10 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.11-1
- Upstream release 0.1.11

* Tue Oct 31 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.10-2
- Clean-up the SPEC

* Thu Oct 12 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.10-1
- New upstream release 0.1.10

* Fri Aug 18 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.9-2
- Fix Requires dependencies

* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.9-1
- First RPM release
