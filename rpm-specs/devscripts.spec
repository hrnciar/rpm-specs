Name:           devscripts
Version:        2.20.3
Release:        2%{?dist}
Summary:        Scripts for Debian Package maintainers

License:        GPLv2+
URL:            https://packages.debian.org/sid/%{name}
Source0:        http://ftp.debian.org/debian/pool/main/d/%{name}/%{name}_%{version}.tar.xz
# Fixes path to xsl-stylesheet manpages docbook.xsl
Patch0:         devscripts_docbook.patch
# Removes the debian-only --install-layout python-setuptools option
Patch1:         devscripts_install-layout.patch
# Install some additional man pages
Patch2:         devscripts_install-man.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Dpkg::Changelog::Debian)
BuildRequires:  perl(Dpkg::Changelog::Parse)
BuildRequires:  perl(Dpkg::Control)
BuildRequires:  perl(Dpkg::Control::Hash)
BuildRequires:  perl(Dpkg::Vendor)
BuildRequires:  perl(Dpkg::Version)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(feature)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::DesktopEntry)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(filetest)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Git::Wrapper)
BuildRequires:  perl(IO::Dir)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(JSON::PP)
BuildRequires:  perl(List::Compare)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(Net::SMTP)
BuildRequires:  perl(open)
BuildRequires:  perl(Parse::DebControl)
BuildRequires:  perl(Pod::Checker)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Text::Wrap)
BuildRequires:  perl(URI) >= 1.37
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

BuildRequires:  docbook-style-xsl
BuildRequires:  libxslt
BuildRequires:  po4a
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  /usr/bin/dpkg-buildflags
BuildRequires:  /usr/bin/dpkg-vendor
BuildRequires:  /usr/bin/dpkg-parsechangelog
BuildRequires:  /usr/bin/help2man
BuildRequires:  pkgconfig(bash-completion)

Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:       dpkg-dev
Requires:       sensible-utils
# man for manpage-alert
Requires:       %{_bindir}/man

Requires:       %{name}-checkbashisms

# rhbz 1508087, 1536718
Obsoletes:      hardening-check < 2.6-8
Provides:       hardening-check = 2.6-8

%description
Scripts to make the life of a Debian Package maintainer easier.

%package checkbashisms
Summary:        Devscripts checkbashisms script
Obsoletes:      devscripts-minimal < 2.16.6-1
# Removed in F30
Obsoletes:      devscripts-compat < 2.19.2-4

%description checkbashisms
This package contains the devscripts checkbashisms script.


%prep
%autosetup -p1


%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{__global_ldflags}"


%install
%make_install

# Install docs through %%doc
rm -rf %{buildroot}%{_datadir}/doc

# archpath requires tla (gnu-arch) or baz (bazaar), both of which are obsolete
# and the respective Fedora packages dead. See #1128503
rm %{buildroot}%{_bindir}/archpath %{buildroot}%{_mandir}/man1/archpath*

# whodepends requires configured deb repositories
rm %{buildroot}%{_bindir}/whodepends %{buildroot}%{_mandir}/man1/whodepends*

# Create symlinks like the debian package does
ln -s %{_bindir}/cvs-debi      %{buildroot}%{_bindir}/cvs-debc
ln -s %{_bindir}/debchange     %{buildroot}%{_bindir}/dch
ln -s %{_bindir}/pts-subscribe %{buildroot}%{_bindir}/pts-unsubscribe
ln -s %{_mandir}/man1/debchange.1.gz     %{buildroot}%{_mandir}/man1/dch.1.gz
ln -s %{_mandir}/man1/pts-subscribe.1.gz %{buildroot}%{_mandir}/man1/pts-unsubscribe.1.gz

# This already is in bash-completion
rm -f %{buildroot}%{_datadir}/bash-completion/completions/bts


%files
%doc README
%license COPYING
%{_datadir}/bash-completion
%{_bindir}/*
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}*.egg-info/
%{_datadir}/%{name}/
%{_mandir}/man1/*
%{perl_vendorlib}/Devscripts
%exclude %{_bindir}/checkbashisms
%exclude %{_mandir}/man1/checkbashisms.1*
%exclude %{_datadir}/bash-completion/completions/checkbashisms

%files checkbashisms
%license COPYING
%{_bindir}/checkbashisms
%{_mandir}/man1/checkbashisms.1*
%{_mandir}/man5/devscripts.conf.5*
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/checkbashisms


%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 2.20.3-2
- Rebuilt for Python 3.9

* Sat Apr 25 2020 Sandro Mani <manisandro@gmail.com> - 2.20.3-1
- Update to 2.20.3

* Thu Feb 06 2020 Sandro Mani <manisandro@gmail.com> - 2.20.2-1
- Update to 2.20.2

* Fri Jan 31 2020 Sandro Mani <manisandro@gmail.com> - 2.20.1-1
- Update to 2.20.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 17 2019 Sandro Mani <manisandro@gmail.com> - 2.19.7-1
- Update to 2.19.7

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.19.6-4
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2.19.6-3
- Rebuilt for Python 3.8

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 22 2019 Sandro Mani <manisandro@gmail.com> - 2.19.6-1
- Update to 2.19.6

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 2.19.5-2
- Perl 5.30 rebuild

* Mon May 13 2019 Sandro Mani <manisandro@gmail.com> - 2.19.5-1
- Update to 2.19.5

* Tue Mar 26 2019 Sandro Mani <manisandro@gmail.com> - 2.19.4-1
- Update to 2.19.4

* Mon Feb 18 2019 Sandro Mani <manisandro@gmail.com> - 2.19.3-1
- Update to 2.19.3

* Tue Feb 12 2019 Pete Walter <pwalter@fedoraproject.org> - 2.19.2-4
- Obsolete devscripts-compat

* Mon Feb 11 2019 Björn Esser <besser82@fedoraproject.org> - 2.19.2-3
- Add Obsoletes / Provides for hardening-check (#1508087, 1536718)

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.19.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Sandro Mani <manisandro@gmail.com> - 2.19.2-1
- Update to 2.19.2

* Mon Dec 10 2018 Sandro Mani <manisandro@gmail.com> - 2.18.10-1
- Update to 2.18.10

* Tue Nov 13 2018 Sandro Mani <manisandro@gmail.com> - 2.18.9-1
- Update to 2.18.9

* Tue Nov 13 2018 Sandro Mani <manisandro@gmail.com> - 2.18.8-1
- Update to 2.18.8

* Sat Oct 27 2018 Sandro Mani <manisandro@gmail.com> - 2.18.7-1
- Update to 2.18.7

* Fri Oct 05 2018 Sandro Mani <manisandro@gmail.com> - 2.18.6-1
- Update to 2.18.6

* Thu Oct 04 2018 Sandro Mani <manisandro@gmail.com> - 2.18.5-1
- Update to 2.18.5

* Tue Sep 04 2018 Sandro Mani <manisandro@gmail.com> - 2.18.4-1
- Update to 2.18.4

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.18.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jul 03 2018 Petr Pisar <ppisar@redhat.com> - 2.18.3-4
- Perl 5.28 rebuild

* Fri Jun 29 2018 Jitka Plesnikova <jplesnik@redhat.com> - 2.18.3-3
- Perl 5.28 rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2.18.3-2
- Rebuilt for Python 3.7

* Mon May 28 2018 Sandro Mani <manisandro@gmail.com> - 2.18.3-1
- Update to 2.18.3

* Mon Apr 23 2018 Sandro Mani <manisandro@gmail.com> - 2.18.2-1
- Update to 2.18.2

* Wed Mar 07 2018 Sandro Mani <manisandro@gmail.com> - 2.18.1-1
- Update to 2.18.1

* Sun Feb 18 2018 Sandro Mani <manisandro@gmail.com> - 2.17.12-3
- Add missing BR: gcc, make

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 31 2017 Sandro Mani <manisandro@gmail.com> - 2.17.12-1
- Update to 2.17.12

* Mon Oct 30 2017 Sandro Mani <manisandro@gmail.com> - 2.17.11-1
- Update to 2.17.11

* Thu Sep 14 2017 Sandro Mani <manisandro@gmail.com> - 2.17.10-1
- Update to 2.17.10

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Sandro Mani <manisandro@gmail.com> - 2.17.9-1
- Update to 2.17.9

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 11 2017 Sandro Mani <manisandro@gmail.com> - 2.17.8-1
- Update to 2.17.8

* Sun Jul 09 2017 Sandro Mani <manisandro@gmail.com> - 2.17.7-1
- Update to 2.17.7

* Mon Jun 05 2017 Jitka Plesnikova <jplesnik@redhat.com> - 2.17.6-2
- Perl 5.26 rebuild

* Sun Jun 04 2017 Sandro Mani <manisandro@gmail.com> - 2.17.6-1
- Update to 2.17.6

* Sun Mar 19 2017 Sandro Mani <manisandro@gmail.com> - 2.17.5-1
- Update to 2.17.5

* Sat Mar 18 2017 Sandro Mani <manisandro@gmail.com> - 2.17.4-1
- Update to 2.17.4

* Mon Mar 06 2017 Sandro Mani <manisandro@gmail.com> - 2.17.2-1
- Update to 2.17.2

* Wed Feb 15 2017 Igor Gnatenko <ignatenko@redhat.com> - 2.17.1-4
- Rebuild for brp-python-bytecompile

* Mon Feb 13 2017 Sérgio Basto <sergio@serjux.com> - 2.17.1-3
- Epel 7 fixes: python3 requires and one compile error

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.17.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Sandro Mani <manisandro@gmail.com> - 2.17.1-1
- Update to 2.17.1

* Fri Jan 13 2017 Sandro Mani <manisandro@gmail.com> - 2.17.0-1
- Update to 2.17.0

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 2.16.13-2
- Rebuild for Python 3.6

* Sat Dec 17 2016 Sandro Mani <manisandro@gmail.com> - 2.16.13-1
- Update to 2.16.13

* Sun Dec 11 2016 Sandro Mani <manisandro@gmail.com> - 2.16.12-1
- Update to 2.16.12

* Wed Dec 07 2016 Sandro Mani <manisandro@gmail.com> - 2.16.11-1
- Update to 2.16.11

* Thu Nov 24 2016 Sandro Mani <manisandro@gmail.com> - 2.16.10-1
- Update to 2.16.10

* Thu Nov 24 2016 Sandro Mani <manisandro@gmail.com> - 2.16.9-1
- Update to 2.16.9

* Tue Oct 18 2016 Sandro Mani <manisandro@gmail.com> - 2.16.8-1
- Update to 2.16.8

* Mon Sep 05 2016 Sandro Mani <manisandro@gmail.com> - 2.16.7-1
- Update to 2.16.7

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.16.6-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Jul 06 2016 Sandro Mani <manisandro@gmail.com> - 2.16.6-1
- Update to 2.16.6
- Introduce devscripts-checkbashisms
- Introduce devscripts-compat compatibility package for
  devscripts-minimal -> {devscripts-checkbashisms, licensecheck} transition
- Remove Conflicts: rpmdevtools < 8.4, no current version of Fedora ships rpmdevtools < 8.4
- Drop unused BRs

* Sun Jun 05 2016 Sandro Mani <manisandro@gmail.com> - 2.16.5-1
- Update to 2.16.5

* Tue May 17 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.16.4-2
- Perl 5.24 rebuild

* Mon Apr 25 2016 Sandro Mani <manisandro@gmail.com> - 2.16.4-1
- Update to 2.16.4

* Mon Mar 21 2016 Sandro Mani <manisandro@gmail.com> - 2.16.2-1
- Update to 2.16.2

* Fri Feb 12 2016 Sandro Mani <manisandro@gmail.com> - 2.16.1-1
- Update to 2.16.1

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.15.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Jan 03 2016 Sandro Mani <manisandro@gmail.com> - 2.15.10-2
- Exclude %%{_datadir}/bash-completion/completions/bts which already is in bash-completion

* Thu Dec 31 2015 Sandro Mani <manisandro@gmail.com> - 2.15.10-1
- Update to 2.15.10

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.9-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Oct 09 2015 Sandro Mani <manisandro@gmail.com> - 2.15.9-2
- Add devscripts_ipc-run.patch to remove dpkg-perl dependency on licensecheck

* Tue Oct 06 2015 Sandro Mani <manisandro@gmail.com> - 2.15.9-1
- Update to 2.15.9

* Mon Aug 03 2015 Sandro Mani <manisandro@gmail.com> - 2.15.8-1
- Update to 2.15.8

* Sat Aug 01 2015 Sandro Mani <manisandro@gmail.com> - 2.15.7-1
- Update to 2.15.7

* Sat Aug 01 2015 Sandro Mani <manisandro@gmail.com> - 2.15.6-2
- Fix licensecheck incorrectly detecting mime strings such as text/x-c++ as a binary file (#1249227)

* Wed Jul 29 2015 Sandro Mani <manisandro@gmail.com> - 2.15.6-1
- Update to 2.15.6

* Thu Jul 09 2015 Sandro Mani <manisandro@gmail.com> - 2.15.5-6
- Make licensecheck print a warning when scanned file is not a text file (#1240914)

* Fri Jun 26 2015 Sandro Mani <manisandro@gmail.com> - 2.15.5-5
- Create symlinks like the debian package does (#1236122)

* Wed Jun 17 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.15.5-4
- Add: "Requires: perl(:MODULE_COMPAT_...)"

* Wed Jun 17 2015 Ralf Corsépius <corsepiu@fedoraproject.org> - 2.15.5-3
- Fix FTBFS.
- Eliminate libvfork, PKGLIBDIR (Abandoned upstream).
- Rework perl-BRs.
- Reflect upstream installing perl-modules into perl_vendordir.
- Reflect upstream installing bash-completion into /usr/share/bash-completion.
- BR: /usr/bin/dpkg-buildflags, /usr/bin/dpkg-vendor, /usr/bin/dpkg-parsechangelog.
- BR: pkgconfig(bash-completion).
- Remove archpath, whodepends's man-pages.
- Rebase patches.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.15.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Sandro Mani <manisandro@gmail.com> - 2.15.5-1
- Update to 2.15.5

* Tue Apr 28 2015 Sandro Mani <manisandro@gmail.com> - 2.15.4-1
- Update to 2.15.4

* Mon Apr 13 2015 Sandro Mani <manisandro@gmail.com> - 2.15.3-1
- Update to 2.15.3

* Fri Apr 03 2015 Sandro Mani <manisandro@gmail.com> - 2.15.2-1
- Update to 2.15.2
- Don't install whodepends (#1185511)

* Fri Jan 02 2015 Sandro Mani <manisandro@gmail.com> - 2.15.1-1
- Update to 2.15.1

* Thu Dec 04 2014 Sandro Mani <manisandro@gmail.com> - 2.14.11-1
- Update to 2.14.11

* Wed Oct 15 2014 Sandro Mani <manisandro@gmail.com> - 2.14.10-1
- Update to 2.14.10

* Mon Oct 13 2014 Sandro Mani <manisandro@gmail.com> - 2.14.9-1
- Update to 2.14.9

* Sat Oct 11 2014 Sandro Mani <manisandro@gmail.com> - 2.14.8-1
- Update to 2.14.8, fixes CVE-2014-1833 (#1059947)

* Fri Sep 26 2014 Sandro Mani <manisandro@gmail.com> - 2.14.7-1
- Update to 2.14.7

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Aug 11 2014 Sandro Mani <manisandro@gmail.com> - 2.14.6-2
- Remove /usr/bin/archpath from package (#1128503)

* Wed Aug 06 2014 Sandro Mani <manisandro@gmail.com> - 2.14.6-1
- Update to 2.14.6

* Wed Jun 11 2014 Sandro Mani <manisandro@gmail.com> - 2.14.5-1
- Update to 2.14.5

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jun 02 2014 Sandro Mani <manisandro@gmail.com> - 2.14.4-1
- Update to 2.14.4

* Thu May 29 2014 Sandro Mani <manisandro@gmail.com> - 2.14.3-1
- Update to 2.14.3

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 2.14.2-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Mon May 12 2014 Sandro Mani <manisandro@gmail.com> - 2.14.2-1
- Update to 2.14.2

* Thu Feb 27 2014 Sandro Mani <manisandro@gmail.com> - 2.14.1-2
- Require sensible-utils (rhbz#1067869)

* Sun Jan 26 2014 Sandro Mani <manisandro@gmail.com> - 2.14.1-1
- Update to 2.14.1

* Wed Dec 25 2013 Sandro Mani <manisandro@gmail.com> - 2.13.9-1
- Update to 2.13.9
- Fixes CVE-2013-7085 (rhbz#1040949)

* Wed Dec 11 2013 Sandro Mani <manisandro@gmail.com> - 2.13.8-1
- Update to 2.13.8

* Wed Dec 11 2013 Sandro Mani <manisandro@gmail.com> - 2.13.5-2
- Add upstream patch to fix arbitrary command execution when using
  USCAN_EXCLUSION (rhbz#1040266, debian#731849)

* Thu Dec 05 2013 Sandro Mani <manisandro@gmail.com> - 2.13.5-1
- Update to 2.13.5

* Sun Oct 20 2013 Sandro Mani <manisandro@gmail.com> - 2.13.4-5
- Honour RPM_LD_FLAGS

* Sat Oct 19 2013 Sandro Mani <manisandro@gmail.com> - 2.13.4-4
- Honour optflags
- Improve -minimal subpackage description

* Thu Oct 17 2013 Sandro Mani <manisandro@gmail.com> - 2.13.4-3
- Split scripts used by rpm developers into a subpackage
- Install some additional manpages

* Mon Oct  7 2013 Ville Skyttä <ville.skytta@iki.fi> - 2.13.4-2
- Add dependency on man for manpage-alert.

* Mon Oct 07 2013 Sandro Mani <manisandro@gmail.com> - 2.13.4-1
- Update to 2.13.4
- Drop devscripts_item.patch
- Drop devscripts_spurious-pod.patch

* Sat Sep 21 2013 Sandro Mani <manisandro@gmail.com> - 2.13.3-5
- Fix typo builroot -> buildroot
- Require perl modules instead of the providing packages

* Fri Sep 20 2013 Sandro Mani <manisandro@gmail.com> - 2.13.3-4
- Conflict with rpmdevtools < 8.4

* Fri Sep 20 2013 Sandro Mani <manisandro@gmail.com> - 2.13.3-3
- Revert: Require rpmdevtools and drop scripts which are in rpmdevtools
- Add conflicts from rpmdevtools < 8.3-6

* Thu Sep 19 2013 Sandro Mani <manisandro@gmail.com> - 2.13.3-2
- Require rpmdevtools and drop scripts which are in rpmdevtools

* Thu Sep 19 2013 Sandro Mani <manisandro@gmail.com> - 2.13.3-1
- Initial package
