Name:		rstp
Summary:	Rapid Spanning Tree User Space Daemon
Version:	04012009git
Release:	31%{dist}
# Note the lack of a URL tag here.  rstp has no official upstream project page,
# just a git repository, so we don't include the URL here. rpmlint will yell
# about this, rpmlint is wrong,

License:	GPLv2+ and LGPLv2+
BuildRequires:	gcc
# Generate this tarball with the following commands in the git tree:
# git clone git://git.kernel.org/pub/scm/linux/kernel/git/shemminger/rstp.git
# cd rstp
# git checkout 76eb7423e188f6852ba9ced4352e0d61f4dace4d
# cd ..
# tar jcf git-04012009git.tar.bz2 rstp 
Source0:	%{name}-%{version}.tar.bz2

# http://patchwork.ozlabs.org/patch/46803/
# Submitted upstream, no reply yet
Patch0:	rstp-type-punning.patch
Patch1: rstp-unused-fix.patch
Patch2: rstp-ftbfs-bz914445.patch
Patch3: rstp-fix-warnings.patch
Patch4: rstp-makefile.patch
Patch5: rstp-ldflags.patch
Patch6: rstp-ldflags-rstpctl.patch

%description
rstp is a user space implementation of the rapid spanning tree protocol.  It
replaces the in-kernel STP implementation

%prep
%setup -q -n rstp

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
export CFLAGS="%{optflags} %__global_ldflags"
export LDFLAGS="%__global_ldflags"

make %{_smp_mflags}

%install
make INSTALLPREFIX=$RPM_BUILD_ROOT install
install -m 755 bridge-stp $RPM_BUILD_ROOT/sbin

%files
/sbin/*
%{_mandir}/man8/*
%doc CHANGES_TO_RSTPLIB TODO LICENSE rstplib/COPYING


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 04012009git-31
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 04012009git-30
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 04012009git-29
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 04012009git-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 04012009git-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 04012009git-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 12 2018 Neil Horman <nhorman@redhat.com> - 04012009git-25
- remove /sbin/bridge from rpm (1599855)

* Mon May 14 2018 Neil Horman <nhorman@redhat.com> - 04012009git-24
- Fixed rstpctl linker flags

* Thu Mar 08 2018 Neil Horman <nhorman@redhat.com> - 04012009git-23
- Fixed missing LDFLAG pickup in makefile (bz 1548674)

* Wed Feb 28 2018 Neil Horman <nhorman@redhat.com> - 04012009git-22
- Update spec file to pull in redhat linker flags

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 04012009git-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 04012009git-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 04012009git-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 04012009git-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Apr 04 2016 Neil Horman <nhorman@redhat.com> - 04012009git-17
- Fix makefile problem (bz1319301)

* Mon Feb 15 2016 Neil Horman <nhorman@redhat.com> - 04012009git-16
- Fix FTBFS (bz 1307998)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 04012009git-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 04012009git-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 04012009git-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 04012009git-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 04012009git-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 22 2013 Neil Horman <nhorman@redhat.com> - 04012009git-10
- Fixed FTBFS (bz 914445)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 04012009git-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 04012009git-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 04012009git-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jun 23 2011 Neil Horman <nhorman@redhat.com> - 041209git-6
- Fixed unused variable build error (bz 716119)
 
* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 04012009git-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 07 2010 Neil Horman <nhorman@redhat.com> - 04012009git-4
- Add more comments
- add LICENSE file and COPYING file

* Wed Apr 07 2010 Neil Horman <nhorman@redhat.com> - 04012009git-3
- Removed clean script
- Added comments regarding patch and tarball

* Wed Apr 07 2010 Neil Horman <nhorman@redhat.com> - 04012009git-2
- Fix review comments in bz 570166
- remove buildroot tag
- remove URL tag
- add requested docs

* Mon Mar 01 2010 Neil Horman <nhorman@redhat.com> - 04012009git-1
- Initial Build

