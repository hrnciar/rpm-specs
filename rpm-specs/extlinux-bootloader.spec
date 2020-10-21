Name:           extlinux-bootloader
Version:        1.2
Release:        12%{?dist}
Summary:        The EXTLINUX bootloader framework, for booting the local system

License:        GPLv2+
URL:            https://src.fedoraproject.org/rpms/extlinux-bootloader
Source1:        extlinux.sh
BuildRequires:  coreutils
%if 0%{?fedora} > 29
Requires:       grubby-deprecated
%endif
Provides:       syslinux-extlinux

ExclusiveArch:  %{arm} aarch64

%description
The EXTLINUX bootloader framework, for booting the local system.
u-boot on arm supports extlinux.conf config files

%prep


%build


%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}/boot/extlinux/

mkdir -p %{buildroot}/etc
( cd %{buildroot}/etc && ln -s ../boot/extlinux/extlinux.conf . )
install -p %{SOURCE1} %{buildroot}%{_sbindir}/extlinux

%files
%doc
%{_sbindir}/extlinux
/boot/extlinux
%config(noreplace) /etc/extlinux.conf



%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri May 03 2019 Petr Pisar <ppisar@redhat.com> - 1.2-9
- Correct URL in RPM metadata (bug #1510763)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Nov 30 2018 Javier Martinez Canillas <javierm@redhat.com> - 1.2-7
- Make syslinux-extlinux to Require grubby-deprecated
  Resolves: rhbz#1654841

* Thu Nov 22 2018 Pablo Greco <pablo@fliagreco.com.ar> - 1.2-6
* Avoid multiple fdtdir entries

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed May 10 2017 Merlin Mathesius <mmathesi@redhat.com> - 1.2-1
- Convert extlinux to bash script to eliminate need for Python.

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1.1-5
- Use python3

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr 01 2015 Dennis Gilmore <dennis@ausil.us> - 1.1-3
- add a missing / when listing the contents of /boot

* Wed Apr 01 2015 Dennis Gilmore <dennis@ausil.us> - 1.1-2
- add a function to copy the dtbs to the rescue boot target if one exists

* Mon Mar 30 2015 Dennis Gilmore <dennis@ausil.us> - 1.1-1
- add a new extlinux script to setup dtb handling on arm 

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 16 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.0-4
- Enable for build on aarch64 too

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 05 2013 Dennis Gilmore <dennis@ausil.us> - 1.0-1
- initial package
