Name:		stress-ng
Version:	0.07.29
Release:	11%{?dist}
Summary:	Stress test a computer system in various ways

License:	GPLv2+
URL:		http://kernel.ubuntu.com/~cking/%{name}
Source0:	http://kernel.ubuntu.com/~cking/tarballs/%{name}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:	glibc-devel
BuildRequires:	kernel-headers
BuildRequires:	keyutils-libs-devel
BuildRequires:	libaio-devel
BuildRequires:	libattr-devel
BuildRequires:	libbsd-devel
BuildRequires:	libcap-devel
BuildRequires:	lksctp-tools-devel
BuildRequires:	zlib-devel

ExcludeArch:	ppc64
ExcludeArch:	ppc64le

%description
Stress test a computer system in various ways. It was designed to exercise
various physical subsystems of a computer as well as the various operating
system kernel interfaces.


%prep
%setup -q


%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build


%install
install -p -m 755 -D %{name} %{buildroot}%{_bindir}/%{name}
install -p -m 644 -D %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1


%files
%license COPYING
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 0.07.29-8
- Rebuilt for libcrypt.so.2 (#1666033)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.07.29-5
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Fedora <sspreitz@redhat.com> - 0.07.29-2
- exclude ppc64 and ppc64le archs

* Tue Apr 18 2017 Fedora <sspreitz@redhat.com> - 0.07.29-1
- new version

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.07.05-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov 21 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.07.05-3
- License is GPLv2+

* Sun Nov 20 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.07.05-2
- enhance building

* Sun Nov 20 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.07.05-1
- new version

* Mon Nov 14 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.07.04-1
- new version

* Mon Jun 13 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.06.06-1
- new version

* Fri Apr 29 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.05.25-1
- initial spec file

