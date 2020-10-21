
%global commit0 4d195e4dc7a47ff5cb51e36a83d4d05808c5befe
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global tag0 VERSION_%{version}

Name:           signon
Version:        8.60
Release:        6%{?dist}
Summary:        Accounts framework for Linux and POSIX based platforms

License:        LGPLv2
URL:            https://gitlab.com/accounts-sso/signond

%if 0%{?tag0:1}
Source0:        https://gitlab.com/accounts-sso/signond/repository/archive.tar.gz?ref=%{tag0}#/%{name}-%{version}.tar.gz
%else
Source0:        https://gitlab.com/accounts-sso/signond/repository/archive.tar.gz?ref=%{commit0}#/%{name}-%{shortcommit0}.tar.gz
%endif

# cmake config files still define SIGNONQT_LIBRARIES_STATIC, but meh, anyone who
# tries to use that deserves what they get
Patch1: signon-8.57-no_static.patch

BuildRequires:  dbus-x11
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libproxy-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  time

# signon-qt5 was in ktp-5 COPR
Obsoletes:      signon-qt5 < 8.57-5
Provides:       signon-qt5 = %{version}-%{release}

# upstream name: signond
Provides:       signond = %{version}-%{release}

# conflicting implementation: gsignond
Conflicts:      gsignond

Requires:       dbus

%description
Single Sign-On is a framework for centrally storing authentication credentials
and handling authentication on behalf of applications as requested by
applications. It consists of a secure storage of login credentials (for example
usernames and passwords), plugins for different authentication systems and a
client library for applications to communicate with this system.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
# upstream name: signond
Provides:       signond-devel = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch

%description doc
The %{name}-doc package contains documentation for %{name}.


%prep
%setup -q -n signond-%{tag0}-%{commit0}

%patch1 -p1 -b .no_static


%build
# Make sure it compiles against Fedora's Qt5
sed -i "s/qdbusxml2cpp/qdbusxml2cpp-qt5/" src/signond/signond.pro

export PATH=%{_qt5_bindir}:$PATH

# FIXME: out-of-src tree build fails -- rex
%{qmake_qt5} signon.pro \
  CONFIG+=release \
  QMF_INSTALL_ROOT=%{_prefix} LIBDIR=%{_libdir}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

# create/own libdir/extensions
mkdir -p %{buildroot}%{_libdir}/extensions/


%check
time \
make check ||:


%ldconfig_scriptlets

%files
## fixme: common/shared _docdir/signon content below gets in the way
#doc README.md TODO NOTES
%license COPYING
%config(noreplace) %{_sysconfdir}/signond.conf
%{_bindir}/signond
%{_bindir}/signonpluginprocess
%{_libdir}/libsignon-extension.so.1*
%{_libdir}/libsignon-plugins-common.so.1*
%{_libdir}/libsignon-plugins.so.1*
%{_libdir}/libsignon-qt5.so.1*
%{_libdir}/signon/
%{_datadir}/dbus-1/services/*.service

%files devel
%{_includedir}/signon-extension/
%{_includedir}/signon-plugins/
%{_includedir}/signon-qt5/
%{_includedir}/signond/
%{_libdir}/cmake/SignOnQt5/
%{_libdir}/libsignon-extension.so
%{_libdir}/libsignon-plugins-common.so
%{_libdir}/libsignon-plugins.so
%{_libdir}/libsignon-qt5.so
%{_libdir}/pkgconfig/SignOnExtension.pc
%{_libdir}/pkgconfig/libsignon-qt5.pc
%{_libdir}/pkgconfig/signon-plugins-common.pc
%{_libdir}/pkgconfig/signon-plugins.pc
%{_libdir}/pkgconfig/signond.pc

%files doc
%{_docdir}/signon/
%{_docdir}/libsignon-qt/
%{_docdir}/signon-plugins/
%{_docdir}/signon-plugins-dev/


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.60-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 8.60-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.60-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 07 2019 Fabio Valentini <decathorpe@gmail.com> - 8.60-3
- Make conflict with gsignond explicit to fix upgrade issues.

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.60-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Oct 20 2018 Rex Dieter <rdieter@fedoraproject.org> - 8.60-1
- signon-8.60 (#1640986)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.59-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 8.59-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.59-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.59-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 8.59-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Jun 08 2016 Rex Dieter <rdieter@fedoraproject.org> 8.59-2
- %%check: time checks

* Tue Jun 07 2016 Rex Dieter <rdieter@fedoraproject.org> - 8.59-1
- 8.59 (#1343792) 

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 8.58-0.2.9fcfc9e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Dec 21 2015 Rex Dieter <rdieter@fedoraproject.org> 8.58-0.1
- 8.58 snapshot, FTBFS against qt-5.6

* Mon Dec 21 2015 Rex Dieter <rdieter@fedoraproject.org> 8.57-8
- fix/update URL/Source0, move xml interface files to -devel, Provides: signond, use %%license

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 8.57-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Daniel Vrátil <dvratil@redhat.com> - 8.57-6
- Obsoletes/Provides signon-qt5 (for compatibility with COPR)

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 8.57-5
- Rebuilt for GCC 5 C++11 ABI change

* Wed Apr 08 2015 Marcin Juszkiewicz <mjuszkiewicz@redhat.com> - 8.57-4
- force proper libdir - fixes build on 64-bit architectures other than x86-64

* Wed Apr 01 2015 Rex Dieter <rdieter@fedoraproject.org> - 8.57-3
- %%files: track closer, less globs (sonames, pkgconfig)
- own libdir/extensions/
- patch out building of (unused) static lib

* Sat Mar 28 2015 Daniel Vrátil <dvratil@redhat.com> - 8.57-2
- rename to signon
- drop glib2-devel dep
- fix %%changelog

* Tue Mar 17 2015 Daniel Vrátil <dvratil@redhat.com> - 8.57-1
- rename to signon-qt5, update

* Wed Feb 26 2014 Daniel Vrátil <dvratil@redhat.com> - 8.56-1
- initial version

