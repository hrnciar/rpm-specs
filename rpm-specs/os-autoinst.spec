# Fedora spec initially based on upstream spec file from OBS:
# https://build.opensuse.org/package/view_file/devel:openQA/os-autoinst/os-autoinst.spec
# License: GPLv2+

# Full stack test only runs reliably on x86
%ifnarch %{ix86} x86_64
%global no_fullstack 1
%endif
# 18-qemu-options.t broken on 32-bit ARM on F30 2019/08
# works on F31, works in a mock root...really not worth debugging more
# 14-isotovideo.t also broken since ~2020/04, os-autoinst apparently
# does not run in first subtest, can't figure out why not
%ifarch %{arm} s390x
%global no_options 1
%global no_isotovideo 1
%endif

# os-autoinst has a bunch of annoyingly-badly-named private modules,
# we do not want automatic provides or requires for these
# ref https://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Perl
# but per https://fedorahosted.org/fpc/ticket/591 , these have been
# improved, and contrary to the wiki it is safe to set them first and
# then call perl_default_filter, the values will be properly merged.
# I tried to sell upstream on naming these properly and installing
# them to the perl vendor dir, but they wouldn't bite.
# https://github.com/os-autoinst/os-autoinst/issues/387
%global __provides_exclude_from %{_libexecdir}/os-autoinst
%global __requires_exclude perl\\((autotest|backend|basetest|bmwqemu|commands|consoles|cv|distribution|lockapi|mmapi|myjsonrpc|needle|ocr|osutils|testapi|OpenQA::Exceptions|OpenQA::Benchmark::Stopwatch|OpenQA::Qemu|OpenQA::Isotovideo)
%{?perl_default_filter}

%global github_owner    os-autoinst
%global github_name     os-autoinst
%global github_version  4.6
%global github_commit   f38e8b174dc1a0cace4d624a197a297f9efdc2bb
# if set, will be a post-release snapshot build, otherwise a 'normal' build
%global github_date     20200610
%global shortcommit     %(c=%{github_commit}; echo ${c:0:7})

Name:           os-autoinst
Version:        %{github_version}
Release:        17%{?github_date:.%{github_date}git%{shortcommit}}%{?dist}
Summary:        OS-level test automation
License:        GPLv2+
URL:            https://os-autoinst.github.io/openQA/
Source0:        https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{github_name}-%{github_commit}.tar.gz

# on SUSE this is conditional, for us it doesn't have to be but we
# still use a macro just to keep build_requires similar for ease of
# cross-comparison
%define opencv_require pkgconfig(opencv)
# The following line is generated from dependencies.yaml (upstream)
%define build_requires %opencv_require autoconf automake gcc-c++ libtool make perl(ExtUtils::Embed) perl(ExtUtils::MakeMaker) >= 7.12 perl(Module::CPANfile) perl(Pod::Html) pkg-config pkgconfig(fftw3) pkgconfig(libpng) pkgconfig(sndfile) pkgconfig(theoraenc)
# this is stuff we added to requires, we put it in its own macro
# to make resyncing with upstream spec changes easier. SUSE has
# perl-base, we have perl(base)
%define main_requires_additional perl(base)
# diff from SUSE: added main_requires_additional, dropped perl-base
# which does not exist in Fedora - we have perl(base) in
# main_requires_additional and the perl(:MODULE_COMPAT) require below
# The following line is generated from dependencies.yaml (upstream)
%define main_requires %main_requires_additional git-core perl(B::Deparse) perl(Carp) perl(Carp::Always) perl(Class::Accessor::Fast) perl(Config) perl(Cpanel::JSON::XS) perl(Crypt::DES) perl(Cwd) perl(Data::Dumper) perl(Digest::MD5) perl(DynaLoader) perl(English) perl(Errno) perl(Exception::Class) perl(Exporter) perl(ExtUtils::testlib) perl(Fcntl) perl(File::Basename) perl(File::Find) perl(File::Path) perl(File::Spec) perl(File::Temp) perl(File::Touch) perl(File::Which) perl(IO::Handle) perl(IO::Scalar) perl(IO::Select) perl(IO::Socket) perl(IO::Socket::INET) perl(IO::Socket::UNIX) perl(IPC::Open3) perl(IPC::Run::Debug) perl(IPC::System::Simple) perl(List::MoreUtils) perl(List::Util) perl(Mojo::IOLoop::ReadWriteProcess) >= 0.23 perl(Mojo::JSON) perl(Mojo::Log) perl(Mojo::URL) perl(Mojo::UserAgent) perl(Mojolicious) >= 8.42 perl(Mojolicious::Lite) perl(Net::DBus) perl(Net::IP) perl(Net::SNMP) perl(Net::SSH2) perl(POSIX) perl(Scalar::Util) perl(Socket) perl(Socket::MsgHdr) perl(Term::ANSIColor) perl(Thread::Queue) perl(Time::HiRes) perl(Try::Tiny) perl(XML::LibXML) perl(XML::SemanticDiff) perl(autodie) perl(base) perl(constant) perl(integer) perl(strict) perl(warnings)
# all requirements needed by the tests, do not require on this in the package
# itself or any sub-packages
# diff from SUSE: replaced qemu-tools with qemu-img, replaced qemu-x86
# with qemu-system-i386, dropped spellcheck requirement stuff as this
# isn't needed in package builds IMO, dropped critic stuff as we don't
# run those tests in our build
# The following line is generated from dependencies.yaml (upstream)
%define test_requires %build_requires %main_requires perl(Benchmark) perl(Devel::Cover) perl(FindBin) perl(Pod::Coverage) perl(Test::Exception) perl(Test::Fatal) perl(Test::Mock::Time) perl(Test::MockModule) perl(Test::MockObject) perl(Test::Mojo) perl(Test::More) perl(Test::Output) perl(Test::Pod) perl(Test::Strict) perl(Test::Warnings) >= 0.029 perl(YAML::PP) qemu-kvm /usr/bin/qemu-img /usr/bin/qemu-system-i386
# diff from SUSE: dropped perl(Devel::Cover::Report::Codecov) as it's
# not currently packaged for Fedora
# The following line is generated from dependencies.yaml (upstream)
%define devel_requires %test_requires perl(Devel::Cover) perl(Perl::Tidy)

BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  systemd
%if 0%{?no_fullstack}
%else
BuildRequires:  perl(Mojo::File)
%endif # no_fullstack
# tinycv is a compiled public module, so we should have this
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Recommends:     tesseract
Recommends:     qemu >= 2.0.0
Recommends:     qemu-kvm
Recommends:     /usr/bin/qemu-img
BuildRequires:  %test_requires
Requires:       %main_requires
Requires(pre):  %{_bindir}/getent
Requires(pre):  %{_sbindir}/useradd

%description
The OS-autoinst project aims at providing a means to run fully
automated tests. Especially to run tests of basic and low-level
operating system components such as bootloader, kernel, installer and
upgrade, which can not easily and safely be tested with other
automated testing frameworks. However, it can just as well be used to
test applications on top of a newly installed OS.

%package devel
Summary:        Development package pulling in all build+test dependencies
Requires:       %devel_requires

%description devel
Development package pulling in all build+test dependencies.

%package openvswitch
Summary:        Open vSwitch support for os-autoinst
Requires:       openvswitch
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
BuildRequires:      systemd

%description openvswitch
This package contains Open vSwitch support for os-autoinst.

%prep
%autosetup -n %{github_name}-%{github_commit} -p1
# Replace version number from git to what's reported by the package
sed  -i 's/ my $thisversion = qx{git.*rev-parse HEAD}.*;/ my $thisversion = "%{version}";/' isotovideo

%if 0%{?no_fullstack}
rm -f t/99-full-stack.t
sed -i -e '/99-full-stack.t/d' Makefile.am
%endif # no_fullstack

%if 0%{?no_options}
rm -f t/18-qemu-options.t
sed -i -e '/18-qemu-options.t/d' Makefile.am
%endif

%if 0%{?no_isotovideo}
rm -f t/14-isotovideo.t
sed -i -e '/14-isotovideo.t/d' Makefile.am
%endif

# Tesseract 4.0.0 (in Rawhide as of 2018-11) fails utterly to OCR
# the test needle properly:
# https://github.com/tesseract-ocr/tesseract/issues/2052
rm -f t/02-test_ocr.t
sed -i -e '/02-test_ocr.t/d' Makefile.am

# https://progress.opensuse.org/issues/60755
rm -f t/07-commands.t
sed -i -e '/07-commands.t/d' Makefile.am

%build
mkdir -p m4
autoreconf -f -i
%configure --docdir=%{_pkgdocdir}
make INSTALLDIRS=vendor %{?_smp_mflags}

%install
%make_install INSTALLDIRS=vendor
# only internal stuff
rm -r %{buildroot}%{_libexecdir}/os-autoinst/tools/
# we don't really need to ship this in the package, usually the web UI
# is much better for needle editing
rm %{buildroot}%{_libexecdir}/os-autoinst/crop.py*
# we're going to %%license this
rm %{buildroot}%{_pkgdocdir}/COPYING
# This is no use for package users
rm %{buildroot}%{_pkgdocdir}/INSTALL.asciidoc
ls -lR %buildroot
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -and -not -name distri -exec rmdir {} \;

# we need the stale symlinks to point to git
export NO_BRP_STALE_LINK_ERROR=yes

%check
# we may not pull Perl::Critic in for RPM builds as we don't run code
# quality checks, so cut it from cpanfile ahead of the next check
sed '/Perl::Critic/d' -i cpanfile
# should work offline
for p in $(cpanfile-dump); do rpm -q --whatprovides "perl($p)"; done
# 00-compile-check-all.t fails if this is present and Perl::Critic is
# not installed
rm tools/lib/perlcritic/Perl/Critic/Policy/*.pm
make test VERBOSE=1

%post openvswitch
%systemd_post os-autoinst-openvswitch.service

%preun openvswitch
%systemd_preun os-autoinst-openvswitch.service

%postun openvswitch
%systemd_postun_with_restart os-autoinst-openvswitch.service

%files
%{_pkgdocdir}
%license COPYING
%{perl_vendorarch}/tinycv.pm
%{perl_vendorarch}/auto/tinycv
%dir %{_libexecdir}/os-autoinst
%{_libexecdir}/os-autoinst/videoencoder
%{_libexecdir}/os-autoinst/basetest.pm
#
%{_libexecdir}/os-autoinst/dmidata
#
%{_libexecdir}/os-autoinst/bmwqemu.pm
%{_libexecdir}/os-autoinst/commands.pm
%{_libexecdir}/os-autoinst/distribution.pm
%{_libexecdir}/os-autoinst/testapi.pm
%{_libexecdir}/os-autoinst/mmapi.pm
%{_libexecdir}/os-autoinst/myjsonrpc.pm
%{_libexecdir}/os-autoinst/lockapi.pm
%{_libexecdir}/os-autoinst/cv.pm
%{_libexecdir}/os-autoinst/ocr.pm
%{_libexecdir}/os-autoinst/osutils.pm
%{_libexecdir}/os-autoinst/needle.pm
%{_libexecdir}/os-autoinst/backend
%{_libexecdir}/os-autoinst/OpenQA
%{_libexecdir}/os-autoinst/consoles
%{_libexecdir}/os-autoinst/autotest.pm
%{_bindir}/isotovideo
%{_bindir}/debugviewer
%{_bindir}/snd2png

%files openvswitch
%{_libexecdir}/os-autoinst/os-autoinst-openvswitch
%{_unitdir}/os-autoinst-openvswitch.service
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.opensuse.os_autoinst.switch.conf

%files devel

%changelog
* Fri Jun 12 2020 Adam Williamson <awilliam@redhat.com> - 4.6-17.20200610gitf38e8b17
- Drop -devel dep that doesn't exist in Fedora

* Wed Jun 10 2020 Adam Williamson <awilliam@redhat.com> - 4.6-16.20200610gitf38e8b17
- Bump to latest git, resync spec again

* Mon Jun 08 2020 Adam Williamson <awilliam@redhat.com> - 4.6-15.20200608gitbcbc6c41
- Bump to latest git, resync spec with upstream

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 4.6-14.20200430git85fa4f1
- Rebuilt for OpenCV 4.3

* Mon May 25 2020 Adam Williamson <awilliam@redhat.com> - 4.6-13.20200430git85fa4f12
- Backport PR #1419 to fix build on Rawhide (opencv4)

* Thu Apr 30 2020 Adam Williamson <awilliam@redhat.com> - 4.6-12.20200430git85fa4f12
- Bump to latest git
- Resync spec with upstream, tweak dependency macro implementation

* Fri Apr 17 2020 Adam Williamson <awilliam@redhat.com> - 4.6-11.20200414git50464d4e
- Rearrange the dependencies ppisar added

* Wed Apr 15 2020 Adam Williamson <awilliam@redhat.com> - 4.6-10.20200414git50464d4e
- Bump to latest git

* Wed Apr 01 2020 Petr Pisar <ppisar@redhat.com>
- Add more Perl dependencies

* Wed Mar 11 2020 Adam Williamson <awilliam@redhat.com> - 4.6-9.20200311git4e3dec50
- Bump to latest git

* Wed Feb 05 2020 Adam Williamson <awilliam@redhat.com> - 4.6-8.20200205git63af2f4f
- Bump to latest git

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.6-7.20191226gitd693abe
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 4.6-6.20191226gitd693abe
- Rebuild for OpenCV 4.2

* Thu Jan 02 2020 Adam Williamson <awilliam@redhat.com> - 4.6-5.20191226gitd693abe0
- Bump to latest git

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 4.6-4.20191121git75fbe1d
- Rebuilt for opencv4

* Thu Nov 21 2019 Adam Williamson <awilliam@redhat.com> - 4.6-3.20191121git75fbe1d3
- Update to latest git again

* Thu Oct 31 2019 Adam Williamson <awilliam@redhat.com> - 4.6-2.20191029git447dab86
- Properly generate -devel package

* Wed Oct 30 2019 Adam Williamson <awilliam@redhat.com> - 4.6-1.20191029git447dab86
- Bump to latest upstream git snapshot (new version 4.6 declared)
- Resync spec with upstream

* Sat Oct 19 2019 Adam Williamson <awilliam@redhat.com> - 4.5-26.20190806git3391d60
- Backport 'click_lastmatch' feature from upstream git master

* Tue Oct 15 2019 Adam Williamson <awilliam@redhat.com> - 4.5-25.20190806git3391d60
- Bump to slightly newer git snapshot to build with OpenCV 4.1

* Wed Aug 21 2019 Adam Williamson <awilliam@redhat.com> - 4.5-24.20190806gitc597122
- Backport PR #1199 to improve validate_script_output result display

* Tue Aug 20 2019 Adam Williamson <awilliam@redhat.com> - 4.5-23.20190806gitc597122
- Allow PXE boot only once (-boot once=n)

* Tue Aug 13 2019 Adam Williamson <awilliam@redhat.com> - 4.5-22.20190806gitc597122
- Disable qemu-options test on 32-bit ARM (it fails on F30)

* Tue Aug 06 2019 Adam Williamson <awilliam@redhat.com> - 4.5-21.20190806gitc597122
- Update to latest git again

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-20.20190706gitc3d5e8a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Jul 12 2019 Adam Williamson <awilliam@redhat.com> - 4.5-19.20190706gitc3d5e8a
- Bump to latest git again, drop merged patch

* Fri Jul 05 2019 Adam Williamson <awilliam@redhat.com> - 4.5-18.20190527git43185de
- Backport #1174 to work around RHBZ #1727388 (key press order)

* Fri May 31 2019 Jitka Plesnikova <jplesnik@redhat.com> - 4.5-17.20190527git43185de
- Perl 5.30 rebuild

* Mon May 27 2019 Adam Williamson <awilliam@redhat.com> - 4.5-16.20190527git43185de
- Bump to latest git again
- Add a couple of new/missing dependencies

* Wed Mar 13 2019 Adam Williamson <awilliam@redhat.com> - 4.5-15.20190312git1080c39
- Bump to latest git again

* Wed Feb 06 2019 Adam Williamson <awilliam@redhat.com> - 4.5-14.20190206git519f2ee
- Bump to latest git again

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-13.20190114gitdfe4780
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Adam Williamson <awilliam@redhat.com> - 4.5-12.20190114gitdfe4780
- Bump to latest git again (including virtio-rng /dev/urandom change)

* Tue Jan 08 2019 Adam Williamson <awilliam@redhat.com> - 4.5-11.20190108gitcb3fa72
- Bump to latest git again

* Tue Dec 18 2018 Adam Williamson <awilliam@redhat.com> - 4.5-10.20181213git44e93d8
- Bump to latest git again, drop backported patch

* Mon Nov 19 2018 Adam Williamson <awilliam@redhat.com> - 4.5-9.20181119gitf5d9165
- Bump to latest git again
- Backport a patch related to new video timestamp feature

* Wed Nov 14 2018 Adam Williamson <awilliam@redhat.com> - 4.5-8.20181113gitdced72b
- Bump to latest git
- Resync with upstream spec
- Disable OCR test on Rawhide as Tesseract 4.0.0 sucks

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-7.20180208gitab8eeda
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Jitka Plesnikova <jplesnik@redhat.com> - 4.5-6.20180208gitab8eeda
- Perl 5.28 rebuild

* Fri Mar 02 2018 Adam Williamson <awilliam@redhat.com> - 4.5-5.20180208gitab8eeda
- Rebuild for opencv 3.4.1

* Thu Feb 08 2018 Adam Williamson <awilliam@redhat.com> - 4.5-4.20180208gitab8eeda
- Bump to latest git

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.5-3.20171222git1c7bb3f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 02 2018 Adam Williamson <awilliam@redhat.com> - 4.5-2.20171222git1c7bb3f
- Bump to latest git, with an upstream bugfix (#901)
- Rebuild for opencv soname bump (Rawhide)

* Wed Dec 20 2017 Adam Williamson <awilliam@redhat.com> - 4.5-1.20171220git25191d5
- Bump to latest git again, bump version to 4.5 (per upstream)

* Thu Aug 17 2017 Adam Williamson <awilliam@redhat.com> - 4.4-26.20170807gitcf2d051
- Bump to latest git again (wait_screen_change enhancement looks nice)

* Tue Aug 15 2017 Adam Williamson <awilliam@redhat.com> - 4.4-25.20170725git734682a
- Revert typing speed change, didn't help and we found the real bug

* Tue Aug 15 2017 Adam Williamson <awilliam@redhat.com> - 4.4-24.20170725git734682a
- Make the default typing speed slower to work around typing fails

* Mon Jul 31 2017 Adam Williamson <awilliam@redhat.com> - 4.4-23.20170725git734682a
- Bump to latest git

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 4.4-22.20170410git97928a2
- Rebuild with binutils fix for ppc64le (#1475636)

* Tue Jul 25 2017 Adam Williamson <awilliam@redhat.com> - 4.4-21.20170410git97928a2
- Recommend git to avoid error messages in logs (RHBZ #1467086)

* Thu Jul 20 2017 Adam Williamson <awilliam@redhat.com> - 4.4-20.20170410git97928a2
- Rebuild for new gdal (for new mariadb)
- Downstream patch the full-stack test to type a bit slower

* Tue Jun 06 2017 Jitka Plesnikova <jplesnik@redhat.com> - 4.4-19.20170410git97928a2
- Perl 5.26 rebuild
- Fixed tests to build on Perl without dot in INC

* Mon Apr 10 2017 Adam Williamson <awilliam@redhat.com> - 4.4-18.20170410git97928a2
- Bump to latest git again
- Adjust isotovideo self-reported version at build time (as did SUSE)

* Tue Mar 28 2017 Adam Williamson <awilliam@redhat.com> - 4.4-17.20170329gitd8f75d2
- Bump again to fix assert_and_click mouse repositioning (see #744)
- Disable full-stack test on non-x86 arches

* Thu Mar 02 2017 Adam Williamson <awilliam@redhat.com> - 4.4-16.20170327git201dc4e
- Update to latest git (many useful fixes)

* Tue Feb 28 2017 Adam Williamson <awilliam@redhat.com> - 4.4-15.20170126gitc29555c
- Rebuild for new opencv

* Mon Jan 30 2017 Adam Williamson <awilliam@redhat.com> - 4.4-14.20170126gitc29555c
- Update to latest git, drop merged patch

* Wed Jan 18 2017 Adam Williamson <awilliam@redhat.com> - 4.4-13.20170104git84d91e6
- Backport fix for duplicated qemu vga options (broke ARM jobs)

* Wed Jan 04 2017 Adam Williamson <awilliam@redhat.com> - 4.4-12.20170104git84d91e6
- Update to latest git, drop merged #686 patch

* Wed Jan 04 2017 Adam Williamson <awilliam@redhat.com> - 4.4-11.20170103git26171f4
- Backport #686 to fix os-autoinst on 32-bit arches, re-enable them

* Tue Jan 03 2017 Adam Williamson <awilliam@redhat.com> - 4.4-10.20170103git26171f4
- Filter out another bogus openQA provide

* Tue Jan 03 2017 Adam Williamson <awilliam@redhat.com> - 4.4-9.20170103git26171f4
- Bump to latest git again
- Add some additional test requirements
- Disable build entirely on arches broken by POO #13822 for now

* Tue Dec 13 2016 Adam Williamson <awilliam@redhat.com> - 4.4-8.20161213git3050cfa
- bump to latest git again

* Mon Nov 28 2016 Adam Williamson <awilliam@redhat.com> - 4.4-7.20161123gitdb6d2ef
- bump to latest git (inc. garretraziel's UEFI boot order patches)
- drop patches merged upstream

* Tue Oct 25 2016 Adam Williamson <awilliam@redhat.com> - 4.4-6.20161021git9672031
- bump to latest git
- backport a couple of small fixes for perl errors
- backport #625 so we can use the distro-packaged EDK2

* Mon Sep 19 2016 Adam Williamson <awilliam@redhat.com> - 4.4-5.20160915gitba7ea22
- disable a failing test on 32-bit x86

* Thu Sep 15 2016 Adam Williamson <awilliam@redhat.com> - 4.4-4.20160915gitba7ea22
- bump to git master again, drop merged patch

* Wed Sep 14 2016 Adam Williamson <awilliam@redhat.com> - 4.4-3.20160912git62f67e7
- final version of POO #13722 fix

* Wed Sep 14 2016 Adam Williamson <awilliam@redhat.com> - 4.4-2.20160912git62f67e7
- test fix for POO #13722

* Mon Sep 12 2016 Adam Williamson <awilliam@redhat.com> - 4.4-1.20160912git62f67e7
- try a new git snapshot again, let's see how it's going
- SUSE started calling this 4.4 at some point, so let's follow along

* Sun Sep 04 2016 Adam Williamson <awilliam@redhat.com> - 4.3-26.20160902git1962d68
- slightly older git snapshot, may fix issues seen in last build

* Sat Sep 03 2016 Adam Williamson <awilliam@redhat.com> - 4.3-25.20160902git0b5d885
- bump to latest git again, drop merged patches

* Wed Aug 31 2016 Adam Williamson <awilliam@redhat.com> - 4.3-24.20160826gitcd35b40
- don't sha1sum qcow assets on shutdown (slow, blocks worker process)

* Mon Aug 29 2016 Adam Williamson <awilliam@redhat.com> - 4.3-23.20160826gitcd35b40
- apply PR #571 to try and fix POO #13456 / #12680

* Fri Aug 26 2016 Adam Williamson <awilliam@redhat.com> - 4.3-22.20160826gitcd35b40
- bump to latest git (to get bug fixes, disable verbose JSON logging)

* Tue Aug 09 2016 Adam Williamson <awilliam@redhat.com> - 4.3-21.20160712gitf5bb0fe
- fix an issue with cursor reset after assert_and_click triggering overview

* Tue Jul 12 2016 Adam Williamson <awilliam@redhat.com> - 4.3-20.20160712gitf5bb0fe
- git bump again (still fixing issues related to the shutdown rewrite)

* Mon Jul 11 2016 Adam Williamson <awilliam@redhat.com> - 4.3-19.20160711git243c036
- bump to git master one more time for PR #536 (more shutdown stuff)

* Sun Jul 10 2016 Adam Williamson <awilliam@redhat.com> - 4.3-18.20160710gitc5e11ab
- bump to git master once more with merged (updated) PR #534

* Sun Jul 10 2016 Adam Williamson <awilliam@redhat.com> - 4.3-17.20160708gitcb0f4a8
- bump to current git master again to make PR apply cleanly
- backport PR #534 to fix #535 and openQA #781

* Fri Jul 08 2016 Adam Williamson <awilliam@redhat.com> - 4.3-16.20160708git7a1901d
- bump to latest git
- drop merged PR #524 patch

* Wed Jul 06 2016 Adam Williamson <awilliam@redhat.com> - 4.3-15.20160624gitfe19b00
- include the whole of PR #524 to help fix multiple interactive mode issues

* Mon Jul 04 2016 Adam Williamson <awilliam@redhat.com> - 4.3-14.20160624gitfe19b00
- fix worker crash on job cancel (#530) with a single commit from PR #524

* Tue Jun 28 2016 Adam Williamson <awilliam@redhat.com> - 4.3-13.20160624gitfe19b00
- bump to latest upstream git, drop merged patches

* Mon May 16 2016 Jitka Plesnikova <jplesnik@redhat.com> - 4.3-12.20160408gitff760a3
- Perl 5.24 rebuild

* Tue May 03 2016 Adam Williamson <awilliam@redhat.com> - 4.3-11.20160408gitff760a3
- update the upload_logs patch to the version merged upstream

* Fri Apr 29 2016 Adam Williamson <awilliam@redhat.com> - 4.3-10.20160408gitff760a3
- add an option to prevent test dying if upload_logs fails (PR #490)

* Tue Apr 26 2016 Adam Williamson <awilliam@redhat.com> - 4.3-9.20160408gitff760a3
- fix incorrect binary path in openvswitch service file (PR #487)

* Sat Apr 23 2016 Adam Williamson <awilliam@redhat.com> - 4.3-8.20160408gitff760a3
- rebuild against updated opencv

* Fri Apr 08 2016 Adam Williamson <awilliam@redhat.com> - 4.3-7.20160408gitff760a3
- bump to current git (to go along with openQA; patch load was getting huge)

* Thu Mar 31 2016 Adam Williamson <awilliam@redhat.com> - 4.3-6
- backport: allow needles to be in nested directories (jskladan)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 15 2016 Adam Williamson <awilliam@redhat.com> - 4.3-4
- simplify requires/provides excludes (thanks Zbigniew)

* Fri Jan 15 2016 Adam Williamson <awilliam@redhat.com> - 4.3-3
- add perl(:MODULE_COMPAT require

* Fri Jan 15 2016 Adam Williamson <awilliam@redhat.com> - 4.3-2
- exclude provides and requires from the private modules

* Thu Jan 14 2016 Adam Williamson <awilliam@redhat.com> - 4.3-1
- new release 4.3, drop patches merged upstream
- resync with upstream spec changes
- some package review cleanups
- fix 'format not a literal' errors in new snd2png (submitted upstream)

* Tue Dec 22 2015 Adam Williamson <awilliam@redhat.com> - 4.2.1-6
- changes requested in package review:
  + improve 'find and destroy' commands
  + drop tests/ directory (upstream did this too)
  + drop git dependency (seems to be ancient stuff)
  + use %%license
  + mark dbus config file as (noreplace)
  + 'Open vSwitch' not 'openvswitch' in summary/description
  + systemd snippets for openvswitch service
  + drop useless python scripts to avoid automatic python requirements

* Thu Dec 03 2015 Adam Williamson <awilliam@redhat.com> - 4.2.1-5
- fix a bug in the UEFI patch

* Thu Dec 03 2015 Adam Williamson <awilliam@redhat.com> - 4.2.1-4
- support Fedora UEFI firmware location (submitted upstream)

* Mon Nov  2 2015 Adam Williamson <awilliam@redhat.com> - 4.2.1-3
- tweak hardcoded path patch a little (upstream request)

* Sat Oct 24 2015 Adam Williamson <awilliam@redhat.com> - 4.2.1-2
- fix a hardcoded path which is incorrect on Fedora

* Thu Oct 15 2015 Adam Williamson <awilliam@redhat.com> - 4.2.1-1
- new release 4.2.1
- merge changes from upstream

* Thu Apr 23 2015 Adam Williamson <awilliam@redhat.com> - 4.1-1.20150423git24609047
- initial Fedora package, based on OBS package
