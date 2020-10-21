Name:              torsocks
Version:           2.3.0
Release:           8%{?dist}

Summary:           Use SOCKS-friendly applications with Tor
License:           GPLv2+
URL:               https://gitweb.torproject.org/torsocks.git

Source0:           https://people.torproject.org/~dgoulet/torsocks/torsocks-%{version}.tar.xz
Source1:           https://people.torproject.org/~dgoulet/torsocks/torsocks-%{version}.tar.xz.asc

Patch0:            %{name}-2.2.0-Do-not-run-tests-that-require-network-access.patch
BuildRequires:     gcc
%if 0%{?rhel} == 7 || 0%{?fedora} > 26
BuildRequires:     automake
%endif

%description
Torsocks allows you to use most SOCKS-friendly applications in a safe way
with Tor. It ensures that DNS requests are handled safely and explicitly
rejects UDP traffic from the application you're using.


%prep
%autosetup -p1
%if 0%{?fedora} >= 33
sed -i 's/1.15/1.16.2/g' aclocal.m4 configure
%endif
%if 0%{?fedora} >= 29 && 0%{?fedora} < 33
sed -i 's/1.15/1.16.1/g' aclocal.m4 configure
%endif
%if 0%{?rhel} == 7
sed -i 's/1.15/1.13.4/g' aclocal.m4 configure
%endif


%build
%if 0%{?fedora} >= 33
aclocal
%endif
%if 0%{?rhel} == 7 || 0%{?fedora} > 26
automake
%endif
%configure
%make_build


%install
%make_install

# Remove extraneous files.
rm -f %{buildroot}%{_libdir}/torsocks/libtorsocks.{a,la}*
rm -fr %{buildroot}%{_datadir}/doc/torsocks

# For bash completion.
install -p -D -m0644 extras/torsocks-bash_completion \
    %{buildroot}%{_sysconfdir}/bash_completion.d/torsocks


%check
pushd tests/
make check-am
popd


%files
%doc ChangeLog doc/notes/DEBUG doc/socks/socks-extensions.txt
%license gpl-2.0.txt
%{_bindir}/torsocks
%{_mandir}/man1/torsocks.1*
%{_mandir}/man5/torsocks.conf.5*
%{_mandir}/man8/torsocks.8*
%dir %{_libdir}/torsocks
# torsocks requires this file so it has not been placed in -devel subpackage
%{_libdir}/torsocks/libtorsocks.so
%{_libdir}/torsocks/libtorsocks.so.0*
%config(noreplace) %{_sysconfdir}/bash_completion.d/torsocks
%config(noreplace) %{_sysconfdir}/tor/torsocks.conf


%changelog
* Tue Aug 04 2020 Marcel Haerry <mh+fedora@scrit.ch> - 2.3.0-8
- Fix bz#1865583 We have newer autotools from F33 on

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Aug 22 2019 Gwyn Ciesla <gwync@protonmail.com> - 2.3.0-4
- Tweak man paths.

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Nov 19 2018 Marcel Haerry <mh+fedora@scrit.ch> - 2.3.0-1
- New upstrem release
- Fixes rbz#1601259

* Tue Oct 30 2018 Marcel Haerry <mh+fedora@scrit.ch> - 2.2.0-3
- Make it build again

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 14 2018 Marcel Haerry <mh+fedora@scrit.ch> - 2.2.0-1
- Update to latest release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 11 2017 Vasiliy N. Glazov <vascom2@gmail.com> - 2.1.0-6.5
- Cleanup spec

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu May 28 2015 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.1.0-1
- update to upstream release 2.1.0
- run test suite

* Wed Apr 29 2015 Jon Ciesla <limburgher@gmail.com> - 2.0.0-3
- Updated to latest to fix syscall errors.

* Tue Nov 11 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-2
- remove extraneous files

* Tue Nov 11 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 2.0.0-1
- update to 2.0.0

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sat Feb 23 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.3-1
- update to upstream release 1.3

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Nov 23 2012 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2-2
- add .sig file
- add links to upstream bug reports
- merge -devel package as torsocks requires libtorsocks.so
- fix directory ownership
- mark bash_completion file as a config file

* Sat Nov 17 2012 Jamie Nguyen <jamielinux@fedoraproject.org> - 1.2-1
- initial package
