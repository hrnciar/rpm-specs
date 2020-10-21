Name:       phoronix-test-suite
Version:    9.0.1
Release:    3%{?dist}
Summary:    An Automated, Open-Source Testing Framework

License:    GPLv3+
URL:        http://%{name}.com/
Source0:    http://www.%{name}.com/releases/%{name}-%{version}.tar.gz
Source1:    README.Fedora
BuildArch:  noarch

BuildRequires: desktop-file-utils
BuildRequires: systemd
BuildRequires: libappstream-glib
BuildRequires: appdata-tools

Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

Requires: php-cli
Requires: php-xml
Requires: php-json
Requires: php-openssl
Requires: php-gd
Requires: php-sqlite3
Requires: php-posix
Requires: php-curl
Requires: hicolor-icon-theme


#These packages are not included anymore
#Packages required by tests. Use the following command to create this list:
#cat phoronix-test-suite/pts-core/external-test-dependencies/xml/fedora-packages.xml phoronix-test-suite/pts-core/external-test-dependencies/xml/generic-packages.xml| grep PackageName |sed -e 's/^.*<PackageName>\([^<]*\)<\/PackageName>.*$/\1/g' |xargs yum info|grep Name|sed -e 's/.*:\s\([^\s]*\)/\1/g'|grep -v devel$|sort|uniq|xargs
#Requires: autoconf automake bison blas cmake curl flex gcc gcc-c++ gcc-gfortran jam libcurl libtool make openmpi p7zip perl python scons tcl tcsh yasm

%description
The Phoronix Test Suite is the most comprehensive testing and benchmarking 
platform available for the Linux operating system. This software is designed to 
effectively carry out both qualitative and quantitative benchmarks in a clean, 
reproducible, and easy-to-use manner. The Phoronix Test Suite consists of a 
lightweight processing core (pts-core) with each benchmark consisting of an 
XML-based profile with related resource scripts. The process from the benchmark 
installation, to the actual benchmarking, to the parsing of important hardware 
and software components is heavily automated and completely repeatable, asking 
users only for confirmation of actions.

%prep
%setup -q -n %{name}
cp -p %{SOURCE1} documentation/
chmod +x pts-core/external-test-dependencies/scripts/install-macports-packages.sh
chmod +x pts-core/static/sample-pts-client-update-script.sh
chmod -x pts-core/objects/phodevi/sensors/network_usage.php

%build
# Nothing needed here

%install
export DESTDIR=%{buildroot}
./install-sh %{_prefix}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}-launcher.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

%post
%systemd_post phoromatic-client.service
%systemd_post phoromatic-server.service

%postun
%systemd_postun_with_restart phoromatic-client.service
%systemd_postun_with_restart phoromatic-server.service

%preun
%systemd_preun phoromatic-client.service
%systemd_preun phoromatic-server.service

%files
%doc %{_datadir}/doc/%{name} 
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/48x48/apps/phoronix-test-suite.png
%{_datadir}/icons/hicolor/64x64/mimetypes/application-x-openbenchmarking.png
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/bash_completion.d
%{_datadir}/applications/*
%{_datadir}/mime/packages/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_unitdir}/phoromatic-client.service
%{_unitdir}/phoromatic-server.service

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 9.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Carl George <carl@george.computer> - 9.0.1-1
- Latest upstream

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Markus Mayer <lotharlutz@gmx.de> 8.6.1-1
- new upstream release

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 8.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 31 2018 Markus Mayer <lotharlutz@gmx.de> 8.2.0-1
- new upstream release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Markus Mayer <lotharlutz@gmx.de> 7.8.0-1
- new upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 7.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 12 2017 Markus Mayer <lotharlutz@gmx.de> 7.4.0-1
- new upstream release

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 7.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 16 2017 Markus Mayer <lotharlutz@gmx.de> 7.2.0-1
- new upstream release

* Fri Mar 24 2017 Markus Mayer <lotharlutz@gmx.de> 7.0.0-1
- new upstream release

* Thu Sep 22 2016 Markus Mayer <lotharlutz@gmx.de> 6.6.0-1
- new upstream release

* Thu Jun 09 2016 Markus Mayer <lotharlutz@gmx.de> 6.4.0-1
- new upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 5.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.8.0-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Markus Mayer <lotharlutz@gmx.de> 5.8.0-0
- new upstream release

* Sat Mar 28 2015 Markus Mayer <lotharlutz@gmx.de> 5.6.0-0
- new upstream release

* Wed Dec 24 2014 Markus Mayer <lotharlutz@gmx.de> 5.4.1-1
- new upstream release

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 5.2.1-2
- update mime scriptlets

* Sun Jul 20 2014 Markus Mayer <lotharlutz@gmx.de> - 5.2.1-1
- new upstream release

* Tue Jun 10 2014 Markus Mayer <lotharlutz@gmx.de> - 5.2.0-1
- new upstream release

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 13 2014 Markus Mayer <lotharlutz@gmx.de> - 5.0.1-1
- new upstream release

* Thu Mar 13 2014 Markus Mayer <lotharlutz@gmx.de> - 5.0.0-1
- new upstream release
- disable dependencies not found on epel7

* Tue Dec 24 2013 Markus Mayer <lotharlutz@gmx.de> - 4.8.6-1
- new upstream

* Wed Nov 27 2013 Markus Mayer <lotharlutz@gmx.de> - 4.8.5-1
- new upstream

* Thu Nov 14 2013 Markus Mayer <lotharlutz@gmx.de> - 4.8.4-1
- new upstream

* Fri Oct 04 2013 Markus Mayer <lotharlutz@gmx.de> - 4.8.3-1
- new upstream

* Sat Sep 07 2013 Markus Mayer <lotharlutz@gmx.de> - 4.8.2-1
- new upstream

* Fri Aug 16 2013 Markus Mayer <lotharlutz@gmx.de> - 4.8.1-1
- new upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 07 2013 Markus Mayer <lotharlutz@gmx.de> - 4.6.1-1
- new upstream

* Wed May 22 2013 Markus Mayer <lotharlutz@gmx.de> - 4.6.0-1
- new upstream

* Sun Mar 17 2013 Markus Mayer <lotharlutz@gmx.de> - 4.4.1-1
- new upstream

* Wed Feb 27 2013 Markus Mayer <lotharlutz@gmx.de> - 4.4.0-1
- new upstream

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 20 2012 Markus Mayer <lotharlutz@gmx.de> - 4.2.0-1
- new upstream
- Fix wrong day of week in changelog

* Mon Dec 17 2012 Markus Mayer <lotharlutz@gmx.de> - 4.0.1-1
- new upstream
- do not install devel packages required by some test-suites

* Mon Aug 13 2012 Markus Mayer <lotharlutz@gmx.de> - 4.0.0-1
- new upstream

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr 09 2012 Markus Mayer <lotharlutz@gmx.de> 3.8.0-1
- new upstream release
- drop fix_install.patch (merged upstream)
- remove devel packages 

* Thu Jan 05 2012 Markus Mayer <lotharlutz@gmx.de> 3.6.1-3
- really remove missing requires for rhel

* Thu Jan 05 2012 Markus Mayer <lotharlutz@gmx.de> 3.6.1-2
- remove missing requires for rhel

* Mon Jan 02 2012 Markus Mayer <lotharlutz@gmx.de> 3.6.1-1
- new upstream release
- install test dependencies
- fix openbenchmark launcher

* Tue Nov 01 2011 Markus Mayer <lotharlutz@gmx.de> 3.4.0-3
- requires hicolor-icon-theme

* Mon Oct 31 2011 Markus Mayer <lotharlutz@gmx.de> 3.4.0-2
- mark bash_completion.d as config file

* Sat Sep 10 2011 Markus Mayer <lotharlutz@gmx.de> 3.4.0-1
- new upstream release

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Apr 16 2009 Joseph Smidt <josephsmidt@gmail.com> 1.8.1-1
- New upstream release

* Mon Apr 6 2009 Joseph Smidt <josephsmidt@gmail.com> 1.8.0-1
- New upstream release

* Thu Mar 26 2009 Joseph Smidt <josephsmidt@gmail.com> 1.6.0-4
- Changed GPLv3 to GPLv3+
- Set mode of dummy_script_module.sh to 755
- Included README.Fedora to explain non-free PTS tests

* Sat Mar 21 2009 Joseph Smidt <josephsmidt@gmail.com> 1.6.0-3
- Added full dependencies

* Tue Mar 3 2009 Joseph Smidt <josephsmidt@gmail.com> 1.6.0-2
- Removed explicite-lib dependencies

* Sun Feb 22 2009 Joseph Smidt <josephsmidt@gmail.com> 1.6.0-1
- Added full path to online source code.
- Added BuildArch: noarch
- Added an empty %%build section

* Sat Feb 14 2009 Joseph Smidt <fedoraproject.org> 1.6.0-0
- Initial RPM Release

