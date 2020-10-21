%global _hardened_build 1
%global __provides_exclude ^sstp-pppd-plugin\\.so$
%global ppp_version %(rpm -q ppp > /dev/null && rpm -q ppp --qf '%{VERSION}' || echo 'broken')
%global commonname sstpc

Name:           sstp-client
Version:        1.0.11
Release:        17%{?dist}
Summary:        Secure Socket Tunneling Protocol(SSTP) Client
License:        GPLv2+
Url:            http://sstp-client.sourceforge.net
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  libevent-devel
BuildRequires:  openssl-devel
BuildRequires:  ppp
BuildRequires:  ppp-devel
Requires(pre):  shadow-utils
# PPP bumps location of the libraries with every new release.
Requires:       ppp = %{ppp_version}

%description
This is a client for the Secure Socket Tunneling Protocol(SSTP). It can be 
used to establish a SSTP connection to a Windows Server.

Features:
* Establish a SSTP connection to a remote Windows 2k8 server.
* Async PPP support.
* Similar command line handling as pptp-client for easy integration with 
pon/poff scripts.
* Basic HTTP Proxy support.
* Certficate handling and verification.
* IPv6 support.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       ppp-devel%{?_isa} = %{ppp_version}

%description    devel
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure --disable-static                                          \
           --disable-silent-rules                                    \
           --with-libevent=2                                         \
           --with-pppd-plugin-dir="%{_libdir}/pppd/%{ppp_version}"   \
           --with-runtime-dir="%{_localstatedir}/run/%{commonname}"  \
           --enable-user=yes                                         \
           --enable-group=yes
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
%make_install

# Use %%doc to handle documentation.
rm -frv %{buildroot}%{_docdir}

find %{buildroot} -name '*.la' -delete -print

%check
make check

%pre
getent group %{commonname} >/dev/null || groupadd -r %{commonname}
getent passwd %{commonname} >/dev/null || \
    useradd -r -g %{commonname} \
    -d %{_localstatedir}/run/%{commonname} \
    -s /sbin/nologin \
    -c "Secure Socket Tunneling Protocol(SSTP) Client" %{commonname}
exit 0

%ldconfig_post

%postun
%{?ldconfig}
rm -rf %{_localstatedir}/run/%{commonname}

%files
%doc AUTHORS README debian/changelog TODO USING *.example
%license COPYING
%{_sbindir}/sstpc
%{_libdir}/libsstp_api-0.so
%{_libdir}/pppd/%{ppp_version}/sstp-pppd-plugin.so
%{_mandir}/man8/sstpc.8*

%files devel
%doc DEVELOPERS
%{_includedir}/sstp-client/
%{_libdir}/libsstp_api.so
%{_libdir}/pkgconfig/sstp-client-1.0.pc

%changelog
* Tue Sep 29 20:45:27 CEST 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.0.11-17
- Rebuilt for libevent 2.1.12

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 22 2020 Kevin Fenzi <kevin@scrye.com> - 1.0.11-15
- Rebuild for new ppp

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Kevin Fenzi <kevin@scrye.com> - 1.0.11-10
- Rebuild for new libevent

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 24 2017 Lubomir Rintel <lkundrak@v3.sk> - 1.0.11-8
- Rebuilt for new ppp
- Drop the superfluous dependency on a particular ppp release

* Tue Aug 22 2017 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.11-7
- Rebuild against (another) new ppp package version

* Fri Aug 18 2017 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.11-6
- Rebuild against new ppp package version - bug 1482840

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Feb 27 2017 Tomas Hozza <thozza@redhat.com> - 1.0.11-3
- Rebuild against new ppp package version

* Sun Feb 05 2017 Kalev Lember <klember@redhat.com> - 1.0.11-2
- Rebuilt for new ppp

* Wed Dec 14 2016 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.11-1
- Update to 1.0.11 which is compatible with OpenSSL 1.1.0c

* Wed Dec 14 2016 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.10-6
- Fix ldconfig call in postun - #1404802

* Thu Jul 21 2016 Marcin Zajaczkowski <mszpak ATT wp DOTT pl> - 1.0.10-5
- Workaround for problem with Rpath

* Fri Feb 19 2016 Tomas Hozza <thozza@redhat.com> - 1.0.10-4
- Rebuild against new ppp package version

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Aug 27 2015 Christopher Meng <i@cicku.me> - 1.0.10-2
- Correct ppp dependency.

* Sat Jun 20 2015 Christopher Meng <rpm@cicku.me> - 1.0.10-1
- Update to 1.0.10

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 27 2014 Christopher Meng <rpm@cicku.me> - 1.0.9-6
- Rebuild against new ppp.

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Aug 01 2013 Christopher Meng <rpm@cicku.me> - 1.0.9-4
- Fix library issue.

* Fri Jul 26 2013 Christopher Meng <rpm@cicku.me> - 1.0.9-3
- Filter out the private library.

* Tue Jul 23 2013 Christopher Meng <rpm@cicku.me> - 1.0.9-2
- Remove Rpath.

* Sun Feb 03 2013 Christopher Meng <rpm@cicku.me> - 1.0.9-1
- Initial Package.
