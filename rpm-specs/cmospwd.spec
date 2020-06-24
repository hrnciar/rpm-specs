Name:           cmospwd
Version:        5.0
Release:        18%{?dist}
Summary:        BIOS password cracker utility

License:        GPLv2+
URL:            http://www.cgsecurity.org/wiki/CmosPwd
Source0:        http://www.cgsecurity.org/%{name}-%{version}.tar.bz2

# Fails to build on other arches and not useful there either, I think
ExclusiveArch:  %{ix86} x86_64

BuildRequires:  gcc
BuildRequires:  dos2unix

%description
CmosPwd decrypts password stored in cmos used to access BIOS SETUP.
Works with the following BIOSes

    * ACER/IBM BIOS
    * AMI BIOS
    * AMI WinBIOS 2.5
    * Award 4.5x/4.6x/6.0
    * Compaq (1992)
    * Compaq (New version)
    * IBM (PS/2, Activa, Thinkpad)
    * Packard Bell
    * Phoenix 1.00.09.AC0 (1994), a486 1.03, 1.04, 1.10 A03, 4.05 rev 1.02.943,
      4.06 rev 1.13.1107
    * Phoenix 4 release 6 (User)
    * Gateway Solo - Phoenix 4.0 release 6
    * Toshiba
    * Zenith AMI

With CmosPwd, you can also backup, restore and erase/kill cmos.


%prep
%setup -q

rm src/%{name}

dos2unix %{name}.txt
iconv -f iso-8859-1 -t utf-8 %{name}.txt > %{name}.new
touch -r %{name}.txt %{name}.new
mv %{name}.new %{name}.txt


%build
cd src
make CFLAGS="%{optflags}" %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 src/%{name} $RPM_BUILD_ROOT%{_sbindir}/%{name}



%files
%doc COPYING %{name}.txt
%{_sbindir}/%{name}


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Oct 15 2009 Alexey Torkhov <atorkhov@gmail.com> - 5.0-1
- Initial packaging
