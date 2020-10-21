Name:           nss_nis
Version:        3.1
Release:        7%{?dist}
Summary:        Name Service Switch (NSS) module using NIS
License:        LGPLv2+
Url:            https://github.com/thkukuk/libnss_nis
Source:         https://github.com/thkukuk/libnss_nis/archive/v%{version}.tar.gz

# https://github.com/systemd/systemd/issues/7074
# https://bugzilla.redhat.com/show_bug.cgi?id=1829572
Source2:        nss_nis.conf

BuildRequires:  libnsl2-devel
BuildRequires:  libtirpc-devel
BuildRequires:  autoconf, automake, libtool
BuildRequires:  systemd


# hacked Provides, normally comes from built files
%if %{__isa_bits} == 64
Provides:       libnss_nis.so.2()(64bit)
%else
Provides:       libnss_nis.so.2
%endif


# recommend 32bit lib on 64bit arch
%if %{__isa_bits} == 64
Recommends:    (libnss_nis.so.2 if glibc(x86-32))
%endif


# I'd recommend an explicit conflict with different versions of the package
# to ensure that 64bit and 32bit packages are equal and compatible
Conflicts:      %{name} < %{version}-%{release}


%description
The nss_nis Name Service Switch module uses the Network Information System (NIS)
to obtain user, group, host name, and other data.

%prep
%setup -q -n libnss_nis-%{version}

%build

export CFLAGS="%{optflags}"

autoreconf -fiv

%configure --libdir=%{_libdir} --includedir=%{_includedir}
%make_build

%install
%make_install
rm  %{buildroot}/%{_libdir}/libnss_nis.{a,la}
rm  %{buildroot}/%{_libdir}/libnss_nis.so

install -D -m 644 %{SOURCE2} %{buildroot}/%{_unitdir}/systemd-logind.service.d/nss_nis.conf
install -D -m 644 %{SOURCE2} %{buildroot}/%{_unitdir}/systemd-userdbd.service.d/nss_nis.conf

%check
make check

%ldconfig_scriptlets


%files
%{_libdir}/libnss_nis.so.2
%{_libdir}/libnss_nis.so.2.0.0
%{_unitdir}/systemd-logind.service.d/*
%{_unitdir}/systemd-userdbd.service.d/*


%license COPYING

%changelog
* Tue Sep 22 2020 Filip Januš <fjanus@redhat.com> - 3.1-7
- improve recommandation of 32 bit-version
- resolves: https://bugzilla.redhat.com/show_bug.cgi?id=1803161

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.1-5
- Make sure that systemd-userdbd.service can access the network too (#1829572)

* Wed Mar 25 2020 Filip Januš <fjanus@redhat.com> - 3.1-4
- addiing: recommending to install 32 bit-version if 32 bit glibc is installed
- resolves: https://bugzilla.redhat.com/show_bug.cgi?id=1803161

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Matej Mužila <mmuzila@redhat.com> - 3.1-1
- Update to version 3.1
- Resolves: #1736327

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 9 2018 Matej Mužila <mmuzila@redhat.com> 3.0-8
- Add systemd-logind snippet (RestrictAddressFamilies)
- Resolves: #1645308

* Wed Aug 1 2018 Matej Mužila <mmuzila@redhat.com> - 3.0-7
- BuildRequire systemd

* Wed Aug 1 2018 Matej Mužila <mmuzila@redhat.com> - 3.0-6
- Add systemd-logind snippet (IPAddressAllow=any)
- Resolves: #1574959

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 30 2018 Matej Mužila <mmuzila@redthat.com> - 3.0-3
- Inital release
