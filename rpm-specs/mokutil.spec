Name:           mokutil
Version:        0.4.0
Release:        2%{?dist}
Epoch:          2
Summary:        Tool to manage UEFI Secure Boot MoK Keys
License:        GPLv3+
URL:            https://github.com/lcp/mokutil
ExclusiveArch:  %{ix86} x86_64 aarch64
BuildRequires:  gcc
BuildRequires:  autoconf automake gnu-efi git openssl-devel openssl
BuildRequires:  efivar-devel >= 31-1
Source0:        https://github.com/lcp/mokutil/archive/%{version}.tar.gz
Conflicts:      shim < 0.8-1%{?dist}
Obsoletes:      mokutil < 0.2.0

Patch0001: 0001-Avoid-taking-pointer-to-packed-struct.patch
Patch0002: 0002-Fix-a-integer-comparison-sign-issue.patch

%description
mokutil provides a tool to manage keys for Secure Boot through the MoK
("Machine's Own Keys") mechanism.

%prep
%setup -q -n %{name}-%{version}
git init
git config user.email "%{name}-owner@fedoraproject.org"
git config user.name "Fedora Ninjas"
git add .
git commit -a -q -m "%{version} baseline."
git am %{patches} </dev/null
git config --unset user.email
git config --unset user.name

%build
./autogen.sh
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make PREFIX=%{_prefix} LIBDIR=%{_libdir} DESTDIR=%{buildroot} install

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README
%{_bindir}/mokutil
%{_mandir}/man1/*
%{_datadir}/bash-completion/completions/mokutil

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 11 2020 Javier Martinez Canillas <javierm@redhat.com> - 0.4.0-1
- Update to 0.4.0 release

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.3.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Nov 12 2019 Peter Jones <pjones@redhat.com> - 0.3.0-14
- Pull one more upstream patch to keep this in sync with the f31 build.

* Thu Oct 24 2019 Leigh Scott <leigh123linux@googlemail.com> - 1:0.3.0-14
- Apply upstream commits to fix FTBFS

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Björn Esser <besser82@fedoraproject.org> - 1:0.3.0-11
- Rebuilt for libcrypt.so.2 (#1666033)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 1:0.3.0-8
- Rebuilt for switch to libxcrypt

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 08 2017 Peter Jones <pjones@redhat.com> - 0.3.0-5
- Rebuild for efivar-31-1.fc26
  Related: rhbz#1468841

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 17 2016 Peter Jones <pjones@redhat.com> - 0.3.0-3
- Rebuild for newer efivar again.

* Wed Aug 10 2016 Peter Jones <pjones@redhat.com> - 0.3.0-2
- Update for newer efivar.

* Tue Jun 14 2016 Peter Jones <pjones@redhat.com> - 0.3.0-1
- Update to 0.3.0 release.
  Resolves: rhbz#1334628

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1:0.2.0-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Mon Oct 06 2014 Peter Jones <pjones@redhat.com> - 0.2.0-1
- First independent package.
