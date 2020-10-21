Name:           inxi
Version:        3.1.06
Release:        1%{?dist}
Summary:        A full featured system information script
Summary(ru):    Скрипт вывода полной информации об оборудовании и системе

License:        GPLv3
URL:            http://smxi.org/docs/inxi.htm
Source0:        https://github.com/smxi/inxi/archive/%{version}-1/%{name}-%{version}-1.tar.gz

BuildArch:      noarch

Requires:       iproute
Requires:       pciutils
Requires:       procps
Requires:       lm_sensors
Requires:       usbutils
Requires:       hddtemp
Requires:       xdpyinfo xprop xrandr
Requires:       bind-utils
Requires:       ipmitool
Requires:       freeipmi
Requires:       wmctrl
Requires:       perl(Cpanel::JSON::XS)
Requires:       perl(JSON::XS)
Requires:       perl(XML::Dumper)
Requires:       perl(Net::FTP)
Requires:       perl(File::Find)

%description
Inxi offers a wide range of built-in options, as well as a good number of extra
features which require having the script recommends installed on the system.


%description -l ru
Inxi позволяет выводить различную информацию об используемом оборудовании и о
работе системы.


%prep
%autosetup -n %{name}-%{version}-1
#Disable update option
sed -i 's/my ($b_sysctl_disk,$b_update,$b_weather) = (1,1,1);/my ($b_sysctl_disk,$b_update,$b_weather) = (1,0,1);/' inxi
#Correct shebang
sed -i 's|/usr/bin/env perl|/usr/bin/perl|' inxi

%build
#Nothing to build


%install
install -p -D -m 755 %{name} %{buildroot}/%{_bindir}/%{name}
gzip %{name}.1
install -p -D -m 644 %{name}.1.gz %{buildroot}/%{_mandir}/man1/%{name}.1.gz

%files
%doc %{name}.changelog README.txt
%license LICENSE.txt
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Aug 20 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.06-1
- Update to 3.1.06

* Tue Jul 28 2020 Adam Jackson <ajax@redhat.com> - 3.1.03-3
- Require xdpyinfo xprop xrandr, not xorg-x11-utils

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.1.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jun 13 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.03-1
- Update to 3.1.03

* Sun Apr 26 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.1.00-1
- Update to 3.1.00

* Thu Apr 16 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.38-2
- Add dependency File::Find

* Mon Mar 16 2020 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.38-1
- Update to 3.0.38

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Nov 20 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.37-1
- Update to 3.0.37

* Thu Aug 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.36-1
- Update to 3.0.36

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jul 17 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.35-1
- Update to 3.0.35

* Mon May 06 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.34-1
- Update to 3.0.34

* Fri Feb 15 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.32-1
- Update to 3.0.32

* Thu Feb 07 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 3.0.31-1
- Update to 3.0.31

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.29-1
- Update to 3.0.29

* Thu Dec 06 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.28-1
- Update to 3.0.28

* Wed Oct 17 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.27-1
- Update to 3.0.27

* Mon Oct 08 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.26-1
- Update to 3.0.26

* Wed Sep 12 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.24-1
- Update to 3.0.24

* Mon Sep 10 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.23-1
- Update to 3.0.23

* Tue Sep 04 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.22-1
- Update to 3.0.22

* Tue Aug 28 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.21-1
- Update to 3.0.21

* Wed Aug 01 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.20-1
- Update to 3.0.20

* Thu Jul 19 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.18-1
- Update to 3.0.18

* Fri Jul 13 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.17-1
- Update to 3.0.17

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.15-1
- Update to 3.0.15

* Thu Jun 28 2018 Vasiliy N. Glazov <vascom2@gmail.com> 3.0.14-1
- Update to 3.0.14

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.56-1
- Update to 2.3.56

* Wed Dec 13 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.53-1
- Update to 2.3.53

* Wed Nov 22 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.45-1
- Update to 2.3.45

* Fri Nov 03 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.43-1
- Update to 2.3.43

* Tue Oct 03 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.40-1
- Update to 2.3.40

* Tue Sep 12 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.38-1
- Update to 2.3.38

* Wed Aug 23 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.36-1
- Update to 2.3.36

* Tue Aug 01 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.31-1
- Update to 2.3.31

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.23-1
- Update to 2.3.23

* Mon Jun 19 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.22-1
- Update to 2.3.22

* Mon Jun 19 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.21-1
- Update to 2.3.21

* Thu Jun 01 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.11-1
- Update to 2.3.11

* Tue May 30 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.9-1
- Update to 2.3.9

* Wed May 17 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.8-3
- Remove deprecated net-tools dependency

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 20 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.8-1
- Update to 2.3.8

* Sat Jan 07 2017 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.7-1
- Update to 2.3.7

* Thu Dec 08 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.5-1
- Update to 2.3.5

* Mon Nov 21 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.4-1
- Update to 2.3.4

* Fri Oct 28 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.3-1
- Update to 2.3.3

* Thu Sep 15 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.1-1
- Update to 2.3.1

* Thu Apr 21 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.3.0-1
- Update to 2.3.0

* Mon Apr 18 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.38-1
- Update to 2.2.38

* Thu Mar 17 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.35-1
- Update to 2.2.35

* Fri Feb 26 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.34-1
- Update to 2.2.34
- Added Requires bind-utils
- Added readme and license files

* Thu Feb 04 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.33-1
- Update to 2.2.33

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 13 2016 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.32-1
- Update to 2.2.32

* Fri Nov 20 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.31-1
- Update to 2.2.31

* Thu Aug 27 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.28-1
- Update to 2.2.28

* Fri Jun 19 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.25-1
- Update to 2.2.25

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri May 15 2015 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.21-1
- Update to 2.2.21

* Thu Nov 06 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.16-1
- Update to 2.2.16

* Mon Sep 29 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.14-1
- Update to 2.2.14

* Mon Sep 22 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.8-1
- Update to 2.2.8

* Fri Aug 22 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.2.1-1
- Update to 2.2.1

* Tue Aug 12 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.1.90-1
- Update to 2.1.90

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 06 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.1.28-1
- Update to 2.1.28

* Fri Apr 18 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.1.20-1
- Update to 2.1.20

* Mon Mar 31 2014 Vasiliy N. Glazov <vascom2@gmail.com> 2.1.13-1
- Update to 2.1.13

* Mon Feb 10 2014 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.18-1
- Update to 1.9.18

* Thu Dec 26 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.17-1
- Update to 1.9.17

* Fri Aug 23 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.14-2
- Correct sources

* Thu Aug 22 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.14-1
- Update to new version
- Disable builtin update

* Mon Aug 19 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.13-1
- Update to new version

* Thu Aug 08 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-5
- Correct executable permissions

* Wed Aug 07 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-4
- Removed unnecessary Requires

* Tue Aug 06 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-3
- Change source0 link
- Added Requires

* Tue Aug 06 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-2
- Correct spec and descriptions

* Wed Jul 03 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.12-1
- Update to 1.9.12

* Tue Jun 18 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.9-1
- Update to 1.9.9

* Tue Jun 04 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.9.7-1
- Update to 1.9.7

* Tue May 07 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.47-1
- Update to 1.8.47

* Mon Apr 22 2013 Vasiliy N. Glazov <vascom2@gmail.com> 1.8.45-1
- Initial release
